from distutils.util import execute
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox



class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1298x553+235+225')

        ########variabels############
        self.var_contact=StringVar()
        self.var_checkin= StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavilable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdayes = StringVar()
        self.var_paidtex = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        #############title####################
        lbl_title = Label(self.root, text='ROOM BOOKING DETAILS ', font=('times new roman', 18, 'bold'), bg='black',
                          fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1298, height=50)
        ###Logo image
        img2 = Image.open('hotel_logo1.jpeg')
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=2, y=2, width=100, height=40)

        #############label frame###########
        label_frame = LabelFrame(self.root, text="Room booking details", font=("arial", 12, "bold"), relief=RIDGE, bd=2)
        label_frame.place(x=5, y=50, width=425, height=490)

        ##############lavel and entry###############
        #customerref
        lbl_cust_contact=Label(label_frame,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(label_frame,textvariable=self.var_contact,width=20,font=("arial",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        #Fetch data
        btnFetchData=Button(label_frame,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",bd=2,width=10)
        btnFetchData.place(x=347,y=4)

        # Checking_date
        checking_in_date= Label(label_frame, text="Check in date:", font=("arial", 12, "bold"), padx=2, pady=6)
        checking_in_date.grid(row=1, column=0, sticky=W)

        textcheck_in_date = ttk.Entry(label_frame, textvariable=self.var_checkin,width=29, font=("arial", 12, "bold"))
        textcheck_in_date.grid(row=1, column=1)

        #Check_out Date
        lbl_Check_out = Label(label_frame, text="Check out:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0,sticky=W)

        text_Check_out = ttk.Entry(label_frame,textvariable=self.var_checkout,width=29, font=("arial", 12, "bold"))
        text_Check_out.grid(row=2, column=1)

        ## room type combo
        label_room_type = Label(label_frame, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_room_type.grid(row="3", column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomType from details")
        ides = my_cursor.fetchall()

        combo_room = ttk.Combobox(label_frame, textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=27,state="readonly")
        combo_room["value"] = ides
        combo_room.current(0)
        combo_room.grid(row="3", column=1)

        #Avaliable room
        lblRoomAvailable = Label(label_frame, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        #text_RoomAvailable = ttk.Entry(label_frame, textvariable=self.var_roomavilable,width=29, font=("arial", 12, "bold"))
        #text_RoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from details")
        rows = my_cursor.fetchall()

      
        combo_RoomNo = ttk.Combobox(label_frame, textvariable=self.var_roomavilable,font=("arial", 12, "bold"), width=27,state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        #Mail
        lbl_Meale = Label(label_frame, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Meale.grid(row=5, column=0, sticky=W)
        text_Meale = ttk.Entry(label_frame,textvariable=self.var_meal,width=29, font=("arial", 12, "bold"))
        text_Meale.grid(row=5, column=1)

        #No Of Day
        lbl_NoOfDays = Label(label_frame, text="No of Days:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_NoOfDays.grid(row=6, column=0, sticky=W)
        text_NoOfDays = ttk.Entry(label_frame, textvariable=self.var_noofdayes,width=29, font=("arial", 12, "bold"))
        text_NoOfDays.grid(row=6, column=1)
        # paid Text
        lbl_paid = Label(label_frame,font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lbl_paid.grid(row=7, column=0, sticky=W)
        text_paid = ttk.Entry(label_frame,textvariable=self.var_paidtex, width=29, font=("arial", 12, "bold"))
        text_paid.grid(row=7, column=1)

        # Sub total
        lbl_sub_totals = Label(label_frame, font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lbl_sub_totals.grid(row=8, column=0, sticky=W)
        text_sub_totals = ttk.Entry(label_frame, textvariable=self.var_actualtotal,width=29, font=("arial", 12, "bold"))
        text_sub_totals.grid(row=8, column=1)

        # Total cost
        lbl_total_cost = Label(label_frame, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lbl_total_cost.grid(row=9, column=0, sticky=W)
        text_total_cost = ttk.Entry(label_frame, textvariable=self.var_total,width=29, font=("arial", 12, "bold"))
        text_total_cost.grid(row=9, column=1)

        #**********bill Buttons*****************
        btnBill = Button(label_frame, text="Bill",command=self.total, font=("arial", 11, "bold"), bg="black", fg="gold", bd=2, width=10)
        btnBill.grid(row=10, column=0, padx=1,sticky=W)

        ###Btn frame
        btn_frame=Frame(label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=1,y=400,width=412,height=40)

        add_btn=Button(btn_frame,command=self.add_data,text="ADD",font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        add_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,command=self.update_data,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        update_btn.grid(row=0,column=1,padx=1)

        delate_btn=Button(btn_frame,command=self.nDelete,text="Delate",font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        delate_btn.grid(row=0,column=2,padx=1)

        resate_btn = Button(btn_frame, command=self.reset,text="Resate", font=("arial", 11, "bold"), bg="black", fg="gold", bd=2, width=10)
        resate_btn.grid(row=0, column=3, padx=1)
        #####right site image######

        img3 = Image.open('hotel_img5.jpeg')
        img3 = img3.resize((520, 200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)


        ######Tabel Frame search system ######
        Tabel_frame = LabelFrame(self.root, text='View details and Search system', font=('times new roman', 18, 'bold'),bg='white', fg='black', bd=4, relief=RIDGE)
        Tabel_frame.place(x=435, y=280, width=860, height=260)
        ####searcbtn
        search_btn = Label(Tabel_frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        search_btn.grid(row="0", column=0, padx=2)

        self.serch_var = StringVar()
        combo_Search = ttk.Combobox(Tabel_frame, textvariable=self.serch_var, font=("arial", 12, "bold"), width=24,state="readonly")
        combo_Search["value"] = ("Contact", "Room_number")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        textSearch = ttk.Entry(Tabel_frame, textvariable=self.text_search, font=("arial", 12, "bold"), width=24)
        textSearch.grid(row=0, column=2, padx=2)

        Search_btn = Button(Tabel_frame, text="Search",command=self.search, font=("arial", 11, "bold"), bg="black",fg="gold", bd=2, width=10)
        Search_btn.grid(row=0, column=3, padx=1)

        Show_all_btn = Button(Tabel_frame,command=self.fetch_data, text="Show All", font=("arial", 11, "bold"),bg="black", fg="gold", bd=2, width=10)
        Show_all_btn.grid(row=0, column=4, padx=1)

        #########Show data tabel#####

        details_tabel = Frame(Tabel_frame, bd=2, relief=RIDGE)
        details_tabel.place(x=0, y=50, width=850, height=180)

        scroll_x = ttk.Scrollbar(details_tabel, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_tabel, orient=VERTICAL)

        self.room_tabel = ttk.Treeview(details_tabel, column=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays",),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_tabel.xview)
        scroll_y.config(command=self.room_tabel.yview)

        self.room_tabel.heading("contact", text="Contact")
        self.room_tabel.heading("checkin", text="Check-in")
        self.room_tabel.heading("checkout", text="Check-out")
        self.room_tabel.heading("roomtype", text="Room-type")
        self.room_tabel.heading("roomavailable", text="Room No")
        self.room_tabel.heading("meal", text="Meale")
        self.room_tabel.heading("noOfdays", text="NoOfDays")

        self.room_tabel["show"] = "headings"

        self.room_tabel.column("contact", width=100)
        self.room_tabel.column("checkin", width=100)
        self.room_tabel.column("checkout", width=100)
        self.room_tabel.column("roomtype", width=100)
        self.room_tabel.column("roomavailable", width=100)
        self.room_tabel.column("meal", width=100)
        self.room_tabel.column("noOfdays", width=100)

        self.room_tabel.pack(fill=BOTH, expand=1)
        self.room_tabel.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    ##########Add data#######
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get()== "":
            messagebox.showerror('Error', 'All fields are requaired', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavilable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdayes.get()

                                                                                    ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room Booking", parent=self.root)
            except Exception as es:
                messagebox.showerror("warning", f"Some things went to wrong:{str(es)}", parent=self.root)
#########fetch data###########
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_tabel.delete(*self.room_tabel.get_children())
            for i in rows:
                self.room_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    #get_cursor
    def get_cursor(self,events=""):
        cursor_row=self.room_tabel.focus()
        content=self.room_tabel.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavilable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdayes.set(row[6])

    #update
    def update_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="hotel_menagemen_customer")
            my_cursor=conn.cursor()
            my_cursor.execute('update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where contact=%s',(

                                                                                                                            self.var_checkin.get(),
                                                                                                                            self.var_checkout.get(),
                                                                                                                            self.var_roomtype.get(),
                                                                                                                            self.var_roomavilable.get(),
                                                                                                                            self.var_meal.get(),
                                                                                                                            self.var_noofdayes.get(),
                                                                                                                            self.var_contact.get()
                                                                                                                           ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('update','Room details hase been updated successfully',parent=self.root)

    def nDelete(self):
        nDelete = messagebox.askyesno('Hotel Management system', 'Do you want to delete this customer room',parent=self.root)
        if nDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
            my_cursor = conn.cursor()
            query = 'delete from room where contact=%s'
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not nDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavilable.set("")
        self.var_meal.set("")
        self.var_noofdayes.set("")
        self.var_paidtex.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    #****************all data fetch##############
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
            my_cursor = conn.cursor()
            query=("select name from customer where mobiel=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This is Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=455,y=55,width=300,height=180)

                lblName=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                #gender
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
                my_cursor = conn.cursor()
                query = ("select gender from customer where mobiel=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName2 = Label(showdataframe, text="Gender:", font=("arial", 12, "bold"))
                lblName2.place(x=0, y=30)

                lbl2 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)
                #gmail
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
                my_cursor = conn.cursor()
                query = ("select email from customer where mobiel=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName2 = Label(showdataframe, text="Email:", font=("arial", 12, "bold"))
                lblName2.place(x=0, y=60)

                lbl2 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=60)
                #Natinality

                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",
                                               database="hotel_menagemen_customer")
                my_cursor = conn.cursor()
                query = ("select natinality from customer where mobiel=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName2 = Label(showdataframe, text="Natinality:", font=("arial", 12, "bold"))
                lblName2.place(x=0, y=90)

                lbl2 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=90)

                ###Address
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
                my_cursor = conn.cursor()
                query = ("select address from customer where mobiel=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName2 = Label(showdataframe, text="Address:", font=("arial", 12, "bold"))
                lblName2.place(x=0, y=120)

                lbl2 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=120)
    

                # id number
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",
                                               database="hotel_menagemen_customer")
                my_cursor = conn.cursor()
                query = ("select idnumber from customer where mobiel=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName2 = Label(showdataframe, text="ID Number:", font=("arial", 12, "bold"))
                lblName2.place(x=0, y=150)

                lbl2 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=150)

    #### search
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from  room where ' + str(self.serch_var.get()) + " LIKE'%" + str(self.text_search.get() + "%'"))
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.room_tabel.delete(*self.room_tabel.get_children())
            for i in rows:
                self.room_tabel.insert("", END, values=i)
                conn.commit()
            conn.close()


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdayes.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfirst" and self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdayes.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtex.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinear" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdayes.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtex.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lanch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(400)
            q3=float(self.var_noofdayes.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtex.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfirst" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdayes.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtex.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        











if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()