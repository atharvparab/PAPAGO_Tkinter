# from tkinter.ttk import *
# import sqlite3
# import os
# import tkinter as tk
# payment_window = tk.Tk()
# payment_window.title("PAPAGO Travel Agency")
# payment_window.geometry("720x420")
# payment_window.resizable(height=False, width=False)
#
# #Creating two Frames of different colours
# frame13 = tk.LabelFrame(payment_window,width = 100 , height = 420, bg = "#AA2B1D")
# frame13.pack(side = tk.LEFT)
# frame14 = tk.LabelFrame(payment_window,width = 620 , height = 420 , bg = "#FBE0C4" )
# frame14.pack(side = tk.RIGHT)
#
#
# payment_title = tk.Label(frame14,text= "PAYMENT", bg = "#FBE0C4", font = 'Times 35 bold')
# payment_title.place(x = 160 , y = 0)
#
# total_cost_label = tk.Label(frame14, text = "Total tour cost :", bg = "#FBE0C4", font = 'Times 25')
#
# total_cost_label.place(x= 35 , y= 55)
#
# label1 = tk.Label(frame14)
# label1.place(x=300 , y=70 , width=200)
#
#
#
# GST_label = tk.Label(frame14,text = "GST @5%      :", bg = "#FBE0C4", font = 'Times 25')
# GST_label.place(x=35, y=115)
#
# label2 = tk.Label(frame14)
# label2.place(x=300 , y=125 , width=200)
# TCS_label = tk.Label(frame14,text = "TCS @5%      :",bg ="#FBE0C4",font = 'Times 25')
# TCS_label.place(x=35, y= 175)
#
# label3 = tk.Label(frame14)
# label3.place(x=300, y=185 ,width=200)
#
# Grand_total_label= tk.Label(frame14,text = "Grand Total    :", bg = "#FBE0C4", font = 'Times 25')
# Grand_total_label.place(x=35, y=235)
#
# label4 = tk.Label(frame14)
# label4.place(x=300 , y=245 , width=200)
#
# Mode_of_payment_label = tk.Label(frame14, text="Mode of payment:", bg="#FBE0C4", font='Times 25')
# Mode_of_payment_label.place(x=35, y=295)
# label5 = tk.Label(frame14)
# label5.place(x=300, y=305, width=200)
#
# options = [
#
#     "credit card",
#     "debit card",
#     "online banking",
#
# ]
# clicked = tk.StringVar()
# clicked.set(options[0])
#
# drop = tk.OptionMenu(frame14, clicked, *options, )
# drop.place(x=300 , y=305, width=200)
#
# mybutton = tk.Button(frame14, text="Sign Out",  font = 'Times 25' ,)
# mybutton.place(x=160 ,y=350 ,width=200)
#
# #total_cost_text = Entry(frame14, text= "total cost", height= 30)
# #username_text.place(x=200, y=115)
#
# payment.mainloop()