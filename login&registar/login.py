from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from hotel_management_system import HotelManagementSystem


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("login")
        self.bg=ImageTk.PhotoImage(file="images (17).jpeg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("user_icon6.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimag1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimag1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        ######Label
        username=lbl=Label(frame,text="username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.textuser=Entry(frame,font=("times new roman",15,"bold"))
        self.textuser.place(x=40,y=180,width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.textpass = Entry(frame, font=("times new roman", 15, "bold"))
        self.textpass.place(x=40, y=250, width=270)

        ##Icon
        img2 = Image.open("user_icon6.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimag2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimag2.place(x=650, y=323, width=25, height=25)


        img3 = Image.open("lock_icon1.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimag3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimag3.place(x=650, y=394, width=25, height=25)

        ###Login btn
        logging_btn=Button(frame,command=self.login,text="login",font=("times new roman","15","bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="blue")
        logging_btn.place(x=110,y=300,width=120,height=35)
        ###registar
        register_btn = Button(frame, text="New user Registretion", command=self.register_window, font=("times new roman", "10", "bold"),borderwidth=0 ,fg="white", bg="black", activeforeground="white", activebackground="black")
        register_btn.place(x=15, y=350, width=160)
        ###forget btn
        forgetbtn = Button(frame, text="Forget Password", font=("times new roman", "10", "bold"),borderwidth=0 , fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=0, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","all field requird")
        elif self.textuser.get()=="mdjohir" and self.textpass.get()=="481826@48":
            messagebox.showinfo("Success","Wellcome to our community")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",
                                           database="hotel_menagemen_customer")
            my_cursor = conn.cursor()
            Query = ("select * from register where email=%s and password=%s",(
                self.var_email.get(),
                self.var_pass.get()
            ))

            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()






class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Register')
        self.root.geometry('1550x800+0+0')

        ####### variables#########
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background image#######
        self.bg = ImageTk.PhotoImage(file="images (100).jpeg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left image#######
        self.bg1 = ImageTk.PhotoImage(file="images (16).jpeg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        ######### main frame######
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen",
                             bg="white")
        register_lbl.place(x=20, y=20)

        #### labels entry fields####

        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)

        self.txt_l_name = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_l_name.place(x=370, y=130, width=250)

        ###Rows2########

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        ###Rows3########

        security_Q = Label(frame, text="Select secqurity Qustions", font=("times new roman", 15, "bold"),
                           bg="white")
        security_Q.place(x=50, y=240)

        self.combo_sequrity_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new roman", 15, "bold"), state="readonly")
        self.combo_sequrity_Q["values"] = ("Select", "Your Birth place", "Your Girlfriend name", "your nick name")
        self.combo_sequrity_Q.place(x=50, y=270, width=250)
        self.combo_sequrity_Q.current(0)

        security_a = Label(frame, text="secqurity Answer", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        security_a.place(x=370, y=240)

        self.txt_secqurity = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_secqurity.place(x=370, y=270, width=250)

        ########rows 4#####
        paswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        paswd.place(x=50, y=310)

        self.txt_paswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_paswd.place(x=50, y=340, width=250)

        confirm_paswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                              fg="black")
        confirm_paswd.place(x=370, y=310)

        self.txt_confirm_paswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_paswd.place(x=370, y=340, width=250)

        ########## check button###############
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree Terms & condition",
                                    font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        ######### Button###############
        img = Image.open("register.jpeg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2",
                    font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=50, y=420, width=200)

        img1 = Image.open("images (20).jpeg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2",
                    font=("times new roman", 15, "bold"))
        b1.place(x=350, y=420, width=200)

        #######*******function diclaretion************#

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are requard")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",
                                           database="hotel_menagemen_customer")
            my_cursor = conn.cursor()
            Query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(Query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User allready exiest,please try another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
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
            messagebox.showinfo("Success", "Register Successfully")


if __name__=="__main__":
    main()

