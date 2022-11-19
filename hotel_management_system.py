from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from detailsRoom import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1550x800+0+0')

        ###first Image

        img1=Image.open('hotel_img8.jpeg')
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        ###Logo image

        img2 = Image.open('hotel_logo1.jpeg')
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=240, height=140)


        #########title#####
        lbl_title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #######  main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=800)

        ##########Menu#############
        lbl_title = Label(main_frame, text='MENU', font=('times new roman', 20, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=230)

        ###btn frame
        btn_frame = Frame(main_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=230, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.Cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=2)

        room_btn= Button(btn_frame, command=self.roombooking,text="ROOM", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=2)

        details_btn = Button(btn_frame, command=self.details_Room,text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=2)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",  fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=2)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=2)

        #########RIGHTSITRE IMAGE###########
        img3 = Image.open('hotel_img2.jpeg')
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1310, height=590)

        ###########down image############
        img4 = Image.open('hotel_img4.jpeg')
        img4 = img4.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=200)

        img5 = Image.open('hotel_img8.jpeg')
        img5 = img5.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=425, width=230, height=200)



    def Cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)
        
    def details_Room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)



if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()