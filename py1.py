from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("3.jpg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
    "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white')
button1.place(x=260, y=360)

def topwin():
    # Top Window
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    # Create widgets INSIDE top window

    label = Label(top, text="Enter Total Amount:", bg="grey")
    label.place(x=230, y=50)

    entry = Entry(top)
    entry.place(x=200, y=80)

    btn = Button(top, text="Calculate", bg="brown", fg="white")
    btn.place(x=240, y=120)

    lbl = Label(top, text="Denomination Count", bg="grey")
    lbl.place(x=140, y=170)

    l1 = Label(top, text="2000 Notes:", bg="grey")
    l1.place(x=180, y=200)

    l2 = Label(top, text="500 Notes:", bg="grey")
    l2.place(x=180, y=230)

    l3 = Label(top, text="100 Notes:", bg="grey")
    l3.place(x=180, y=260)

    t1 = Entry(top)
    t1.place(x=270, y=200)

    t2 = Entry(top)
    t2.place(x=270, y=230)

    t3 = Entry(top)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()