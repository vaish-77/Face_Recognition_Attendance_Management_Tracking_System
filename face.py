import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import numpy as np


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Recognition:
    WIDTH = 400
    HEIGHT = 400

    def __init__(self, root):
        # super().__init__()

        self.root_train = root
        self.root_train.title("Face Recognition")
        self.root_train.geometry(f"{Recognition.WIDTH}x{Recognition.HEIGHT}")


        # Frame
        self.frame = customtkinter.CTkFrame(master=self.root_train,
                                                 width=300,
                                                 corner_radius=20)
        self.frame.place(x=15, y=15, width=555, height=555)

        # Button
        logo_image = ImageTk.PhotoImage(Image.open("Logos\DataLogo.png").resize((60, 50)))

        self.button = customtkinter.CTkButton(master=self.root_train,
                                              command=self.face_recognise,
                                              image=logo_image,
                                              text="Face Recognition",
                                              fg_color=("gray75", "gray30"),
                                              width=190, height=40,
                                              compound="right",
                                              corner_radius=20
                                              )

        # self.button.grid(column=1, row=1, padx=100, pady=100)
        self.button.place(x=120, y=180, width=270, height=50)


        # =========== ATTENDANCE ===========

    # def mark_attendance(self, e, n, dep):
    #     already_in_file = set()
    #     with open("Attendance.csv", "r+", newline="\n") as f:
    #         myDataList = f.readlines()
    #         name_list = []
    #
    #         for line in myDataList:
    #             # entry = line.split((", "))
    #             # name_list.append(entry[0])
    #             already_in_file.add(line.split(",")[0])
    #
    #
    #         if ((e not in already_in_file)):
    #             dt = datetime.now()
    #             d1 = dt.strftime("%d/%m/%Y")
    #             dtString = dt.strftime("%H:%M")
    #             date = str(dt).split(' ')[0]
    #             time = str(dt).split(' ')[1]
    #             time_hour = time.split(':')[0]
    #             time_minute = time.split(':')[1]
    #             start_hour = 0
    #             end_hour = 24
    #             f.writelines(f"\n{e}, {n}, {dep}, {dtString}, {d1}, Present")
    #             if (int(time_hour) >= start_hour and int(time_hour) <= end_hour):
    #                 f.writelines(f"\n{e}, {n}, {dep}, {dtString}, {d1}, Present")


            # ========== RECOGNITION ==========
    def face_recognise(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbhors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbhors)

            cord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100*(1-predict/300)))

            # Extracting data from database
                conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                               database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("select EntryNo from student where EntryNo= " + str(id))  # Connecting name(from mySQL) with 'id'
                e = my_cursor.fetchone()
                e = "+".join(e)

                my_cursor.execute("select Name from student where EntryNo= "+str(id))   #Connecting name(from mySQL) with 'id'
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Department from student where EntryNo= " + str(id))  # Connecting name(from mySQL) with 'id'
                dep = my_cursor.fetchone()
                dep = "+".join(dep)

            # Lower confidence ==> Distance less between two histograms [better]
                if confidence > 77:
                    cv2.putText(img, f"ID: {e}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    # already_in_file = set()
                    with open("Attendance.csv", "r+", newline="\n") as f:
                        myDataList = f.readlines()
                        name_list = []

                        for line in myDataList:
                            entry = line.split((", "))
                            name_list.append(entry[0])
                            #already_in_file.add(line.split(",")[0])

                        if ((e not in name_list)):
                            dt = datetime.now()
                            d1 = dt.strftime("%d/%m/%Y")
                            dtString = dt.strftime("%H:%M:%S")
                            date = str(dt).split(' ')[0]
                            time = str(dt).split(' ')[1]
                            time_hour = time.split(':')[0]
                            time_minute = time.split(':')[1]
                            start_hour = 0
                            end_hour = 24

                            if (int(time_hour) >= start_hour and int(time_hour) <= end_hour):
                                f.writelines(f"\n{e}, {n}, {dep}, {dtString}, {d1}, Present")

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y + 7), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                cord = [x, y, w, h]

            return cord

        def recognise(img, clf, faceCascade):
            cord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), 'Face', clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # For both Detection and Recognition
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Train_classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret,img = video_cap.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Face_Recognition", img)

            if cv2.waitKey(1) == 13:  # Close the window by Enter
                break
        video_cap.release()
        cv2.destroyAllWindows()













    def markAttendance(self, n, date, time):
        conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                       database="face_recogniser")
        my_cursor = conn.cursor()
        insert = "Insert into student values(%s, %s, %s, %s, %s)"
        val = ( n, date, time)
        my_cursor.execute(insert, val)
        conn.commit()




if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Recognition(root)
    root.mainloop()