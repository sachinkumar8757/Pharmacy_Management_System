from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sys
class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1530x800+0+0")



# ====================add variable=============
        self.addref_var=StringVar()
        self.addmedname_var=StringVar()

#====================add main variable==========
        self.ref_var=StringVar()
        self.comname_var=StringVar()
        self.typemed_var=StringVar()
        self.medname_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffect_var=StringVar()
        self.warning_var=StringVar()
        self.doses_var=StringVar()
        self.price_var=StringVar()
        self.productqt_var=StringVar()




        labeltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',fg="darkgreen"
        ,font=("times new roman",50,"bold"),padx=2,pady=4)

        labeltitle.pack(side=TOP,fill=X)
        
        
        
        img1=Image.open(r"C:\Users\sachin kumar\OneDrive\Desktop\pharma\images\logo orignal.jpg")
        img1=img1.resize((90,70),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=50,y=20) 

        #========================DataFrameleft==========================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
        fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        
        #========================ButtonsFrame=========================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        #========================MainButton===========================
        BtnAddData=Button(ButtonFrame,text="MEDICINE ADD",bg="darkgreen",fg="white",font=("arial",12,"bold"),command=self.add_data)
        BtnAddData.grid(row=0,column=0)

        BtnUpdateData=Button(ButtonFrame,text="UPDATE",bg="darkgreen",fg="white",width=14,font=("arial",12,"bold"),command=self.Update)
        BtnUpdateData.grid(row=0,column=1)

        BtnDeleteData=Button(ButtonFrame,text="DELETE",bg="red",fg="white",width=14,font=("arial",12,"bold"),command=self.Delete)
        BtnDeleteData.grid(row=0,column=2)

        BtnResetData=Button(ButtonFrame,text="RESET",bg="darkgreen",fg="white",width=14,font=("arial",12,"bold"),command=self.Reset)
        BtnResetData.grid(row=0,column=3)

        BtnExitData=Button(ButtonFrame,text="EXIT",bg="darkgreen",fg="white",width=14,font=("arial",12,"bold"),command=self.exit)
        BtnExitData.grid(row=0,column=4)

        #==========================SearchBy===========================
        lblsearch=Button(ButtonFrame,text="SEARCH BY",bg="red",fg="white",width=14,font=("arial",12,"bold"))
        lblsearch.grid(row=0,column=5)

        #variable
        self.search_var=StringVar()

        Search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17),state="readonly")
        Search_combo["values"]=("Reference Number","Medicine Name","Lot Number")
        Search_combo.grid(row=0,column=6)
        Search_combo.current(0)

        self.txtsearch_var=StringVar()
        Txtsearch=Entry(ButtonFrame,textvariable=self.txtsearch_var,bd=3,relief=RIDGE,width=12,font=("arial",12,"bold"))
        Txtsearch.grid(row=0,column=7)

        Searchbtn=Button(ButtonFrame,text="SEARCH",bg="darkgreen",fg="white",width=13,font=("arial",12,"bold"),command=self.Search)
        Searchbtn.grid(row=0,column=8)

        Showall=Button(ButtonFrame,text="SHOW ALL",bg="darkgreen",fg="white",width=13,font=("arial",12,"bold"),command=self.fetch_data)
        Showall.grid(row=0,column=9)


        #=====================Label and Entry=========================
        Lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Refrence Number",padx=2)
        Lblrefno.grid(row=0,column=0,stick=W)

        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref_num from pharma")
        row=my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=16,font=("arial",17),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
    


        Lblcompanyname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2)
        Lblcompanyname.grid(row=1,column=0,stick=W)

        txtcompanyname=Entry(DataFrameLeft,textvariable=self.comname_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtcompanyname.grid(row=1,column=1)



        Lbltypemedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type of Medicine",padx=2)
        Lbltypemedicine.grid(row=2,column=0,stick=W)

        Medicinetype_combo=ttk.Combobox(DataFrameLeft,textvariable=self.typemed_var,width=16,font=("arial",17),state="readonly")
        Medicinetype_combo["values"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        Medicinetype_combo.grid(row=2,column=1)
        Medicinetype_combo.current(0)



        Lblmedicinename=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        Lblmedicinename.grid(row=3,column=0,stick=W)

        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select Med_name from pharma")
        med=my_cursor.fetchall()

        Medicinename_combo=ttk.Combobox(DataFrameLeft,textvariable=self.medname_var,width=16,font=("arial",17),state="readonly")
        Medicinename_combo["values"]=med
        Medicinename_combo.grid(row=3,column=1)
        Medicinename_combo.current(0)



        Lbllotnumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot Number:",padx=2,pady=6)
        Lbllotnumber.grid(row=4,column=0,stick=W)

        txtlotnumber=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtlotnumber.grid(row=4,column=1)



        Lblissuedate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        Lblissuedate.grid(row=5,column=0,stick=W)

        txtissuedate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtissuedate.grid(row=5,column=1)



        Lblexpdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        Lblexpdate.grid(row=6,column=0,stick=W)

        txtexpdate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtexpdate.grid(row=6,column=1)



        Lbluses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        Lbluses.grid(row=7,column=0,stick=W)

        txtuses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtuses.grid(row=7,column=1)



        Lblsideeffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        Lblsideeffect.grid(row=8,column=0,stick=W)

        txtsideeffect=Entry(DataFrameLeft,textvariable=self.sideeffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtsideeffect.grid(row=8,column=1)

        #=================2nd part DataFrameLeft==========================

        Lblprecwarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Pre&Warning:",padx=2,pady=6)
        Lblprecwarning.grid(row=0,column=2,stick=W)

        txtprecwarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtprecwarning.grid(row=0,column=3)



        Lbldoses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Doses:",padx=2,pady=6)
        Lbldoses.grid(row=1,column=2,stick=W)

        txtdoses=Entry(DataFrameLeft,textvariable=self.doses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtdoses.grid(row=1,column=3)



        Lbltabletprice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=2,pady=6)
        Lbltabletprice.grid(row=2,column=2,stick=W)

        txttabletprice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txttabletprice.grid(row=2,column=3)



        Lblpquantity=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=2,pady=6)
        Lblpquantity.grid(row=3,column=2,stick=W)

        txtpquantity=Entry(DataFrameLeft,textvariable=self.productqt_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtpquantity.grid(row=3,column=3)



        #===========image in DataframeLeft===================

        Lbltext=Label(DataFrameLeft,font=("arial",18,"bold"),text="GOOD MEDICINE ALWAYS TASTE BAD",padx=2,pady=6,bg="white",fg="red")
        Lbltext.place(x=380,y=150)



        img2=Image.open(r"C:\Users\sachin kumar\OneDrive\Desktop\pharma\images\medicine.jpg")
        img2=img2.resize((450,122),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=450,y=356) 


        #===================data frame right=====================
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
        fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=550,height=350)



        img3=Image.open(r"C:\Users\sachin kumar\OneDrive\Desktop\pharma\images\medicine.jpg")
        img3=img3.resize((205,80),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=965,y=165) 



        img4=Image.open(r"C:\Users\sachin kumar\OneDrive\Desktop\pharma\images\medicine.jpg")
        img4=img4.resize((205,80),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1169,y=165) 



        img5=Image.open(r"C:\Users\sachin kumar\OneDrive\Desktop\pharma\images\medicine.jpg")
        img5=img5.resize((105,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=1374,y=165) 



        Lblrefnum=Label(DataFrameRight,font=("arial",12,"bold"),text="Refrence Number:",padx=2)
        Lblrefnum.place(x=0,y=100)

        txtrefnum=Entry(DataFrameRight,textvariable=self.addref_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtrefnum.place(x=150,y=100)



        Lblmedicinenam=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=2)
        Lblmedicinenam.place(x=0,y=140)

        txtmedicinenam=Entry(DataFrameRight,textvariable=self.addmedname_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
        txtmedicinenam.place(x=150,y=140)



        #===============side frame==================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=170,width=290,height=150)


        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        

        self.medicine_table =ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)


        #===============medicine add button===============
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=170,width=129,height=150)


        BtnAddmed=Button(down_frame,text="ADD",bg="darkgreen",fg="white",width=11,pady=2,font=("arial",12,"bold"),command=self.addMed)
        BtnAddmed.grid(row=0,column=0)

        Btnupdatemed=Button(down_frame,text="UPDATE",bg="blue",fg="white",width=11,pady=2,font=("arial",12,"bold"),command=self. UpdateMed)
        Btnupdatemed.grid(row=1,column=0)

        Btndeletemed=Button(down_frame,text="DELETE",bg="red",fg="white",width=11,pady=2,font=("arial",12,"bold"),command=self.DeleteMed)
        Btndeletemed.grid(row=2,column=0)

        Btnclearmed=Button(down_frame,text="CLEAR",bg="pink",fg="white",width=11,pady=2,font=("arial",12,"bold"),command=self.ClearMed)
        Btnclearmed.grid(row=3,column=0)


        #===============Main table and Scroll bar=============

        TableFrame=Frame(self.root,bd=15,relief=RIDGE)
        TableFrame.place(x=0,y=580,width=1525,height=200)

        scrol_x=ttk.Scrollbar(TableFrame,orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y=ttk.Scrollbar(TableFrame,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y)

        self.Pharmacy_table=ttk.Treeview(TableFrame,columns=("ref","companyname","type","tabletname","lotno",
        "issuedate","expdate","uses","sideeffect","warning","doses","price","productqt"),
        xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)

        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x.config(command=self.Pharmacy_table.xview)
        scrol_y.config(command=self.Pharmacy_table.yview)

        self.Pharmacy_table["show"]="headings"


        self.Pharmacy_table.heading("ref",text="Reference No")
        self.Pharmacy_table.heading("companyname",text="Company Name")
        self.Pharmacy_table.heading("type",text="Type of Medicine")
        self.Pharmacy_table.heading("tabletname",text="Tablet Name")
        self.Pharmacy_table.heading("lotno",text="Lot No")
        self.Pharmacy_table.heading("issuedate",text="Issue Date")
        self.Pharmacy_table.heading("expdate",text="Exp Date")
        self.Pharmacy_table.heading("uses",text="Uses")
        self.Pharmacy_table.heading("sideeffect",text="Side Effect")
        self.Pharmacy_table.heading("warning",text="Warning")
        self.Pharmacy_table.heading("doses",text="Doses")
        self.Pharmacy_table.heading("price",text="Price")
        self.Pharmacy_table.heading("productqt",text="Product Qts")

        self.Pharmacy_table.pack(fill=BOTH,expand=1)

        self.Pharmacy_table.column("ref",width=100)
        self.Pharmacy_table.column("companyname",width=100)
        self.Pharmacy_table.column("type",width=100)
        self.Pharmacy_table.column("tabletname",width=100)
        self.Pharmacy_table.column("lotno",width=100)
        self.Pharmacy_table.column("issuedate",width=100)
        self.Pharmacy_table.column("expdate",width=100)
        self.Pharmacy_table.column("uses",width=100)
        self.Pharmacy_table.column("sideeffect",width=100)
        self.Pharmacy_table.column("warning",width=100)
        self.Pharmacy_table.column("doses",width=100)
        self.Pharmacy_table.column("price",width=100)
        self.Pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.Pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)



# =======================ADD MEDICINE FUNCTION declaration====================
    def exit(self):
        sys.exit(0)

    def addMed(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(ref_num,med_name) values(%s,%s)",(
                                                                        self.addref_var.get(),
                                                                        self.addmedname_var.get()

                                                                    ))
        conn.commit()
        self.fetch_dataMed()
        #self.Medget_cursor()
        conn.close() 
        messagebox.showinfo("Success","Medicine Added")


    def fetch_dataMed(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()   
        conn.close()     

    # ================medicine get cursor=======
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.addref_var.set(row[0])
        self.addmedname_var.set(row[1])


    def UpdateMed(self):
        if self.addref_var.get()=="" or self.addmedname_var.get()=="":
            messagebox.showerror("Error","All field are Required")
        else:
            conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set med_name=%s where Ref_num=%s",(
                                                                        self.addmedname_var.get(),
                                                                        self.addref_var.get()

                                          ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success","Medicine Updated")


    def DeleteMed(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from pharma where Ref_num=%s"
        val=(self.addref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()

        messagebox.showinfo("Success","Medicine Deleted")


    def ClearMed(self):
        self.addref_var.set("")
        self.addmedname_var.set("")    


    #============Main Table============== 
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get=="":
            messagebox.showerror("Error","All field are Required")
        else:
            conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy(Ref_no,Company_name ,Types ,Medicine_name ,Lot_no ,Issue_date ,Exp_date ,Uses ,Side_effect,Warning ,Doses ,Price,Product_Qts)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.ref_var.get(),
                                                                        self.comname_var.get(),
                                                                        self.typemed_var.get(),
                                                                        self.medname_var.get(),
                                                                        self.lot_var.get(),
                                                                        self.issuedate_var.get(),
                                                                        self.expdate_var.get(),
                                                                        self.uses_var.get(),
                                                                        self.sideeffect_var.get(),
                                                                        self.warning_var.get(),
                                                                        self.doses_var.get(),
                                                                        self.price_var.get(),
                                                                        self.productqt_var.get()

                                          ))
            conn.commit()
            self.fetch_data()
            #self.get_cursor()
            conn.close()
            messagebox.showinfo("Success","Data inserted Successfully")


    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Pharmacy_table.delete(*self.Pharmacy_table.get_children())
            for i in rows:
                self.Pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,ev=""):
        cursor_row=self.Pharmacy_table.focus()
        content=self.Pharmacy_table.item(cursor_row)
        row=content["values"]

        self.ref_var.set(row[0]),
        self.comname_var.set(row[1]),
        self.typemed_var.set(row[2]),
        self.medname_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideeffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.doses_var.set(row[10]),
        self.price_var.set(row[11]),
        self.productqt_var.set(row[12])    


    def Update(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All field are Required")
        else:
            conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set Company_name=%s ,Types=%s ,Medicine_name=%s ,Lot_no=%s ,Issue_date=%s ,Exp_date=%s ,Uses=%s ,Side_effect=%s,Warning=%s ,Doses=%s ,Price=%s,Product_Qts=%s where Ref_no=%s",(
                                                                        
                                                                        self.comname_var.get(),
                                                                        self.typemed_var.get(),
                                                                        self.medname_var.get(),
                                                                        self.lot_var.get(),
                                                                        self.issuedate_var.get(),
                                                                        self.expdate_var.get(),
                                                                        self.uses_var.get(),
                                                                        self.sideeffect_var.get(),
                                                                        self.warning_var.get(),
                                                                        self.doses_var.get(),
                                                                        self.price_var.get(),
                                                                        self.productqt_var.get(),
                                                                        self.ref_var.get()

                                          ))
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success","Data Updated Successfully")

   


    def Delete(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from pharmacy where Ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Data Deleted Successfully")


    def Reset(self):
        #self.ref_var.set(""),
        self.comname_var.set(""),
        #self.typemed_var.set(""),
        #self.medname_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideeffect_var.set(""),
        self.warning_var.set(""),
        self.doses_var.set(""),
        self.price_var.set(""),
        self.productqt_var.set("")


    def Search(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sachin@123",database="mydata")
        my_cursor=conn.cursor()
        d = {"Reference Number":"Ref_no","Medicine Name":"Medicine_name","Lot Number":"Lot_no"}
        c = d[str(self.search_var.get())]

        my_cursor.execute("select * from pharmacy where "+c +" LIKE '%"+str(self.txtsearch_var.get())+"%'")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Pharmacy_table.delete(*self.Pharmacy_table.get_children())
            for i in rows:
                self.Pharmacy_table.insert("",END,values=i)
            conn.commit()    
        conn.close()    
        



    
if __name__== "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
    