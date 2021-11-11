# from tkinter.ttk import *
# #import login
# import sqlite3
# import os
# import re
# import tkinter as tk
# from tkinter import messagebox
#
#
# def admin_screen():
#
#     #def get_login():
#         #admin.destroy()
#         #login.login_screen()
#
#     #def get_package():
#     #    login.destroy()
#     #    packages.package_screen()
#
#     def validatefields():
#         if username_var.get() == "":
#             tk.messagebox.showinfo('Information','Enter Username')
#         elif password_var.get() == "":
#             tk.messagebox.showinfo('Information','Enter Password')
#
#
#         else:
#             tk.messagebox.showinfo('Information','Login Successful!')
#             #login.destroy()
#             #packages.package_screen()
#
#     #def validatefileds_package():
#       #  validatefields()
#         #get_package()
#     def check_credentials_admin():
#         status = 0
#         username_var_admin = username_text.get()
#         password_var_admin = password_text.get()
#         while True:
#             with sqlite3.connect('Miniproject.db') as db:
#                 cursor = db.cursor()
#             find_user = ("SELECT * FROM userInfo WHERE userNAME = ? AND userPASSWORD = ?")
#             cursor.execute(find_user, [(username_var_admin), (password_var_admin)])
#             result = cursor.fetchall()
#             db.commit()
#
#             if  result:
#                 for i in result:
#                     print("welcome"+i[2])
#                     tk.messagebox.showinfo('Information', 'Login Successful')
#                     return(exit)
#
#             else :
#                 tk.messagebox.showinfo('Information','Invalid Credentials')
#                 return(exit)
#
#
#     admin = tk.Tk()
#
#     username_var = tk.StringVar()
#     password_var = tk.StringVar()
#
#     admin.title("PAPAGO Travel Agency")
#     admin.geometry("720x420")
#     admin.resizable(height=False, width=False)
#
#     # Creating two Frames of different colours
#     frame1 = tk.LabelFrame(admin, width=100, height=420,bg="#AA2B1D")
#     frame1.pack(side=tk.LEFT)
#     frame2 = tk.LabelFrame(admin, width=620, height=420,bg="#FBE0C4")
#     frame2.pack(side=tk.RIGHT)
#     #frame1.configure(bg="#AA2B1D")
#     #frame2.configure(bg="#FBE0C4")
#
#     login_title = tk.Label(frame2, text="ADMIN LOGIN",font = 'Times 35 bold')
#     sign_in_label = tk.Label(frame2, text="Sign in as admin",font = 'Times 15 italic')
#     login_title.place(x=160, y=0)
#     sign_in_label.place(x=240, y=50)
#     login_title.configure(bg="#FBE0C4")
#     sign_in_label.configure(bg="#FBE0C4")
#
#     username_label = tk.Label(frame2, text="Username:",font = 'Times 25',bg="#FBE0C4")
#     username_label.place(x=70, y=115)
#     password_label = tk.Label(frame2, text="Password:",font = 'Times 25',bg="#FBE0C4")
#     password_label.place(x=70, y=175)
#     #username_label.configure(bg="#FBE0C4")
#     #password_label.configure(bg="#FBE0C4")
#
#     username_text = tk.Entry(frame2, width=15,font = 'Times 25')
#     username_text.place(x=280, y=115)
#
#     password_text = tk.Entry(frame2, width=15,font = 'Times 25',show= "*")
#     password_text.place(x=280, y=175)
#
#     login_button = tk.Button(frame2, text="LOGIN ",font = 'Times 20',bg="#AA2B1D",command =check_credentials_admin)
#     #register_button = tk.Button(frame2, text=" ",font='Times 20',c,ommand = get_register,bg="#AA2B1D")
#     #user_sign_in = tk.Button(frame2, text="User Login",font='Times 10',bg="#EABF9F",command= get_login)
#
#     login_button.place(x=240, y=270)
#     #register_button.place(x=240, y=340)
#     #user_sign_in.place(x=15, y=380)
#
#     admin.mainloop()
# if __name__=="__main__":
#     admin_screen()