from tkinter import*
#from PIL import ImageTk,Image
#import PIL.Image
#import PIL.ImageTk
from PIL import ImageTk
from PIL import Image
root=Tk()
root.title("Registration Page")

root.geometry("1350x650")

taway = ImageTk.PhotoImage(Image.open("take-away-drawn450.png"))
dining= ImageTk.PhotoImage(Image.open("dining450.png"))
free_home= ImageTk.PhotoImage(Image.open("freehomedelivery_485.jpg"))
edt_cust_profile= ImageTk.PhotoImage(Image.open("editcus450.jpg"))
vw_cust_profile= ImageTk.PhotoImage(Image.open("viw_profile450.png"))
lgt_cust_profile= ImageTk.PhotoImage(Image.open("logout450.jpg"))
# make sure app can't be resized
root.resizable(width=False, height=False)
my_canvas = Canvas(root, width=1350, height=650, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)
canvastake=Canvas(my_canvas, width=1350, height=650, bd=0, highlightthickness=0)
canvastake.create_image(0,0, image=taway,anchor="nw")
canvastake.create_image(450,0,image=dining,anchor="nw")
canvastake.create_image(900,0,image=free_home,anchor="nw")
canvastake.create_image(0,325,image=edt_cust_profile,anchor="nw")
canvastake.create_image(450,325,image=vw_cust_profile,anchor="nw")
canvastake.create_image(900,325,image=lgt_cust_profile,anchor="nw")canvastake.pack()

my_canvas.pack()
canvastake.create_line(0, 325, 1350, 325)
canvastake.create_line(450, 0, 450, 325)
canvastake.create_line(900, 0, 900, 325)
canvastake.create_line(450,325, 450, 650)
canvastake.create_line(900, 325, 900, 650)
take_away_btn = Button(root, text="Take Away", font=("Courier", 15), width=37, fg="white",bg="black")
take_away_btn_window = my_canvas.create_window(0, 285, anchor="nw", window=take_away_btn)


dining_btn = Button(root, text="Dine Restaurant", font=("Courier", 15), width=37, fg="black",bg="#F5B041")
dining_btn_window = my_canvas.create_window(450, 285, anchor="nw", window=dining_btn)

free_home_btn = Button(root, text="Home Delivery", font=("Courier", 15), width=37, fg="black",bg="#85C1E9")
free_home_btn_window = my_canvas.create_window(900, 285, anchor="nw", window=free_home_btn)


edit_cust_pr_btn = Button(root, text="Edit Profile", font=("Courier", 15), width=37, fg="black",bg="#F4D03F")
edit_cust_pr_window = my_canvas.create_window(0, 610, anchor="nw", window=edit_cust_pr_btn)


vw_cust_pr_btn = Button(root, text="View Profile", font=("Courier", 15), width=37, fg="black",bg="#48C9B0")
vw_cust_pr_window = my_canvas.create_window(450, 610, anchor="nw", window=vw_cust_pr_btn)


lgt_cust_pr_btn = Button(root, text="Logout", font=("Courier", 15), width=37, fg="black",bg="#EBF5FB")
lgt_cust_pr_window = my_canvas.create_window(900, 610, anchor="nw", window=lgt_cust_pr_btn)


root.mainloop()