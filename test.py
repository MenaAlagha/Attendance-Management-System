import AdminPanel
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import csv
import openpyxl
from tkinter import messagebox
import customtkinter



class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+150+30")
        self.root.resizable(0, 0)
        self.root.title("Attendance Management System")
        self.load_main_page()

    # Main Page Design #
    def load_main_page(self):
        image = Image.open("images\\MainPage.jpg")
        photo = ImageTk.PhotoImage(image)
        label = Label(self.root, image=photo)
        label.place(x=-2, y=0)

        # say_welcome = tk.Label(
        #     self.root,
        #     text=f"Welcome {AdminPanel.username.capitalize()} :)",
        #     font=("Times New Romans", 19, " bold "),
        #     fg="#3A6B35",
        #     bg="#4E87F6",
        # )
        # say_welcome.place(x=25, y=20)

        self.load_auto_attendance_section()
        self.load_manual_attendance_section()

#################################################################

    def load_auto_attendance_section(self):
        # Automatic Attendance Label #
        auto_attendance_label = tk.Label(
            self.root,
            text="Automatically Fill Attendance",
            font=("times", 19, " bold "),
            fg="#FFFFFF",
            bg="#4E87F6",
        )
        auto_attendance_label.place(x=120, y=150)
        # Subject Messsage and Text Box #
        # subject_label_auto = tk.Label(
        #     self.root,
        #     text="Enter Subject",
        #     font=("times", 19, " bold "),
        #     fg="#FFFFFF",
        #     bg="#4E87F6",
        # )
        # subject_label_auto.place(x=30, y=300)
        
        global SUBTXTA
        SUBTXTA = customtkinter.CTkEntry(master=self.root,width=400,bg_color='#4E87F6',border_color="#4E87F6" , placeholder_text_color="#4E87F6" , fg_color="#FFFFFF" ,placeholder_text="Enter Subject..",font=('PT BOLD HEADING', 18),height=45)
        SUBTXTA.place(x=100, y=300)

        # SUBTXTA = tk.Entry(
        #     self.root, bg="#4E87F6", fg="#FFFFFF", relief=FLAT, highlightthickness=1 , font=("times", 25, " bold ")
        # )
        # SUBTXTA.place(x=240, y=297)

        # Fill Attendance Button For Automatic#
        fill_attendance_button_auto = tk.Button(
            self.root,
            text="Fill Attendance",
            cursor="hand2",
            relief=FLAT,
            font=("times", 15, " bold "),
            fg="#4E87F6",
            bg="#FFFFFF",
            activebackground="green",
        )
        fill_attendance_button_auto.place(x=220, y=450)
        

#################################################################

    def load_manual_attendance_section(self):
        # Manually Attendance Label #
        manual_attendance_label = tk.Label(
            self.root,
            text="Manually Fill Attendance",
            font=("times", 19, " bold "),
            fg="#4895EF",
            bg="#FFFFFF",
        )
        manual_attendance_label.place(x=810, y=150)
        # Subject Messsage and Text Box For Manual #
        # subject_label_man = tk.Label(
        #     self.root,
        #     text="Enter Subject",
        #     font=("times", 19, " bold "),
        #     fg="#4895EF",
        #     bg="#FFFFFF",
        # )
        # subject_label_man.place(x=690, y=300)

        global SUBTXTM
        # SUBTXTM = tk.Entry(
        #     self.root, bg="#FFFFFF", fg="#4895EF", relief=FLAT,  highlightthickness=1 , font=("times", 25, " bold ")
        # )
        # SUBTXTM.place(x=900, y=300)
        
        SUBTXTM = customtkinter.CTkEntry(master=self.root,width=400,bg_color='#FFFFFF' ,fg_color="#4895EF" ,placeholder_text_color="#FFFFFF",border_color= '#FFFFFF',placeholder_text="Enter Subject..",font=('PT BOLD HEADING', 18),height=45)
        SUBTXTM.place(x=770, y=300)
        # Fill Attendance Button For Manual #
        fill_attendance_man = tk.Button(
            self.root,
            text="Fill Attendance",
            cursor="hand2",
            relief=FLAT,
            font=("times", 15, " bold "),
            fg="#FFFFFF",
            # command=self.register,
            bg="#4895EF",
            activebackground="green",
        )
        fill_attendance_man.place(x=890, y=450)
        
        self.root.mainloop()

window = Tk()
StudentManagementSystem(window)
window.mainloop()

import tkinter
import customtkinter
from PIL import ImageTk,Image

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# w = customtkinter.CTk()  
# w.geometry("1280x720")
# w.title('Welcome')
# l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
# # l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
# l1.place(x=20,y=150)
# w.mainloop()

# app = customtkinter.CTk()  #creating cutstom tkinter window
# app.geometry("600x440")
# app.title('Login')
# app.mainloop()