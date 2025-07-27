from tkinter import*
from PIL import ImageTk
from PIL import Image
import sqlite3
from tkinter import messagebox
root=Tk()
root.title("Registration Page")

root.geometry("1000x630")
# make sure app can't be resizedPillo

#databases
#create databases oer connection
conn=sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

#cursor
c=conn.cursor()
#create table
'''c.execute(""" CREATE TABLE cust_reg (
            name text,
            email text primary key,
            cntct text,
            dob text,
            addres text,
            pincode text,
            passwrd text)



""")'''


#commit changesconn.close()
conn.commit()



root.resizable(width=False, height=False)

# Define Background Image
bg = ImageTk.PhotoImage(Image.open("reg.png"))
bt = ImageTk.PhotoImage(Image.open("reg here175.gif"))
# Define Canvas
my_canvas = Canvas(root, width=1350, height=650, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")
#my_canvas.create_image((120,50,image=bt,anchor="nw")
#my_canvas.create_image(350,315, image=bt,anchor="nw")
'''canvas = Canvas(my_canvas, width = 175, height = 175,bd=0,highlightthickness=0)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("reg here175.gif"))
canvas.create_image(400,1200, anchor=NW, image=img)'''





# Create welcome screen
def welcome():
   uname_entry.destroy()
   uemail_entry.destroy()
   #login_btn.destroy()
   # Add a welcome message
#my_canvas.create_text(160, 450, text="Welcome!", font=("Helvetica", 40), fill="white",image_names())

#Headline------------
my_canvas.create_text(600,20,text="Registration",font=("Courier",35,"italic","bold"),fill="white")
#------------------




my_canvas.create_text(38,75,text="Name:",font=("Courier",15,"bold"),fill="white")
my_canvas.create_text(60,135,text="Email-Id:",font=("Courier",15,"bold"),fill="white")
my_canvas.create_text(50,195,text="Address:",font=("Courier",15,"bold"),fill="white")
my_canvas.create_text(70,255,text="Mobile No.:",font=("Courier",15,"bold"),fill="white")
my_canvas.create_text(65,315,text="Birth Date:",font=("Courier",14,"bold"),fill="white")
my_canvas.create_text(50,375,text="Password:",font=("Courier",14,"bold"),fill="white")
my_canvas.create_text(50,435,text="Confirm:",font=("Courier",15,"bold"),fill="white")
my_canvas.create_text(50,495,text="Pincode:",font=("Courier",15,"bold"),fill="white")



# Define Entry Boxes
uname_entry = Entry(root, font=("Helvetica", 15), width=15, fg="black", bd=0)
uemail_entry = Entry(root, font=("Helvetica", 15), width=15, fg="black", bd=0)
uadd_entry = Entry(root, font=("Helvetica", 15), width=15, fg="black", bd=0)
ucntct_entry = Entry(root, font=("Helvetica",15), width=15,fg="black",bd=0)
udob_entry= Entry(root, font=("Helvetica",15), width=15,fg="black",bd=0)
upassword_entry= Entry(root, font=("Helvetica",15), width=15,fg="black",bd=0)
ucp_entry= Entry(root, font=("Helvetica",15), width=15,fg="black",bd=0)
#ustreet_entry =Entry(root, font=("Helvetica",15), width=15,fg="black",bd=0)
upincode_entry =Entry(root, font=("Helvetica",15), width=15,fg="black",bd=0)




uname_entry.insert(0, "User_name")
uemail_entry.insert(0, "Email-id")
uadd_entry.insert(0, "Address")
ucntct_entry.insert(0,"Mobile No.")
udob_entry.insert(0,"dd//mm//yyyy")
ucp_entry.insert(0,"Confirm Password")
upassword_entry.insert(0,"Password")
#ustreet_entry.insert(0,"Area")
upincode_entry.insert(0,"Pincode")

def submit():
   conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

   # cursor
   c = conn.cursor()
   #insert into table

   # for n in range(16)
   res=c.execute("INSERT INTO cust_reg VALUES (:uname,:email,:ucntct,:udob,:uadd,:upin,:ucp)",
             {
                'uname':uname_entry.get(),
                'email':uemail_entry.get(),
                'uadd':uadd_entry.get(),    # did = d[n]
                'ucntct':ucntct_entry.get(),
                'udob':udob_entry.get(),
                'upin':upincode_entry.get(),
                'ucp': ucp_entry.get(),

            })
   if res:
      messagebox.showinfo("congrulations","Registered Successfully")
      root.destroy()
      import loginpage




   conn.commit()
   conn.close()

   uname_entry.delete(0, END)
   uemail_entry.delete(0, END)
   uadd_entry.delete(0, END)
   ucntct_entry.delete(0, END)
   udob_entry.delete(0, END)
   ucp_entry.delete(0, END)
   upassword_entry.delete(0, END)
   #ustreet_entry.delete(0, END)
   upincode_entry.delete(0, END)

   return



def show():
   conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

   # cursor
   c = conn.cursor()
   # insert into table

   c.execute("SELECT passwrd,oid FROM cust_reg")
   records=c.fetchall()
   print(records)

   conn.commit()
   conn.close()




   return


def back():
   root.destroy()
   import loginpage
   return


show_btn = Button(root, text="Go Back", font=("Courier", 20, "bold"), width=15, fg="white", bg="black", command=back)
show_btn_window = my_canvas.create_window(400, 560, anchor="nw", window=show_btn)


# Add the entry boxes to the canvas
un_window = my_canvas.create_window(150, 60, anchor="nw", window=uname_entry)
pw_window = my_canvas.create_window(150, 120, anchor="nw", window=uemail_entry)
uadd_window= my_canvas.create_window(150,180,anchor="nw",window=uadd_entry)
ucntct_window=my_canvas.create_window(150,240,anchor="nw",window=ucntct_entry)
udob_window=my_canvas.create_window(150,300,anchor="nw",window=udob_entry)
ucp_window = my_canvas.create_window(150,420,anchor="nw",window=ucp_entry)
upassword_window = my_canvas.create_window(150,360,anchor="nw",window=upassword_entry)
#ustreet_window = my_canvas.create_window(150,480,anchor="nw",window=ustreet_entry)
upincode_window = my_canvas.create_window(150,480,anchor="nw",window=upincode_entry)

# Define Button
submit_btn = Button(root, text="Submit", font=("Courier", 20, "bold"), width=15, fg="white",bg="black", command=submit)
submit_btn_window = my_canvas.create_window(400, 500, anchor="nw", window=submit_btn)

#show_btn = Button(root, text="show", font=("Courier", 20, "bold"), width=15, fg="white",bg="black", command=show)
#show_btn_window = my_canvas.create_window(400, 550, anchor="nw", window=show_btn)

# Define entry_clear function
def entry_clear(e):
   if uname_entry.get() == 'User_name' or uemail_entry.get() == 'Email-id' or uadd_entry.get() == "Address" or ucntct_entry.get()=="Mobile No." or udob_entry=="dd//mm//yyyy" or ucp_entry == "Confirm Password" or upassword_entry == "Password"  or upincode_entry.get() == "Pincode":
      uname_entry.delete(0, END)
      uemail_entry.delete(0, END)
      uadd_entry.delete(0, END)
      ucntct_entry.delete(0,END)
      udob_entry.delete(0,END)
      ucp_entry.delete(0,END)
      upassword_entry.delete(0,END)
      #ustreet_entry.delete(0, END)
      upincode_entry.delete(0, END)
ucp_entry.config(show='*')
      # change text to stars
      #pw_entry.config(show="*")

# Bind the entry boxes
uname_entry.bind("<Button-1>", entry_clear)
uemail_entry.bind("<Button-1>", entry_clear)
uadd_entry.bind("<Button-1>", entry_clear)
ucntct_entry.bind("<Button-1>", entry_clear)
udob_entry.bind("<Button-1>",entry_clear)
ucp_entry.bind("<Button-1>",entry_clear)
upassword_entry.bind("<Button-1>",entry_clear)
#ustreet_entry.bind("<Button-1>",entry_clear)
upincode_entry.bind("<Button-1>",entry_clear)


#commit changesconn.close()
conn.commit()


conn.close()
root.mainloop()