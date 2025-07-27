from tkinter import*
#from PIL import ImageTk,Image
#import PIL.Image
#import PIL.ImageTk
from PIL import ImageTk
from PIL import Image
from PIL import Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("DashBoard")

root.geometry("1350x650")



taway = ImageTk.PhotoImage(Image.open("takeaway.jpg"))
dining= ImageTk.PhotoImage(Image.open("dining450.png"))
free_home= ImageTk.PhotoImage(Image.open("freehomedelivery_485.jpg"))
edt_cust_profile= ImageTk.PhotoImage(Image.open("editcus450.jpg"))
vw_cust_profile= ImageTk.PhotoImage(Image.open("deleteacc450.jpg"))
lgt_cust_profile= ImageTk.PhotoImage(Image.open("logout450.jpg"))
# make sure app can be resized
root.resizable(width=False, height=False)
my_canvas = Canvas(root, width=1350, height=650, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)
canvastake=Canvas(my_canvas, width=1350, height=650, bd=0, highlightthickness=0)
canvastake.create_image(0,0, image=taway,anchor="nw")

canvastake.create_image(450,0,image=dining,anchor="nw")
canvastake.create_image(900,0,image=free_home,anchor="nw")
canvastake.create_image(0,325,image=edt_cust_profile,anchor="nw")
canvastake.create_image(450,325,image=vw_cust_profile,anchor="nw")
canvastake.create_image(900,325,image=lgt_cust_profile,anchor="nw")
canvastake.pack()

my_canvas.pack()
canvastake.create_line(0, 325, 1350, 325)
canvastake.create_line(450, 0, 450, 325)
canvastake.create_line(900, 0, 900, 325)
canvastake.create_line(450,325, 450, 650)
canvastake.create_line(900, 325, 900, 650)


def menu():
    root.destroy()
    import menupage
    return

def lgtout():

    root.destroy()
    import loginpage
    return
def edit():
    root.destroy()
    import updatereg
    return

take_away_btn = Button(root, text="Take Away", font=("Courier", 15), width=37, fg="white",bg="black",command=menu)
take_away_btn_window = my_canvas.create_window(0, 285, anchor="nw", window=take_away_btn)


dining_btn = Button(root, text="Dine Restaurant", font=("Courier", 15), width=37, fg="black",bg="#F5B041",command=menu)
dining_btn_window = my_canvas.create_window(450, 285, anchor="nw", window=dining_btn)

free_home_btn = Button(root, text="Home Delivery", font=("Courier", 15), width=37, fg="black",bg="#85C1E9",command=menu)
free_home_btn_window = my_canvas.create_window(900, 285, anchor="nw", window=free_home_btn)


edit_cust_pr_btn = Button(root, text="Edit Profile", font=("Courier", 15), width=37, fg="black",bg="#F4D03F",command=edit)
edit_cust_pr_window = my_canvas.create_window(0, 610, anchor="nw", window=edit_cust_pr_btn)



def delete():
    pop = Tk()
    pop.title("Info")
    pop.geometry("400x150+0+0")
    lbl_gmail = Label(pop, text="Gmail", fg="BLACK", font=("Courier", 10, "bold"))
    lbl_gmail.grid(row=0, column=0)
    En_gmail = Entry(pop, font=("Helvetica", 10, "bold"))
    En_gmail.grid(row=0, column=1)

    def cnf_del(gmail):

        mail=gmail
        conn = sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")

        # cursor
        c = conn.cursor()


        query = "DELETE  FROM cust_reg WHERE email=? "
        # insert into table
        res=c.execute(query, [(mail)])


        if res:
            messagebox.showinfo("Message", "Deleted Account  Successfully")
            conn.commit()
            conn.close()
            pop.destroy()
            root.destroy()
            import loginpage

        else:
            conne=sqlite3.connect("C:\\Users\\shrey\\OneDrive\\Desktop\\restaurant management system\\restaurant management system\\hotel.db")
            cu=conne.cursor()
            query1 = "DELETE  FROM cust_reg WHERE email=? "
            # insert into table
            re = c.execute(query, [(mail)])
            if re:
                messagebox.showinfo("Message", "Deleted Account  Successfully")
                conn.commit()
                conn.close()
                pop.destroy()
                import loginpage
            else:



                messagebox.showerror("Message", "Error Occur while deleting your Account")
                pop.destroy()



        return

    bt_cnf_del = Button(pop, text="Delete Account", fg="White", font=("Courier", 15), bg="#1589FF",
                          command=lambda: cnf_del(En_gmail.get()))
    bt_cnf_del.grid(row=1, column=1, pady=10)
    pop.mainloop()

    return

vw_cust_pr_btn = Button(root, text="Delete Profile", font=("Courier", 15), width=37, fg="black",bg="#48C9B0",command=delete)
vw_cust_pr_window = my_canvas.create_window(450, 610, anchor="nw", window=vw_cust_pr_btn)


lgt_cust_pr_btn = Button(root, text="Logout", font=("Courier", 15), width=37, fg="black",bg="#EBF5FB",command=lgtout)
lgt_cust_pr_window = my_canvas.create_window(900, 610, anchor="nw", window=lgt_cust_pr_btn)



root.mainloop()















