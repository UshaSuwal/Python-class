import tkinter
from tkinter import ttk
from tkinter import messagebox


from sqlalchemy import create_engine, Column, String,Integer,CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base=declarative_base()
class User(Base):
    __tablename__="Form"
    id=Column('Id',Integer,primary_key=True)
    first_name= Column('First name',String)
    last_name= Column("Last name", String)
    title= Column("Title", String)
    age= Column("age", Integer)
    nationality= Column("Nationality", String)
    registration= Column("Registration",String)
    courses= Column("Completed courses", Integer)
    semester= Column("Semester", Integer)

    def __init__(self, id,first_name,last_name,title,age,nationality,num_courses,num_semesters,registration_status):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.title=title
        self.age=age
        self.nationality=nationality
        self.courses=num_courses
        self.semester=num_semesters
        self.registration=registration_status

engine=create_engine("sqlite:///form1.db",echo=True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()
print("Connection Established")


def submit_data():
    status = terms_check_var.get()
    if status == "Accepted":
        id=id_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        num_courses = num_courses_spinbox.get()
        num_semesters = num_semesters_spinbox.get()
        registration_status = reg_status_var.get()
        u_obj=User(id,first_name,last_name,title,age,nationality,num_courses,num_semesters,registration_status)
        session.add(u_obj)
        session.commit()

        print("Data of ",first_name,"has been added")
        
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms and conditions")




window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()


# Saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label=tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)
id_label = tkinter.Label(user_info_frame, text="ID")
id_label.grid(row=0, column=2)


first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
id_entry=tkinter.Entry(user_info_frame)

first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
id_entry.grid(row=1,column=2)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms."])
title_label.grid(row=0, column=3)
title_combobox.grid(row=1, column=3)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Nepal", "Singapore", "Japan"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")

registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

num_courses_label = tkinter.Label(courses_frame, text="# Completed Courses")
num_courses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)

num_semesters_label = tkinter.Label(courses_frame, text="# Semesters")
num_semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
num_semesters_label.grid(row=0, column=2)
num_semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_check_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",variable=terms_check_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Submit", command=submit_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)




def update_row():
    update_id=int(input(print("Which id you want to update?\n")))
    count=int(input(print("What do you want to update?\n 1.First name,2.Last name,3.Age,4.Title,5.Nationality,6.Registration status,7.Completed course,8.Semester")))
    
    if(count==1):
        new_first=input(print("Enter new first name"))
        session.query(User).filter(User.id==update_id).update({"first_name":new_first})  #ORM
        session.commit()
    elif(count==2):
        new_last=input(print("Enter new last name"))
        session.query(User).filter(User.id==update_id).update({"last_name":new_last})
        session.commit()
    elif(count==3):
        new_age=int(input(print("Enter new age")))
        session.query(User).filter(User.id==update_id).update({"age":new_age})
        session.commit()
    else:
        print("Enter valid choice!!(1/2/3/4/5/6/7/8):")
        update_row()
    upgrade_form()


def delete_row():
    update_id=int(input(print("Which id you want to delete?\n")))
    session.query(User).filter(User.id==update_id).delete()  #ORM
    session.commit()
    print("Deleted Successfully")
    upgrade_form()

def exit_message():
    print("Thankyou!")

def upgrade_form():
    upgrade=int(input(print(" Do you want to 1.Delete, 2.Update, 3.Exit:\n")))
    if(upgrade==1):
        delete_row()
    elif(upgrade==2):
        update_row()
    elif(upgrade==3):
        exit_message()
    else:
        print("Enter valid choice(1/2/3)")
        upgrade_form()

upgrade_form()
