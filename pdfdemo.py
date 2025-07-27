# Python program to create
# a pdf file


from fpdf import FPDF
import sqlite3
conn=sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

#cursor
c=conn.cursor()
query = "SELECT dishname  FROM place_orderss WHERE order_id=? and quantity>=1 "
query1 = "SELECT quantity  FROM place_orderss WHERE order_id=? and quantity>=1"
query2 = "SELECT price  FROM place_orderss WHERE order_id=? and quantity>=1 "
a = "vruttigorega81@gmail.com"

# insert into table
c.execute(query, [(a)])
res=c.fetchall()
conn.commit()
name=res
dname=list(name)
c.execute(query1,[(a)])
res1=c.fetchall()
conn.commit()
p=res1
quantity=list(p)
c.execute(query2,[(a)])
res2=c.fetchall()
quantity=res2
price=list(p)


conn.commit()
conn.close()

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 25)

# create a cell
pdf.cell(200, 10, txt = "RANE FOODS",
		ln = 2, align = 'C')
pdf.set_font("Arial", size = 15)

# add another cell
pdf.cell(200, 10, txt = "|| SHREE LALBAUGHCHA RAJA PRASNA ||",
		ln = 2, align = 'C')

pdf.set_font("Arial", size = 10)
#pdf.cell(100, 20, txt = "Dish Name",
#		ln = 0 ,align = 'left')
#pdf.cell(180, 0, txt = "Quantity",
#		ln = 3, align = 'C')
pdf.cell(60, 10, 'DishName', ln=0,border=1 )




pdf.cell(20, 10, 'Quantity',ln=0 ,border=1)
pdf.cell(20, 10, 'Price',ln=1 ,border=1)
c=len(price)
for n in range(c):
	pdf.cell(60, 10, txt=str(dname[n]), ln=0, border=1)
	pdf.cell(20, 10, txt=str(price[n]), ln=0, border=1)
	pdf.cell(20, 10, txt=str(quantity[n]), ln=1, border=1)



pdf.set_font("Arial", size = 25)
pdf.cell(60, 10, txt="Total Bill", ln=0, border=1)
pdf.cell(40, 10, txt="Total Bill", ln=2, border=1)



# create a cell
#pdf.cell(200, 10, txt = "Visit Again",
#		ln = 2, align = 'left')

pdf.set_font("Arial", size = 15)

# create a cell
pdf.cell(200, 10, txt = "Hotel Manager",
		ln = 2, align = 'R')
pdf.cell(200, 10, txt = "Vanjare",
		ln = 2, align = 'R')


# save the pdf with name .pdf
pdf.output("Hotel.pdf")
