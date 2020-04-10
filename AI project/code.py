
from tkinter import *
import os

# Designing window for registration of new Faculty

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Staff Login", bg="orange").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="yellow", command=register_user).pack()


# Designing window for  login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title(" Staff Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter your Details ").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    global delete_login_success_screen
   
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Welcome to Faculty page")
    login_success_screen.geometry("300x250")
    Label(login_success_screen,text="Enter the  Subject and Department",bg="orange",width="300",height="2",font=("Calibri",13)).pack()
    Label(login_success_screen,text="").pack()
    Button(login_success_screen,text="Department", height="2", width="30", command=generate_time_table).pack()
    Label(login_success_screen,text="").pack()
    Button(login_success_screen,text="Subjects", height="2", width="30", command=generate_time_table).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
   
def generate_time_table():
    global generate_time_table
    global delete_generate_time_table
    generate_time_table=Toplevel(login_screen)
    generate_time_table.title("Time table Generator")
    generate_time_table.geometry("800x600")
    Label(generate_time_table, text="Enter the details below as per the slots given",bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    global sub1
    global sub1_entry
    global sub2
    global sub2_entry
    global sub3
    global sub3_entry
    global sub4
    global sub4_entry
    global sub5
    global sub5_entry
    global sub6
    global sub6_entry
    global sub7
    global sub7_entry
    global sub8
    global sub8_entry
    global sub9
    global sub9_entry
    global sub10
    global sub10_entry
    global sub11
    global sub11_entry
    global sub12
    global sub12_entry
    """global sub13
    global sub13_entry
    global sub14
    global sub14_entry
    global sub15
    global sub15_entry
    global sub16
    global sub16_entry
    global sub17
    global sub17_entry
    global sub18
    global sub18_entry
    global sub19
    global sub19_entry
    global sub20
    global sub20_entry
    """
    sub1 = StringVar()
    sub2 = StringVar()
    sub3 = StringVar()
    sub4 = StringVar()    
    sub5 = StringVar()
    sub6 = StringVar()
    sub7 = StringVar()
    sub8 = StringVar()
    sub9 = StringVar()
    sub10 = StringVar()
    sub11 = StringVar()
    sub12= StringVar()
    """sub13 = StringVar()
    sub15= StringVar()
    sub16 = StringVar()
    sub17 = StringVar()
    sub18= StringVar()
    sub19 = StringVar()
    sub20= StringVar()
    """
    #Monday Time table
    Label(generate_time_table, text="Monday",bg="red", fg="white").pack()
    Label(generate_time_table,text="Enter Subject 1").pack()
    sub1= Entry(generate_time_table, textvariable=sub1)
    sub1.pack()
    Label(generate_time_table,text="Enter Subject 2").pack()
    sub2= Entry(generate_time_table, textvariable=sub2)
    sub2.pack()
    sub2_entry = Entry(generate_time_table, textvariable=sub2)
    sub2.pack()
    Label(generate_time_table,text="Enter Subject 3").pack()
    sub3= Entry(generate_time_table, textvariable=sub3)
    sub3.pack()
    sub3_entry = Entry(generate_time_table, textvariable=sub3)
    sub3.pack()
    Label(generate_time_table,text="Enter Subject 4").pack()
    sub4= Entry(generate_time_table, textvariable=sub4)
    sub4.pack()
    sub4_entry = Entry(generate_time_table, textvariable=sub4)
    sub4.pack()
   
    #Tuesday
    Label(generate_time_table, text="").pack()
    Label(generate_time_table, text="Tuesday",bg="red", fg="white").pack()
    Label(generate_time_table,text="Enter Subject 1").pack()
    sub5= Entry(generate_time_table, textvariable=sub5)
    sub5.pack()
    sub5_entry = Entry(generate_time_table, textvariable=sub5)
    sub5.pack()
    Label(generate_time_table,text="Enter Subject 2").pack()
    sub6 = Entry(generate_time_table, textvariable=sub6)
    sub6.pack()
    sub6_entry = Entry(generate_time_table, textvariable=sub6)
    sub6.pack()
    Label(generate_time_table,text="Enter Subject 3").pack()
    sub7= Entry(generate_time_table, textvariable=sub7)
    sub7.pack()
    sub7_entry = Entry(generate_time_table, textvariable=sub7)
    sub7.pack()
    Label(generate_time_table,text="Enter Subject 4").pack()
    sub8= Entry(generate_time_table, textvariable=sub8)
    sub8.pack()
    sub8_entry = Entry(generate_time_table, textvariable=sub8)
    sub8.pack()
   
    #Wednesday
    Label(generate_time_table, text="").pack()
    Label(generate_time_table, text="Wednesday",bg="red", fg="white").pack()
    Label(generate_time_table,text="Enter Subject 1").pack()
    sub9= Entry(generate_time_table, textvariable=sub9)
    sub9.pack()
    sub9_entry = Entry(generate_time_table, textvariable=sub9)
    sub9.pack()
    Label(generate_time_table,text="Enter Subject 2").pack()
    sub10 = Entry(generate_time_table, textvariable=sub10)
    sub10.pack()
    sub10_entry = Entry(generate_time_table, textvariable=sub10)
    sub10.pack()
    Label(generate_time_table,text="Enter Subject 3").pack()
    sub11= Entry(generate_time_table, textvariable=sub11)
    sub11.pack()
    sub11_entry = Entry(generate_time_table, textvariable=sub11)
    sub11.pack()
    Label(generate_time_table,text="Enter Subject 4").pack()
    sub12= Entry(generate_time_table, textvariable=sub12)
    sub12.pack()
    sub12_entry = Entry(generate_time_table, textvariable=sub12)
    sub12.pack()
    """#Thursday
    Label(generate_time_table, text="").pack()
    Label(generate_time_table, text="Thursday",bg="red", fg="white").pack()
    Label(generate_time_table,text="Enter Subject 1").pack()
    sub13= Entry(generate_time_table, textvariable=sub13)
    sub13.pack()
    sub13_entry = Entry(generate_time_table, textvariable=sub13)
    sub13.pack()
    Label(generate_time_table,text="Enter Subject 2").pack()
    sub14 = Entry(generate_time_table, textvariable=sub10)
    sub14.pack()
    sub14_entry = Entry(generate_time_table, textvariable=sub14)
    sub14.pack()
    Label(generate_time_table,text="Enter Subject 3").pack()
    sub15= Entry(generate_time_table, textvariable=sub15)
    sub15.pack()
    sub15_entry = Entry(generate_time_table, textvariable=sub15)
    sub15.pack()
    Label(generate_time_table,text="Enter Subject 4").pack()
    sub16= Entry(generate_time_table, textvariable=sub16)
    sub16.pack()
    sub16_entry = Entry(generate_time_table, textvariable=sub16)
    sub16.pack()    
    #Friday
    Label(generate_time_table, text="",bg="red", fg="white").pack()
    Label(generate_time_table, text="Friday").pack()
    Label(generate_time_table,text="Enter Subject 1").pack()
    sub17= Entry(generate_time_table, textvariable=sub17)
    sub17.pack()
    sub17_entry = Entry(generate_time_table, textvariable=sub17)
    sub17.pack()
    Label(generate_time_table,text="Enter Subject 2").pack()
    sub18 = Entry(generate_time_table, textvariable=sub18)
    sub18.pack()
    sub18_entry = Entry(generate_time_table, textvariable=sub18)
    sub18.pack()
    Label(generate_time_table,text="Enter Subject 3").pack()
    sub19= Entry(generate_time_table, textvariable=sub19)
    sub19.pack()
    sub19_entry = Entry(generate_time_table, textvariable=sub19)
    sub19.pack()
    Label(generate_time_table,text="Enter Subject 4").pack()
    sub20= Entry(generate_time_table, textvariable=sub20)
    sub20.pack()
    sub20_entry = Entry(generate_time_table, textvariable=sub20)
    sub20.pack()
    """
    Label(generate_time_table,text="").pack()
    Label(generate_time_table, text="CSE").pack()
    Button(generate_time_table, text="Submit",command=time_table_input).pack()
   


def time_table_input():
    if os.path.exists("Time_table"):
        os.remove("Time_table")
    else:
        print("The file does not exist")
    sub1_info=sub1.get()
    sub2_info=sub2.get()
    sub3_info=sub3.get()
    sub4_info=sub4.get()
    sub5_info=sub5.get()
    sub6_info=sub6.get()
    sub7_info=sub7.get()
    sub8_info=sub8.get()
    sub9_info=sub9.get()
    sub10_info=sub10.get()
    sub11_info=sub11.get()
    sub12_info=sub12.get()
    """sub13_info=sub13.get()
    sub14_info=sub14.get()
    sub15_info=sub15.get()"""
    file=open("Time_table",'at')
    file.write("Monday")
    file.write("\n")
    file.write(sub1_info + " ")
    file.write(sub2_info + " ")
    file.write(sub3_info + " ")
    file.write(sub4_info + " ")
    file.write("\nTuesday")
    file.write("\n")
    file.write(sub5_info + " ")
    file.write(sub6_info + " ")
    file.write(sub7_info + " ")
    file.write(sub8_info + " ")
    file.write("\nWednesday")
    file.write("\n")
    file.write(sub9_info + " ")
    file.write(sub10_info + " ")
    file.write(sub11_info + " ")
    file.write(sub12_info + " ")
    file.close()
    file = open("Time_table", 'r')
    for x in file:
        print(x)
    file.close()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
   
def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_generate_time_table():
    generate_time_table.destroy()
   
# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Intelligent Time Table Maker", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Faculty Login", height="2", width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Student Time Table", height="2", width="30",command=delete_login_success).pack()
    Label(text="").pack()    
    Button(text="Register new ID Login", height="2", width="30",command=register).pack()
    Label(text="").pack()
    main_screen.mainloop()


main_account_screen()

