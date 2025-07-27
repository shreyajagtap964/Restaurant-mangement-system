from tkinter import *
#  import place as place
from PIL import ImageTk, Image
from tkinter import messagebox







#import  PIL as pillow
#from PIL import Image,ImageTk
import sqlite3
#create a database or connect the database which already exist
#conn=sqlite3.connect('customer.db')

#create a cursor\
#c=conn.cursor()

#def login():





root = Tk()
root.title('Login Page')
#root.iconbitmap('c:/gui/codemy.ico')
#root.geometry("323x576")
root.geometry("1350x650")

# make sure app can be resized
root.resizable(width=True, height=True)

# Define Background Image
#bg = ImageTk.PhotoImage(file="C:\\Users\\hemangi\\PycharmProjects\\login page\\biryani image.jpeg")
bg=ImageTk.PhotoImage(Image.open("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\abc.jpg"))
                                 
my_canvas = Canvas(root, width=1350, height=650, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

#create frame
Frame_login=Frame(root,bg="whitesmoke")
Frame_login.place(x=55,y=225,width=340,height=250)

title=Label(Frame_login,text="LOGIN HERE",font=("impact",20),fg="chocolate1",bg="whitesmoke").place(x=100,y=2)

#label
lbl_user=Label(Frame_login,text="LOGIN ID",font=("impact",15),fg="BLACK",bg="whitesmoke").place(x=40,y=50)
pw_user=Label(Frame_login,text="PASSWORD",font=("impact",15),fg="BLACK",bg="whitesmoke").place(x=40,y=115)
# Create wele screen
def loging():







   '''res= "SELECT * FROM cust_reg WHERE email=? and passwrd=?"
   c.execute(res, [(un_entry.get()),(pw_entry.get())])
   rec=c.fetchone()
   if rec:
      messagebox.showinfo("Message","Login Successfully")

   else:
      messagebox.showerror("Alert","Wrong UserId OR Password")
   conn.mit()
   conn.close()'''

   # Add a wele message
   #my_canvas.create_text(160, 450, text="Wele!", font=("Helvetica", 40), fill="white")



   try :
      '''if ( a or b):
         messagebox.showerror("Alert", "Wrong UserId OR Password")'''

      conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")
      # cursor
      c = conn.cursor()
      query = "SELECT * FROM cust_reg WHERE email=? and passwrd=?"

      a = un_entry.get()

      b = pw_entry.get()
      # insert into table
      c.execute(query, [(un_entry.get()),(pw_entry.get())])
      rec=c.fetchone()

      if rec:
         messagebox.showinfo("Message","User Login successfully")
         #import dashboard
         root.destroy()
         import dashboard

         #import seta
         #print(a)
         #seta.name(a)


         conn.commit()
         conn.close()
      
      else:
         con = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")
         # cursor
         cn = con.cursor()
         querys = "SELECT * FROM chef_reg WHERE c_email=? and c_passwrd=?"
         cn.execute(querys, [(un_entry.get()), (pw_entry.get())])
         re = cn.fetchall()

         if re:
            messagebox.showinfo("Message", " Chef Login successfully")
            root.destroy()
            import test



         else:
            messagebox.showerror("Alert", "Wrong UserId OR Password")

   except:
      messagebox.showerror("Alert", "Wrong UserId OR Password")


def forget():
   import smtplib
   from email.message import EmailMessage
   # from smtplib import SMTP


   try:
      conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")
                        
      # cursor
      c = conn.cursor()
      query = "SELECT passwrd FROM cust_reg WHERE email=? "

      a = un_entry.get()
      print(a)
      # insert into table
      c.execute(query, [(a)])
      rec = c.fetchone()
      pas = rec
      pase = list(pas)
      print(pase)
      text = "Forget Password: " + str(pase[0])

      print(text)
      #receiver_mail = a
      subject = "Your Password"
      '''sender='restaurantbill01@gmail.com'

      server = smtplib.SMTP('smtp.gmail.', 587)
      server.starttls()
      server.login('restaurantbill01@gmail.com', 'Restaurant@123')
      email = EmailMessage()
      email['From'] = sender
      email['To'] = receiver_mail
      email['Subject'] = subject
      email.set_content(text)
      server.send_message(email)
      #messagebox.showinfo("Message", " Please Check Your Email")'''

      import smtplib
      from email.mime.multipart import MIMEMultipart
      from email.mime.text import MIMEText
      from email.mime.base import MIMEBase
      from email import encoders

      body = '''Hello Sir/Maam,
      This email Contains Total Bill
      Visit Again To Our Restaurant AADHI POTOBA
      '''
      # put your email here
      sender = 'restaurantbill01@gmail.com'

      password = 'Restaurant@123'
      # put the email of the receiver here
      receiver = un_entry.get()
      text = "Forget Password: " + str(pase[0])
      # Setup the MIME
      message = MIMEMultipart()
      message['From'] = sender
      message['To'] = receiver
      message['Subject'] = 'Forgot password'+text

      # use gmail with port
      session = smtplib.SMTP('smtp.gmail.com', 587)

      # enable security
      session.starttls()

      # login with mail_id and password
      session.login(sender, password)

      #text = message.as_string(text1)
      session.sendmail(sender, receiver, text)
      session.quit()
      print('Mail Sent')



   except:
      print("Error: unable to send email")






   return





# Define Entry Boxes
un_entry = Entry(root, font=("Helvetica", 16,"italic"), width=10, fg="black", bd=0)
pw_entry = Entry(root, font=("Helvetica", 16,"italic"), width=10, fg="black", bd=0)

un_entry.insert(0, "Email ID")
pw_entry.insert(0, "Password")

# labels

my_canvas.create_text(125,290,text="Login ID:",font=("Courier",17,"bold"),fill="white")
my_canvas.create_text(125,360,text="Password:",font=("Courier",17,"bold"),fill="white")

# Add the entry boxes to the canvas
un_window = my_canvas.create_window(220, 275, anchor="nw", window=un_entry)
pw_window = my_canvas.create_window(222, 340, anchor="nw", window=pw_entry)

# Define Button
login_btn = Button(root, text="Login", font=("Helvetica", 15, "italic","bold"), width=10, fg="white",bg="black", command=loging)
login_btn_window = my_canvas.create_window(80, 400, anchor="nw", window=login_btn)



def reg():

   root.destroy()
   import custreg

   return

reg_btn = Button(root, text="SignUp", font=("Helvetica", 15, "italic","bold"), width=10, fg="white",bg="black", command=reg)
reg_btn_window = my_canvas.create_window(230, 400, anchor="nw", window=reg_btn)




frgt_btn = Button(root, text="Forget Password", font=("Helvetica", 10, "italic","bold"), width=20, fg="white",bg="#6F4E37", command=forget)
frgt_btn_window = my_canvas.create_window(140, 460, anchor="nw", window=frgt_btn)


# Define entry_clear function
def entry_clear(e):
   if un_entry.get() == 'Email-ID' or pw_entry.get() == 'Password':
      un_entry.delete(0, END)
      pw_entry.delete(0, END)
      # change text to stars
      pw_entry.config(show="*")
un_entry.bind("<Button-1>", entry_clear)
pw_entry.bind("<Button-1>", entry_clear)

root.mainloop()



#-------------------------------------------------------------Login Page------------------------------------------------------------------
