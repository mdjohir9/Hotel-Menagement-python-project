from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1298x553+235+225')

        # **************variable*********#
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email= StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()





#############title####################
        lbl_title = Label(self.root, text='Add Customer Details', font=('times new roman', 18, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1298, height=50)
        ###Logo image
        img2 = Image.open('hotel_logo1.jpeg')
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=2, y=2, width=100, height=40)

        #############label frame###########
        label_frame=LabelFrame(self.root,text="Customer details",font=("arial",12,"bold"),relief=RIDGE,bd=2)
        label_frame.place(x=5,y=50,width=425,height=490)

        ##############lavel and entry###############
        #customerref
        lbl_cust_relif=Label(label_frame,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_relif.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(label_frame,textvariable=self.var_ref,width=29,state="readonly",font=("arial",12,"bold"))
        entry_ref.grid(row=0,column=1)

        ##########customer name##########
        lbl_cust_name = Label(label_frame, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0,sticky=W)
        lbl_cust_name = ttk.Entry(label_frame,textvariable=self.var_cust_name,width=29, font=("arial", 12, "bold"))
        lbl_cust_name.grid(row=1, column=1)

        ####customer mother name#############
        lbl_cust_mothe_name = Label(label_frame, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_mothe_name.grid(row=2, column=0,sticky=W)
        text_mother_name = ttk.Entry(label_frame, textvariable=self.var_mother,width=29, font=("arial", 12, "bold"))
        text_mother_name.grid(row=2, column=1)

        ## gender combo
        label_gender=Label(label_frame,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row="3",column=0,sticky=W)

        combo_gender=ttk.Combobox(label_frame,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","others")
        combo_gender.current(0)
        combo_gender.grid(row="3",column=1)

        ############post cord#########
        lbl_cust_mothe_name = Label(label_frame, text="Post Cord:", font=("arial", 12, "bold"), padx=2,  pady=6)
        lbl_cust_mothe_name.grid(row=4, column=0,sticky=W)
        text_mother_name = ttk.Entry(label_frame, textvariable=self.var_post,width=29, font=("arial", 12, "bold"))
        text_mother_name.grid(row=4, column=1)
        #######Mobil number#########
        lbl_mobiel_number = Label(label_frame, text="Mobiel Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobiel_number.grid(row=5, column=0, sticky=W)
        text_mobiel_number =ttk.Entry(label_frame,textvariable=self.var_mobile, width=29, font=("arial", 12, "bold"))
        text_mobiel_number.grid(row=5, column=1)

        #######Email##########

        lbl_email = Label(label_frame, text="Email:", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)
        text_email_number = ttk.Entry(label_frame, textvariable=self.var_email,width=29, font=("arial", 12, "bold"))
        text_email_number.grid(row=6, column=1)

        #####combo netionality#######
        label_Natinality = Label(label_frame, font=("arial", 12, "bold"), text="Nationality:", padx=2, pady=6)
        label_Natinality.grid(row="7", column=0, sticky=W)

        combo_netinality=ttk.Combobox(label_frame,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_netinality["value"]=("Banglades","India","Nepal","America","Japan","China","Butan")
        combo_netinality.current(0)
        combo_netinality.grid(row=7,column=1)
        ######Idproop type combo#######
        Idprop = Label(label_frame, font=("arial", 12, "bold"), text="Id Proop Type:", padx=2, pady=6)
        Idprop.grid(row="8", column=0,sticky=W)

        combo_idproop=ttk.Combobox(label_frame,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_idproop["value"]=("Netinal Id","Passport","Driving Laisens")
        combo_idproop.current(0)
        combo_idproop.grid(row=8,column=1)

        ###id number
        lbl_id_number = Label(label_frame, font=("arial",12,"bold"),text="Id Number:", padx=2, pady=6)
        lbl_id_number.grid(row=9, column=0, sticky=W)
        text_id_number = ttk.Entry(label_frame, textvariable=self.var_id_number,width=29, font=("arial", 12, "bold"))
        text_id_number.grid(row=9, column=1)

        ###address########
        lbl_email = Label(label_frame, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=10, column=0, sticky=W)
        text_email_number = ttk.Entry(label_frame, width=29, textvariable=self.var_address,font=("arial", 12, "bold"))
        text_email_number.grid(row=10, column=1)
        ###Btn frame
        btn_frame=Frame(label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=1,y=400,width=412,height=40)

        add_btn=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        add_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,command=self.update_data,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        update_btn.grid(row=0,column=1,padx=1)

        delate_btn=Button(btn_frame,command=self.nDelete,text="Delate",font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        delate_btn.grid(row=0,column=2,padx=1)

        resate_btn = Button(btn_frame,command=self.reset, text="Resate", font=("arial", 11, "bold"), bg="black", fg="gold", bd=2, width=10)
        resate_btn.grid(row=0, column=3, padx=1)
        ######Tabel Frame search system ######
        Tabel_frame = LabelFrame(self.root, text='View details and Search system', font=('times new roman', 18, 'bold'), bg='white',fg='black', bd=4, relief=RIDGE)
        Tabel_frame.place(x=435, y=50, width=860, height=490)
        ####searcbtn
        search_btn = Label(Tabel_frame, font=("arial", 12, "bold"), text="Search By:",bg="red",fg="white")
        search_btn.grid(row="0", column=0,padx=2)

        self.serch_var=StringVar()
        combo_Search = ttk.Combobox(Tabel_frame,textvariable=self.serch_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Mobiel", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        self.text_search=StringVar()
        textSearch = ttk.Entry(Tabel_frame, textvariable=self.text_search,font=("arial", 12, "bold"),width=24)
        textSearch.grid(row=0, column=2,padx=2)

        Search_btn= Button(Tabel_frame, command=self.search,text="Search", font=("arial", 11, "bold"), bg="black", fg="gold", bd=2, width=10)
        Search_btn.grid(row=0, column=3, padx=1)

        Show_all_btn= Button(Tabel_frame, command=self.fetch_data,text="Show All", font=("arial", 11, "bold"), bg="black", fg="gold", bd=2, width=10)
        Show_all_btn.grid(row=0, column=4,padx=1)

        #########Show data tabel#####

        details_tabel = Frame(Tabel_frame, bd=2, relief=RIDGE)
        details_tabel.place(x=0, y=50, width=850, height=350)

        scroll_x=ttk.Scrollbar(details_tabel,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_tabel, orient=VERTICAL)

        self.Cust_Detailos_tabel=ttk.Treeview(details_tabel,column=("ref","name","mother","gender","post","mobiel","email","natinality","idproop","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Detailos_tabel.xview)
        scroll_y.config(command=self.Cust_Detailos_tabel.yview)

        self.Cust_Detailos_tabel.heading("ref",text="Refer No")
        self.Cust_Detailos_tabel.heading("name", text="Name")
        self.Cust_Detailos_tabel.heading("mother", text="Mother Name")
        self.Cust_Detailos_tabel.heading("gender", text="Gender")
        self.Cust_Detailos_tabel.heading("post", text="Position")
        self.Cust_Detailos_tabel.heading("mobiel", text="Mobaiel")
        self.Cust_Detailos_tabel.heading("email", text="Email")
        self.Cust_Detailos_tabel.heading("natinality", text="Natinality")
        self.Cust_Detailos_tabel.heading("idproop", text="Id proof")
        self.Cust_Detailos_tabel.heading("idnumber", text="Id Number")
        self.Cust_Detailos_tabel.heading("address", text="Address")

        self.Cust_Detailos_tabel["show"]="headings"

        self.Cust_Detailos_tabel.column("ref",width=100)
        self.Cust_Detailos_tabel.column("name", width=100)
        self.Cust_Detailos_tabel.column("mother", width=100)
        self.Cust_Detailos_tabel.column("gender", width=100)
        self.Cust_Detailos_tabel.column("post", width=100)
        self.Cust_Detailos_tabel.column("mobiel",width=100)
        self.Cust_Detailos_tabel.column("email", width=100)
        self.Cust_Detailos_tabel.column("natinality", width=100)
        self.Cust_Detailos_tabel.column("idproop", width=100)
        self.Cust_Detailos_tabel.column("idnumber", width=100)
        self.Cust_Detailos_tabel.column("address", width=100)

        self.Cust_Detailos_tabel.pack(fill=BOTH,expand=1)
        self.Cust_Detailos_tabel.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
##########Add data#######
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror('Error','All fields are requaired',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("warning",f"Some things went to wrong:{str(es)}",parent=self.root)
    #####def fetch#########
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="481826@48", database="hotel_menagemen_customer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows= my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Detailos_tabel.delete(*self.Cust_Detailos_tabel.get_children())
            for i in rows:
                self.Cust_Detailos_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.Cust_Detailos_tabel.focus()
        content=self.Cust_Detailos_tabel.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update_data(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="hotel_menagemen_customer")
            my_cursor=conn.cursor()
            my_cursor.execute('update customer set name=%s,mother=%s,gender=%s,post=%s,mobiel=%s,email=%s,natinality=%s,idproop=%s,idnumber=%s,address=%s where ref=%s',(

                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                        ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('update','Customer details hase been updated successfully',parent=self.root)
    ########delate funcation###########
    def nDelete(self):
        nDelete = messagebox.askyesno('Hotel Management system', 'Do you want to delete this customer',parent=self.root)
        if nDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
            my_cursor = conn.cursor()
            query = 'delete from customer where ref=%s'
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not nDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    ###reste data########
    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from  customer where ' + str(self.serch_var.get()) + " LIKE'%" + str(self.text_search.get() + "%'"))
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Cust_Detailos_tabel.delete(*self.Cust_Detailos_tabel.get_children())
            for i in rows:
                self.Cust_Detailos_tabel.insert("", END, values=i)
                conn.commit()
            conn.close()









if __name__=="__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()