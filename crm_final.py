from tkinter import *
from tkinter import ttk
import sqlite3



root = Tk()
root.title('TreeBase')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x500")



# Do some database stuff
# Create a database or connect to one that exists
conn=sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")


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
	#conn = sqlite3.connect('tree_crm.db')
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
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[3], record[4], record[5], record[6]), tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[3], record[4], record[5], record[6]), tags=('oddrow',))
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
my_tree['columns'] = ("Order-ID", "Dish-ID", "Unique-ID", "Dish-Name", "Table-No", "Quantity", "Price","Status")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Order-ID", anchor=W, width=140)
my_tree.column("Dish-ID", anchor=W, width=140)
my_tree.column("Unique-ID", anchor=CENTER, width=100)
my_tree.column("Dish-Name", anchor=CENTER, width=140)
my_tree.column("Table-No", anchor=CENTER, width=140)
my_tree.column("Quantity", anchor=CENTER, width=140)
my_tree.column("Price", anchor=CENTER, width=140)
my_tree.column("Status",anchor=CENTER,width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Order-ID", text="Order-ID", anchor=W)
my_tree.heading("Dish-ID", text="Dish-ID", anchor=W)
my_tree.heading("Unique-ID", text="Unique-ID", anchor=CENTER)
my_tree.heading("Dish-Name", text="Dish-Name", anchor=CENTER)
my_tree.heading("Table-No", text="Table-No", anchor=CENTER)
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)
my_tree.heading("Status",text="Status", anchor=CENTER)

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

# Move Row Up
def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Rown Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Remove one record
def remove_one():
	x = my_tree.selection()[0]
	my_tree.set(x)

# Remove Many records
def remove_many():
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)

# Remove all records
def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

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
	selected = my_tree.focus()
	# Update record
	my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get(),))

	# Clear entry boxes
	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	address_entry.delete(0, END)
	city_entry.delete(0, END)
	state_entry.delete(0, END)
	zipcode_entry.delete(0, END)



# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Cancel one Order", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Cancel Many Order", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<Double-1>", select_record)

# Run to pull data from database on start
query_database()

root.mainloop()