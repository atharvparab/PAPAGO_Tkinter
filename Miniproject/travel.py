# import tkinter as tk
# from tkcalendar import*
# from packages import *
# import booking
# def travel_screen():
#
#     def get_booking():
#         travel.destroy()
#         booking.booking_screen()
#
#
#     #window
#     travel = tk.Tk()
#     travel.title("TRAVEL DETAILS")
#     travel.geometry("720x420")
#     travel.resizable(height=False, width=False)
#
#     #frame
#     frame1 = tk.LabelFrame(travel,width = 100 , height = 420, bg = "#AA2B1D")
#     frame1.pack(side = tk.LEFT)
#     frame2 = tk.LabelFrame(travel,width = 620 , height = 420 , bg = "#FBE0C4" )
#     frame2.pack(side = tk.RIGHT)
#
#
#     page_title = tk.Label(frame2,text= "TRAVEL DETAILS", bg = "#FBE0C4", font = 'Times 35 bold')
#     page_title.place(x = 90 , y = 0)
#
#     adult_label = tk.Label(frame2,text="Adult :",bg = "#FBE0C4", font = 'Times 25 ')
#     adult_label.place(x = 15, y = 70)
#     child_label = tk.Label(frame2,text="Child :",bg = "#FBE0C4", font = 'Times 25 ')
#     child_label.place(x = 15 , y = 170)
#     infant_label = tk.Label(frame2,text="Infant :",bg = "#FBE0C4", font = 'Times 25 ')
#     infant_label.place(x = 15, y = 270)
#     date_label = tk.Label(frame2,text="Date :",bg = "#FBE0C4", font = 'Times 25 ')
#     date_label.place(x = 235 , y = 70)
#         #passenger_label = Label(frame2,text="Passenger Name :",bg = "#FBE0C4", font = 'Times 25 bold')
#         #passenger_label.place(x=35,y=115)
#
#     #spin_box
#     spin_adult = tk.Spinbox(frame2, from_=0 ,to=100 ,width=5)
#     spin_adult.config(font = 'Times 12 italic')
#     spin_adult.place(x =  120,y = 80)
#     spin_infant = tk.Spinbox(frame2, from_=0 ,to=100 ,width=5)
#     spin_infant.config(font = 'Times 12 italic')
#     spin_infant.place(x = 120,y = 180)
#     spin_child = tk.Spinbox(frame2, from_=0 ,to=100 ,width=5)
#     spin_child.config(font = 'Times 12 italic')
#     spin_child.place(x = 120,y = 280)
#
#     #calendar
#     cal = Calendar(frame2,selectmode="day",year=2021,month=5,day=5)
#     cal.place(x= 345,y= 70)
#     def grab_date():
#      my_label.config(text="The Selected Date is : " + cal.get_date())
#
#
#     #my_label_var = tk.StringVar()
#
#     button_cal = tk.Button(frame2,text = "Get Date" , command=grab_date)
#     button_cal.place(x=440,y=280)
#
#     my_label = tk.Label(frame2,text="")
#     my_label.place(x= 395,y=315)
#
#     #button
#     bt = tk.Button(frame2,text="CONTINUE",bg ="#AA2B1D",font = "Times 20",command = get_booking )
#     bt.place(x = 210  , y = 330, width =150)
#     #trial = package_screen.Destination.get()
#     travel.mainloop()
# if __name__=="__main__":
#     travel_screen()