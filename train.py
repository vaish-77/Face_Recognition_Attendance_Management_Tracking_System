import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Train:
    WIDTH = 400
    HEIGHT = 400

    def __init__(self, root):
        # super().__init__()

        self.root_train = root
        self.root_train.title("Training Data")
        self.root_train.geometry(f"{Train.WIDTH}x{Train.HEIGHT}")


        # Frame
        self.frame = customtkinter.CTkFrame(master=self.root_train,
                                                 width=300,
                                                 corner_radius=20)
        self.frame.place(x=15, y=15, width=555, height=555)

        # Button
        logo_image = ImageTk.PhotoImage(Image.open("Logos\DataLogo.png").resize((60, 50)))

        self.button = customtkinter.CTkButton(master=self.root_train,
                                              command=self.train_classifier,
                                              image=logo_image,
                                              text="TRAIN",
                                              fg_color=("gray75", "gray30"),
                                              width=190, height=40,
                                              compound="right",
                                              corner_radius=20
                                              )

        # self.button.grid(column=1, row=1, padx=100, pady=100)
        self.button.place(x=120, y=180, width=250, height=50)


            # Train Data using LBPH ALgorithm
    def train_classifier(self):
        data_direct = ("data_img")    # extracting data to data_direct variable
        path = [os.path.join(data_direct, file) for file in os.listdir(data_direct)]  # List Comprehension

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # generate GRAY scale image
            imageNp = np.array(img, 'uint8')

            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)          # Numpy gives more efficiency to convert in array

               # ====== Train the Classifier ========
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier_train.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets completed")
















if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Train(root)
    root.mainloop()