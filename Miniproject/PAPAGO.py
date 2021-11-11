import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
from tkcalendar import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd



x =[]



def automated_email():
    found = 0
    username_travel = username_var.get()
    des_receipt = Destination.get()
    travel_date = cal.get_date()
    modepay_var_payment = clicked.get()

    while (found == 0):

        with sqlite3.connect('Miniproject.db') as db:
            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        find_userID = ("SELECT * FROM userInfo WHERE userName = ? ")
        cursor.execute(find_userID, [(username_travel)])
        result = cursor.fetchall()




        db.commit()
        if result:
            for i in result:
                userid_email = i[5]


        with sqlite3.connect('Miniproject.db') as db:
            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        email_query = ("SELECT * FROM PAYMENT WHERE userID = ?")
        cursor.execute(email_query, [userid_email])
        results = cursor.fetchall()
        db.commit()

        if results:
            for i in results:
                total_email = i[3]
                global total
                total = total_email
                print(total_email)


        # from_addr = 'papagotravel78@gmail.com'
        # to_addr = userid_email
        # msg = MIMEMultipart()
        # msg['From'] = from_addr
        # msg['To'] = " ,".join(to_addr)
        # msg['Subject'] = 'Travel Details'

        from_addr = 'papagotravel78@gmail.com'
        to_addr = userid_email
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = " ,".join(to_addr)
        msg['Subject'] = 'Travel Details'

        body = f'Hello {username_travel}. Thank you for choosing our service.\n\nThese are your travel details:\n\n' \
               f'Passenger Names: {x}\n\n' \
               f'Destination: {des_receipt}\n\n' \
               f'Travel Date: {travel_date}\n\n' \
               f'Mode of Payment: {modepay_var_payment}\n\n' \






        msg.attach(MIMEText(body, 'plain'))

        email = "papagotravel78@gmail.com"
        password = "miniproject"

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        text = msg.as_string()
        mail.sendmail(from_addr, to_addr, text)
        mail.quit()
        db.commit()
        found = 1
        db.close()
        return (exit)






def enter_name():
    found = 0
    username_travel = username_var.get()
    NoOfAdult_var = spin_adult.get()
    NoOfChild_var = spin_child.get()
    NoOfInfant_var = spin_infant.get()
    Travel_Date = cal.get_date()
    int1 = int(NoOfAdult_var)
    int2 = int(NoOfChild_var)
    int3 = int(NoOfInfant_var)

    Total = int1 + int2 + int3

    for i in range(0,Total):
        y = passenger_name.get()
        x.append(y)
        clear_entry()
        if (i==Total):
            tk.messagebox.showinfo('Information','Max entry')
            return (exit)

        return (exit)


#******Receipt Function******
def get_receipt():
    receipt_window.deiconify()
    payment_window.withdraw()

def get_logout():
    tk.messagebox.showinfo('Information','Thank You For Choosing Us! Happy Journey!')
    login_window.deiconify()
    username_text.delete(0,tk.END)
    password_text.delete(0,tk.END)
    receipt_window.withdraw()









def clear_entry():
    passenger_name.delete(0, tk.END)





#******FUNCTIONS(LOGIN SCREEN)******

def get_admin_login():
    admin_window.deiconify()
    login_window.withdraw()

def validatefieldslogin():
    if username_var.get() == "":
        tk.messagebox.showinfo('Information', 'Enter Username')
    elif password_var.get() == "":
        tk.messagebox.showinfo('Information', 'Enter Password')
    elif username_var.get() == "admin":
        tk.messagebox.showinfo('Information', 'Invalid Login Screen. Click on Admin Login')
        username_text.delete(0,tk.END)
        password_text.delete(0,tk.END)
        return (exit)




def check_credentialslogin():
    username_var=username_text.get()
    password_var=password_text.get()

    while True:
        with sqlite3.connect('Miniproject.db') as db:
            cursor = db.cursor()
            find_user = ("SELECT * FROM userInfo WHERE userNAME = ? AND userPASSWORD = ?")
            cursor.execute(find_user,[(username_var),(password_var)])
            result = cursor.fetchall()

        if result:
            for i in result:
                print("welcome " + i[2])

                tk.messagebox.showinfo('Information','Login Successful')
                get_package()
                return (exit)
        else:
            tk.messagebox.showinfo('Information','Invalid user')
            return (exit)

def get_register():
    register_window.deiconify()
    login_window.withdraw()

def get_package():
    package_window.deiconify()
    login_window.withdraw()










#*****FUNCTIONS (REGISTER SCREEN)******

def get_login_page():
    login_window.deiconify()
    register_window.withdraw()


def validate_phoneno(user_phoneno):
  if user_phoneno.isdigit():
     return True
  elif user_phoneno == "":
     return True
  else:
     tk.messagebox.showinfo('Information','Only digits are allowed in phone number entry field')
     return False

#Email validation
def isvalidemail(email_text):

  if len(email_text) > 7:
     if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[_a-z0-9-]+(\.[_a-z0-9-]+)*(\.[a-z]{2,4})$' , email_text) != None:
        return True
     else:
        tk.messagebox.showinfo('Information', 'Invalid Email!')
  else:
       tk.messagebox.showinfo('Information','Invalid Email!')
       return False




#Remaining field validation
def validatefieldsregister():
    if name_text_register.get() == "":
        tk.messagebox.showinfo('Information','Enter full name')
    elif username_text_register.get() == "":
        tk.messagebox.showinfo('Information','Enter username')
    elif password_text_register.get() == "":
        tk.messagebox.showinfo('Information','Enter password')
    elif repassword_text_register.get() == "":
        tk.messagebox.showinfo('Information','Confirm your password')
    elif repassword_text_register.get() != password_text_register.get():
        tk.messagebox.showinfo('Information','Password does not match')
    elif len(contact_text_register.get()) != 10:
        tk.messagebox.showinfo('Information', 'Enter 10 digits for phone number')
    elif email_text_register.get() != "":
        tk.status = isvalidemail(email_text_register.get())
        register_user()
        tk.messagebox.showinfo('Information', 'Registration Successful!')
        name_text_register.delete(0, tk.END)
        username_text_register.delete(0, tk.END)
        password_text_register.delete(0, tk.END)
        repassword_text_register.delete(0, tk.END)
        email_text_register.delete(0, tk.END)
        contact_text_register.delete(0, tk.END)




def register_user():
    found =0

    name_var_register = name_text_register.get()
    username_var_register = username_text_register.get()
    password_var_register = password_text_register.get()
    repassword_var_register = repassword_text_register.get()
    contact_var_register = contact_text_register.get()
    email_var_register = email_text_register.get()
    while found == 0:
     with sqlite3.connect('Miniproject.db') as db:
        cursor = db.cursor()
     findUser = ("SELECT  * FROM userInfo where userName = ?" )
     cursor.execute(findUser,[(username_var_register)])
     result = cursor.fetchall()

     if (result):
        tk.messagebox.showinfo('Information','Username already taken. Enter different username')
     else:
        found = 1
     while password_var_register != repassword_var_register:
        tk.messagebox.showinfo('Information','Password dont match')
     insertData = ("""
     INSERT INTO userInfo(userFULLNAME,userName,userPassword,userCONTACT,userEMAIL) VALUES (?,?,?,?,?)
     """)
     cursor.execute(insertData,[(name_var_register),(username_var_register),(password_var_register),(contact_var_register),(email_var_register)])
     db.commit()









#***Admin Page Functions*****
def check_credentials_admin():
    status = 0
    username_var_admin = username_text_admin.get()
    password_var_admin = password_text_admin.get()
    while True:
        with sqlite3.connect('Miniproject.db') as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM AdminDetails WHERE admin_username = ? AND admin_password = ?")
        cursor.execute(find_user, [(username_var_admin),(password_var_admin)])
        result = cursor.fetchall()
        db.commit()

        if  result:
            for i in result:
                print("welcome "+i[2])
                tk.messagebox.showinfo('Information', 'Login Successful')
                get_nextpage()
                return(exit)

        else :
            tk.messagebox.showinfo('Information','Invalid Credentials')
            return(exit)



def get_login_admin():
    login_window.deiconify()
    admin_window.withdraw()

def get_nextpage():
    admin2_window.deiconify()
    admin_window.withdraw()


#******Admin Page 2 Functions*******
def plot_graph():
    # cursor.execute("SELECT desNAME ,COUNT(*) FROM TravelDetails GROUP BY desNAME")
    with sqlite3.connect('Miniproject.db') as db:
        cursor = db.cursor()
    count_occurences = ("SELECT COUNT(desNAME),desName FROM TravelDetails GROUP BY desNAME")
    cursor.execute(count_occurences)
    Destination_Name = []

    result = cursor.fetchall()
    db.commit()

    df = pd.DataFrame(result,columns = ["Visit","Destination"])

    df.plot(x = 'Destination',y = 'Visit',kind = 'bar')

    plt.show()

def travel_table():
    with sqlite3.connect("Miniproject.db") as db:
        cursor=db.cursor()

    sql = ("SELECT travel_id,desName,userID,totaladult,totalchild,totalinfant,traveldate FROM TravelDetails")
    cursor.execute(sql)
    rows = cursor.fetchall()

    db.commit()
    treeview = tk.Toplevel()

    my_tree = ttk.Treeview(treeview,columns=('Travel id','Destination Name','User id','Total Adult','Total Child','Total Infant','Travel Date'),show="headings",height = "5")
    my_tree.pack(fill="both",expand=True)
    # Define our column
    my_tree['column'] = (
    "Travel id", "Destination Name", "User id", "Total Adult", "Total Child", "Total Infant", "Travel Date")

    # Format Our column
    my_tree.column("#0")
    my_tree.column("Travel id", anchor=tk.CENTER, width=120)
    my_tree.column("Destination Name", anchor=tk.CENTER, width=120)
    my_tree.column("User id", anchor=tk.CENTER, width=120)
    my_tree.column("Total Adult", anchor=tk.CENTER, width=80)
    my_tree.column("Total Child", anchor=tk.CENTER, width=80)
    my_tree.column("Total Infant", anchor=tk.CENTER, width=80)
    my_tree.column("Travel Date", anchor=tk.CENTER, width=120)

    # Create Heading

    my_tree.heading("#0")
    my_tree.heading("Travel id", text="Travel id", anchor=tk.CENTER)
    my_tree.heading("Destination Name", text="Destination Name", anchor=tk.CENTER)
    my_tree.heading("User id", text="User id", anchor=tk.CENTER)
    my_tree.heading("Total Adult", text="Total Adult", anchor=tk.CENTER)
    my_tree.heading("Total Child", text="Total Child", anchor=tk.CENTER)
    my_tree.heading("Total Infant", text="Total Infant", anchor=tk.CENTER)
    my_tree.heading("Travel Date", text="Travel Date", anchor=tk.CENTER)

    if rows:
        for i in rows:
            my_tree.insert('','end',values=i)


def payment_table():
    with sqlite3.connect("Miniproject.db") as db:
        cursor=db.cursor()

    sql = ("SELECT * FROM PAYMENT")
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.commit()
    treeview = tk.Toplevel()
    my_tree = ttk.Treeview(treeview,columns=('Payment ID','User ID','Payment Mode','Total Amount'),show="headings",height = "5")
    my_tree.pack(fill="both",expand=True)

    # Define our column
    my_tree['column'] = ("Payment ID","User ID","Payment Mode","Total Amount")

    # Format Our column
    my_tree.column("#0")
    my_tree.column("Payment ID", anchor=tk.CENTER, width=120)
    my_tree.column("User ID", anchor=tk.CENTER, width=120)
    my_tree.column("Payment Mode", anchor=tk.CENTER, width=120)
    my_tree.column("Total Amount", anchor=tk.CENTER, width=80)

    # Create Heading

    my_tree.heading("#0")
    my_tree.heading("Payment ID", text="payID", anchor=tk.CENTER)
    my_tree.heading("User ID", text="userID", anchor=tk.CENTER)
    my_tree.heading("Payment Mode", text="paymentMode", anchor=tk.CENTER)
    my_tree.heading("Total Amount", text="totalAmount", anchor=tk.CENTER)

    if rows:
        for i in rows:
            my_tree.insert('','end',values=i)

def logout_admin():
    login_window.deiconify()
    admin2_window.withdraw()





#*****PACKAGE SCREEN FUNCTION*******
def get_logout_package():
    login_window.deiconify()
    package_window.withdraw()

def get_travel():
    travel_window.deiconify()
    package_window.withdraw()



def check_DestinationDetails():

    desName_var = Destination.get()
        #print(Des)
        # Destination_Name(desName_var)

    while True:
        with sqlite3.connect('Miniproject.db') as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM Destination WHERE desName = ? ")
        cursor.execute(find_user, [(desName_var)])
        result = cursor.fetchall()

        db.commit()

        if result:
            for i in result:
                budgetadult = i[2]

                    #tk.messagebox.showinfo('Information', 'Destination Selected successfully')
                Label1 = tk.Label(frame8, font='Times 25', text=budgetadult)
                Label1.place(x=320, y=185, width=200)

                budgetchild = i[3]

                Label2 = tk.Label(frame8, font='Times 25',text=budgetchild)
                Label2.place(x=320, y=245, width=200)

                budgetinfant = i[4]

                Label3 = tk.Label(frame8, font='Times 25', text=budgetinfant)
                Label3.place(x=320, y=295, width=200)
                    # Budget_Details(budgetadult,budgetchild,budgetinfant)
                return (exit)


        else:
            tk.messagebox.showinfo('Information', 'Invalid Credentials')
            return (exit)






#*****Travel Screen Functions*******
def grab_date():
    my_label.config(text="The Selected Date is : " + cal.get_date())
    date = cal.get_date()
    right_travel_date = tk.Label(frame12, textvariable=date, font='Times 20 italic', text=date)
    right_travel_date.place(x=275, y=240, width=250, height=35)




def get_booking():
    booking_window.deiconify()
    travel_window.withdraw()








#*******BOOKING WINDOW FUNCTIONS*********

def get_payment():
    payment_window.deiconify()
    booking_window.withdraw()










#********LOGIN GUI*********
login_window = tk.Tk()

username_var = tk.StringVar()
password_var = tk.StringVar()
login_window.title("PAPAGO Travel Agency")
login_window.geometry("720x420")
login_window.resizable(height=False, width=False)

# Creating two Frames of different colours
frame1 = tk.LabelFrame(login_window, width=100, height=420,bg="#AA2B1D")
frame1.pack(side=tk.LEFT)
frame2 = tk.LabelFrame(login_window, width=620, height=420,bg="#FBE0C4")
frame2.pack(side=tk.RIGHT)

login_title = tk.Label(frame2, text="LOGIN",font = 'Times 35 bold')
sign_in_label = tk.Label(frame2, text="Sign in to your account",font = 'Times 15 italic')
login_title.place(x=230, y=0)
sign_in_label.place(x=210, y=50)
login_title.configure(bg="#FBE0C4")
sign_in_label.configure(bg="#FBE0C4")

username_label = tk.Label(frame2, text="Username:",font = 'Times 25',bg="#FBE0C4")
username_label.place(x=70, y=115)
password_label = tk.Label(frame2, text="Password:",font = 'Times 25',bg="#FBE0C4")
password_label.place(x=70, y=175)

username_text = tk.Entry(frame2,textvariable = username_var, width=15,font = 'Times 25')
username_text.place(x=280, y=115)

password_text = tk.Entry(frame2,textvariable= password_var, width=15,font = 'Times 25',show= "*")
password_text.place(x=280, y=175)

login_button = tk.Button(frame2, text="LOGIN ",font = 'Times 20',bg="#AA2B1D",command = lambda: [validatefieldslogin(), check_credentialslogin()])
register_button = tk.Button(frame2, text="Sign-up ",font='Times 20',command = get_register,bg="#AA2B1D")
admin_sign_in = tk.Button(frame2, text="Admin Login",font='Times 10',bg="#EABF9F",command= get_admin_login)

login_button.place(x=240, y=270)
register_button.place(x=240, y=340)
admin_sign_in.place(x=15, y=380)











#****REGISTER GUI*****
register_window = tk.Toplevel(login_window)
register_window.title("PAPAGO Travel Agency")
register_window.geometry("720x420")
register_window.resizable(height=False, width=False)

name_var_register = tk.StringVar()
username_var_register = tk.StringVar()
password_var_register = tk.StringVar()
repassword_var_register = tk.StringVar()
contact_var_register = tk.StringVar()
email_var_register = tk.StringVar()

# Creating two Frames of different colours
frame3 = tk.LabelFrame(register_window, width=100, height=420, bg="#AA2B1D")
frame3.pack(side=tk.LEFT)
frame4 = tk.LabelFrame(register_window, width=620, height=420, bg="#FBE0C4")
frame4.pack(side=tk.RIGHT)

register_title = tk.Label(frame4, text="REGISTER", bg="#FBE0C4", font='Times 35 bold')
register_title.place(x=190, y=0)

name_label = tk.Label(frame4, text="Full Name:", font='Times 20', bg="#FBE0C4")
name_label.place(x=40, y=65)
username_label = tk.Label(frame4, text="Username:", font='Times 20', bg="#FBE0C4")
username_label.place(x=40, y=105)
password_label = tk.Label(frame4, text="Password:", font='Times 20', bg="#FBE0C4")
password_label.place(x=40, y=145)
repassword_label = tk.Label(frame4, text="Confirm Password:", font='Times 20', bg="#FBE0C4")
repassword_label.place(x=40, y=185)
contact_label = tk.Label(frame4, text="Contact No:", font='Times 20', bg="#FBE0C4")
contact_label.place(x=40, y=225)
email_label = tk.Label(frame4, text="Email:", font='Times 20', bg="#FBE0C4")
email_label.place(x=40, y=265)

register_button = tk.Button(frame4, text="Register", command= validatefieldsregister,font='Times 20',bg="#AA2B1D")
register_button.place(x=245, y=305)
login_button = tk.Button(frame4, text="Go Back To Login", command=get_login_page, font='Times 20',bg="#EABF9F")
login_button.place(x=185, y=365)

name_text_register = tk.Entry(frame4, width=20, font='Times 20')
name_text_register.place(x=280, y=65)
username_text_register = tk.Entry(frame4, width=20, font='Times 20')
username_text_register.place(x=280, y=105)
password_text_register = tk.Entry(frame4, width=20, font='Times 20',show = "*")
password_text_register.place(x=280, y=145)
repassword_text_register = tk.Entry(frame4, width=20, font='Times 20',show = "*")
repassword_text_register.place(x=280, y=185)
contact_text_register = tk.Entry(frame4, width=20, font='Times 20')
contact_text_register.place(x=280, y=225)
email_text_register = tk.Entry(frame4, width=20, font='Times 20')
email_text_register.place(x=280, y=265)

valid_phone = login_window.register(validate_phoneno)
contact_text_register.config(validate ="key",validatecommand = (valid_phone, '%P'))











#***Admin Gui****

admin_window = tk.Toplevel(login_window)
username_var_admin = tk.StringVar()
password_var_admin = tk.StringVar()

admin_window.title("PAPAGO Travel Agency")
admin_window.geometry("720x420")
admin_window.resizable(height=False, width=False)

# Creating two Frames of different colours
frame5 = tk.LabelFrame(admin_window, width=100, height=420,bg="#AA2B1D")
frame5.pack(side=tk.LEFT)
frame6 = tk.LabelFrame(admin_window, width=620, height=420,bg="#FBE0C4")
frame6.pack(side=tk.RIGHT)

login_title = tk.Label(frame6, text="ADMIN LOGIN",font = 'Times 35 bold')
sign_in_label = tk.Label(frame6, text="Sign in as admin",font = 'Times 15 italic')
login_title.place(x=160, y=0)
sign_in_label.place(x=240, y=50)
login_title.configure(bg="#FBE0C4")
sign_in_label.configure(bg="#FBE0C4")

username_label_admin = tk.Label(frame6, text="Username:",font = 'Times 25',bg="#FBE0C4")
username_label_admin.place(x=70, y=115)
password_label_admin = tk.Label(frame6, text="Password:",font = 'Times 25',bg="#FBE0C4")
password_label_admin.place(x=70, y=175)

username_text_admin = tk.Entry(frame6, width=15,font = 'Times 25')
username_text_admin.place(x=280, y=115)

password_text_admin = tk.Entry(frame6, width=15,font = 'Times 25',show= "*")
password_text_admin.place(x=280, y=175)

login_button = tk.Button(frame6, text="LOGIN ",font = 'Times 20',bg="#AA2B1D",command =check_credentials_admin)
user_sign_in = tk.Button(frame6, text="User Login",font='Times 10',bg="#EABF9F",command= get_login_admin)

login_button.place(x=240, y=270)
user_sign_in.place(x=15, y=380)

# my_tree = ttk.Treeview(admin_window)
#
# my_tree['columns'] = ("Travel Id","User ID","Destination","Adult Count","Child Count","Infant Count","Travel Date")
#
# my_tree.column("#0")
#
# my_tree.heading("#0")
# my_tree.heading()
# my_tree.heading()
# my_tree.heading()





#******Admin Page 2*************
admin2_window = tk.Toplevel(login_window)
admin2_window.title("PAPAGO Travel Agency")
admin2_window.geometry("720x420")
admin2_window.resizable(height=False, width=False)

# Creating two Frames of different colours
frame5 = tk.LabelFrame(admin2_window, width=100, height=420,bg="#AA2B1D")
frame5.pack(side=tk.LEFT)
frame6 = tk.LabelFrame(admin2_window, width=620, height=420,bg="#FBE0C4")
frame6.pack(side=tk.RIGHT)


login_title = tk.Label(frame6, text="ADMIN ",font = 'Times 35 bold')
login_title.place(x=220, y=0)
login_title.configure(bg="#FBE0C4")


travel_details = tk.Button(frame6, text="Show Travel Details",font='Times 20',bg="#AA2B1D",command = travel_table)
travel_details.place(x=170, y=80,width =276)

payment_details = tk.Button(frame6, text="Show Payment Details ",font = 'Times 20',bg="#AA2B1D",command=payment_table)
payment_details.place(x=170, y=160)

plot_button = tk.Button(frame6, text="Visualize ",font = 'Times 20',bg="#AA2B1D",command= plot_graph)
plot_button.place(x=170, y=240,width = 276)

logout_button = tk.Button(frame6, text="Logout ",font = 'Times 20',bg="#AA2B1D",command = logout_admin)
logout_button.place(x=245, y=320)







#*****PACKAGES GUI******
package_window = tk.Toplevel(login_window)
package_window.title("PAPAGO Travel Agency")
package_window.geometry("720x420")
package_window.resizable(height=False, width=False)




#Creating two Frames of different colours
frame7 = tk.LabelFrame(package_window,width = 100 , height = 420, bg = "#AA2B1D")
frame7.pack(side = tk.LEFT)
frame8 = tk.LabelFrame(package_window,width = 620 , height = 420 , bg = "#FBE0C4" )
frame8.pack(side = tk.RIGHT)

package_title = tk.Label(frame8,text= "PACKAGES", bg = "#FBE0C4", font = 'Times 35 bold')

package_title.place(x = 185 , y = 0)

destination_label     = tk.Label(frame8,text = "Destination            :", bg = "#FBE0C4", font = 'Times 25')
destination_label.place(x=35, y=115)
BudgetPerAdult_label = tk.Label(frame8,text = "Budget Per Adult  :",bg ="#FBE0C4",font = 'Times 25')
BudgetPerAdult_label .place(x=35, y= 175)
BudgetPerChild_label = tk.Label(frame8,text = "Budget Per Child  :",bg = "#FBE0C4", font ='Times 25')
BudgetPerChild_label.place(x=35, y=235)

BudgetPerInfant_label = tk.Label(frame8,text = "Budget Per Infant  :",bg = "#FBE0C4", font ='Times 25')
BudgetPerInfant_label.place(x=35, y=295)

Destination = tk.StringVar()
Destination_Options = [
    "Maldives",
    "Bali",
    "Bangkok",
    "Europe"
    ]
test=Destination.get()
dropDestination = tk.OptionMenu(frame8,Destination,*Destination_Options)
dropDestination.config(font ="Times 15 italic")
dropDestination.place(x=320,y=115,width =150)

LabelBudgetadult = tk.Label(frame8,font = 'Times 25')
LabelBudgetadult.place(x=320,y=185,width=200)
LabelBudgetchild = tk.Label(frame8,font = 'Times 25')
LabelBudgetchild.place(x=320,y=245,width=200)
LabelBudgetinfant = tk.Label(frame8,font = 'Times 25')
LabelBudgetinfant.place(x=320,y=295,width =200)

ButtonContinue = tk.Button(frame8,text = "CONTINUE",font = 'Times 20', bg = "#AA2B1D",command= get_travel)
ButtonContinue.place(x=150,y=360,width=150)
ButtonBack = tk.Button(frame8,text = "Logout",font = 'Times 20', bg = "#AA2B1D",command= get_logout_package)
ButtonBack.place(x=350,y=360,width=100)

Btn_Confirm = tk.Button(frame8,text = "Confirm",font = 'Times 15', bg = "#AA2B1D",command = check_DestinationDetails)
Btn_Confirm.config(font ="Times 15 italic")
Btn_Confirm.place(x=480,y=115,width=90)












#****Travel GUI******
travel_window = tk.Toplevel(login_window)
travel_window.title("TRAVEL DETAILS")
travel_window.geometry("720x420")
travel_window.resizable(height=False, width=False)

# frame
frame9 = tk.LabelFrame(travel_window, width=100, height=420, bg="#AA2B1D")
frame9.pack(side=tk.LEFT)
frame10 = tk.LabelFrame(travel_window, width=620, height=420, bg="#FBE0C4")
frame10.pack(side=tk.RIGHT)

page_title = tk.Label(frame10, text="TRAVEL DETAILS", bg="#FBE0C4", font='Times 35 bold')
page_title.place(x=90, y=0)

adult_label = tk.Label(frame10, text="Adult :", bg="#FBE0C4", font='Times 25 ')
adult_label.place(x=15, y=70)
child_label = tk.Label(frame10, text="Child :", bg="#FBE0C4", font='Times 25 ')
child_label.place(x=15, y=170)
infant_label = tk.Label(frame10, text="Infant :", bg="#FBE0C4", font='Times 25 ')
infant_label.place(x=15, y=270)
date_label = tk.Label(frame10, text="Date :", bg="#FBE0C4", font='Times 25 ')
date_label.place(x=235, y=70)
# passenger_label = Label(frame2,text="Passenger Name :",bg = "#FBE0C4", font = 'Times 25 bold')
# passenger_label.place(x=35,y=115)

# spin_box
spin_adult = tk.Spinbox(frame10, from_=0, to=100, width=5)
spin_adult.config(font='Times 12 italic')
spin_adult.place(x=120, y=80)

spin_infant = tk.Spinbox(frame10, from_=0, to=100, width=5)
spin_infant.config(font='Times 12 italic')
spin_infant.place(x=120, y=180)
spin_child = tk.Spinbox(frame10, from_=0, to=100, width=5)
spin_child.config(font='Times 12 italic')
spin_child.place(x=120, y=280)

# calendar
cal = Calendar(frame10, selectmode="day", year=2021, month=5, day=5)
cal.place(x=345, y=70)

button_cal = tk.Button(frame10, text="Get Date", command=grab_date)
button_cal.place(x=440, y=280)
# date = tk.StringVar()
date = cal.get_date()

my_label = tk.Label(frame10, text="")
my_label.place(x=395, y=315)

# button
bt = tk.Button(frame10, text="CONTINUE", bg="#AA2B1D", font="Times 20", command=lambda: [traveldetails(),get_booking()])
bt.place(x=210, y=330, width=150)







#*****BOOKING SUMMARY GUI*************
booking_window = tk.Toplevel(login_window)
booking_window.title("PAPAGO Travel Agency")
booking_window.geometry("720x420")
booking_window.resizable(height=False, width=False)

frame11 = tk.LabelFrame(booking_window,width = 100 , height = 420, bg = "#AA2B1D")
frame11.pack(side = tk.LEFT)
frame12 = tk.LabelFrame(booking_window,width = 620 , height = 420 , bg = "#FBE0C4" )
frame12.pack(side = tk.RIGHT)

page_title = tk.Label(frame12,text= "BOOKING SUMMARY", bg = "#FBE0C4", font = 'Times 35 bold')
page_title.place(x = 90 , y = 0)

destination_label = tk.Label(frame12,text="Destination         :",bg = "#FBE0C4", font = 'Times 25 ')
destination_label.place(x = 35, y = 115)
passenger_label = tk.Label(frame12,text="Passenger Name :",bg = "#FBE0C4", font = 'Times 25 ')
passenger_label.place(x = 35 , y = 175)
travel_date_label = tk.Label(frame12,text="Travel Date        :",bg = "#FBE0C4", font = 'Times 25 ')
travel_date_label.place(x = 35 , y = 235)



#RHS
right_destination = tk.Label(frame12,textvariable=Destination,font = 'Times 20 italic')
passenger_name = tk.Entry(frame12,font='Times 20')
right_travel_date = tk.Label(frame12,text=grab_date(),font= 'Times 20 italic')
right_destination.place(x=275,y=120, width= 250, height= 35)
passenger_name.place(x = 275 ,y =180 ,width =250 ,height = 35)
right_travel_date.place(x = 275,y = 240 ,width = 250 ,height =35)
confirm = tk.Button(frame12,text="Confirm",bg ="#AA2B1D",font = "Times 15",command=enter_name )
confirm.place(x=532,y = 175)
bt = tk.Button(frame12,text="CONTINUE",bg ="#AA2B1D",font = "Times 20",command= lambda: [get_payment(),get_total_amount()])
bt.place(x = 210  , y = 320, width =150)






#******PAYMENT GUI*********
payment_window = tk.Toplevel(login_window)
payment_window.title("PAPAGO Travel Agency")
payment_window.geometry("720x420")
payment_window.resizable(height=False, width=False)

#Creating two Frames of different colours
frame13 = tk.LabelFrame(payment_window,width = 100 , height = 420, bg = "#AA2B1D")
frame13.pack(side = tk.LEFT)
frame14 = tk.LabelFrame(payment_window,width = 620 , height = 420 , bg = "#FBE0C4" )
frame14.pack(side = tk.RIGHT)


payment_title = tk.Label(frame14,text= "PAYMENT", bg = "#FBE0C4", font = 'Times 35 bold')
payment_title.place(x = 160 , y = 0)

total_cost_label = tk.Label(frame14, text = "Total tour cost :", bg = "#FBE0C4", font = 'Times 25')

total_cost_label.place(x= 35 , y= 55)

label1 = tk.Label(frame14)
label1.place(x=300 , y=55 , width=200)



GST_label = tk.Label(frame14,text = "GST @5%      :", bg = "#FBE0C4", font = 'Times 25')
GST_label.place(x=35, y=115)

label2 = tk.Label(frame14)
label2.place(x=300 , y=115 , width=200)
TCS_label = tk.Label(frame14,text = "TCS @5%      :",bg ="#FBE0C4",font = 'Times 25')
TCS_label.place(x=35, y= 175)

label3 = tk.Label(frame14)
label3.place(x=300, y=175 ,width=200)

Grand_total_label= tk.Label(frame14,text = "Grand Total    :", bg = "#FBE0C4", font = 'Times 25')
Grand_total_label.place(x=35, y=235)

label4 = tk.Label(frame14)
label4.place(x=300 , y=235 , width=200)

Mode_of_payment_label = tk.Label(frame14, text="Mode of payment:", bg="#FBE0C4", font='Times 25')
Mode_of_payment_label.place(x=35, y=295)


options = [

    "Credit Card",
    "Debit Card",
    "Online Banking",

]
clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(frame14, clicked, *options )
drop.config(font= 'Times 20 italic')
drop.place(x=300 , y=300, width=200)


mybutton = tk.Button(frame14,bg="#AA2B1D", text="Get Receipt ",  font = 'Times 25',command= lambda : [grab_date_receipt(),get_receipt(),print_receipt()])
mybutton.place(x=160 ,y=350 ,width=200)

#total_cost_text = Entry(frame14, text= "total cost", height= 30)
#username_text.place(x=200, y=115)




#*******RECEIPT GUI*************

receipt_window = tk.Toplevel(login_window)
receipt_window.title("PAPAGO Travel Agency")
receipt_window.geometry("720x420")
receipt_window.resizable(height=False, width=False)

frame15 = tk.LabelFrame(receipt_window,width = 100 , height = 420, bg = "#AA2B1D")
frame15.pack(side = tk.LEFT)
frame16 = tk.LabelFrame(receipt_window,width = 620 , height = 420 , bg = "#FBE0C4" )
frame16.pack(side = tk.RIGHT)

page_title = tk.Label(frame16,text= "PAPAGO Travel Agency", bg = "#FBE0C4", font = 'Times 30 bold italic')
page_title.place(x = 90 , y = 0)

destination_label = tk.Label(frame16,text="Destination:",bg = "#FBE0C4", font = 'Times 25 italic')
destination_label.place(x = 35, y = 80)

travel_date_label = tk.Label(frame16,text="Travel Date:",bg = "#FBE0C4", font = 'Times 25 italic ')
travel_date_label.place(x = 35 , y = 140)
total_amount_label = tk.Label(frame16,text="Total Amount:",bg = "#FBE0C4", font = 'Times 25 italic ')
total_amount_label.place(x=35, y= 200 )
mode_of_payment_label = tk.Label(frame16,text="Mode of payment:",bg = "#FBE0C4", font = 'Times 25 italic ')
mode_of_payment_label.place(x=35 , y= 260)
status_label = tk.Label(frame16,text="Status:",bg = "#FBE0C4", font = 'Times 25 italic ')
status_label.place(x=180 , y= 315)


def grab_date_receipt():
    # my_label.config(text="The Selected Date is : " + cal.get_date())
    date = cal.get_date()
    right_travel_date = tk.Label(frame16,font='Times 20 italic', text=date)
    right_travel_date.place(x=285, y=145, width=250, height=35)



#RHS
right_destination = tk.Label(frame16,font = 'Times 20 italic',textvariable = Destination )
right_destination.place(x=285, y=85, width=250, height=35)
right_travel_date = tk.Label(frame16,font = 'Times 20 italic',text = grab_date_receipt())
right_travel_date.place(x = 285,y = 145 ,width = 250 ,height =35)
right_totalamount = tk.Label(frame16)
right_totalamount.place(x =285, y=205,width = 250 ,height =35)
right_modeofpayment = tk.Label(frame16,font = 'Times 20 italic',textvariable = clicked)
right_modeofpayment.place(x=285, y=265,width = 250 ,height =35)
right_status_label = tk.Label(frame16, text="Paid", bg="#FBE0C4", font='Times 25 italic ')
right_status_label.place(x=285, y=315)

btn = tk.Button(frame16,text="PRINT RECEIPT",bg ="#AA2B1D",font = "Times 20 italic",command = lambda : [automated_email(),get_logout()])
btn.place(x = 180  , y = 360, width =200)







#*****DATABASE*********
with sqlite3.connect('Miniproject.db') as db:
    cursor = db.cursor()
cursor.execute("""
   CREATE TABLE IF NOT EXISTS userInfo(
   userID INTEGER PRIMARY KEY AUTOINCREMENT,
   userFULLNAME VARCHAR(50) NOT NULL,
   userNAME VARCHAR(50) NOT NULL UNIQUE,
   userPASSWORD VARCHAR(5) NOT NULL,
   userCONTACT VARCHAR(10) NOT NULL,
   userEMAIL VARCHAR(50) NOT NULL UNIQUE
   );
   """)

# cursor.execute("""
# INSERT INTO userInfo(userID,userFULLNAME,userNAME,userPASSWORD,userCONTACT,userEMAIL)
# VALUES (101,"Atharv Parab","atharvparab","atharv33","1234567899","atharv.parab01@gmail.com")
# """)

db.commit()


with sqlite3.connect('Miniproject.db') as db:

    db.execute("PRAGMA FOREIGN_KEYS=off")
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Destination(
    desID INTEGER PRIMARY KEY AUTOINCREMENT,
    desNAME VARCHAR(50) NOT NULL UNIQUE,
    priceadult VARCHAR(5) NOT NULL,
    pricechild VARCHAR(10) NOT NULL,
    priceinfant VARCHAR(50) NOT NULL UNIQUE
    );
    """)
    # cursor.execute("""
    #     INSERT INTO Destination(desID,desNAME,priceadult,pricechild,priceinfant)
    #     VALUES (201,"Maldives","200000",",100000","50000")
    #     """)
    #
    # cursor.execute("""
    # INSERT INTO Destination(desID,desNAME,priceadult,pricechild,priceinfant)
    # VALUES (202,"Bali","100000","50000","20000")
    # """)
    #
    # cursor.execute("""
    # INSERT INTO Destination(desID,desNAME,priceadult,pricechild,priceinfant)
    # VALUES (203,"Bangkok","150000","90000","40000")
    # """)
    #
    # cursor.execute("""
    # INSERT INTO Destination(desID,desNAME,priceadult,pricechild,priceinfant)
    # VALUES (204,"Europe","300000","200000","150000")
    # """)





    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TravelDetails(
    travel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    desID INTEGER,
    desNAME VARCHAR (50),
    userID INTEGER,
    totaladult INTEGER,
    totalchild INTEGER,
    totalinfant INTEGER,
    traveldate VARCHAR(10),
    CONSTRAINT des_name
    FOREIGN KEY (desNAME)
    REFERENCES Destination (desNAME),
    CONSTRAINT des_no
    FOREIGN KEY (desID)
    REFERENCES Destination (desID),
    CONSTRAINT user_no
    FOREIGN KEY (userID)
    REFERENCES userINFO (userID)
    );

    """)
    # cursor.execute("""
    # INSERT INTO TravelDetails (travel_id,userID,desID,desNAME,totaladult,totalchild,totalinfant,traveldate)
    # VALUES (301,101,201,"Bali",2,0,0,"9/16/21")
    # """)



    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS AdminDetails(
    # admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    # admin_username VARCHAR(50) NOT NULL,
    # admin_password VARCHAR(50) NOT NULL
    # );
    #
    # """)






    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PAYMENT(
    payID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER,
    paymentMode VARCHAR(50),
    totalAmount VARCHAR(1000),
    CONSTRAINT user_id
    FOREIGN KEY (userID)
    REFERENCES userInfo (userID)
    );
    """)

    # cursor.execute("""
    # INSERT INTO PAYMENT(payID,userID,paymentMode,totalAmount)
    # VALUES (401,101,"Credit Card","150000")
    # """)




def traveldetails():
    found = 0
    username_travel = username_var.get()
    destination_var = Destination.get()
    travel_date = cal.get_date()
    adult_var = spin_adult.get()
    child_var = spin_child.get()
    infant_var = spin_infant.get()
    while (found == 0):
        with sqlite3.connect('Miniproject.db') as db:
            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        find_userID = ("SELECT * FROM userInfo WHERE userName = ? ")
        cursor.execute(find_userID, [(username_travel)])
        result = cursor.fetchall()

        db.commit()
        if result:
            for i in result:
                userid_pass = i[0]

                # return (exit)
                break




        with sqlite3.connect('Miniproject.db') as db:
            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        get_id = ("SELECT * FROM Destination WHERE desNAME = ? ")
        cursor.execute(get_id,[(destination_var)])
        results = cursor.fetchall()

        db.commit()
        if results:
            for j in results:
                desid_pass = j[0]

                break



        with sqlite3.connect('Miniproject.db') as db:
            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        insert_details = ("INSERT INTO TravelDetails(userID,desID,desNAME,totaladult,totalchild,totalinfant,traveldate) VALUES (?,?,?,?,?,?,?)")
        cursor.execute(insert_details,[(userid_pass),(desid_pass),(destination_var),(adult_var),(child_var),(infant_var),(travel_date)])
        db.commit()
        found = 1
        db.close()

def get_total_amount():
    found = 0
    username_travel = username_var.get()
    adult_var_payment = spin_adult.get()
    child_var_payment = spin_child.get()
    infant_var_payment = spin_infant.get()
    modepay_var_payment = clicked.get()
    destination_var_payment = Destination.get()
    while (found ==0):

        with sqlite3.connect('Miniproject.db') as db:
            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        find_userID = ("SELECT * FROM userInfo WHERE userName = ? ")
        cursor.execute(find_userID, [(username_travel)])
        result = cursor.fetchall()

        db.commit()
        if result:
            for i in result:
                userid_pass = i[0]

                # return (exit)
                break




        with sqlite3.connect('Miniproject.db') as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM Destination WHERE desName = ? ")
        cursor.execute(find_user, [(destination_var_payment)])
        result = cursor.fetchall()

        db.commit()

        if result:
            for i in result:

                budgetadult = i[2]

                #print(budgetadult)
                total_adult = int(adult_var_payment) * int(budgetadult)



                budgetchild = i[3]
                total_child = int(child_var_payment) * int(budgetchild)



                budgetinfant = i[4]
                total_infant = int(infant_var_payment) * int(budgetinfant)


                total_amount = total_adult + total_child + total_infant
                label1 = tk.Label(frame14,font = 'Times 25 italic',text=total_amount)
                label1.place(x=300, y=70, width=200)

                gst_price = 0.05 * total_amount
                label2 = tk.Label(frame14,font = 'Times 25 italic',text=gst_price)
                label2.place(x=300, y=125, width=200)

                tcs_price = 0.05 *total_amount
                label3 = tk.Label(frame14,font = 'Times 25 italic',text=tcs_price)
                label3.place(x=300, y=185, width=200)

                grand_total = total_amount + gst_price + tcs_price
                label4 = tk.Label(frame14,font = 'Times 25 italic',text=grand_total)
                label4.place(x=300, y=245, width=200)


        db.commit()
        found = 1
        db.close()

            # Budget_Details(budgetadult,budgetchild,budgetinfant)
        return (exit)

def print_receipt():
    found = 0
    username_travel = username_var.get()
    adult_var_payment = spin_adult.get()
    child_var_payment = spin_child.get()
    infant_var_payment = spin_infant.get()
    modepay_var_payment = clicked.get()
    destination_var_payment = Destination.get()
    while (found == 0):

        with sqlite3.connect('Miniproject.db') as db:
            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        find_userID = ("SELECT * FROM userInfo WHERE userName = ? ")
        cursor.execute(find_userID, [(username_travel)])
        result = cursor.fetchall()

        db.commit()
        if result:
            for i in result:
                userid_pass = i[0]

                # return (exit)
                break

        with sqlite3.connect('Miniproject.db') as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM Destination WHERE desName = ? ")
        cursor.execute(find_user, [(destination_var_payment)])
        result = cursor.fetchall()

        db.commit()

        if result:
            for i in result:
                budgetadult = i[2]

                # print(budgetadult)
                total_adult = int(adult_var_payment) * int(budgetadult)


                budgetchild = i[3]
                total_child = int(child_var_payment) * int(budgetchild)


                budgetinfant = i[4]
                total_infant = int(infant_var_payment) * int(budgetinfant)


                total_amount = total_adult + total_child + total_infant


                gst_price = 0.05 * total_amount


                tcs_price = 0.05 * total_amount


                grand_total = total_amount + gst_price + tcs_price
                right_totalamount = tk.Label(frame16,text=grand_total,font = 'Times 25 italic')
                right_totalamount.place(x=285, y=205, width=250, height=35)

        with sqlite3.connect('Miniproject.db') as db:

            db.execute("PRAGMA FOREIGN_KEYS=on")
            cursor = db.cursor()
        insert_payment = (
            "INSERT INTO PAYMENT(userID,paymentMode,totalAmount) VALUES (?,?,?)")
        cursor.execute(insert_payment,[(userid_pass), (modepay_var_payment), (grand_total)])
        db.commit()
        found = 1
        db.close()

        # Budget_Details(budgetadult,budgetchild,budgetinfant)
        return (exit)






admin2_window.withdraw()
receipt_window.withdraw()
payment_window.withdraw()
booking_window.withdraw()
travel_window.withdraw()
package_window.withdraw()
register_window.withdraw()
admin_window.withdraw()
login_window.mainloop()

