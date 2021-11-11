# import tkinter as tk
# from tkinter import messagebox
# # from tkinter.ttk import *
# # import register, packages, admin
# import sqlite3
# import os
# import re
#
# def download_screen():
#
#     download = tk.Tk()
#     download.title("PAPAGO Travel Agency")
#     download.geometry("720x420")
#     download.resizable(height=False, width=False)
#
#     # Creating two Frames of different colours
#     frame1 = tk.LabelFrame(download, width=100, height=420, bg="#AA2B1D")
#     frame1.pack(side=tk.LEFT)
#     frame2 = tk.LabelFrame(download, width=620, height=420, bg="#FBE0C4")
#     frame2.pack(side=tk.RIGHT)
#
#     admin_title = tk.Label(frame2, text="Admin", font='Times 35 bold')
#     admin_label = tk.Label(frame2, text="Download data ", font='Times 15 italic')
#     admin_title.place(x=230, y=0)
#     admin_label.place(x=210, y=50)
#     admin_title.configure(bg="#FBE0C4")
#     admin_label.configure(bg="#FBE0C4")
#
#
#
#     download.mainloop()
# if __name__=="__main__":
#     download_screen()