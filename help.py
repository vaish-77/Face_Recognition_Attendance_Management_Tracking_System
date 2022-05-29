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

PATH = os.path.dirname(os.path.realpath(__file__))
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Help():
    WIDTH = 780
    HEIGHT = 520

    def __init__(self, root):
        self.root = root
        # super().__init__()
        self.root.title("Help_Desk")
        self.root.geometry(f"{Help.WIDTH}x{Help.HEIGHT}")

        # self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ Create Two Frames ============
        # configure grid

        self.frame = customtkinter.CTkFrame(master=self.root,
                                            width=300,
                                            corner_radius=20)
        self.frame.place(x=15, y=15, width=1125, height=730)

        self.frame_info = customtkinter.CTkFrame(master=self.frame, corner_radius=20)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        # ============ frame_info ============
        self.frame_info.rowconfigure(1, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        #


        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="HELP",
                                                   text_font=("Candara", 20, "bold"),
                                                   height=50,
                                                   # fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   text_color=("cyan"),
                                                   justify=tkinter.LEFT,
                                                   corner_radius=20)
        self.label_info_1.grid(column=0, row=0, padx=10, pady=10, sticky ="nsew")

        self.label_info_2 = customtkinter.CTkLabel(master=self.frame,
                                                   text="If you have any concerns or questions about how this programme works,\n "+
                                                        "you've come to the right place.\n"+
                                                        "\n" +
                                                        "Please read carefully and follow the process step by step.\n"+
                                                        "The application's menu is visible on the left. This section displays the features.\n"+
                                                        "\n"+
                                                        "To begin using the application, go through the following steps:\n"+
                                                        "— First, you can register in the attendance system through student management.\n"+
                                                        "   Other functions, such as updating and deleting student data, are also available.\n"+
                                                        "   Create the sample photo dataset using the CREATE SAMPLE button.\n"+
                                                        "— Use the Recognition button on the main window to record your attendance.\n"+
                                                        "— Clicking on the attendance page displays the attendance list's name, date, time,\n"+
                                                        "   and other information.",
                                                   width=500,
                                                   height=120,
                                                   fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                   # text_color=("cyan"),
                                                   justify=tkinter.LEFT,
                                                   corner_radius=10)
        self.label_info_2.grid(column=7, row=12, padx=10, pady=10, sticky="nsew")


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Help(root)
    root.mainloop()