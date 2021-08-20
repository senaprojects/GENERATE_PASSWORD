#import the required packages.

import random
from tkinter import *
import string

#to generate password randomly.

def generate_password():
    password=[]
    for i in range(5):
        alpha=random.choice(string.ascii_letters)
        symbol=random.choice(string.punctuation)
        numbers=random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
    y="".join(str(i)for i in password)
    lbl.config(text=y)
#to view the tkinter window inblack background.

root=Tk()
root.title('Tkinter Password Generator')
root.geometry("300x300")
root.configure(bg='black')

#button
btn=Button(root,text="generate password!",command=generate_password,background='white',height=8,width=20,font=("times",10,"bold")).pack(pady=10)

lbl=Label(root,font=("times",15,"bold"))
lbl.pack(anchor='center')

mainloop()