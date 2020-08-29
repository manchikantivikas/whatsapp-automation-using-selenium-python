# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:29:31 2020
lf.who_goes_first = tkinter.StringVar(None, "B")

@author: Vikas
"""

import tkinter as tk
from tkinter import *
from tkinter import filedialog
contactlist=""
image=""
document=""
inputmessage=""
imb=0
docb=0
sendmessb=0
sendmessrandb=0
sendmesspersonalb=0

def switchButtonState():
    global imb,docb,sendmessb,sendmesspersonalb,sendmessrandb
    if(imgradio.get()==1):
        imgbutton['state']=tk.NORMAL
        imb=1
    elif(imgradio.get()==0):
        imgbutton['state']=tk.DISABLED
        imb=0
    if(docradio.get()==1):
        docbutton['state']=tk.NORMAL
        docb=1
    elif(docradio.get()==0):
        docbutton['state']=tk.DISABLED
        docb=0
    if(messradio.get()==1):
        messrand['state']=tk.NORMAL
        messpersonal['state']=tk.NORMAL
        sendmessb=1
        #sendmesspersonalb=1
        #sendmessrandb=1
    elif(messradio.get()==0):
        messrand['state']=tk.DISABLED
        messpersonal['state']=tk.DISABLED
        sendmessb=0
        sendmesspersonalb=0
        sendmessrandb=0
        buttontypelabel.grid_forget()

    if(mess.get()=="1"):
        message['state']=tk.NORMAL
        sendmesspersonalb=1
        sendmessrandb=0
    elif(mess.get()=="0"):
        message['state']=tk.DISABLED
        sendmesspersonalb=0
        sendmessrandb=1
        messtypelabel.grid_forget()
        buttontypelabel.grid_forget()

def retrieve_input():
    global contactlist,image,document,inputmessage,imb,docb,sendmessb,sendmesspersonalb,sendmessrandb
    l1=[contactlist,image,document,inputmessage,imb,docb,sendmessb,sendmesspersonalb,sendmessrandb]
    l2=["contactlist","image","document","inputmessage","imb","docb","sendmessb","sendmesspersonalb","sendmessrandb"]
    inputmessage=message.get("1.0","end-1c")
    #print(inputmessage)
    #if(len(inputmessage)>0):
    #    print("False")
    #else:print("True")
    '''print(contactlist)
    print(image)
    print(document)
    #contactlist,image,document=selectfile("retrieve")'''
    for i in range(len(l1)):
        s=str(l1[i])
        print(l2[i],s)
    vanishwindow()


def selectfile(event):
    global contactlist,image,document,inputmessage
    if(event=="phonebutton"):
        window.filename=filedialog.askopenfilename(title="select a file",filetypes=(("Custom Files",".xlsx"),("All Files","*.*")))
        s=window.filename
        contactlist=s
        s=s.split("/")
        phonenumlist= s[len(s)-1] 
        phonenamelabel.config(text = phonenumlist,fg="black")
        s.clear()
        
    
    if(event=="imgbutton"):
        window.filename=filedialog.askopenfilename(title="select a file",filetypes=(("Custom Files",".png and .jpg"),("All Files","*.*")))
        s=window.filename
        image=0
        image=s
        s=s.split("/")
        selection = s[len(s)-1] 
        imgnamelabel.config(text = selection,fg="black")
        s.clear()
    
    if(event=="docbutton"):
        window.filename=filedialog.askopenfilename(title="select a file",filetypes=(("Custom Files",".pdf and .xlsx and .txt and .doc"),("All Files","*.*")))
        s=window.filename
        document=0
        document=s
        s=s.split("/")
        selection = s[len(s)-1] 
        docnamelabel.config(text = selection,fg='black')
        s.clear()
    



def vanishwindow():
    global contactlist,image,document,inputmessage,imb,docb,sendmessb,sendmesspersonalb,sendmessrandb
    l1=[-1,-1,-1,-1,-1]
    if len(contactlist)<=0:
        #tk.messagebox.showinfo('Window Title',"select phone number list")
        l1[0]=0
        phonenamelabel.config(text="*choose file to submit",fg="red")
    else:
        selectfile(phonebutton)
        l1[0]=1
    if len(image)<=0 and imb==1:
        imgnamelabel.config(text="*choose file to submit",fg="red")
        l1[1]=0
    else:
        selectfile(imgbutton)
        l1[1]=1
    if len(document)<=0 and docb==1:
        docnamelabel.config(text="*choose file to submit",fg="red")
        l1[2]=0
    else:
        selectfile(docbutton)
        l1[2]=1
    if(sendmessb==1 and sendmessrandb==0 and sendmesspersonalb==0):
        buttontypelabel.config(text="*select type of message",fg="red")
        buttontypelabel.grid(row=8,column=2,sticky="w")
        l1[3]=0
    else:
        #switchButtonState()
        buttontypelabel.grid_forget()
        l1[3]=1
    if(sendmesspersonalb==1 and len(inputmessage)<=0):
        messtypelabel.config(text="*enter message",fg="red")
        messtypelabel.grid(row=9,column=2,sticky="w")
        l1[4]=0
    else:
        l1[4]=1
    print(l1)    
    print("=========================================")
    if 0 not in l1:
        window.destroy()

window=tk.Tk()

window.geometry("600x600")
window.resizable(0, 0)
window.title("WhatsappGUI")
window.config(bg="white")
window.iconbitmap(r"C:\Users\Vikas\Desktop\tkinter\Whatsappicon.ico")

phonelabel=tk.Label(text="Select the phone numbers:",font=("Times", 13,"bold"),bg="white").grid(row=0,column=0,sticky="w")
phonebutton=tk.Button(text="Select",width="11",font=("Times", 11),relief=GROOVE,command=lambda:selectfile("phonebutton"))#,command=selectfile)
phonebutton.grid(row=1,column=0,sticky="e")
phonenamelabel=tk.Label(window,text="No file choosen",bg="white")
phonenamelabel.grid(row=1,column=1,sticky="w")

imglabel=tk.Label(text="want to send image:",font=("Times",13,"bold"),bg="white").grid(row=2,column=0,sticky="w")
imgradio = IntVar()
imgR1 = tk.Radiobutton(window, text="Yes", value=1, var=imgradio,command=switchButtonState,bg="white").grid(row=2,column=1,sticky="w")
imgR2 = tk.Radiobutton(window, text="No",  value=0, var=imgradio,command=switchButtonState,bg="white").grid(row=2,column=2,sticky="e",padx="45")
imgbutton = tk.Button(window, text="Select",width="11",font=("Times", 11),state=tk.DISABLED,relief=GROOVE,command=lambda:selectfile("imgbutton"))
imgbutton.grid(row=3,column=0,sticky="e")
imgnamelabel=tk.Label(window,text="No file choosen",bg="white")
imgnamelabel.grid(row=3,column=1,sticky="w")

docradio=IntVar()
doclabel=tk.Label(text="want to send document:",font=("Times",13,"bold"),pady="15",padx="1",bg="white").grid(row=4,column=0,sticky="w")
docR1 = tk.Radiobutton(window, text="Yes", value=1, var=docradio,command=switchButtonState,bg="white").grid(row=4,column=1,sticky="w")
docR2 = tk.Radiobutton(window, text="No",  value=0, var=docradio,command=switchButtonState,bg="white").grid(row=4,column=2,sticky="e",padx="45")
docbutton = tk.Button(window, text="Select",width="11",font=("Times", 11),state=tk.DISABLED,relief=GROOVE,command=lambda:selectfile("docbutton"))
docbutton.grid(row=5,column=0,sticky="e")
docnamelabel=tk.Label(window,text="No file choosen",bg="white")
docnamelabel.grid(row=5,column=1,sticky="w")

messlabel=tk.Label(text="want to send message:",font=("Times",13,"bold"),pady="15",padx="1",bg="white").grid(row=6,column=0,sticky="w",pady="10")
messradio=tk.IntVar()
messR1 = tk.Radiobutton(window, text="Yes", value=1, var=messradio,command=switchButtonState,bg="white").grid(row=6,column=1,sticky="w")
messR2 = tk.Radiobutton(window, text="No",  value=0, var=messradio,command=switchButtonState,bg="white").grid(row=6,column=2,sticky="e",padx="45")



mess = tk.StringVar()
messrand=tk.Radiobutton(window,text="Send random message",value="0",var=mess,indicator=0,bg="light blue",width="17",state=tk.DISABLED,command=switchButtonState)
messrand.grid(row=7,column=1)
messpersonal=tk.Radiobutton(window,text="Send personal message",value="1",var=mess,indicator=0,bg="light blue",width="17",state=tk.DISABLED,command=switchButtonState)
messpersonal.grid(row=8,column=1)
buttontypelabel=tk.Label(window,bg="white")
buttontypelabel.grid(row=8,column=2,sticky="e")


message=tk.Text(window,bg="white",width="22",height="7",padx="2",state=tk.DISABLED)
message.grid(row=9,column=1,pady="22",sticky="w")
message.config(highlightbackground="#66ffff",highlightthickness="3",highlightcolor="#66ffff")
messtypelabel=tk.Label(window,bg="white")
messtypelabel.grid(row=9,column=2,sticky="e")

submit=tk.Button(window,text="submit",height=1, width=10,command=lambda: retrieve_input(),padx="17")
submit.grid(row=10,column=1,pady="12",sticky="w",padx="22")
window.mainloop()
