from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1298x553+235+225')

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
        label_frame = LabelFrame(self.root, text="New Room Add", font=("arial", 12, "bold"), relief=RIDGE, bd=2)
        label_frame.place(x=5, y=50, width=540, height=350)

        #floor
        lbl_floor=Label(label_frame,text="Floor:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()

        entry_floor=ttk.Entry(label_frame,textvariable=self.var_floor, width=20,font=("arial",12,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Room Number
        lbl_RoomNo=Label(label_frame,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()

        entry_RoomNo=ttk.Entry(label_frame,textvariable=self.var_RoomNo,width=20,font=("arial",12,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type

        lbl_RoomType=Label(label_frame,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()

        entry_RoomType=ttk.Entry(label_frame,textvariable=self.var_RoomType,width=20,font=("arial",12,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

        ###Btn frame
        btn_frame=Frame(label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=1,y=200,width=412,height=40)

        add_btn=Button(btn_frame,text="ADD",command=self.add_data,  font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        add_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="Update",command=self.update, font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        update_btn.grid(row=0,column=1,padx=1)

        delate_btn=Button(btn_frame,text="Delate",command=self.nDelete,font=("arial",11,"bold"),bg="black",fg="gold",bd=2,width=10)
        delate_btn.grid(row=0,column=2,padx=1)

        resate_btn = Button(btn_frame,text="Resate", command=self.reset,font=("arial", 11, "bold"), bg="black", fg="gold", bd=2, width=10)
        resate_btn.grid(row=0, column=3, padx=1)

        #Tabel Frame search system###########

        Tabel_frame = LabelFrame(self.root, text='Show Room Details', font=('times new roman', 18, 'bold'),bg='white', fg='black', bd=4, relief=RIDGE)
        Tabel_frame.place(x=600, y=55, width=600, height=350)

        
        scroll_x = ttk.Scrollbar(Tabel_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Tabel_frame, orient=VERTICAL)

        self.room_tabel = ttk.Treeview(Tabel_frame, column=("floor", "roomno", "roomType", ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_tabel.xview)
        scroll_y.config(command=self.room_tabel.yview)

        self.room_tabel.heading("floor", text="Floor")
        self.room_tabel.heading("roomno", text="Room No")
        self.room_tabel.heading("roomType", text="Room Type")
       

        self.room_tabel["show"] = "headings"

        self.room_tabel.column("floor", width=100)
        self.room_tabel.column("roomno", width=100)
        self.room_tabel.column("roomType", width=100)
        

        self.room_tabel.pack(fill=BOTH, expand=1)
        self.room_tabel.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    
    ##########Add data#######
    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get()== "":
            messagebox.showerror('Error', 'All fields are requaired', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomNo.get(),
                                                                                        self.var_RoomType.get()
                                                                                        

                                                                                    ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "New room added successfull", parent=self.root)
            except Exception as es:
                messagebox.showerror("warning", f"Some things went to wrong:{str(es)}", parent=self.root)

    #########fetch data###########
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_tabel.delete(*self.room_tabel.get_children())
            for i in rows:
                self.room_tabel.insert("", END, values=i)
            conn.commit()
        conn.close()
    #get cursor
    def get_cursor(self,events=""):
        cursor_row=self.room_tabel.focus()
        content=self.room_tabel.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

   
    #update
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="hotel_menagemen_customer")
            my_cursor=conn.cursor()
            my_cursor.execute('update details set floor=%s,roomType=%s where roomno=%s',(

                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_RoomNo.get(),
                                                                                                                            
                                                                                    ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('update','Room details hase been updated successfully',parent=self.root)

    def nDelete(self):
        nDelete = messagebox.askyesno('Hotel Management system', 'Do you want to delete this customer',parent=self.root)
        if nDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="hotel_menagemen_customer")
            my_cursor = conn.cursor()
            query = 'delete from details where roomno=%s'
            value = (self.var_RoomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not nDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")








if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()