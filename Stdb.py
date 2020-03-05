from tkinter import *
import mysql.connector
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ssssss",
  database="db1"
  
)
cur=mydb.cursor()
s="CREATE TABLE IF NOT EXISTS stdapp(stdno integer(4),stdname varchar(30))"
cur.execute(s)



def add():
    
    
    try:
      a=int(e1.get())
      b=e2.get()
      c=float(e3.get())
      
      if b=="" :
          messagebox.showinfo("Required","Please Input All Fields")
      else:
        
        cur=mydb.cursor()
        s="INSERT INTO  stdapp(stdno,stdname) VALUES(%s,%s,%s)"
        b1=(a,b,c)
        cur.execute(s,b1)
        mydb.commit()
        
    except ValueError:
        messagebox.showinfo("Error")

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()
    


def closescrn1():
    rt.destroy()

def closescrn2():
    rot.destroy()
def closescrn3():
    rooot.destroy()

def closescrn4():
    roooot.destroy()
def closescrn5():
    r.destroy()

def updateemp():
    
    i=e5.get()
    j=e6.get()
    s="UPDATE stdapp WHERE stdname=%s"
    u=(j,i)
    cur.execute(s,u)
    x=cur.rowcount
    if x==0:
        messagebox.showinfo("Error","Not Found")
    else:
        messagebox.showinfo("Done","Successfully Updated rows:"+str(x))
    

    mydb.commit()
    e5.delete(0,END)
    e6.delete(0,END)
    e4.delete(0,END)
    e4.focus()

def search():
    t1.delete("1.0",END)
    s="SELECT * FROM stdapp where stdname LIKE '%s' "
    i=en1.get()
    cur.execute(s%(i))
    result=cur.fetchall()
    st=""
    for j in result:
        for u in j:
            st+=str(u)+" "
    if st=="":
        t1.insert(END,"Not Found!")
    else:
        t1.insert(END,st)       
            
    

def remove():
    rem=ent.get()
    ent.delete(0,END)
    tet.delete('1.0',END)
    s="DELETE FROM stdapp WHERE stdname=%s"
    cur.execute(s,(rem,))
    x=cur.rowcount
    if x==0:
        tet.insert(END,"Not Found")
    else:
        tet.insert(END,"Deleted rows:"+str(x))
    
    
    
    
    mydb.commit()



def dotask():
    a=var.get()
    if a==1:
        global rt
        rt=Tk()
        rt.title("Add Student")
        w=400
        h=390
        ws = rt.winfo_screenwidth()
        hs = rt.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        rt.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rt.resizable(0,0)
        rt.configure(bg="black")
       

        lbl2=Label(rt,text=" Add   Student ",relief="ridge",font="Arial 18 bold",fg="white",bg="black")
        lbl2.place(x=110,y=20)

        lbl3=Label(rt,text="Studnet No:",font="Arial 13 bold",fg="white",bg="black")

        lbl3.place(x=50,y=85)


        lbl4=Label(rt,text="Student Name:",font="Arial 13 bold",fg="white",bg="black")

        lbl4.place(x=50,y=135)

        
        global e1,e2,e3
        e1=Entry(rt,width=25)
        e1.place(x=175,y=85)

        e2=Entry(rt,width=25)
        e2.place(x=175,y=135)

        e3=Entry(rt,width=25)
        e3.place(x=175,y=185)

        btn1=Button(rt,text="Add Student",command=add,font="Arial 10 bold",bg="red")
        btn1.place(x=80,y=245)

        btn2=Button(rt,text="Go Back",font="Arial 10 bold",command=closescrn1,bg="red")
        btn2.place(x=220,y=245)


    elif a==2:
        global rot
        rot=Tk()
        rot.title("Search Student")
        w=400
        h=390
        ws = rot.winfo_screenwidth()
        hs = rot.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        rot.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rot.resizable(0,0)
        rot.configure(bg="black")
       

        l2=Label(rot,text=" Search   Student ",relief="ridge",font="Arial 18 bold",fg="white",bg="black")
        l2.place(x=90,y=20)

        lbl4=Label(rot,text="Student Name:",font="Arial 13 bold",fg="white",bg="black")

        lbl4.place(x=50,y=85)
        global en1
        en1=Entry(rot,width=25)
        en1.place(x=175,y=85)

        butn1=Button(rot,text="Search",font="Arial 11 bold",command=search,bg="red")
        butn1.place(x=105,y=145)

        butn2=Button(rot,text="Go Back",font="Arial 11 bold",command=closescrn2,bg="red")
        butn2.place(x=205,y=145)
        global t1
        t1=Text(rot,width=35,height=6)
        t1.place(x=50,y=200)
    elif a==3:
        global rooot
        rooot=Tk()
        rooot.title("Show All Students")
        w=400
        h=390
        ws = rooot.winfo_screenwidth()
        hs = rooot.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        rooot.geometry('%dx%d+%d+%d' % (w, h, x, y))
        rooot.resizable(0,0)
        
        rooot.configure(bg="black")

        l2=Label(rooot,text="  Show All Students  ",relief="ridge",font="Arial 18 bold",fg="white",bg="black")
        l2.place(x=80,y=20)


        global t2
        t2=Text(rooot,width=35,height=15)
        t2.place(x=75,y=85)

        t2.delete("1.0",END)
        
        s="SELECT * FROM stdapp"
        cur.execute(s)
        result=cur.fetchall()
        for rec in result:
            for i in rec:
               t2.insert(END,str(i)+" ")
            t2.insert(END,"\n\n")
        butn2=Button(rooot,text="Go Back",font="Arial 11 bold",command=closescrn3,bg="red")
        butn2.place(x=175,y=345)

    elif a==4:
        global roooot
        roooot=Tk()
        roooot.title("Update Studentdetails")
        w=400
        h=390
        ws = roooot.winfo_screenwidth()
        hs = roooot.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        roooot.geometry('%dx%d+%d+%d' % (w, h, x, y))
        roooot.resizable(0,0)
        roooot.configure(bg="black")
       

        lbl2=Label(roooot,text=" Update   Studentdetails ",relief="ridge",font="Arial 18 bold",fg="white",bg="black")
        lbl2.place(x=80,y=20)

        lbl3=Label(roooot,text="Student ID:",font="Arial 13 bold",fg="white",bg="black")

        lbl3.place(x=50,y=85)


        lbl4=Label(roooot,text="Student Name:",font="Arial 13 bold",fg="white",bg="black")

        lbl4.place(x=50,y=135)

        
        global e4,e5,e6
        e4=Entry(roooot,width=25)
        e4.place(x=175,y=85)

        e5=Entry(roooot,width=25)
        e5.place(x=175,y=135)

        e6=Entry(roooot,width=25)
        e6.place(x=175,y=185)

        btne1=Button(roooot,text="Update Emp",command=updateemp,font="Arial 10 bold",bg="red")
        btne1.place(x=80,y=245)

        btne2=Button(roooot,text="Go Back",font="Arial 10 bold",command=closescrn4,bg="red")
        btne2.place(x=220,y=245)

        
        
    elif a==5:
        global r
        r=Tk()
        r.title("Delete Employee")
        w=400
        h=390
        ws = r.winfo_screenwidth()
        hs = r.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        r.geometry('%dx%d+%d+%d' % (w, h, x, y))
        r.resizable(0,0)
        
        r.configure(bg="black")

        l2=Label(r,text=" Delete Student ",relief="ridge",font="Arial 18 bold",fg="white",bg="black")
        l2.place(x=100,y=20)

        l3=Label(r,text="Student Name",font="Arial 14 bold",fg="white",bg="black")
        l3.place(x=125,y=95)
        global ent 
        ent=Entry(r,width=25)
        ent.place(x=125,y=130)

        b1=Button(r,text="Remove",font="Arial 10 bold",command=remove,bg="red")
        b1.place(x=129,y=165)

        b2=Button(r,text="Go Back",font="Arial 10 bold",command=closescrn5,bg="red")
        b2.place(x=209,y=165)
        global tet
        tet=Text(r,width=20,height=4,font="Arial 10 bold")
        tet.place(x=125,y=205)

        
    elif a==6:
         ans=messagebox.askyesno("Quitting","Are you sure you want to Quit")
         if ans==True:
             global root
             root.destroy()
            
         

        


        


        
        
        
        
 

root = Tk()
root.title("Employee Management System")
w=550
h=500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
# calculate position x, y
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(0,0)
root.configure(bg="black")

lbl1=Label(root,text=" Select   Your   Choice ",relief="ridge",font="Arial 18 bold",bg="black",fg="white")
lbl1.place(x=140,y=20)


var = IntVar()
R1 = Radiobutton(root, variable=var,bg="black", value=1,command=dotask)
R1.place(x=160,y=100)


R2 = Radiobutton(root, variable=var,bg="black", value=2,command=dotask)

R2.place(x=160,y=160)
R3 = Radiobutton(root, variable=var,bg="black", value=3,command=dotask)
R3.place(x=160,y=220)

R4 = Radiobutton(root, variable=var,bg="black", value=4,command=dotask)
R4.place(x=160,y=280)
R5 = Radiobutton(root, variable=var,bg="black", value=5,command=dotask)
R5.place(x=160,y=340)

R6 = Radiobutton(root, variable=var,bg="black", value=6,command=dotask)

R6.place(x=160,y=400)


lbl2=Label(root,text="Add  Employee",font="Arial 15 bold",bg="black",fg="white")
lbl2.place(x=190,y=100)


lbl3=Label(root,text="Search  Employee",font="Arial 15 bold",bg="black",fg="white")
lbl3.place(x=190,y=160)


lbl4=Label(root,text="Show All Employees",font="Arial 15 bold",bg="black",fg="white")
lbl4.place(x=190,y=220)

lbl5=Label(root,text="Update  Employee",font="Arial 15 bold",bg="black",fg="white")
lbl5.place(x=190,y=280)

lbl6=Label(root,text="Delete  Employee",font="Arial 15 bold",bg="black",fg="white")
lbl6.place(x=190,y=340)


lbl7=Label(root,text="Quit",font="Arial 15 bold",bg="black",fg="white")
lbl7.place(x=190,y=400)








root.mainloop()
