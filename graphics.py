# This is a program working as an Application Tracking System 
from tkinter import Tk, Button, Label, END, Text, Checkbutton, IntVar, RIGHT
from tkmacosx import Button
import tkinter.font as tkFont
from main import red_list, yellow_list, green_list, answers_list
from datetime import date

#Now start creating the actual Graphical User Interface
root = Tk()
root.title("Applicant Screening App")
root.configure(bg="#D1EEEE")
font_heading= tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
font_body= tkFont.Font(family="Arial", size=14, weight="normal")

#Introductory message
hellomenu = """
Welcome to Applicant Screening made easy!

Please press on one of the buttons below to select an option:
"""
myLabel = Label (root, text= hellomenu, font=font_heading, bg="#D1EEEE")
myLabel.grid()

#The next functions will be the actions done by each button when pressed
def press_green():
    count = 1
    T.delete(1.0, END)
    if len(green_list) == 0:
        message = "\t \t No candidates to display"
        T.insert(END, message)
        T.insert(END, '\n')
    else:
        for key in green_list:
            message = "\t [" + str(count) + "] \t" + key + " - " + green_list[key] + "."
            T.insert(END, message)
            T.insert(END, '\n')
            T.insert(END, '\n')
            count += 1

def press_yellow():
    count = 1
    T.delete(1.0, END)
    if len(yellow_list) == 0:
        message = "\t \t No candidates to display"
        T.insert(END, message)
        T.insert(END, '\n')
    else:
        for key in yellow_list:
            message = "\t [" + str(count) + "] \t" + key + " - " + yellow_list[key] + "."
            T.insert(END, message)
            T.insert(END, '\n')
            T.insert(END, '\n')
            count += 1

def press_red():
    count = 1
    T.delete(1.0, END)
    if len(red_list) == 0:
        message = "\t \t No candidates to display"
        T.insert(END, message)
        T.insert(END, '\n')
    else:
        for key in red_list:
            message = "\t [" + str(count) + "] \t" + key + " - " + red_list[key] + "."
            T.insert(END, message)
            T.insert(END, '\n')
            T.insert(END, '\n')
            count += 1
            
def press_info():
    T.delete(1.0, END)
    day = date.today()
    candidates = len(answers_list)
    deleted = len(red_list)
    booked = len(green_list) + len(yellow_list)
    message = f"""\t Date: {day} 
    \n \t Number of Candidates Processed: {candidates} 
    \n \t Number of Candidates Deleted: {deleted}
    \n \t Number of Viable Candidates: {booked}"""
    T.insert(END, message)
    
#------------------------------------------------------------------------------------
#This function deals with the entire process of the e-mail window
#This function will be long and it shouldn't. Keeping it for "simplification"
def press_email():
    #Describe and create the additional window
    new = Tk()
    new.title("Email rejected candidates")
    myLabel2 = Label(new, text="\n If you confirm the action, the following people will be informed via e-mail about being rejected. \n")
    myLabel2.grid()

    # email_list = []

    # # #Function should make a list of the people user checked the box on sending the e-mail to
    # # #Could be actually left out as probably will e-mail everyone rejected anyway
    # # #Currently this is here to prevent wrongfully e-mailing someone who should be accepted (user double-checks)
    # def press_checkbox():
    #     if var.get() == 1:
    #         print(key)

    # #Function defines the steps the program will take when the user confirms they want to send e-mail
    # def confirm_email():
    #     return
    
    # #The loop goes through the list of rejected people and creates a checkbox for each person
    # for key in red_rejections:
    #     var = IntVar()
    #     a_checkbox =  Checkbutton(new, text = key, variable= var, command= press_checkbox)
    #     a_checkbox.grid()
    
    #Let's try a simpler solution to the problem, where it emails everyone on the red list
    for key in red_list:
        myLabel = Label(new, text= key)
        myLabel.grid()
    more_space = Label(new, text="\n\n")
    more_space.grid()

    #Define and place the Confirm and Cancel buttons at the bottom
    confirm_button = Button(new, text= "Confirm", command= 1)
    cancel_button = Button(new, text= "Cancel", command= new.destroy)

    confirm_button.grid()
    cancel_button.grid()

    new.mainloop() #End definition of email window

#---------------------------------------------------------------------------
#Now define the buttons in the main interface
T = Text(root)
green_button = Button(root, text= "Green Light", font=font_body, padx= 119, pady= 20, bg= "#66CD00", command= press_green)
yellow_button = Button(root, text= "Yellow Light", font=font_body, padx= 117, pady= 20, bg= "#eeee00", command= press_yellow)
red_button = Button(root, text= "Red Light", font=font_body, padx= 126, pady= 20, bg= "#ff3030", command= press_red)
blank = Button(root, padx= 130, pady= 20, bg="#D1EEEE")
email_button = Button(root, text= "Email", font=font_body, padx=5, pady=5, bg= "#a9a9a9", command= press_email).place(x=120, y=615)
info_button = Button(root, text= "More Info", font=font_body, padx=5, pady=5, bg= "#a9a9a9", command= press_info).place(x=233, y=615)
exit_button = Button(root, text= "Exit",font=font_body, padx= 5, pady= 5, bg= "#a9a9a9", command= root.destroy).place(x=355, y=615)

#Arrange buttons in the main interface
T.grid()
green_button.grid()
yellow_button.grid()
red_button.grid()
blank.grid()
T.grid()
# info_button.grid()
# exit_button.grid()

root.mainloop() # End the definition of the main window