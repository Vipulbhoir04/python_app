from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
from subprocess import call        
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title("Main Detail Page")
root.geometry('1270x685')

'''id = StringVar()
name = StringVar()

transaction_details_frame=LabelFrame(root,text='Transaction Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame.pack(fill=X)
idLabel=Label(transaction_details_frame,text='Your Id',font=('times new roman',15,'bold'),fg='white',bg='grey20')
idLabel.grid(row=0,column=0,padx=20,pady=2)
idEntry=Entry(transaction_details_frame,font=('arial',15),bd=7,width=18,textvariable=id)#,textvariable=rollno)
idEntry.grid(row=0,column=1)

nameLabel=Label(transaction_details_frame,text='Your Name',font=('times new roman',15,'bold'),fg='white',bg='grey20')
nameLabel.grid(row=0,column=2,padx=20,pady=2)
nameEntry=Entry(transaction_details_frame,font=('arial',15),bd=7,width=18,textvariable=name)
nameEntry.grid(row=0,column=3)


typeLabel=Label(transaction_details_frame,text='Type',font=('times new roman',15,'bold'),fg='white',bg='grey20')
typeLabel.grid(row=0,column=4,padx=20,pady=2)
choices=['small','medium','large']
typeEntry=ttk.Combobox(transaction_details_frame,values=choices)
typeEntry.grid(row=0,column=5)


# def GET_DATA():
# 	con=pymysql.connect(host='localhost',user='root',password='',database='python_app')
# 	cur=con.cursor() 
# 	cur.execute('SELECT * FROM ')
# 	rows=cur.fetchall()
  			
# 	if len(rows)!=0: 
#          Student_table.delete(*Student_table.get_children())
#          for row in rows:
#              Student_table.insert('',END,values=row)
#          con.commit()
#          con.close()

getbtn=Button(transaction_details_frame,text='Sumbit',font=('Open Sans',10,'bold'),fg='white',bg='grey20',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=10)
getbtn.grid(row=0,column=6,padx=20,pady=2)
        #or dropdown ke leay
        #option=StringVar()
        #option.set('small')
        #typeEntry=OptionMenu(transaction_details_frame,option,'small','medium','large')
        #typeEntry.grid(row=0,column=5)'''

variableFrame=Frame(root)
variableFrame.pack()
#IP
transaction_details_frame1=LabelFrame(variableFrame,text='IP VAR',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame1.grid(row=0,column=0)
var1label=Label(transaction_details_frame1,text='NT',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var1label.grid(row=0,column=0,pady=14,padx=7)
var2label=Label(transaction_details_frame1,text='RU',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var2label.grid(row=1,column=0,pady=14,padx=7)
var3label=Label(transaction_details_frame1,text='CBE',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var3label.grid(row=2,column=0,pady=14,padx=7)
var4label=Label(transaction_details_frame1,text='OUB',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var4label.grid(row=3,column=0,pady=14,padx=7)
var5label=Label(transaction_details_frame1,text='PD ',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var5label.grid(row=4,column=0,pady=14,padx=7)


#EV
var1ev=IntVar()
var2ev=IntVar()
var3ev=IntVar()
var4ev=IntVar()
var5ev=IntVar()
transaction_details_frame2=LabelFrame(variableFrame,text='EV Entry',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame2.grid(row=0,column=1)
var1Entry=Entry(transaction_details_frame2,textvariable=var1ev,font=('arial',15),bd=7,width=15)
var1Entry.grid(row=0,column=1,pady=9,padx=8)
var2Entry=Entry(transaction_details_frame2,textvariable=var2ev,font=('arial',15),bd=7,width=15)
var2Entry.grid(row=1,column=1,pady=9,padx=8)
var3Entry=Entry(transaction_details_frame2,textvariable=var3ev,font=('arial',15),bd=7,width=15)
var3Entry.grid(row=2,column=1,pady=9,padx=8)
var4Entry=Entry(transaction_details_frame2,textvariable=var4ev,font=('arial',15),bd=7,width=15)
var4Entry.grid(row=3,column=1,pady=9,padx=8)
var5Entry=Entry(transaction_details_frame2,textvariable=var5ev,font=('arial',15),bd=7,width=15)
var5Entry.grid(row=4,column=1,pady=9,padx=8)

#CV
var1cv=IntVar()
var2cv=IntVar()
var3cv=IntVar()
var4cv=IntVar()
var5cv=IntVar()
transaction_details_frame3=LabelFrame(variableFrame,text='CV Entry',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame3.grid(row=0,column=2)
cventry1=Entry(transaction_details_frame3,textvariable=var1cv,font=('arial',15),bd=7,width=15)
cventry1.grid(row=0,column=2,pady=9,padx=8)
cventry2=Entry(transaction_details_frame3,textvariable=var2cv,font=('arial',15),bd=7,width=15)
cventry2.grid(row=1,column=2,pady=9,padx=8)
cventry3=Entry(transaction_details_frame3,textvariable=var3cv,font=('arial',15),bd=7,width=15)
cventry3.grid(row=2,column=2,pady=9,padx=8)
cventry4=Entry(transaction_details_frame3,textvariable=var4cv,font=('arial',15),bd=7,width=15)
cventry4.grid(row=3,column=2,pady=9,padx=8)
cventry5=Entry(transaction_details_frame3,textvariable=var5cv,font=('arial',15),bd=7,width=15)
cventry5.grid(row=4,column=2,pady=9,padx=8)

def calculate_c():
        evvar1=var1ev.get()
        evvar2=var2ev.get()
        evvar3=var3ev.get()
        evvar4=var4ev.get()
        evvar5=var5ev.get()

        cvvar1=var1cv.get()
        cvvar2=var2cv.get()
        cvvar3=var3cv.get()
        cvvar4=var4cv.get()
        cvvar5=var5cv.get()

        cs1res="{:.4f}".format((cvvar1/evvar1)*100)
        cs2res="{:.4f}".format((cvvar2/evvar2)*100)
        cs3res="{:.4f}".format((cvvar3/evvar3)*100)
        cs4res="{:.4f}".format((cvvar4/evvar4)*100)
        cs5res="{:.4f}".format((cvvar5/evvar5)*100)
        
        #current status value block
        var1cs.set(cs1res)
        var2cs.set(cs2res)
        var3cs.set(cs3res)
        var4cs.set(cs4res)
        var5cs.set(cs5res)

        resvar1=(cvvar1/evvar1)*100
        resvar2=(cvvar2/evvar2)*100
        resvar3=(cvvar3/evvar3)*100
        resvar4=(cvvar4/evvar4)*100
        resvar5=(cvvar5/evvar5)*100

        if(resvar1<=50):
                dentryvar1.set('Low')
                ndentryvar1.set('NA')
                ch1=resvar1-50
                ch1res=round(ch1,4)
        elif(resvar1>51 and resvar1<99):
                dentryvar1.set('Medium')
                ndentryvar1.set('NA')
                ch1=resvar1-99
                ch1res==round(ch1,4)
        elif(resvar1>99):
                dentryvar1.set('NA')
                ndentryvar1.set('High')
                ch1=resvar1-100
                ch1res=round(ch1,4)
        if(resvar2>=51 and resvar1<=100):
                dentryvar2.set('Medium')
                ndentryvar2.set('NA')
                ch2=resvar2-99
                ch2res=round(ch2,4)
        elif(resvar2>99):
                dentryvar2.set('NA')
                ndentryvar2.set('High')
                ch2=resvar2-101
                ch2res=round(ch2,4)
        elif(resvar2<=50):
                dentryvar2.set('NA')
                ndentryvar2.set('Low')
                ch2=resvar2-50
                ch2res=round(ch2,4)
        if(resvar3<10):
                dentryvar3.set('Low')
                ndentryvar3.set('NA')
                ch3=resvar3-10
                ch3res=round(ch3,4)
        elif(resvar3==100):
                dentryvar3.set('OK')
                ndentryvar3.set('NA')
                ch3=resvar3-100
                ch3res=round(ch3,4)
        elif(resvar3>10):
                dentryvar3.set('NA')
                ndentryvar3.set('High')
                ch3=resvar3-11
                ch3res=round(ch3,4)
        if(resvar4<5):
                dentryvar4.set('Low')
                ndentryvar4.set('NA')
                ch4=resvar4-5
                ch4res=round(ch4,4)
        elif(resvar4==100):
                dentryvar4.set('OK')
                ndentryvar4.set('NA')
                ch4=resvar4-100
                ch4res=round(ch4,4)
        elif(resvar4>5):
                dentryvar4.set('NA')
                ndentryvar4.set('High')
                ch4=resvar4-6
                ch4res=round(ch4,4)
        if(resvar5>98 and resvar5!=100):
                dentryvar5.set('High')
                ndentryvar5.set('NA')
                ch5=resvar5-99
                ch5res=round(ch5,4)
        elif(resvar5==100):
                dentryvar5.set('OK')
                ndentryvar5.set('NA')
                ch5=resvar5-100
                ch5res=round(ch5,4)
        elif(resvar5<98):
                dentryvar5.set('NA')
                ndentryvar5.set('Low')
                ch5=resvar5-98
                ch5res=round(ch5,4)

        #%C values block
        varc1.set(ch1res)
        varc2.set(ch2res)
        varc3.set(ch3res)
        varc4.set(ch4res)
        varc5.set(ch5res)

        '''chvar1result=Label(transaction_details_frame7, text=ch1res, font=('times new roman',15,'bold'),fg='white',bg='grey20')
        chvar1result.grid(row=0,column=4,pady=14,padx=10)
        chvar2result=Label(transaction_details_frame7, text=ch2res, font=('times new roman',15,'bold'),fg='white',bg='grey20')
        chvar2result.grid(row=1,column=4,pady=14,padx=10)
        chvar3result=Label(transaction_details_frame7, text=ch3res, font=('times new roman',15,'bold'),fg='white',bg='grey20')  
        chvar3result.grid(row=2,column=4,pady=14,padx=10)
        chvar4result=Label(transaction_details_frame7, text=ch4res, font=('times new roman',15,'bold'),fg='white',bg='grey20')
        chvar4result.grid(row=3,column=4,pady=14,padx=10)
        chvar5result=Label(transaction_details_frame7, text=ch5res, font=('times new roman',15,'bold'),fg='white',bg='grey20')
        chvar5result.grid(row=4,column=4,pady=14,padx=10)'''

#CURRENT STATUS BLOCK
var1cs=StringVar()
var2cs=StringVar()
var3cs=StringVar()
var4cs=StringVar()
var5cs=StringVar()

var1cs.set('NULL')
var2cs.set('NULL')
var3cs.set('NULL')
var4cs.set('NULL')
var5cs.set('NULL')

transaction_details_frame4=LabelFrame(variableFrame,text='C S',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame4.grid(row=0,column=3)
csvar1=Label(transaction_details_frame4,textvariable=var1cs,font=('arial',15),bd=7,width=15)
csvar1.grid(row=0,column=2,pady=9,padx=7)
csvar2=Label(transaction_details_frame4,textvariable=var2cs,font=('arial',15),bd=7,width=15)
csvar2.grid(row=1,column=2,pady=9,padx=7)
csvar3=Label(transaction_details_frame4,textvariable=var3cs,font=('arial',15),bd=7,width=15)
csvar3.grid(row=2,column=2,pady=9,padx=7)
csvar4=Label(transaction_details_frame4,textvariable=var4cs,font=('arial',15),bd=7,width=15)
csvar4.grid(row=3,column=2,pady=9,padx=7)
csvar5=Label(transaction_details_frame4,textvariable=var5cs,font=('arial',15),bd=7,width=15)
csvar5.grid(row=4,column=2,pady=9,padx=7)


#D RANGE
dentryvar1=StringVar()
dentryvar2=StringVar()
dentryvar3=StringVar()
dentryvar4=StringVar()
dentryvar5=StringVar()

transaction_details_frame5=LabelFrame(variableFrame,text='D_Range',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame5.grid(row=0,column=4)

dentry1 = ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", width=10, textvariable=dentryvar1)
dentry1["value"]=("Low","Medium","High")
dentry1.grid(row=0,column=1,pady=14,padx=6)

dentry2 = ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", width=10, textvariable=dentryvar2)
dentry2["value"]=("Low","Medium","High")
dentry2.grid(row=1,column=1,pady=14,padx=6)

dentry3=ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", width=10, textvariable=dentryvar3)
dentry3["value"]=("Low","NA","High")
dentry3.grid(row=2,column=1,pady=14,padx=6)

dentry4=ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", width=10, textvariable=dentryvar4)
dentry4["value"]=("Low","NA","High")
dentry4.grid(row=3,column=1,pady=14,padx=6)

dentry5=ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", width=10, textvariable=dentryvar5)
dentry5["value"]=("Low","NA","High")
dentry5.grid(row=4,column=1,pady=14,padx=6)



#ND RANGE
ndentryvar1=StringVar()
ndentryvar2=StringVar()
ndentryvar3=StringVar()
ndentryvar4=StringVar()
ndentryvar5=StringVar()

transaction_details_frame6=LabelFrame(variableFrame,text='ND_Range',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame6.grid(row=0,column=5)

ndentry1=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly", width=10,textvariable=ndentryvar1)
ndentry1["value"]=("Low","Medium","High")
ndentry1.grid(row=0,column=1,pady=14,padx=6)

ndentry2=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly", width=10,textvariable=ndentryvar2)
ndentry2["value"]=("Low","Medium","High")
ndentry2.grid(row=1,column=1,pady=14,padx=6)

ndentry3=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly", width=10,textvariable=ndentryvar3)
ndentry3["value"]=("Low","NA","High")
ndentry3.grid(row=2,column=1,pady=14,padx=6)

ndentry4=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly", width=10,textvariable=ndentryvar4)
ndentry4["value"]=("Low","NA","High")
ndentry4.grid(row=3,column=1,pady=14,padx=6)

ndentry5=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly", width=10,textvariable=ndentryvar5)
ndentry5["value"]=("Low","NA","High")
ndentry5.grid(row=4,column=1,pady=14,padx=6)

#% C BLOCK
varc1=StringVar()
varc2=StringVar()
varc3=StringVar()
varc4=StringVar()
varc5=StringVar()

varc1.set('NULL')
varc2.set('NULL')
varc3.set('NULL')
varc4.set('NULL')
varc5.set('NULL')

transaction_details_frame7=LabelFrame(variableFrame,text='% CHANGES',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame7.grid(row=0,column=6)
csvar1=Label(transaction_details_frame7,textvariable=varc1,font=('arial',15),bd=7,width=15)
csvar1.grid(row=0,column=5,pady=9,padx=7)
csvar2=Label(transaction_details_frame7,textvariable=varc2,font=('arial',15),bd=7,width=15)
csvar2.grid(row=1,column=5,pady=9,padx=7)
csvar3=Label(transaction_details_frame7,textvariable=varc3,font=('arial',15),bd=7,width=15)
csvar3.grid(row=2,column=5,pady=9,padx=7)
csvar4=Label(transaction_details_frame7,textvariable=varc4,font=('arial',15),bd=7,width=15)
csvar4.grid(row=3,column=5,pady=9,padx=7)
csvar5=Label(transaction_details_frame7,textvariable=varc5,font=('arial',15),bd=7,width=15)
csvar5.grid(row=4,column=5,pady=9,padx=7)


#result block function
def result():
        getev1=var1ev.get()
        getev2=var2ev.get()
        getev3=var3ev.get()
        getev4=var4ev.get()
        getev5=var5ev.get()

        getcv1=var1cv.get()
        getcv2=var2cv.get()
        getcv3=var3cv.get()
        getcv4=var4cv.get()
        getcv5=var5cv.get()

        getcs1=var1cs.get()
        getcs2=var2cs.get()
        getcs3=var3cs.get()
        getcs4=var4cs.get()
        getcs5=var5cs.get()

        d1entry=dentryvar1.get()
        d2entry=dentryvar2.get()
        d3entry=dentryvar3.get()
        d4entry=dentryvar4.get()
        d5entry=dentryvar5.get()

        nd1entry=ndentryvar1.get()
        nd2entry=ndentryvar2.get()
        nd3entry=ndentryvar3.get()
        nd4entry=ndentryvar4.get()
        nd5entry=ndentryvar5.get()

        getc1=varc1.get()
        getc2=varc2.get()
        getc3=varc3.get()
        getc4=varc4.get()
        getc5=varc5.get()

        setev1=Label(transaction_details_frame02,text=getev1,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setev1.grid(row=0,column=1,pady=10,padx=10)
        setev2=Label(transaction_details_frame02,text=getev2,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setev2.grid(row=1,column=1,pady=10,padx=10)
        setev3=Label(transaction_details_frame02,text=getev3,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setev3.grid(row=2,column=1,pady=10,padx=10)
        setev4=Label(transaction_details_frame02,text=getev4,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setev4.grid(row=3,column=1,pady=10,padx=10)
        setev5=Label(transaction_details_frame02,text=getev5,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setev5.grid(row=4,column=1,pady=10,padx=10)

        setcv1=Label(transaction_details_frame03,text=getcv1,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcv1.grid(row=0,column=2,pady=10,padx=10)
        setcv2=Label(transaction_details_frame03,text=getcv2,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcv2.grid(row=1,column=2,pady=10,padx=10)
        setcv3=Label(transaction_details_frame03,text=getcv3,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcv3.grid(row=2,column=2,pady=10,padx=10)
        setcv4=Label(transaction_details_frame03,text=getcv4,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcv4.grid(row=3,column=2,pady=10,padx=10)
        setcv5=Label(transaction_details_frame03,text=getcv5,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcv5.grid(row=4,column=2,pady=10,padx=10)

        '''setcs1=Label(transaction_details_frame04,text=getcs1,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcs1.grid(row=0,column=3,pady=10,padx=10)
        setcs2=Label(transaction_details_frame04,text=getcs2,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcs2.grid(row=1,column=3,pady=10,padx=10)
        setcs3=Label(transaction_details_frame04,text=getcs3,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcs3.grid(row=2,column=3,pady=10,padx=10)
        setcs4=Label(transaction_details_frame04,text=getcs4,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcs4.grid(row=3,column=3,pady=10,padx=10)
        setcs5=Label(transaction_details_frame04,text=getcs5,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setcs5.grid(row=4,column=3,pady=10,padx=10)'''

        setdentry1=Label(transaction_details_frame05,text=d1entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setdentry1.grid(row=0,column=3,pady=10,padx=10)
        setdentry2=Label(transaction_details_frame05,text=d2entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setdentry2.grid(row=1,column=3,pady=10,padx=10)
        setdentry3=Label(transaction_details_frame05,text=d3entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setdentry3.grid(row=2,column=3,pady=10,padx=10)
        setdentry4=Label(transaction_details_frame05,text=d4entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setdentry4.grid(row=3,column=3,pady=10,padx=10)
        setdentry5=Label(transaction_details_frame05,text=d5entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setdentry5.grid(row=4,column=3,pady=10,padx=10)

        setndentry1=Label(transaction_details_frame06,text=nd1entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry1.grid(row=0,column=4,pady=10,padx=10)
        setndentry2=Label(transaction_details_frame06,text=nd2entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry2.grid(row=1,column=4,pady=10,padx=10)
        setndentry3=Label(transaction_details_frame06,text=nd3entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry3.grid(row=2,column=4,pady=10,padx=10)
        setndentry4=Label(transaction_details_frame06,text=nd4entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry4.grid(row=3,column=4,pady=10,padx=10)
        setndentry5=Label(transaction_details_frame06,text=nd5entry,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry5.grid(row=4,column=4,pady=10,padx=10)

        setndentry5=Label(transaction_details_frame07,text=getc1,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry5.grid(row=0,column=5,pady=10,padx=10)
        setndentry5=Label(transaction_details_frame07,text=getc2,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry5.grid(row=1,column=5,pady=10,padx=10)
        setndentry5=Label(transaction_details_frame07,text=getc3,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry5.grid(row=2,column=5,pady=10,padx=10)
        setndentry5=Label(transaction_details_frame07,text=getc4,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry5.grid(row=3,column=5,pady=10,padx=10)
        setndentry5=Label(transaction_details_frame07,text=getc5,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        setndentry5.grid(row=4,column=5,pady=10,padx=10)


#result block
variableFrame2=LabelFrame(root,text='RESULT',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
variableFrame2.pack()

transaction_details_frame01=LabelFrame(variableFrame2,text='IP VAR',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame01.grid(row=0,column=0)
var1res=Label(transaction_details_frame01,text='NT',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var1res.grid(row=0,column=0,pady=10,padx=10)
var2res=Label(transaction_details_frame01,text='RU',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var2res.grid(row=1,column=0,pady=10,padx=10)
var3res=Label(transaction_details_frame01,text='CBE',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var3res.grid(row=2,column=0,pady=10,padx=10)
var4res=Label(transaction_details_frame01,text='OUB',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var4res.grid(row=3,column=0,pady=10,padx=10)
var5res=Label(transaction_details_frame01,text='PD',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var5res.grid(row=4,column=0,pady=10,padx=10)

#EV
transaction_details_frame02=LabelFrame(variableFrame2,text='EV',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame02.grid(row=0,column=1)

#CV
transaction_details_frame03=LabelFrame(variableFrame2,text='CV',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame03.grid(row=0,column=2)

#CS
'''transaction_details_frame04=LabelFrame(variableFrame2,text='C S',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame04.grid(row=0,column=3)'''

#D_RANGE
transaction_details_frame05=LabelFrame(variableFrame2,text='D_RANGE',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame05.grid(row=0,column=4)

#ND_RANGE
transaction_details_frame06=LabelFrame(variableFrame2,text='ND_RANGE',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame06.grid(row=0,column=5)

#%C
transaction_details_frame07=LabelFrame(variableFrame2,text='% CHANGES',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame07.grid(row=0,column=6)


#BUTTON

variableFrame1=Frame(root)
variableFrame1.pack()
transaction_details_frame5=LabelFrame(variableFrame1,text="OPTIONS",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame5.grid(row=1,column=0)

#calculate %C button
calc_btn = Button(transaction_details_frame5,text = "Calculate %C",command=calculate_c,font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
calc_btn.grid(row = 1,column = 1,ipadx = 20,padx = 10)

#result button
res_btn = Button(transaction_details_frame5, text="Result", command=result, font=("lucida",12,"bold"),bd = 7, relief = GROOVE)
res_btn.grid(row = 1,column = 2,ipadx = 20, padx = 10)

#exit button       
exit_btn = Button(transaction_details_frame5,text = "Exit",font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = exit)
exit_btn.grid(row = 1,column = 3,ipadx = 20, padx = 10)

root.mainloop()
