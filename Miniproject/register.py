# import tkinter as tk
# import login
# from tkinter import messagebox
# import sqlite3
# import re
# global username_text
# def register_screen():
#
#    #Phone Number validation (Cannot enter alphabets)
#    def validate_phoneno(user_phoneno):
#       if user_phoneno.isdigit():
#          return True
#       elif user_phoneno == "":
#          return True
#       else:
#          tk.messagebox.showinfo('Information','Only digits are allowed in phone number entry field')
#          return False
#
#    #Email validation
#    def isvalidemail(email_text):
#       print(email_text)
#       if len(email_text) > 7:
#          if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[_a-z0-9-]+(\.[_a-z0-9-]+)*(\.[a-z]{2,4})$' , email_text) != None:
#             return True
#          else:
#             tk.messagebox.showinfo('Information', 'Invalid Email!')
#       else:
#          tk.messagebox.showinfo('Information','Invalid Email!')
#          return False
#
#    #Remaining field validation
#    def validatefields():
#       if name_var.get() == "":
#          tk.messagebox.showinfo('Information','Enter full name')
#       elif username_var.get() == "":
#          tk.messagebox.showinfo('Information','Enter username')
#       elif password_var.get() == "":
#          tk.messagebox.showinfo('Information','Enter password')
#       elif repassword_var.get() == "":
#          tk.messagebox.showinfo('Information','Confirm your password')
#       elif repassword_var.get() != password_var.get():
#          tk.messagebox.showinfo('Information','Password does not match')
#       elif len(contact_var.get()) != 10:
#          tk.messagebox.showinfo('Information', 'Enter 10 digits for phone number')
#       elif email_var.get() != "":
#          tk.status = isvalidemail(email_var.get())
#          tk.messagebox.showinfo('Information', 'Registration Successful!')
#
#       else:
#          tk.messagebox.showinfo('Information', 'Registration Successful!')
#
#
#    def register_click():
#       register.destroy()
#       login.login_screen()
#
#    #Function forms objects of register_click function and validatefields function
#    #def validate_click():
#      # validatefields()
#       #register_click()
#
#
#
#    register = tk.Tk()
#    register.title("PAPAGO Travel Agency")
#    register.geometry("720x420")
#    register.resizable(height=False, width=False)
#
#    name_var = tk.StringVar()
#    username_var = tk.StringVar()
#    password_var = tk.StringVar()
#    repassword_var = tk.StringVar()
#    contact_var = tk.StringVar()
#    email_var = tk.StringVar()
#
# #def login_fun():
#  #   register.destroy()
#   # os.system('login.py')
#
# # Creating two Frames of different colours
#    frame1 = tk.LabelFrame(register, width=100, height=420, bg="#AA2B1D")
#    frame1.pack(side=tk.LEFT)
#    frame2 = tk.LabelFrame(register, width=620, height=420, bg="#FBE0C4")
#    frame2.pack(side=tk.RIGHT)
#
#
#    register_title = tk.Label(frame2, text="REGISTER", bg="#FBE0C4", font='Times 35 bold')
#    register_title.place(x=190, y=0)
#
#
#    name_label = tk.Label(frame2, text="Full Name:", font='Times 20', bg="#FBE0C4")
#    name_label.place(x=40, y=65)
#    username_label = tk.Label(frame2, text="Username:", font='Times 20', bg="#FBE0C4")
#    username_label.place(x=40, y=105)
#    password_label = tk.Label(frame2, text="Password:", font='Times 20', bg="#FBE0C4")
#    password_label.place(x=40, y=145)
#    repassword_label = tk.Label(frame2, text="Confirm Password:", font='Times 20', bg="#FBE0C4")
#    repassword_label.place(x=40, y=185)
#    contact_label = tk.Label(frame2, text="Contact No:", font='Times 20', bg="#FBE0C4")
#    contact_label.place(x=40, y=225)
#    email_label = tk.Label(frame2, text="Email:", font='Times 20', bg="#FBE0C4")
#    email_label.place(x=40, y=265)
#
#    register_button = tk.Button(frame2, text="Register", command= lambda: [validatefields(),register_user()],font='Times 20',bg="#AA2B1D")
#    register_button.place(x=245, y=305)
#    login_button = tk.Button(frame2, text="Go Back To Login", command=register_click, font='Times 20',bg="#EABF9F")
#    login_button.place(x=185, y=365)
#
#    name_text = tk.Entry(frame2, width=20, font='Times 20')
#    name_text.place(x=280, y=65)
#    username_text = tk.Entry(frame2, width=20, font='Times 20')
#    username_text.place(x=280, y=105)
#    password_text = tk.Entry(frame2, width=20, font='Times 20',show = "*")
#    password_text.place(x=280, y=145)
#    repassword_text = tk.Entry(frame2, width=20, font='Times 20',show = "*")
#    repassword_text.place(x=280, y=185)
#    contact_text = tk.Entry(frame2, width=20, font='Times 20')
#    contact_text.place(x=280, y=225)
#    email_text = tk.Entry(frame2, width=20, font='Times 20')
#    email_text.place(x=280, y=265)
#
#    valid_phone = register.register(validate_phoneno)
#    contact_text.config(validate ="key",validatecommand = (valid_phone, '%P'))
#
#    #databse connectioncursor.execute("""
#    CREATE TABLE IF NOT EXISTS userInfo(
#    userID INTEGER PRIMARY KEY AUTOINCREMENT,
#    userFULLNAME VARCHAR(50) NOT NULL,
#    userNAME VARCHAR(50) NOT NULL UNIQUE,
#    userPASSWORD VARCHAR(5) NOT NULL,
#    userCONTACT VARCHAR(10) NOT NULL,
#    userEMAIL VARCHAR(50) NOT NULL UNIQUE
#    );
#    """)
#
#    # cursor.execute("""
#    # INSERT INTO userInfo(userID,userFULLNAME,userNAME,userPASSWORD,userCONTACT,userEMAIL)
#    # VALUES (101,"admin","adminlogin","adminlogin","1234567899","adminlogin17@gmail.com")
#    # """)
#    db.commit()
#    with sqlite3.connect('Miniproject.db') as db:
#       cursor = db.cursor()
#
#
#    def register_user():
#       found =0
#       name_var = tk.StringVar()
#       name_var = name_text.get()
#       username_var = username_text.get()
#       password_var = password_text.get()
#       repassword_var = repassword_text.get()
#       contact_var = contact_text.get()
#       email_var = email_text.get()
#       while found == 0:
#          with sqlite3.connect('Miniproject.db') as db:
#             cursor = db.cursor()
#          findUser = ("SELECT  * FROM userInfo where userName = ?" )
#          cursor.execute(findUser,[(username_var)])
#          result = cursor.fetchall()
#
#          if (result):
#             tk.messagebox.showinfo('Information','Username already taken. Enter different username')
#          else:
#             found = 1
#          while password_var != repassword_var:
#             tk.messagebox.showinfo('Information','Password dont match')
#          insertData = ("""
#          INSERT INTO userInfo(userFULLNAME,userName,userPassword,userCONTACT,userEMAIL) VALUES (?,?,?,?,?)
#          """)
#          cursor.execute(insertData,[(name_var),(username_var),(password_var),(contact_var),(email_var)])
#          db.commit()
#
#
#
#    cursor.execute("SELECT * FROM userInfo")
#    print(cursor.fetchall())
#
#    register.mainloop()
#
# if __name__=="__main__":
#     register_screen()