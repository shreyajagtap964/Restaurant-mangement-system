from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Menu")

conn=sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

#cursor
c=conn.cursor()

#c.execute("ALTER TABLE placeorder DROP COLUMN autogen;")
#create table
#c.execute("CREATE TABLE dishes (dish_id int primary key,dish_name text ,price double)")
#c.execute("SELECT *,oid FROM dishes ")
#create table
'''c.execute("""CREATE TABLE place_order (order_id text,dish_id int,dishname text,
    tableno int,
    quantity int,
    price double,
    primary key(order_id,
    dish_id,
    tableno
    ),
    FOREIGN KEY(dish_id) REFERENCES dishes(dish_id),
    
    FOREIGN KEY(price) REFERENCES dishes(price))"""
          )'''
#r=c.fetchall()
#print(r)
conn.commit()
conn.close()
names=["Paneer Achari-Tikka","Masala-Papad","Corn Kabab","Bread Katori","Veg-Tripple Fried Rice","Manchow Soup","Schezwan Noodles","Fried Rice","Plain Dosa","Medu-Vada","Utappa","Idli Sambhar","Kombdi Wade","Ghavane","Kaju Masala","Malvani Spcl Thali","Baba Spcl Falooda","Brownie","Gulab Jamun","Ice Cream"]

id =[11,22,33,44,55,66,77,88,99,100,111,122,133,144,155,166,177,188,199,200]
prices=[170.0,50.0,120.0,90.0,210.0,90.0,180.0,190.0,100.0,50.0,120.0,50.0,200.0,100.0,180.0,375.0,150.0,120.0,30.0,75.0]


'''for n in range(20):
    conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")
    c = conn.cursor()
    c.execute("INSERT INTO dishes VALUES (:d_id,:d_name,:d_price)",
                 {
                    'd_id':id[n],
                    'd_name':names[n],
                     'd_price':prices[n],

                })

    #commit changesconn.close()
    conn.commit()
    conn.close()'''


root.geometry("1350x650+0+0")
#root['background']='white'

img_starter1=ImageTk.PhotoImage(Image.open("masala papad1350.jpg"))
img_starter2=ImageTk.PhotoImage(Image.open("veg crispy 1350.jpg"))
img_starter3=ImageTk.PhotoImage(Image.open("acharipaneer1350.jpg"))
img_starter4=ImageTk.PhotoImage(Image.open("corn image 1350.jpg"))
img_starter5=ImageTk.PhotoImage(Image.open("bread katori1350.jpg "))


img_chin_main1= ImageTk.PhotoImage(Image.open("manchow-soup1350.jpg"))
img_chin_main2= ImageTk.PhotoImage(Image.open("schzewan-noodles1350.jpg"))
img_chin_main3= ImageTk.PhotoImage(Image.open("fried-rice1350.jpg"))
img_chin_main4= ImageTk.PhotoImage(Image.open("triple-rice.1350jpg.jpg"))


img_south_main1= ImageTk.PhotoImage(Image.open("dosa 1350.png"))
img_south_main2= ImageTk.PhotoImage(Image.open("meduvada 1350.jpg"))
img_south_main3= ImageTk.PhotoImage(Image.open("uthapa 1350.jpg"))
img_south_main4= ImageTk.PhotoImage(Image.open("idli 1350.jpg"))

img_malvani_main1=ImageTk.PhotoImage(Image.open("komdi vade1350.jpg"))
img_malvani_main2=ImageTk.PhotoImage(Image.open("ghavane 1350.jpg"))
img_malvani_main3=ImageTk.PhotoImage(Image.open("kaju masala 1350.jpg"))
img_malvani_main4=ImageTk.PhotoImage(Image.open("malvani thali 1350.jpg"))


img_dst_main1=ImageTk.PhotoImage(Image.open("baba falooda 1350.jpg"))
img_dst_main2=ImageTk.PhotoImage(Image.open("brownie1350.jpg"))
img_dst_main3=ImageTk.PhotoImage(Image.open("ice cream 1350.jpg"))
img_dst_main4=ImageTk.PhotoImage(Image.open("gulabjamun1350.jpg"))



label1 = Label(root,image=img_starter1)
label1.grid(row=0,column=0,columnspan=9)

lst_img_st=[img_starter1,img_starter2,img_starter3,img_starter4,img_starter5]
lst_img_main_chin=[img_chin_main1,img_chin_main2,img_chin_main3,img_chin_main4]
lst_img_main_south=[img_south_main1,img_south_main2,img_south_main3,img_south_main4]
lst_img_main_malvani=[img_malvani_main1,img_malvani_main2,img_malvani_main3,img_malvani_main4]
lst_img_dst=[img_dst_main1,img_dst_main2,img_dst_main3,img_dst_main4]














lbl_starters=Label(root,text="Starters",fg="BLACK",font=("Courier", 25,"bold"))
lbl_starters.grid(row=5,column=0,columnspan=3)
lb_main=Label(root,text="South India Cuisine",fg="Black",font=("Courier", 25,"bold"))
lb_main.grid(row=5,column=3,columnspan=3)
lbl_desert=Label(root,text="Deserts",fg="BLACK",font=("Courier", 25,"bold"))
lbl_desert.grid(row=5,column=6,columnspan=3)
lb_main_chin=Label(root,text="Chinese Cuisine",fg="Black",font=("Courier", 25,"bold"))
lb_main_chin.grid(row=11,column=0,columnspan=3)
lb_main_malvani=Label(root,text="Malvani Cuisine",fg="Black",font=( "Courier",25,"bold"))
lb_main_malvani.grid(row=11,column=3,columnspan=3)

label_blank=Label(root,text="")
label_blank.grid(row=17,column=1,rowspan=2)





lbl_st_tikka=Label(root,text="Paneer Achari-Tikka",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_st_tikka.grid(row=6,column=0)
lbl_st_papad=Label(root,text="Masala-Papad",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_st_papad.grid(row=7,column=0)
lbl_st_kabab=Label(root,text="Corn Kabab",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_st_kabab.grid(row=8,column=0)
#lbl_st_crispy=Label(root,text="Veg-Crispy",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
#lbl_st_crispy.grid(row=9,column=0)
lbl_st_katori=Label(root,text="Bread Katori",fg="Black",font=("Helvetica",10,"bold"),justify=LEFT)
lbl_st_katori.grid(row=9,column=0)


lbl_main_tripple=Label(root,text="Veg-Tripple Fried rice",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_tripple.grid(row=12,column=0)
lbl_main_soup=Label(root,text="Manchow Soup",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_soup.grid(row=13,column=0)
lbl_main_noodle=Label(root,text="Schezwan Noodles",fg="Black",font=("Helvetica", 10,"bold"), justify=LEFT)
lbl_main_noodle.grid(row=14,column=0)
lbl_main_fried_rice=Label(root,text="Fried Rice",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_fried_rice.grid(row=15,column=0)



lbl_st_tikka_p=Label(root,text="170₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_st_tikka_p.grid(row=6,column=2)
lbl_st_papad_p=Label(root,text="50₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_st_papad_p.grid(row=7,column=2)
lbl_st_kabab_p=Label(root,text="120₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_st_kabab_p.grid(row=8,column=2)
#lbl_st_crispy_p=Label(root,text="180₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
#lbl_st_crispy_p.grid(row=9,column=2)
lbl_st_katori_p=Label(root,text="90₹",fg="Black",font=("Helvetica",10,"bold"),justify=LEFT)
lbl_st_katori_p.grid(row=9,column=2)

lbl_main_dosa=Label(root,text="Plain Dosa",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_dosa.grid(row=6,column=3)
lbl_main_vada=Label(root,text="Medu-Vada",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_vada.grid(row=7,column=3)
lbl_main_utappa=Label(root,text="Utappa",fg="Black",font=("Helvetica", 10,"bold"), justify=LEFT)
lbl_main_utappa.grid(row=8,column=3)
lbl_main_idli=Label(root,text="Idli Sambhar",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_idli.grid(row=9,column=3)


lbl_dosa_p=Label(root,text="100₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_dosa_p.grid(row=6,column=5)
lbl_vada_p=Label(root,text="50₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_vada_p.grid(row=7,column=5)
lbl_utapa_p=Label(root,text="120₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_utapa_p.grid(row=8,column=5)
lbl_idli_p=Label(root,text="50₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_idli_p.grid(row=9,column=5)



lbl_main_komdi=Label(root,text="Kombdi Wade",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_komdi.grid(row=12,column=3)
lbl_main_ghavane=Label(root,text="Ghavane",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_ghavane.grid(row=13,column=3)
lbl_main_kaju=Label(root,text="Kaju Masala",fg="Black",font=("Helvetica", 10,"bold"), justify=LEFT)
lbl_main_kaju.grid(row=14,column=3)
lbl_main_thali=Label(root,text="Malvani Spcl Thali ",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_thali.grid(row=15,column=3)



lbl_main_komdi_p=Label(root,text="200₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_komdi_p.grid(row=12,column=5)
lbl_main_ghavane_p=Label(root,text="100₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_ghavane_p.grid(row=13,column=5)
lbl_main_kaju_p=Label(root,text="180₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_kaju_p.grid(row=14,column=5)
lbl_main_thali_p=Label(root,text="375₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_thali_p.grid(row=15,column=5)




lbl_dst_faluda=Label(root,text="Baba Spcl Faluda",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_dst_faluda.grid(row=6,column=6)
lbl_dst_brownie=Label(root,text="Brownie",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_dst_brownie.grid(row=7,column=6)
lbl_dst_jamun=Label(root,text="Gulab-Jamun",fg="Black",font=("Helvetica", 10,"bold"), justify=LEFT)
lbl_dst_jamun.grid(row=8,column=6)
lbl_dst_icream=Label(root,text="Ice-Cream",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_dst_icream.grid(row=9,column=6)

lbl_dst_faluda_p=Label(root,text="150₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_dst_faluda_p.grid(row=6,column=8)
lbl_dst_brownie_p=Label(root,text="120₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_dst_brownie_p.grid(row=7,column=8)
lbl_dst_jamun_p=Label(root,text="30₹",fg="Black",font=("Helvetica", 10,"bold"), justify=LEFT)
lbl_dst_jamun_p.grid(row=8,column=8)
lbl_dst_icream_p=Label(root,text="75₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_dst_icream_p.grid(row=9,column=8)





lbl_main_tripple_p=Label(root,text="210₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_tripple_p.grid(row=12,column=2)
lbl_main_soup_p=Label(root,text="90₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_soup_p.grid(row=13,column=2)
lbl_main_noodles_p=Label(root,text="180₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_noodles_p.grid(row=14,column=2)
lbl_main_fried_rice_p=Label(root,text="190₹",fg="Black",font=("Helvetica", 10,"bold"),justify=LEFT)
lbl_main_fried_rice_p.grid(row=15,column=2)






En_st_tikka=Entry(root,font=("Helvetica", 10,"bold"))
En_st_tikka.grid(row=6,column=1)
En_st_papad=Entry(root,font=("Helvetica", 10,"bold"))
En_st_papad.grid(row=7,column=1)
En_st_kabab=Entry(root,font=("Helvetica", 10,"bold"))
En_st_kabab.grid(row=8,column=1)
#En_st_crispy=Entry(root,textvariable="st3",font=("Helvetica", 10,"bold"))
#En_st_crispy.grid(row=9,column=1)
En_st_katori=Entry(root,font=("Helvetica", 10,"bold"))
En_st_katori.grid(row=9,column=1)





En_dosa=Entry(root,font=("Helvetica", 10,"bold"))
En_dosa.grid(row=6,column=4)
En_vada=Entry(root,font=("Helvetica", 10,"bold"))
En_vada.grid(row=7,column=4)
En_utappa=Entry(root,font=("Helvetica", 10,"bold"))
En_utappa.grid(row=8,column=4)
En_idli=Entry(root,font=("Helvetica", 10,"bold"))
En_idli.grid(row=9,column=4)

En_faluda=Entry(root,font=("Helvetica", 10,"bold"))
En_faluda.grid(row=6,column=7)
En_brownie=Entry(root,font=("Helvetica", 10,"bold"))
En_brownie.grid(row=7,column=7)
En_jamun=Entry(root,font=("Helvetica", 10,"bold"))
En_jamun.grid(row=8,column=7)
En_ice=Entry(root,font=("Helvetica", 10,"bold"))
En_ice.grid(row=9,column=7)

En_main_komdi=Entry(root,font=("Helvetica", 10,"bold"))
En_main_komdi.grid(row=12,column=4)
En_main_ghavane=Entry(root,font=("Helvetica", 10,"bold"))
En_main_ghavane.grid(row=13,column=4)
En_main_kaju=Entry(root,font=("Helvetica", 10,"bold"))
En_main_kaju.grid(row=14,column=4)
En_main_thali=Entry(root,font=("Helvetica", 10,"bold"))
En_main_thali.grid(row=15,column=4)




En_main_tripple=Entry(root,font=("Helvetica", 10,"bold"))
En_main_tripple.grid(row=12,column=1)
En_main_soup=Entry(root,font=("Helvetica", 10,"bold"))
En_main_soup.grid(row=13,column=1)
En_main_noodles=Entry(root,font=("Helvetica", 10,"bold"))
En_main_noodles.grid(row=14,column=1)
En_main_fried_rice=Entry(root,font=("Helvetica", 10,"bold"))
En_main_fried_rice.grid(row=15,column=1)





entryboxes=[En_st_tikka.get(),En_st_papad.get(),En_st_kabab.get(),En_st_katori.get(),En_main_tripple.get(),En_main_soup.get(),En_main_noodles.get(),En_main_fried_rice.get(),En_dosa.get(),En_vada.get(),En_utappa.get(),En_idli.get(),En_main_komdi.get(),En_main_ghavane.get(),En_main_kaju.get(),En_main_thali.get(),En_faluda.get(),En_brownie.get(),En_jamun.get(),En_ice.get()]

# Create welcome screen



# Define Button
'''Order_btn = Button(root, text="Walk in!", font=("Helvetica", 20, "bold"), width=15, fg="white",bg="black", command=welcome)
Order_btn_window = my_canvas.create_window(900,120, anchor="nw", window=Order_btn)
Homedelivery_btn = Button(root, text="Home Delivery", font=("Helvetica", 12 ), width=11,height=3, fg="white",bg="#F87217", command=welcome)
Homedelivery_btn_window = my_canvas.create_window(286, 209, anchor="nw", window=Homedelivery_btn)'''

# Define entry_clear function
'''def entry_clear(e):
   if un_entry.get() == 'Username' or pw_entry.get() == 'Password':
      un_entry.delete(0, END)
      pw_entry.delete(0, END)
      # change text to stars
      pw_entry.config(show="*") '''
def tikka(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_st[2])
    label1.grid(row=0, column=0, columnspan=9)


def crispy(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_st[1])
    label1.grid(row=0, column=0, columnspan=9)

def kabab(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_st[3])
    label1.grid(row=0, column=0, columnspan=9)

def katori(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_st[4])
    label1.grid(row=0, column=0, columnspan=9)

def papad(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_st[0])
    label1.grid(row=0, column=0, columnspan=9)


def fried(e):
    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_chin[2])
    label1.grid(row=0, column=0, columnspan=9)
def noodles(e):
    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_chin[1])
    label1.grid(row=0, column=0, columnspan=9)
def soup(e):
    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_chin[0])
    label1.grid(row=0, column=0, columnspan=9)
def tripple(e):
    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_chin[3])
    label1.grid(row=0, column=0, columnspan=9)


def utapa(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_south[2])
    label1.grid(row=0, column=0, columnspan=9)

def idli(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_south[3])
    label1.grid(row=0, column=0, columnspan=9)

def vada(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_south[1])
    label1.grid(row=0, column=0, columnspan=9)

def dosa(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_south[0])
    label1.grid(row=0, column=0, columnspan=9)


def komdi(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_malvani[0])
    label1.grid(row=0, column=0, columnspan=9)

def ghavane(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_malvani[1])
    label1.grid(row=0, column=0, columnspan=9)

def kaju(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_malvani[2])
    label1.grid(row=0, column=0, columnspan=9)


def thali(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_main_malvani[3])
    label1.grid(row=0, column=0, columnspan=9)


def jamun(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_dst[3])
    label1.grid(row=0, column=0, columnspan=9)



def faluda(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_dst[0])
    label1.grid(row=0, column=0, columnspan=9)

def brownie(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_dst[1])
    label1.grid(row=0, column=0, columnspan=9)

def ice(e):

    global label1
    label1.grid_forget()
    label1 = Label(root, image=lst_img_dst[2])
    label1.grid(row=0, column=0, columnspan=9)
# Bind the entry boxes
#un_entry.bind("<Button-1>", entry_clear)
#pw_entry.bind("<Button-1>", entry_clear)
En_st_tikka.bind("<Button-1>",tikka)
#En_st_crispy.bind("<Button-1>",crispy)
En_st_kabab.bind("<Button-1>",kabab)
En_st_katori.bind("<Button-1>",katori)
En_st_papad.bind("<Button-1>",papad)


En_main_fried_rice.bind("<Button-1>",fried)
En_main_noodles.bind("<Button-1>",noodles)
En_main_soup.bind("<Button-1>",soup)
En_main_tripple.bind("<Button-1>",tripple)

En_utappa.bind("<Button-1>",utapa)
En_idli.bind("<Button-1>",idli)
En_dosa.bind("<Button-1>",dosa)
En_vada.bind("<Button-1>",vada)

En_main_komdi.bind("<Button-1>",komdi)
En_main_ghavane.bind("<Button-1>",ghavane)
En_main_kaju.bind("<Button-1>",kaju)
En_main_thali.bind("<Button-1>",thali)


En_faluda.bind("<Button-1>",faluda)
En_jamun.bind("<Button-1>",jamun)
En_brownie.bind("<Button-1>",brownie)
En_ice.bind("<Button-1>",ice)


'''def place_order():
    pop = Tk()
    pop.title("Info")
    pop.geometry("450x150")
    lbl_gmail = Label(pop, text="Gmail", fg="BLACK", font=("Courier", 10, "bold"))
    lbl_gmail.grid(row=0, column=0)
    En_gmail = Entry(pop, font=("Helvetica", 10, "bold"))
    En_gmail.grid(row=0, column=1)
    lbl_tableno = Label(pop, text="Table no.", fg="BLACK", font=("Courier", 10, "bold"))
    lbl_tableno.grid(row=1, column=0)
    En_table = Entry(pop, font=("Helvetica", 10, "bold"))
    En_table.grid(row=1, column=1)

    def cnf_order(gmail, table):
        conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

        c = conn.cursor()
        en = DoubleVar()
        p = DoubleVar()

        for n in range(20):
            print(entryboxes[n])
            print(prices[n])
            # en=float(entryboxes[n])
            # p=float(prices[n])
            pri = 120 * 1
            res = c.execute()
                INSERT INTO place_order VALUES (:c_id,:d_id,:d_name,:no_table,:quantity,:d_price)",
                #{
                    'c_id': gmail,
                    'd_id': id[n],
                    'd_name': names[n],
                    'no_table': int(table),
                    'quantity': entryboxes[n],
                    'd_price': pri

                })
            if res:
                messagebox.showinfo("Message", "Place Order  Successfully")
            else:
                messagebox.showerror("Error", "Some Thing Went Wrong")

        conn.commit()
        conn.close()

        return ()

    bt_cnf_order = Button(pop, text="Confirm order", fg="White", font=("Courier", 15, "bold"), bg="#1589FF",
                            command=lambda:cnf_order(En_gmail.get(),En_table.get()))
    bt_cnf_order = Button(pop, text="Confirm order", fg="White", font=("Courier", 15, "bold"), bg="#1589FF",
                          command=lambda: cnf_order(En_gmail.get(), En_table.get()))
    bt_cnf_order.grid(row=2, column=1, pady=10)

    return'''


def place_order(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12,
                entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20):
    entryboxes1 = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12,
                   entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20]
    # print(entryboxes1)
    pop = Tk()
    pop.title("Info")
    pop.geometry("450x150")
    lbl_gmail = Label(pop, text="Gmail", fg="BLACK", font=("Courier", 10, "bold"))
    lbl_gmail.grid(row=0, column=0)
    En_gmail = Entry(pop, font=("Helvetica", 10, "bold"))
    En_gmail.grid(row=0, column=1)
    lbl_tableno = Label(pop, text="Table no.", fg="BLACK", font=("Courier", 10, "bold"))
    lbl_tableno.grid(row=1, column=0)
    En_table = Entry(pop, font=("Helvetica", 10, "bold"))
    En_table.grid(row=1, column=1)

    def cnf_order(gmail, table):
        # conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")
        conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")
                            

        c = conn.cursor()

        # c = conn.cursor()
        en = DoubleVar()
        p = DoubleVar()
        pri = DoubleVar()
        # print(en)
        for n in range(20):
            conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

            c = conn.cursor()
            #print(prices[n])
            #print(entryboxes1[n])
            en = float(int(entryboxes1[n]))
            p = float(int(prices[n]))
            # print(entryboxes[n])
            pri = en * p
            #print(pri)

            res = c.execute("INSERT INTO place_orderss VALUES (:c_id,:d_id,:d_name,:no_table,:quantity,:d_price)",
                {
                    'c_id': gmail,
                    'd_id': id[n],
                    'd_name': names[n],
                    'no_table': int(table),
                    'quantity': en,
                    'd_price': pri

                })
            conn.commit()
            conn.close()
            #print(res)
        if res:
            messagebox.showinfo("Message", "Place Order Successfully")
            pop.destroy()
        else:
            messagebox.showerror("Error", "Some Thing Went Wrong")
            pop.destroy()



        return ()



    bt_cnf_order = Button(pop, text="Confirm order", fg="White", font=("Courier", 15, "bold"), bg="#1589FF",
                          command=lambda: cnf_order(En_gmail.get(), En_table.get()))
    bt_cnf_order.grid(row=2, column=1, pady=10)

    return


#bt_place_order=Button(root,text="Place Order",fg="White",font=("Courier",20,"bold"),bg="#1589FF",command=place_order())
#bt_place_order.grid(row=19,column=3,columnspan="3")
bt_place_order=Button(root,text="Place Order",fg="White",font=("Courier",20,"bold"),bg="#1589FF",command=lambda:place_order(En_st_tikka.get(),En_st_papad.get(),En_st_kabab.get(),En_st_katori.get(),En_main_tripple.get(),En_main_soup.get(),En_main_noodles.get(),En_main_fried_rice.get(),En_dosa.get(),En_vada.get(),En_utappa.get(),En_idli.get(),En_main_komdi.get(),En_main_ghavane.get(),En_main_kaju.get(),En_main_thali.get(),En_faluda.get(),En_brownie.get(),En_jamun.get(),En_ice.get()))
bt_place_order.grid(row=19,column=3,columnspan="3")


En_ice.insert(0,"0")
En_st_katori.insert(0,"0")
En_faluda.insert(0,"0")
En_main_kaju.insert(0,"0")
En_jamun.insert(0,"0")
En_brownie.insert(0,"0")
En_main_thali.insert(0,"0")
En_main_ghavane.insert(0,"0")
En_idli.insert(0,"0")
En_utappa.insert(0,"0")
En_vada.insert(0,"0")
En_dosa.insert(0,"0")
En_main_komdi.insert(0,"0")
En_st_kabab.insert(0,"0")
En_main_fried_rice.insert(0,"0")
En_main_tripple.insert(0,"0")
En_main_soup.insert(0,"0")
En_main_noodles.insert(0,"0")
En_st_papad.insert(0,"0")
En_st_tikka.insert(0,"0")

root.mainloop()


