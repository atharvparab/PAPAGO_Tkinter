# # import  tkinter as tk
# # import login,travel
# # import sqlite3
# # from tkinter import messagebox
# #
# #
# #
# # def get_logout():
# #     packages.destroy()
# #     login.login_screen()
# #
# # def get_travel():
# #     packages.destroy()
# #     travel.travel_screen()
# #
# #
# #
# # packages = tk.Tk()
# # packages.title("PAPAGO Travel Agency")
# # packages.geometry("720x420")
# # packages.resizable(height=False, width=False)
# #
# # #Creating two Frames of different colours
# # frame1 = tk.LabelFrame(packages,width = 100 , height = 420, bg = "#AA2B1D")
# # frame1.pack(side = tk.LEFT)
# # frame2 = tk.LabelFrame(packages,width = 620 , height = 420 , bg = "#FBE0C4" )
# # frame2.pack(side = tk.RIGHT)
# #
# #
# # package_title = tk.Label(frame2,text= "PACKAGES", bg = "#FBE0C4", font = 'Times 35 bold')
# #     #sign_in_label = Label(frame2, text = "Sign in to your account", bg = "#FBE0C4", font = 'Times 15 italic')
# # package_title.place(x = 185 , y = 0)
# #     #sign_in_label.place(x= 210, y= 50)
# #
# # destination_label     = tk.Label(frame2,text = "Destination            :", bg = "#FBE0C4", font = 'Times 25')
# # destination_label.place(x=35, y=115)
# # BudgetPerAdult_label = tk.Label(frame2,text = "Budget Per Adult  :",bg ="#FBE0C4",font = 'Times 25')
# # BudgetPerAdult_label .place(x=35, y= 175)
# # BudgetPerChild_label = tk.Label(frame2,text = "Budget Per Child  :",bg = "#FBE0C4", font ='Times 25')
# # BudgetPerChild_label.place(x=35, y=235)
# #     #TravelMonth_label = tk.Label(frame2,text = "Travel Month        :",bg = "#FBE0C4", font ='Times 25')
# #     #TravelMonth_label.place(x=35, y=295)
# # BudgetPerInfant_label = tk.Label(frame2,text = "Budget Per Infant  :",bg = "#FBE0C4", font ='Times 25')
# # BudgetPerInfant_label.place(x=35, y=295)
# #
# # #Drop Down Box
# # # global Destination
# # # global trial
# # Destination = tk.StringVar()
# # # trial = tk.StringVar(frame2)
# #     # trial = Destination.get()
# #     # trial.set(Destination.get())
# #     # tk.StringVar(trial)
# # Destination_Options = [
# #     "Maldives",
# #     "Bali",
# #     "Bangkok",
# #     "Europe"
# #     ]
# #
# # dropDestination = tk.OptionMenu(frame2,Destination,*Destination_Options)
# # dropDestination.config(font ="Times 15 italic")
# # dropDestination.place(x=320,y=115,width =150)
# #
# #
# # #Drop Down Box
# # #DestinationMonth = tk.StringVar()
# # #DestinationMonth_Options = [
# #    # "January",
# #    # "February",
# #    # "March",
# #     #"April",
# #     #"May",
# #    # "June",
# #     #"July",
# #     #"August",
# #    # "September",
# # #    "November",
# #     #"December"
# # #]
# #
# # #dropDestinationMonth = tk.OptionMenu(frame2,DestinationMonth,*DestinationMonth_Options)
# # #dropDestinationMonth.config(font ="Times 20 italic")
# # #dropDestinationMonth.place(x=320,y=300,width =200)
# #
# # #Database Connection
# #
# # def check_DestinationDetails():
# #     desName_var = tk.StringVar()
# #
# #     desName_var = Destination.get()
# #         #print(Des)
# #         # Destination_Name(desName_var)
# #
# #     while True:
# #         with sqlite3.connect('Miniproject.db') as db:
# #             cursor = db.cursor()
# #         find_user = ("SELECT * FROM Destination WHERE desName = ? ")
# #         cursor.execute(find_user, [(desName_var)])
# #         result = cursor.fetchall()
# #
# #         db.commit()
# #
# #         if result:
# #             for i in result:
# #                 budgetadult = i[2]
# #                 print(budgetadult)
# #                     #tk.messagebox.showinfo('Information', 'Destination Selected successfully')
# #                 Label1 = tk.Label(frame2, font='Times 25', text=budgetadult)
# #                 Label1.place(x=320, y=185, width=200)
# #
# #                 budgetchild = i[3]
# #                 print(budgetchild)
# #                 Label2 = tk.Label(frame2, font='Times 25',text=budgetchild)
# #                 Label2.place(x=320, y=245, width=200)
# #
# #                 budgetinfant = i[4]
# #                 print(budgetinfant)
# #                 Label3 = tk.Label(frame2, font='Times 25', text=budgetinfant)
# #                 Label3.place(x=320, y=295, width=200)
# #                     # Budget_Details(budgetadult,budgetchild,budgetinfant)
# #                 return (exit)
# #
# #
# #         else:
# #             tk.messagebox.showinfo('Information', 'Invalid Credentials')
# #             return (exit)
# #
# #
# #
# #     # def Destination_Name(a):
# #     #     print(a)
# #     #     return a
# #     # def Budget_Details(b,c,d):
# #     #     print(b)
# #     #     print(c)
# #     #     print(d)
# #     #     return b
# #     #     return c
# #     #     return d
# # LabelBudgetadult = tk.Label(frame2,font = 'Times 25')
# # LabelBudgetadult.place(x=320,y=185,width=200)
# # LabelBudgetchild = tk.Label(frame2,font = 'Times 25')
# # LabelBudgetchild.place(x=320,y=245,width=200)
# # LabelBudgetinfant = tk.Label(frame2,font = 'Times 25')
# # LabelBudgetinfant.place(x=320,y=300,width =200)
# #
# #
# # ButtonContinue = tk.Button(frame2,text = "CONTINUE",font = 'Times 20', bg = "#AA2B1D",command= get_travel)
# # ButtonContinue.place(x=150,y=360,width=150)
# # ButtonBack = tk.Button(frame2,text = "Logout",font = 'Times 20', bg = "#AA2B1D",command= get_logout)
# # ButtonBack.place(x=350,y=360,width=100)
# #
# # Btn_Confirm = tk.Button(frame2,text = "Confirm",font = 'Times 15', bg = "#AA2B1D",command = check_DestinationDetails)
# # Btn_Confirm.config(font ="Times 15 italic")
# # Btn_Confirm.place(x=480,y=115,width=90)
# #     #username = login.login_screen.username_text.get()
# #
# #     #databse connection
# with sqlite3.connect('Miniproject.db') as db:
#
#     db.execute("PRAGMA FOREIGN_KEYS=1")
#     cursor = db.cursor()
#
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Destination(
#     desID INTEGER PRIMARY KEY AUTOINCREMENT,
#     desNAME VARCHAR(50) NOT NULL UNIQUE,
#     priceadult VARCHAR(5) NOT NULL,
#     pricechild VARCHAR(10) NOT NULL,
#     priceinfant VARCHAR(50) NOT NULL UNIQUE,
#     userID INTEGER,
#     FOREIGN KEY (userID)
#         REFERENCES userInfo (userID)
#     );
#     """)
#
#
#
#     cursor.execute("""
# INSERT INTO Destination(desID,desNAME,priceadult,pricechild,priceinfant)
# VALUES (202,"Bali","1,00,000","50,000","20,000")
# """)
#
#     cursor.execute("""
# INSERT INTO Destination(desID,desNAME,priceadult,pricechild,priceinfant)
# VALUES (203,"Bangkok","1,50,000","90,000","40,000")
# """)
#
#     cursor.execute("""
# INSERT INTO Destination(desID,desNAME,priceadult,pricechild,priceinfant)
# VALUES (204,"Europe","3,00,000","2,00,000","150,000")
# """)
#     db.commit()
#
#     cursor.execute("SELECT * FROM Destination")
#     print(cursor.fetchall())
# #
# # packages.mainloop()
# #
# # # if __name__=="__main__":
# # #     package_screen()