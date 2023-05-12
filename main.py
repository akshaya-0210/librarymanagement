from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
mypass = "123456"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password='123456',database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("700x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text=" Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='white', fg='black', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='white', fg='black', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Issue Book to Student",bg='white', fg='black', command = issueBook)
btn3.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn4.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
'''btn5 = Button(root,text="view Book",bg='black', fg='white', command = view)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)'''

root.mainloop()
