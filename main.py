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

from engine_heat import engine_heat
from environment_awareness import environment_awareness
from operator_training import operator_training
from digging_depth import digging_depth
from cost_calculation import cost_calculation
from digging_monitoring import digging_monitoring




def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Koyala Yantrik")

        #background Image
        img=Image.open(r"images/bgimage.png")
        img=img.resize((1530,795),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=795)

        frame=Frame(self.root,bg="green")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"images/image30.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="green",borderwidth=0,)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="green")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="green")
        username.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="green")
        password.place(x=40,y=225)

        self.textpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textpass.place(x=40,y=250,width=270)

        #========================Icon images==========================
        img2=Image.open(r"images/image30.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="green",borderwidth=0,)
        lblimg2.place(x=650,y=325,width=25,height=25)
        #===========================Login button=====================
        loginbtn=Button(frame,command=self.login1,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #==========================Register button===================
        loginbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="green",activeforeground="white",activebackground="green")
        loginbtn.place(x=20,y=350,width=160)

        #==========================Forgot password button===================
        loginbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="green",activeforeground="white",activebackground="green")
        loginbtn.place(x=10,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login1(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All Field Required")
        elif self.textuser.get()=="Abhishek" and self.textpass.get()=="007":
            messagebox.showinfo("Success","Welcome to Smart Attendance")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Satara@123",database="face")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.textuser.get(),
                                                                                    self.textpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=dashboard(self.new_window)
                else:
                    if not open_main():
                        return
            conn.commit()
            conn.close()

#===========================reset password====================================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Satara@123",database="face")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.textuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.textuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()


#===========================forgot password window===========================

    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Satara@123",database="face")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your friend name","your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=120,y=290,width=100)



            
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Koyala Yantri")
        #========================================varibles
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #background Image
        img=Image.open(r"images/coal1.jpg")
        img=img.resize((1530,795),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=795)

        #Left Image
        img1=Image.open(r"images/coal2.png")
        img1=img1.resize((470,550),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img1=Label(self.root,image=self.photoimg1)
        bg_img1.place(x=120,y=100,width=470,height=550)


        #========main frame=========================
        frame=Frame(self.root,bg="white")
        frame.place(x=590,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        #=======label and entry=====================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #=============================second row============================
        contact=Label(frame,text="Contact No:",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #=============================third row===============================
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your friend name","your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #===========================row4===========================
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #============================checkbutton============================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions",font=("times new roman",12,"bold"))
        self.checkbtn.place(x=50,y=380)

        #===========================buttons=================================
        img4=Image.open(r"images/image31.jpeg")
        img4=img4.resize((300,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimg4,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=300,height=100)

        img5=Image.open(r"images/image32.png")
        img5=img5.resize((300,100),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(frame,image=self.photoimg5,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=420,width=300,height=100)

        #============================Function declaration======================
    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()==""or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Satara@123",database="face")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")


    def return_login(self):
        self.root.destroy()

class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("dashboard")

         
        
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
        title_lbl=Label(bg_img,text="Koyla Yantrik",font=("times new roman",35,"bold"),bg="gray",fg="cyan")
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
        img11=Image.open(r"images/advantage1.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.button1)
        b1.place(x=1200,y=380,width=220,height=220)
        b1=Button(bg_img,text="Environmental Awareness",cursor="hand2",command=self.button1,font=("times new roman",15,),bg="darkblue",fg="white")
        b1.place(x=1200,y=580,width=220,height=40)
        
        #button 2
        img12=Image.open(r"images/depth.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        b2=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.button2)
        b2.place(x=1200,y=100,width=220,height=220)
        b2=Button(bg_img,text="Dragline bench designing",cursor="hand2",command=self.button2,font=("times new roman",15,),bg="darkblue",fg="white")
        b2.place(x=1200,y=320,width=220,height=40)
        
        #button 3
        img13=Image.open(r"images/cost_calc.png")
        img13=img13.resize((220,220),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        b2=Button(bg_img,image=self.photoimg13,cursor="hand2",command=self.button3)
        b2.place(x=880,y=100,width=220,height=220)
        b2=Button(bg_img,text="Dragline Cost Calculation",cursor="hand2",command=self.button3,font=("times new roman",15,),bg="darkblue",fg="white")
        b2.place(x=880,y=320,width=220,height=40)
        
        
        #button 4
        img14=Image.open(r"images/advantage4.jpg")
        img14=img14.resize((220,220),Image.ANTIALIAS)
        self.photoimg14=ImageTk.PhotoImage(img14)
        b4=Button(bg_img,image=self.photoimg14,cursor="hand2",command=self.button4)
        b4.place(x=880,y=380,width=220,height=220)
        b4=Button(bg_img,text="Operator Training",cursor="hand2",command=self.button4,font=("times new roman",15,),bg="darkblue",fg="white")
        b4.place(x=880,y=580,width=220,height=40)
        
        #button 5      
        img15=Image.open(r"images/engineheat.jpeg")
        img15=img15.resize((220,220),Image.ANTIALIAS)
        self.photoimg15=ImageTk.PhotoImage(img15)
        b5=Button(bg_img,image=self.photoimg15,cursor="hand2",command=self.button5)
        b5.place(x=550,y=380,width=220,height=220)
        b5=Button(bg_img,text="Temperature Monitoring",cursor="hand2",command=self.button5,font=("times new roman",15,),bg="darkblue",fg="white")
        b5.place(x=550,y=580,width=220,height=40)
        
         #button 6      
        img16=Image.open(r"images/digging_monitoring.jpg")
        img16=img16.resize((220,220),Image.ANTIALIAS)
        self.photoimg16=ImageTk.PhotoImage(img16)
        b6=Button(bg_img,image=self.photoimg16,cursor="hand2",command=self.button6)
        b6.place(x=550,y=100,width=220,height=220)
        b6=Button(bg_img,text="Digging Monitoring",cursor="hand2",command=self.button6,font=("times new roman",15,),bg="darkblue",fg="white")
        b6.place(x=550,y=320,width=220,height=40)
        
        
        
        

    def open_img(self):
        os.startfile("data")


    #=================EXIT button=======================================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Koyala Yantrik","Are you sure \nYou want to exit application",parent=self.root)
        if self.iExit>0:
           self.root.destroy()
        else:
            return

       
        #=============================function button==============
    def button1(self):
        self.new_window=Toplevel(self.root)
        self.app=environment_awareness(self.new_window)
        
    def button2(self):
        self.new_window=Toplevel(self.root)
        self.app=digging_depth(self.new_window)
        
    def button3(self):
        self.new_window=Toplevel(self.root)
        self.app=cost_calculation(self.new_window)   
   
    def button4(self):
        self.new_window=Toplevel(self.root)
        self.app=operator_training(self.new_window)
        
    def button5(self):
        self.new_window=Toplevel(self.root)
        self.app=engine_heat(self.new_window)
        
    def button6(self):
        self.new_window=Toplevel(self.root)
        self.app=digging_monitoring(self.new_window)




if __name__=="__main__":
    main()
