# import tkinter as tk
# from tkinter import messagebox
# #from tkinter.ttk import *
# import register, packages, admin
# import sqlite3
# import os
# import re
#
#
# def get_register():
#     login.destroy()
#     register.register_screen()
#
#
# def get_admin():
#     login.destroy()
#     admin.admin_screen()
#
#
# def get_package():
#     login.destroy()
#     packages.package_screen()
#
#
# def validatefields():
#     if username_var.get() == "":
#         tk.messagebox.showinfo('Information', 'Enter Username')
#     elif password_var.get() == "":
#         tk.messagebox.showinfo('Information', 'Enter Password')
#     elif username_var.get() == "admin":
#         tk.messagebox.showinfo('Information', 'Invalid Login Screen. Click on Admin Login')
#
#     else:
#         tk.messagebox.showinfo('Information', 'Login Successful!')
#         # login.destroy()
#         # packages.package_screen()
#
#
# # def validatefileds_package():
# #  validatefields()
# # get_package()
#
#
# login = tk.Tk()
#
# username_var = tk.StringVar()
# password_var = tk.StringVar()
#
#
# # databse connection
# def check_credentials():
#     while True:
#         with sqlite3.connect('Miniproject.db') as db:
#             cursor = db.cursor()
#             find_user = ("SELECT * FROM userInfo WHERE userNAME = ? AND userPASSWORD = ?")
#             cursor.execute(find_user, [(username_var), (password_var)])
#             result = cursor.fetchall()
#
#         if result is (True):
#             tk.messagebox.showinfo('Information', 'Login Successful')
#
#
# login.title("PAPAGO Travel Agency")
# login.geometry("720x420")
# login.resizable(height=False, width=False)
#
# # Creating two Frames of different colours
# frame1 = tk.LabelFrame(login, width=100, height=420, bg="#AA2B1D")
# frame1.pack(side=tk.LEFT)
# frame2 = tk.LabelFrame(login, width=620, height=420, bg="#FBE0C4")
# frame2.pack(side=tk.RIGHT)
# # frame1.configure(bg="#AA2B1D")
# # frame2.configure(bg="#FBE0C4")
#
# login_title = tk.Label(frame2, text="LOGIN", font='Times 35 bold')
# sign_in_label = tk.Label(frame2, text="Sign in to your account", font='Times 15 italic')
# login_title.place(x=230, y=0)
# sign_in_label.place(x=210, y=50)
# login_title.configure(bg="#FBE0C4")
# sign_in_label.configure(bg="#FBE0C4")
#
# username_label = tk.Label(frame2, text="Username:", font='Times 25', bg="#FBE0C4")
# username_label.place(x=70, y=115)
# password_label = tk.Label(frame2, text="Password:", font='Times 25', bg="#FBE0C4")
# password_label.place(x=70, y=175)
# # username_label.configure(bg="#FBE0C4")
# # password_label.configure(bg="#FBE0C4")
# global username_text
# username_text = tk.Entry(frame2, textvariable=username_var, width=15, font='Times 25')
# username_text.place(x=280, y=115)
#
# password_text = tk.Entry(frame2, textvariable=password_var, width=15, font='Times 25', show="*")
# password_text.place(x=280, y=175)
#
# login_button = tk.Button(frame2, text="LOGIN ", font='Times 20', bg="#AA2B1D",
#                          command=lambda: [validatefields(), get_package()])
# register_button = tk.Button(frame2, text="Sign-up ", font='Times 20', command=get_register, bg="#AA2B1D")
# admin_sign_in = tk.Button(frame2, text="Admin Login", font='Times 10', bg="#EABF9F", command=get_admin)
#
# login_button.place(x=240, y=270)
# register_button.place(x=240, y=340)
# admin_sign_in.place(x=15, y=380)
#
# register_window = tk.Toplevel(login)
#
#
# # Phone Number validation (Cannot enter alphabets)
# def validate_phoneno(user_phoneno):
#     if user_phoneno.isdigit():
#         return True
#     elif user_phoneno == "":
#         return True
#     else:
#         tk.messagebox.showinfo('Information', 'Only digits are allowed in phone number entry field')
#         return False
#
#
# # Email validation
# def isvalidemail(email_text):
#     print(email_text)
#     if len(email_text) > 7:
#         if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[_a-z0-9-]+(\.[_a-z0-9-]+)*(\.[a-z]{2,4})$', email_text) != None:
#             return True
#         else:
#             tk.messagebox.showinfo('Information', 'Invalid Email!')
#     else:
#         tk.messagebox.showinfo('Information', 'Invalid Email!')
#         return False
#
#
# # Remaining field validation
# def validatefields():
#     if name_var.get() == "":
#         tk.messagebox.showinfo('Information', 'Enter full name')
#     elif username_var.get() == "":
#         tk.messagebox.showinfo('Information', 'Enter username')
#     elif password_var.get() == "":
#         tk.messagebox.showinfo('Information', 'Enter password')
#     elif repassword_var.get() == "":
#         tk.messagebox.showinfo('Information', 'Confirm your password')
#     elif repassword_var.get() != password_var.get():
#         tk.messagebox.showinfo('Information', 'Password does not match')
#     elif len(contact_var.get()) != 10:
#         tk.messagebox.showinfo('Information', 'Enter 10 digits for phone number')
#     elif email_var.get() != "":
#         tk.status = isvalidemail(email_var.get())
#         tk.messagebox.showinfo('Information', 'Registration Successful!')
#
#     else:
#         tk.messagebox.showinfo('Information', 'Registration Successful!')
#
#
# def register_click():
#     register.destroy()
#     login.login_screen()
#
#
# # Function forms objects of register_click function and validatefields function
# # def validate_click():
# # validatefields()
# # register_click()
#
#
# register = tk.Tk()
# register.title("PAPAGO Travel Agency")
# register.geometry("720x420")
# register.resizable(height=False, width=False)
#
# name_var = tk.StringVar()
# username_var = tk.StringVar()
# password_var = tk.StringVar()
# repassword_var = tk.StringVar()
# contact_var = tk.StringVar()
# email_var = tk.StringVar()
#
# # def login_fun():
# #   register.destroy()
# # os.system('login.py')
#
# # Creating two Frames of different colours
# frame1 = tk.LabelFrame(register, width=100, height=420, bg="#AA2B1D")
# frame1.pack(side=tk.LEFT)
# frame2 = tk.LabelFrame(register, width=620, height=420, bg="#FBE0C4")
# frame2.pack(side=tk.RIGHT)
#
# register_title = tk.Label(frame2, text="REGISTER", bg="#FBE0C4", font='Times 35 bold')
# register_title.place(x=190, y=0)
#
# name_label = tk.Label(frame2, text="Full Name:", font='Times 20', bg="#FBE0C4")
# name_label.place(x=40, y=65)
# username_label = tk.Label(frame2, text="Username:", font='Times 20', bg="#FBE0C4")
# username_label.place(x=40, y=105)
# password_label = tk.Label(frame2, text="Password:", font='Times 20', bg="#FBE0C4")
# password_label.place(x=40, y=145)
# repassword_label = tk.Label(frame2, text="Confirm Password:", font='Times 20', bg="#FBE0C4")
# repassword_label.place(x=40, y=185)
# contact_label = tk.Label(frame2, text="Contact No:", font='Times 20', bg="#FBE0C4")
# contact_label.place(x=40, y=225)
# email_label = tk.Label(frame2, text="Email:", font='Times 20', bg="#FBE0C4")
# email_label.place(x=40, y=265)
#
# register_button = tk.Button(frame2, text="Register", command=lambda: [validatefields(), register_user()],
#                             font='Times 20', bg="#AA2B1D")
# register_button.place(x=245, y=305)
# login_button = tk.Button(frame2, text="Go Back To Login", command=register_click, font='Times 20', bg="#EABF9F")
# login_button.place(x=185, y=365)
#
# name_text = tk.Entry(frame2, width=20, font='Times 20')
# name_text.place(x=280, y=65)
# username_text = tk.Entry(frame2, width=20, font='Times 20')
# username_text.place(x=280, y=105)
# password_text = tk.Entry(frame2, width=20, font='Times 20', show="*")
# password_text.place(x=280, y=145)
# repassword_text = tk.Entry(frame2, width=20, font='Times 20', show="*")
# repassword_text.place(x=280, y=185)
# contact_text = tk.Entry(frame2, width=20, font='Times 20')
# contact_text.place(x=280, y=225)
# email_text = tk.Entry(frame2, width=20, font='Times 20')
# email_text.place(x=280, y=265)
#
# valid_phone = register.register(validate_phoneno)
# contact_text.config(validate="key", validatecommand=(valid_phone, '%P'))
#
# # databse connection
# with sqlite3.connect('Miniproject.db') as db:
#     cursor = db.cursor()
#
# cursor.execute("""
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
# # cursor.execute("""
# # INSERT INTO userInfo(userID,userFULLNAME,userNAME,userPASSWORD,userCONTACT,userEMAIL)
# # VALUES (101,"admin","adminlogin","adminlogin","1234567899","adminlogin17@gmail.com")
# # """)
# db.commit()
#
#
# def register_user():
#     found = 0
#     name_var = tk.StringVar()
#     name_var = name_text.get()
#     username_var = username_text.get()
#     password_var = password_text.get()
#     repassword_var = repassword_text.get()
#     contact_var = contact_text.get()
#     email_var = email_text.get()
#     while found == 0:
#         with sqlite3.connect('Miniproject.db') as db:
#             cursor = db.cursor()
#         findUser = ("SELECT  * FROM userInfo where userName = ?")
#         cursor.execute(findUser, [(username_var)])
#         result = cursor.fetchall()
#
#         if (result):
#             tk.messagebox.showinfo('Information', 'Username already taken. Enter different username')
#         else:
#             found = 1
#         while password_var != repassword_var:
#             tk.messagebox.showinfo('Information', 'Password dont match')
#         insertData = ("""
#          INSERT INTO userInfo(userFULLNAME,userName,userPassword,userCONTACT,userEMAIL) VALUES (?,?,?,?,?)
#          """)
#         cursor.execute(insertData, [(name_var), (username_var), (password_var), (contact_var), (email_var)])
#         db.commit()
#
#
# cursor.execute("SELECT * FROM userInfo")
# print(cursor.fetchall())
#
# login.mainloop()