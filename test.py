from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox




root = Tk()
root.title('Billing-Page')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x500")

# Do some database stuff
# Create a database or connect to one that exists
conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

# Create a cursor instance
c = conn.cursor()

# Create Table

# Add dummy data to table
'''
for record in data:
    c.execute("INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :zipcode)", 
        {
        'first_name': record[0],
        'last_name': record[1],
        'id': record[2],
        'address': record[3],
        'city': record[4],
        'state': record[5],
        'zipcode': record[6]
        }
        )
'''

# Commit changes
conn.commit()

# Close our connection
conn.close()


def query_database():
    # Create a database or connect to one that exists
    # conn = sqlite3.connect('tree_crm.db')
    conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM place_orderss WHERE quantity>=1")
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        print(record)

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[0], record[3], record[4], record[5], record[6]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[0], record[3], record[4], record[5], record[6]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Order-ID", "Dish-ID", "Unique-ID", "Dish-Name", "Table-No", "Quantity", "Price")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Order-ID", anchor=W, width=140)
my_tree.column("Dish-ID", anchor=W, width=140)
my_tree.column("Unique-ID", anchor=CENTER, width=100)
my_tree.column("Dish-Name", anchor=CENTER, width=140)
my_tree.column("Table-No", anchor=CENTER, width=140)
my_tree.column("Quantity", anchor=CENTER, width=140)
my_tree.column("Price", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Order-ID", text="Order-ID", anchor=W)
my_tree.heading("Dish-ID", text="Dish-ID", anchor=W)
my_tree.heading("Unique-ID", text="Unique-ID", anchor=CENTER)
my_tree.heading("Dish-Name", text="Dish-Name", anchor=CENTER)
my_tree.heading("Table-No", text="Table-No", anchor=CENTER)
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="Ordr-ID")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Dish_ID")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="Unique-ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Dish-Name")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="Table-No")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

state_label = Label(data_frame, text="Quantity")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Price")
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)

total_bill_label = Label(data_frame, text="Total-Bill")
total_bill_label.grid(row=0, column=6, padx=10, pady=10)
total_bill_entry = Entry(data_frame)
total_bill_entry.grid(row=0, column=7, padx=10, pady=10)


# Move Row Up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


# Move Rown Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


# Remove one record
def remove_one():
    conn=sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

    #cursor
    c=conn.cursor()


    query = "DELETE  FROM place_orderss WHERE order_id=? and oid=? "
    a = fn_entry.get()
    b = int(id_entry.get())
    # insert into table
    c.execute(query, [(a), (b)])

    # print(res)
    conn.commit()
    conn.close()
    x = my_tree.selection()[0]
    my_tree.delete(x)
    #query_database()


# Remove Many records
def total_bill():
    import sqlite3
    conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

    # cursor
    c = conn.cursor()
    query = "SELECT sum(price)  FROM place_orderss WHERE order_id=? "
    a = fn_entry.get()

    # insert into table
    c.execute(query, [(a)])
    res=c.fetchone()
    res1=res
    res2=list(res1)
    bill=res2[0]
    messagebox.showinfo("Message", "Total Bill :"+str(res2[0]))


    conn.commit()
    conn.close()

    from fpdf import FPDF
    import sqlite3
    conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

    # cursor
    c = conn.cursor()
    query = "SELECT dishname  FROM place_orderss WHERE order_id=? and quantity>=1 "
    query1 = "SELECT quantity  FROM place_orderss WHERE order_id=? and quantity>=1"
    query2 = "SELECT price  FROM place_orderss WHERE order_id=? and quantity>=1 "
    a = fn_entry.get()

    # insert into table
    c.execute(query, [(a)])
    res = c.fetchall()
    conn.commit()
    name = res
    dname = list(name)
    c.execute(query1, [(a)])
    res1 = c.fetchall()
    conn.commit()
    p = res1
    quantity = list(p)
    c.execute(query2, [(a)])
    res2 = c.fetchall()
    quantity = res2
    price = list(p)

    conn.commit()
    conn.close()

    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=25)

    # create a cell
    pdf.cell(200, 10, txt="AADHI POTOBA",
             ln=2, align='C')
    pdf.set_font("Arial", size=15)

    # add another cell
    pdf.cell(200, 10, txt="|| SHREE LALBAUGHCHA RAJA PRASNA ||",
             ln=2, align='C')

    pdf.set_font("Arial", size=10)
    # pdf.cell(100, 20, txt = "Dish Name",
    #		ln = 0 ,align = 'left')
    # pdf.cell(180, 0, txt = "Quantity",
    #		ln = 3, align = 'C')
    pdf.cell(60, 10, 'DishName', ln=0, border=1)

    pdf.cell(20, 10, 'Quantity', ln=0, border=1)
    pdf.cell(20, 10, 'Price', ln=1, border=1)
    c = len(price)
    for n in range(c):
        pdf.cell(60, 10, txt=str(dname[n]), ln=0, border=1)
        pdf.cell(20, 10, txt=str(price[n]), ln=0, border=1)
        pdf.cell(20, 10, txt=str(quantity[n]), ln=1, border=1)

    pdf.set_font("Arial", size=25)
    pdf.cell(60, 10, txt="Total Bill", ln=0, border=1)
    pdf.cell(40, 10, txt=str(bill), ln=2, border=1)

    # create a cell
    # pdf.cell(200, 10, txt = "Visit Again",
    #		ln = 2, align = 'left')

    pdf.set_font("Arial", size=15)

    # # create a cell
    # pdf.cell(200, 10, txt=a,
    #          ln=2, align='R')
    # pdf.cell(200, 10, txt="Vanjare",
    #          ln=2, align='R')

    # save the pdf with name .pdf
    pdf.output("Bill.pdf")

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
    # get the password in the gmail (manage your google account, click on the avatar on the right)
    # then go to security (right) and app password (center)
    # insert the password and then choose mail and this computer and then generate
    # copy the password generated here
    password = 'Restaurant@123'
    # put the email of the receiver here
    receiver = a

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'This email has an attacment, a pdf file'

    message.attach(MIMEText(body, 'plain'))

    pdfname = 'Bill.pdf'

    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    # use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # enable security
    session.starttls()

    # login with mail_id and password
    session.login(sender, password)

    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent')





    '''import os
    if os.path.exists("Bill.pdf"):
        os.remove("Bill.pdf")
    else:
        print("The file does not exist")'''

    "C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db"



# Remove all records
def remove_all():
    conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

    # cursor
    c = conn.cursor()
    a =fn_entry.get()

    query = "DELETE  FROM place_orderss WHERE order_id=? "
    # insert into table
    c.execute(query, [(a)])


    conn.commit()
    conn.close()

    for record in my_tree.get_children():
        my_tree.delete(record)
    query_database()


# Clear entry boxes
def clear_entries():
    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)


# Select Record
def select_record(e):
    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

    # Grab record Number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # outpus to entry boxes
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zipcode_entry.insert(0, values[6])


# Update record
def update_record():
    # Grab the record number
    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

    # Create a cursor instance
    c = conn.cursor()

    c.execute("""UPDATE place_orderss SET
                order_id = :o,
                dish_id = :did,
                dishname = :d,
                tableno = :t,
                quantity = :q,
                price = :p
    
                WHERE oid = :oid""",
              {
                  'o': fn_entry.get(),
                  'did': ln_entry.get(),
                  'd': address_entry.get(),
                  't': city_entry.get(),
                  'q': state_entry.get(),
                  'p': zipcode_entry.get(),
                  'oid': id_entry.get(),
              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()



    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

def dash():
    root.destroy()
    import dashboard
    return


def add_member():
    root.destroy()
    import chef_reg
    return

# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="DashBoard",command=dash)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Total Bill", command=total_bill)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

add_button = Button(button_frame, text="Add a Staff", command=add_member)
add_button.grid(row=0, column=8, padx=10, pady=10)


# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database on start
query_database()

root.mainloop()


