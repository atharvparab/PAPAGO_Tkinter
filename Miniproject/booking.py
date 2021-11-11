# import tkinter as tk
# import packages
#
#
# #response = packages.check_DestinationDetails()
# def booking_screen():
#     # def getName():
#     #     package_screen().Destination.get()
#     booking = tk.Tk()
#     booking.title("Booking_summary")
#     booking.geometry("720x420")
#     booking.resizable(height=False, width=False)
#
#     frame1 = tk.LabelFrame(booking,width = 100 , height = 420, bg = "#AA2B1D")
#     frame1.pack(side = tk.LEFT)
#     frame2 = tk.LabelFrame(booking,width = 620 , height = 420 , bg = "#FBE0C4" )
#     frame2.pack(side = tk.RIGHT)
#
#     page_title = tk.Label(frame2,text= "BOOKING SUMMARY", bg = "#FBE0C4", font = 'Times 35 bold')
#     page_title.place(x = 90 , y = 0)
#
#     destination_label = tk.Label(frame2,text="Destination         :",bg = "#FBE0C4", font = 'Times 25 ')
#     destination_label.place(x = 35, y = 115)
#     passenger_label = tk.Label(frame2,text="Passenger Name :",bg = "#FBE0C4", font = 'Times 25 ')
#     passenger_label.place(x = 35 , y = 175)
#     travel_date_label = tk.Label(frame2,text="Travel Date        :",bg = "#FBE0C4", font = 'Times 25 ')
#     travel_date_label.place(x = 35 , y = 235)
#
#
#
# #RHS
#     right_destination = tk.Label(frame2,font = 'Times 20 italic',text=packages.Destination.get())
#     right_passenger = tk.Label(frame2)
#     right_travel_date = tk.Label(frame2)
#     # get_name =tk.Button(frame2,command= lambda: getName() )
#     right_destination.place(x = 275, y = 120,width = 250,height = 35)
#     right_passenger.place(x = 275 ,y =180 ,width =250 ,height = 35)
#     right_travel_date.place(x = 275,y = 240 ,width = 250 ,height =35)
#
#
#
#
#     bt = tk.Button(frame2,text="CONTINUE",bg ="#AA2B1D",font = "Times 20")
#     bt.place(x = 210  , y = 320, width =150)
#
#     booking.mainloop()
# if __name__=="__main__":
#     booking_screen()