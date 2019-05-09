from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('Records')
cur=con.cursor()
root=Tk()
root.title('Phonebook')

def fun():
    root.destroy()
    root1=Tk()
    #root1.geometry('300x500')
    root1.title('Phonebook')
    Label(root1,text='Phone',width='22',font='times 20 bold',bg='green',relief='ridge').grid(row=0,column=0,columnspan=5)
    t=Entry(root1,width=15,bd=3,justify='left')
    t.grid(row=1,column=4)
    n=Entry(root1,width=20,bd=3,justify='center')
    n.grid(row=2,column=0,columnspan=3)
    
    
    def call():
        root2=Tk()
        root2.title('LOG')
        #root2.geometry('400x400')
        cur.execute('select name,phone_no from details')
        a=cur.fetchall()
        global count
        count=0
        for i in a:
            count=count+1
            l=Listbox(root2,height=1)
            l.grid()
            l.insert(0,(str(i[0])+' :- '+str(i[1])))
            l.grid(row=0+count,column=1)
            con.commit()
        

    def add():
        root3=Tk()
        root3.title('ADD')
        #root3.geometry('400x300')
        cur.execute('create table if not exists details(id_no varchar(10) primary key,name varchar(20), phone_no number(10), email varchar(20))')
        Label(root3,text="Id_no:").grid(row=1, column=0)
        id_no =Entry(root3)
        id_no.grid(row=1,column=1)
        Label(root3,text="Name :").grid(row=2, column=0)
        name=Entry(root3)
        name.grid(row=2,column=1)
        Label(root3,text="Phone_no :").grid(row=3,column=0)
        phone_no=Entry(root3)
        phone_no.grid(row=3,column=1)
        Label(root3,text="Email :").grid(row=4,column=0)
        email=Entry(root3)
        email.grid(row=4,column=1)
        def save():
            cur.execute('insert into details values(?,?,?,?)',(id_no.get(), name.get(), phone_no.get(), email.get()))
            showinfo('title','SAVE')
        Button(root3,text='Save',command=save).grid(row=5,column=1)


    def update():
        root5=Tk()
        root5.geometry('400x300')
        root5.title('Update After Delete')
        Label(root5,text="Id_no : ").grid(row=1,column=2)
        e=Entry(root5)
        e.grid(row=1,column=3)
        Label(root5,text="Name : ").grid(row=2,column=2)
        e1=Entry(root5)
        e1.grid(row=2,column=3)
        def update_record():
            cur.execute('update details set name=? where id_no = ?',(e1.get(),e.get()))
            showinfo('title','UPDATE')
        Button(root5,text='OK',command=update_record).grid(row=5,column=2)
        con.commit()
        

    def contact():
        root4=Tk()
        #root4.geometry('300x300')
        root4.title('Contact')
        Label(root4,text='Id_no',font='times 10 bold',relief='raised').grid(row=0,column=0)
        Label(root4,text='Name',font='times 10 bold',relief='raised').grid(row=0,column=1)
        Label(root4,text='Phone_no',font='times 10 bold',relief='raised').grid(row=0,column=2)
        Label(root4,text='Email',font='times 10 bold',relief='raised').grid(row=0,column=3)
        cur.execute('select * from details')
        a= cur.fetchall()
        global count
        count=0
        for i in a:
            count=count+1
            Label(root4,text=str(i[0])).grid(row=0+count,column=0)
            Label(root4,text=str(i[1])).grid(row=0+count,column=1)
            Label(root4,text=str(i[2])).grid(row=0+count,column=2)
            Label(root4,text=str(i[3])).grid(row=0+count,column=3)
            p=Entry(root4)
            p.grid(row=0,column=4)
            def delete(): 
                cur.execute('delete from details where details.id_no=?',(p.get(),))
                p.delete(0,END)
                showinfo('Deleted',"Record Successfully Deleted")
            Button(root4,text='Delete',command=delete).grid(row=0,column=5)
            con.commit()

    

    Button(root1,text="Log",width=7,bd=5,font="times 10 italic  bold",command=call).grid(row=1,column=0)
    Button(root1,text="Add",width=7,bd=5,font="times 10 italic  bold",command=add).grid(row=1,column=1)
    Button(root1,text="Contacts",width=7,font="times 10 italic  bold",bd=5,command=contact).grid(row=1,column=2)
    def show():
        root6=Tk()
        #root6.geometry('300x300')
        root6.title('Show')
        Label(root6,text="Id_no : ").grid(row=1,column=2)
        e1=Entry(root6)
        e1.grid(row=1,column=3)
        Label(root6,text="Name : ").grid(row=2,column=2)
        e2=Entry(root6)
        e2.grid(row=2,column=3)
        Label(root6,text="Phone_no : ").grid(row=3,column=2)
        e3=Entry(root6)
        e3.grid(row=3,column=3)
        Label(root6,text="Email : ").grid(row=4,column=2)
        e4=Entry(root6)
        e4.grid(row=4,column=3)
        global k
        a=(t.get(),)
        cur.execute('select * from details where id_no=?',a)
        res=cur.fetchall()
        e1.insert(0,res[0][0])
        e2.insert(0,res[0][1])
        e3.insert(0,res[0][2])
        e4.insert(0,res[0][3])
        #Label(root6,text=cur.fetchall()).grid(row=k,column=0)
    Button(root1,text="Update ",width=7,height=1,bd=5,font="times 10 italic  bold",command=update).grid(row=2,column=4)   
    Button(root1,text="Search",width=7,height=1,bd=5,font="times 10 italic  bold",command=show).grid(row=1,column=3)
    def clear():
            n.delete(0,END)
    Button(root1,text="clear",width=7,bd=5,font="times 10 italic bold",command=clear).grid(row=2,column=3)
    def insert(x):
        n.insert(12,x)
    Button(root1,text="1",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(1)).grid(row=3,column=0)
    Button(root1,text="2",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(2)).grid(row=3,column=1)
    Button(root1,text="3",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(3)).grid(row=3,column=2)
    Button(root1,text="4",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(4)).grid(row=4,column=0)
    Button(root1,text="5",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(5)).grid(row=4,column=1)
    Button(root1,text="6",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(6)).grid(row=4,column=2)
    Button(root1,text="7",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(7)).grid(row=5,column=0)
    Button(root1,text="8",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(8)).grid(row=5,column=1)
    Button(root1,text="9",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(9)).grid(row=5,column=2)
    Button(root1,text="*",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert('*')).grid(row=6,column=0)
    Button(root1,text="0",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert(0)).grid(row=6,column=1)
    Button(root1,text="#",width=7,height=1,bd=5,font="times 10 bold",command=lambda:insert('#')).grid(row=6,column=2)

a=PhotoImage(file='project.gif')
lb=Label(root,image=a)
lb.after(5000,fun)
lb.grid()


root.mainloop()
