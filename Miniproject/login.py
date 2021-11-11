# import tkinter as tk
# from tkinter import messagebox
# #from tkinter.ttk import *
# import register, packages, admin
# import sqlite3
# import os
# import re
#
#
# def login_screen():
#
#     def get_register():
#         login.destroy()
#         register.register_screen()
#
#     def get_admin():
#         login.destroy()
#         admin.admin_screen()
#
#     # def get_package():
#     #     login.destroy()
#     #     packages.package_screen()
#
#     def validatefields():
#         if username_var.get() == "":
#             tk.messagebox.showinfo('Information','Enter Username')
#         elif password_var.get() == "":
#             tk.messagebox.showinfo('Information','Enter Password')
#         elif username_var.get() == "admin":
#             tk.messagebox.showinfo('Information','Invalid Login Screen. Click on Admin Login')
#
#         else:
#             tk.messagebox.showinfo('Information','Login Successful!')
#             #login.destroy()
#             #packages.package_screen()
#
#     #def validatefileds_package():
#       #  validatefields()
#         #get_package()
#
#
#     login = tk.Tk()
#
#     username_var = tk.StringVar()
#     password_var = tk.StringVar()
#     #databse connection
#     def check_credentials():
#         while True:
#             with sqlite3.connect('Miniproject.db') as db:
#                 cursor = db.cursor()
#                 find_user = ("SELECT * FROM userInfo WHERE userNAME = ? AND userPASSWORD = ?")
#                 cursor.execute(find_user,[(username_var),(password_var)])
#                 result = cursor.fetchall()
#
#             if result is (True):
#                 tk.messagebox.showinfo('Information','Login Successful')
#
#
#     login.title("PAPAGO Travel Agency")
#     login.geometry("720x420")
#     login.resizable(height=False, width=False)
#
#     # Creating two Frames of different colours
#     frame1 = tk.LabelFrame(login, width=100, height=420,bg="#AA2B1D")
#     frame1.pack(side=tk.LEFT)
#     frame2 = tk.LabelFrame(login, width=620, height=420,bg="#FBE0C4")
#     frame2.pack(side=tk.RIGHT)
#     #frame1.configure(bg="#AA2B1D")
#     #frame2.configure(bg="#FBE0C4")
#
#     login_title = tk.Label(frame2, text="LOGIN",font = 'Times 35 bold')
#     sign_in_label = tk.Label(frame2, text="Sign in to your account",font = 'Times 15 italic')
#     login_title.place(x=230, y=0)
#     sign_in_label.place(x=210, y=50)
#     login_title.configure(bg="#FBE0C4")
#     sign_in_label.configure(bg="#FBE0C4")
#
#     username_label = tk.Label(frame2, text="Username:",font = 'Times 25',bg="#FBE0C4")
#     username_label.place(x=70, y=115)
#     password_label = tk.Label(frame2, text="Password:",font = 'Times 25',bg="#FBE0C4")
#     password_label.place(x=70, y=175)
#     #username_label.configure(bg="#FBE0C4")
#     #password_label.configure(bg="#FBE0C4")
#     global username_text
#     username_text = tk.Entry(frame2,textvariable = username_var, width=15,font = 'Times 25')
#     username_text.place(x=280, y=115)
#
#     password_text = tk.Entry(frame2,textvariable= password_var, width=15,font = 'Times 25',show= "*")
#     password_text.place(x=280, y=175)
#
#     login_button = tk.Button(frame2, text="LOGIN ",font = 'Times 20',bg="#AA2B1D",command = lambda: [validatefields(), check_credentials()])
#     register_button = tk.Button(frame2, text="Sign-up ",font='Times 20',command = get_register,bg="#AA2B1D")
#     admin_sign_in = tk.Button(frame2, text="Admin Login",font='Times 10',bg="#EABF9F",command= get_admin)
#
#     login_button.place(x=240, y=270)
#     register_button.place(x=240, y=340)
#     admin_sign_in.place(x=15, y=380)
#
#
#     login.mainloop()
# if __name__=="__main__":
#     login_screen()
#
