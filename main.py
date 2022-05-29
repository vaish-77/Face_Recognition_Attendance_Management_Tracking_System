import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from recognition import Recognition
from attendance import Attendance
from help import Help


PATH = os.path.dirname(os.path.realpath(__file__))
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Face_Recognition_System:
    WIDTH = 780
    HEIGHT = 520

    def __init__(self, root):
        self.root = root
        # super().__init__()
        self.root.title("FACE RECOGNITION - ATTENDANCE SYSTEM")
        self.root.geometry(f"{Face_Recognition_System.WIDTH}x{Face_Recognition_System.HEIGHT}")

        # self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ Create Two Frames ============
        # configure grid

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self.root,
                                                width = 180,
                                                corner_radius = 0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")
        self.frame_right = customtkinter.CTkFrame(master=self.root)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

         # ============ frame_left ============

            # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Home",
                                              text_font =("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Student Management",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.student_details)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                    text=" Photos",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.open_images)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                command=self.train_data,
                                                text="Train Data",
                                                fg_color=("gray75", "gray30"))  # <- custom tuple-color

        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Attendance",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.attendance)
        self.button_4.grid(row=5, column=0, pady=10, padx=20)
        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=10)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        # ============ frame_info ============

        # configure grid layout (1x1)

        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        #

        # logo_image = ImageTk.PhotoImage(Image.open("MyLogo.png").resize((400, 400)))
        # logo = ImageTk.PhotoImage(file='MyLogo.png')
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   # image=logo_image,
                                                   # compound="center",
                                                   text="Welcome",
                                                   text_font=("Bauhaus 93", 35),
                                                   height=70,
                                                  # fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   text_color=("cyan"),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Help",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.help)
        self.button_5.grid(row=6, column=0, pady=10, padx=20)

        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                command=self.recognise,
                                                text="Recognition",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                )
        self.button_6.place(x=30, y=250)

    # Functions for Features/Buttons
    def student_details(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.app = Student(self.new_window)

    def open_images(self):
        os.startfile("data_img")

    def train_data(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.app = Train(self.new_window)

    def recognise(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.app = Recognition(self.new_window)

    def attendance(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.app = Attendance(self.new_window)

    def help(self):
        self.new_window = customtkinter.CTkToplevel(self.root)
        self.app = Help(self.new_window)


    # def on_closing(self, event=0):
    #     self.destroy()
    #
    # def start(self):
    #     self.mainloop()

# if __name__ == "__main__":
#     app = Face_Recognition_System()
#     app.start()


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Face_Recognition_System(root)
    root.mainloop()






