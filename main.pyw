# from tkinter import *
import os
from tkinter import messagebox, Tk, Frame, Label, Entry, PhotoImage, Button, font

# mainWindow
w = Tk()
w.geometry("350x500")
w.title("LOGIN")
# w.resizable(0,0)
icon1 = PhotoImage(file="login.png")
w.iconphoto(False, icon1)

# background
j = 0
r = 0
for i in range(100):
    c = str(222222 + r)
    Frame(w, width=10, height=500, bg="#" + c).place(x=j, y=0)
    j = j + 10
    r = r + 1

Frame(w, width=250, height=435, bg="white").place(x=50, y=50)
normalFont = font.Font(family="Helvetica", name="normalFont", size=14)

# Label & Entry 1
l1 = Label(w, text="Username", bg="white")
l = ("consolas", 13)
l1.config(font=normalFont)
l1.place(x=80, y=200)

e1 = Entry(w, width=20, border=0)
e1.config(font=normalFont)
e1.place(x=80, y=230)

# Label & Entry 2
l2 = Label(w, text="Password", bg="white")
l = ("consolas", 13)
l2.config(font=normalFont)
l2.place(x=80, y=280)

e2 = Entry(w, width=20, border=0)
e2.config(font=normalFont)
e2.place(x=80, y=310)

Frame(w, width=180, height=2, bg="#141414").place(x=80, y=250)
Frame(w, width=180, height=2, bg="#141414").place(x=80, y=330)

# Image
from PIL import ImageTk, Image

image1 = Image.open("login2.png")
image2 = ImageTk.PhotoImage(image1)

label1 = Label(image=image2, border=0, justify="center")
label1.place(x=115, y=50)

# login function
def cmd():
    sucess = False
    with open("user_details.txt", "r") as file:
        for line in file:
            a, b = line.split(",")
            a, b = a.strip(), b.strip()
            print(a + " " + b)
            if a == e1.get() and b == e2.get():
                messagebox.showinfo("LOGIN SUCCESSFULLY", "       WELCOME       ")
                w.destroy()

                q = Tk()
                q.geometry("600x300")
                label11 = Label(q, text=f"Hello {a}")
                label11.place(x=250, y=120)
                q.mainloop()
                file.close()
                break
        else:
            messagebox.showinfo(
                "? LOGIN FAILED ?", "   !!       PLEASE TRY AGAIN       !!  "
            )
            print(e1.get() + " " + e2.get())


# register function
def cmd2():
    file = open("user_details.txt", "a")
    file.write(e1.get() + "," + e2.get() + "\n")
    messagebox.showinfo("REGISRED SUCCESSFULLY", "       SUCCESS       ")

    file.close()


# Button
Button(
    w, text="Login", width=20, height=2, fg="white", bg="#994422", border=0, command=cmd
).place(x=100, y=375)
Button(
    w,
    text="Register",
    width=20,
    height=2,
    fg="white",
    bg="#994422",
    border=0,
    command=cmd2,
).place(x=100, y=420)
w.mainloop()
