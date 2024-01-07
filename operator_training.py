from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime

from move_left import move_left
from bucket_left import bucket_left
from bucket_down import bucket_down
from bucket_up import bucket_up
from bucket_right import bucket_right
from claw_drop import claw_drop
from claw_up import claw_up
from rotation_right import rotation_right
from rotation_left import rotation_left


class operator_training:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Koyala Yantri")
        
        #first Image
        img1=Image.open(r"images/coal2.png")
        img1=img1.resize((130,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=130,height=130)
        
        #second Image
        img=Image.open(r"images/image1_2.jpg")
        img=img.resize((1400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=150,y=0,width=1400,height=130)
        
        

        #background Image
        img3=Image.open(r"images/performance_bg.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #Title=Koyala Yantri
        title_lbl=Label(bg_img,text="Simulation",font=("times new roman",35,"bold"),bg="gray",fg="cyan")
        title_lbl.place(x=0,y=0,width=1530,height=55)

    #==============time===================================
        def time():
            string=strftime('%I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(bg_img,font=('times new roman',14,'bold'),background='violet',foreground='blue')
        lbl.place(x=1400,y=600,width=110,height=50)
        time()

       
        #button 1
        

        b2=Button(bg_img,text="Bucket going Right",cursor="hand2",command=self.button2,font=("times new roman",15,),bg="darkblue",fg="white")
        b2.place(x=1200,y=200,width=220,height=40)

        b3=Button(bg_img,text="Bucket going down",cursor="hand2",command=self.button3,font=("times new roman",15,),bg="darkblue",fg="white")
        b3.place(x=1200,y=300,width=220,height=40)
        
        b4=Button(bg_img,text="Bucket going up",cursor="hand2",command=self.button4,font=("times new roman",15,),bg="darkblue",fg="white")
        b4.place(x=1200,y=400,width=220,height=40)
        
        b5=Button(bg_img,text="Bucket going left",cursor="hand2",command=self.button5,font=("times new roman",15,),bg="darkblue",fg="white")
        b5.place(x=1200,y=500,width=220,height=40)

        b6=Button(bg_img,text="Swing Right to Left",cursor="hand2",command=self.button6,font=("times new roman",15,),bg="darkblue",fg="white")
        b6.place(x=20,y=600,width=220,height=40)

        b8=Button(bg_img,text="claw drop",cursor="hand2",command=self.button8,font=("times new roman",15,),bg="darkblue",fg="white")
        b8.place(x=1200,y=100,width=220,height=40)

        b9=Button(bg_img,text="claw up",cursor="hand2",command=self.button9,font=("times new roman",15,),bg="darkblue",fg="white")
        b9.place(x=600,y=600,width=220,height=40)

        b10=Button(bg_img,text="Swing Left to Right",cursor="hand2",command=self.button10,font=("times new roman",15,),bg="darkblue",fg="white")
        b10.place(x=1100,y=600,width=220,height=40)

        
        
    def open_img(self):
        os.startfile("data")


    #=================EXIT button=======================================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Koyala Yantrik","Are you sure \nYou want to exit application",parent=self.root)
        if self.iExit>0:
           self.root.destroy()
        else:
            return

       
        
    def button2(self):
        self.new_window=Toplevel(self.root)
        self.app=bucket_right(self.new_window)       #done
    
    def button3(self):     
        self.new_window=Toplevel(self.root)           #done
        self.app=bucket_down(self.new_window)
        
    def button4(self):
        self.new_window=Toplevel(self.root)         #done
        self.app=bucket_up(self.new_window)
        
    def button5(self):      
        self.new_window=Toplevel(self.root)         #done
        self.app=bucket_left(self.new_window)
        
    def button6(self):
        self.new_window=Toplevel(self.root)         
        self.app=rotation_left(self.new_window)
        

    def button8(self):                            
        self.new_window=Toplevel(self.root)         #done
        self.app=claw_drop(self.new_window)

    def button9(self):                              #done
        self.new_window=Toplevel(self.root) 
        self.app=claw_up(self.new_window)
        
    def button10(self): 
        self.new_window=Toplevel(self.root)           #done
        self.app=rotation_right(self.new_window)
        
   



if __name__=="__main__":
    root=Tk()
    obj=operator_training(root)
    root.mainloop()