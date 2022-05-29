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


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Student:
    WIDTH = 1000
    HEIGHT = 600

    def __init__(self, root):
        # super().__init__()

        self.root_student = root
        self.root_student.title("Student Profile")
        self.root_student.geometry(f"{Student.WIDTH}x{Student.HEIGHT}")

        # VARIABLES
        self.var_dep = tkinter.StringVar()
        self.var_sem = tkinter.StringVar()
        self.var_name = tkinter.StringVar()
        self.var_entryNo = tkinter.StringVar()
        self.var_email = tkinter.StringVar()
        self.var_dob = tkinter.StringVar()
        self.var_phone = tkinter.StringVar()


        # =======Frame using grid========

        self.root_student.grid_columnconfigure(1, weight=1)
        self.root_student.grid_rowconfigure(0, weight=1)
        # Left frame
        self.frame_left = customtkinter.CTkFrame(master=self.root_student,
                                                width=500,
                                                corner_radius=10)
        self.frame_left.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
        # Right frame
        self.frame_right = customtkinter.CTkFrame(master=self.root_student)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=15)

                         # ============= Left Label Frame ================
        # Labels and entry box
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Student Details",
                                              text_font=("Roboto Medium", -16),
                                              text_color=("light blue"))  # font name and size in px
        self.label_1.grid(row=0, column=0)



        # Department
        self.dep_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Department", width=15)
                                                # fg_color=("gray75", "gray30"))  # <- custom tuple-color

        self.dep_label.grid(row=1, column=0,pady=10, sticky="W")
        self.dep_combo = ttk.Combobox(self.frame_left, textvariable=self.var_dep, width=15, state="read only")

        self.dep_combo["values"] = ("Select Department", "CSE", "EE", "Civil", "Mechanical")
        self.dep_combo.current(0)
        self.dep_combo.grid(row=1, column=1, sticky="W")

        #  Semester
        self.sem_label = customtkinter.CTkLabel(master=self.frame_left,
                                                text="Semester", width=15)
        # fg_color=("gray75", "gray30"))  # <- custom tuple-color

        self.sem_label.grid(row=1, column=2,pady=10, sticky="w")
        self.sem_combo = ttk.Combobox(self.frame_left, textvariable=self.var_sem, width=15, state="read only")

        self.sem_combo["values"] = ("Select", "1", "2", "3", "4", "5", "6", "7", "8")
        self.sem_combo.current(0)
        self.sem_combo.grid(row=1, column=3, padx=10, pady=3, sticky="w")

        # Name
        self.name_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Name", width=15)
        # fg_color=("gray75", "gray30"))  # <- custom tuple-color

        self.name_label.grid(row=2, column=0,pady=10, sticky="W")
        self.name_entry = customtkinter.CTkEntry(self.frame_left, textvariable=self.var_name,
                                                 width=150,
                                                 placeholder_text="Enter",
                                                 border_width=1,
                                                 corner_radius=4)
        self.name_entry.grid(row=2, column=1, sticky="W")

        # Entry No.
        self.entryno_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Entry Number", width=15)
        # fg_color=("gray75", "gray30"))  # <- custom tuple-coentryno
        self.entryno_label.grid(row=3, column=0, pady=10, sticky="W")
        self.entryno_entry = customtkinter.CTkEntry(self.frame_left, textvariable=self.var_entryNo,
                                                 width=150,
                                                 placeholder_text="Enter",
                                                 border_width=1,
                                                 corner_radius=4)
        self.entryno_entry.grid(row=3, column=1, sticky="W")

        # Email Address.
        self.email_label = customtkinter.CTkLabel(master=self.frame_left,
                                                    text="Email Address", width=15)

        self.email_label.grid(row=4, column=0, pady=10, sticky="W")
        self.email_entry = customtkinter.CTkEntry(self.frame_left, textvariable=self.var_email,
                                                    width=150,
                                                    placeholder_text="Enter",
                                                    border_width=1,
                                                    corner_radius=4)
        self.email_entry.grid(row=4, column=1, sticky="W")

        # Date of Birth
        self.dob_label = customtkinter.CTkLabel(master=self.frame_left,
                                                  text="Date of Birth", width=15)

        self.dob_label.grid(row=5, column=0, pady=10, sticky="W")
        self.dob_entry = customtkinter.CTkEntry(self.frame_left, textvariable=self.var_dob,
                                                  width=150,
                                                  placeholder_text="DD/MM/YYYY",
                                                  border_width=1,
                                                  corner_radius=4)
        self.dob_entry.grid(row=5, column=1, sticky="W")

        # Phone Number
        self.phone_label = customtkinter.CTkLabel(master=self.frame_left,
                                                text="Phone Number", width=15)
        # fg_color=("gray75", "gray30"))  # <- custom tuple-coentryno
        self.phone_label.grid(row=6, column=0, pady=10, sticky="W")
        self.phone_entry = customtkinter.CTkEntry(self.frame_left, textvariable=self.var_phone,
                                                width=150,
                                                placeholder_text="Enter",
                                                border_width=1,
                                                corner_radius=4)
        self.phone_entry.grid(row=6, column=1, sticky="W")

        # Radio buttons
        self.var_radio1 = tkinter.StringVar()
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.var_radio1,
                                                           text="Create photo Sample",
                                                           width=15, height=15,
                                                           value="Yes",
                                                           corner_radius=0,
                                                           border_width_unchecked=1,
                                                           border_width_checked=2)
        self.radio_button_1.grid(row=7, column=0, padx=3, pady=5)

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.var_radio1,
                                                           text="No photo Sample",
                                                           width=15, height=15,
                                                           value="No",
                                                           corner_radius=1,
                                                           border_width_unchecked=1,
                                                           border_width_checked=2)
        self.radio_button_2.grid(row=7, column=1, padx=3, pady=5)
        # self.radio_button_1.select()

                                # ===Button Frame===
        frame = customtkinter.CTkFrame(master=self.frame_left, width=400, height =100, corner_radius=10)
        frame.place(x=15, y=350, width=700, height=325)
        # SAVE
        self.save_button = customtkinter.CTkButton(master=frame,
                                                   command=self.add_data,
                                                   text="Save",
                                                   fg_color=("gray75", "gray30"),
                                                   height=35, width=105)  # <- custom tuple-color
        self.save_button.grid(row=0, column=0, pady=25, padx=5)

        # Update
        self.update_button = customtkinter.CTkButton(master=frame,
                                                     command=self.update_data,
                                                   text="Update",
                                                   fg_color=("gray75", "gray30"),
                                                   height=35, width=105)  # <- custom tuple-color
        self.update_button.grid(row=0, column=1, pady=25, padx=5)
        # Delete
        self.delete_button = customtkinter.CTkButton(master=frame,
                                                     command=self.delete_data,
                                                     text="Delete",
                                                     fg_color=("gray75", "gray30"),
                                                     height=35, width=105)  # <- custom tuple-color
        self.delete_button.grid(row=0, column=2, pady=25, padx=5)
        # Reset
        self.reset_button = customtkinter.CTkButton(master=frame,
                                                    command=self.reset_data,
                                                    text="Reset",
                                                    fg_color=("gray75", "gray30"),
                                                    height=35, width=105)  # <- custom tuple-color
        self.reset_button.grid(row=0, column=3, pady=25, padx=5)

        # ===Sample Button Frame===
        frame_1 = customtkinter.CTkFrame(master=frame, width=400, height=100, corner_radius=10)
        frame_1.place(x=15, y=90, width=650, height=100)

        # Take Photo
        self.takePhoto_button = customtkinter.CTkButton(master=frame_1,
                                                        command=self.generate_data,
                                                        text="Create Sample",
                                                        fg_color=("gray75", "gray30"),
                                                        height=35,width=205)  # <- custom tuple-color
        self.takePhoto_button.grid(row=1, column=0, pady=20, padx=5)

        # Update Photo
        # self.updatePhoto_button = customtkinter.CTkButton(master=frame_1,
        #                                             text="Update Sample",
        #                                             fg_color=("gray75", "gray30"),
        #                                             height=35,width=205)  # <- custom tuple-color
        # self.updatePhoto_button.grid(row=1, column=1, pady=20, padx=5)

                        # ============= Right Label Frame ================
        frame_2 = customtkinter.CTkFrame(master=self.frame_right, width=400, height=100, corner_radius=10)
        frame_2.place(x=15, y=30, width=640, height=150)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Search System",
                                              text_font=("Roboto Medium", -16),
                                              width=10, height=10,
                                              text_color=("light blue"))  # font name and size in px
        self.label_2.grid(row=0, column=0, pady=5)

        # Frame 2_ Search System
            # Variables
        self.var_com_search = tkinter.StringVar()     # combo box
        self.var_search = tkinter.StringVar()        # Entry box
        self.search_label = customtkinter.CTkLabel(master=frame_2,
                                                text="Search By:", width=20)
        # fg_color=("gray75", "gray30"))  # <- custom tuple-color

        self.search_label.grid(row=0, column=0, pady=10, sticky="nsew")
        self.search_combo = ttk.Combobox(frame_2, textvariable=self.var_com_search,  width=17, state="read only")

        self.search_combo["values"] = ("Select ", "Name", "Department")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, sticky="W")

        self.search_entry = customtkinter.CTkEntry(frame_2,
                                                   textvariable=self.var_search,
                                                  width=150,
                                                  placeholder_text="Enter",
                                                  border_width=1,
                                                  corner_radius=4)
        self.search_entry.grid(row=0, column=2, padx=10, sticky="W")

        self.search_button = customtkinter.CTkButton(master=frame_2,
                                                     command=self.search_data,
                                                     text="Search",
                                                     fg_color=("gray75", "gray30"),
                                                     height=35, width=120)  # <- custom tuple-color
        self.search_button.grid(row=1, column=1, pady=10, padx=5, sticky="W")

        self.showAll_button = customtkinter.CTkButton(master=frame_2,

                                                      text="Show All",
                                                      fg_color=("gray75", "gray30"),
                                                      height=35, width=120)  # <- custom tuple-color
        self.showAll_button.grid(row=1, column=2, pady=10, padx=5, sticky="W")

        # ======Table Frame======
        frame_table = customtkinter.CTkFrame(master=self.frame_right, width=400, height=100, corner_radius=10)
        frame_table.place(x=15, y=150, width=1057, height=695)
        scroll_x = ttk.Scrollbar(frame_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frame_table, orient=VERTICAL)

        # Add Some Style
        style = ttk.Style()
        # Pick a Theme
        style.theme_use("clam")
        # Configure our tree
        style.configure("Treeview", background="dark grey", rowheight=45, foreground="black",fieldbackground="silver")
        style.map('Treeview', 'blue')
        self.student_table = ttk.Treeview(frame_table, columns=("Department", "sem", "Name", "EntryNo", "Email", "DOB",
                                                                "Phone", "Photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("EntryNo", text="ID Number")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.heading("Phone", text="Phone Number")
        self.student_table.heading("Photo", text="PhotoSample_Status")
        self.student_table["show"] = "headings"

        # Customizing column
        self.student_table.column("Department", width=150, anchor="center")
        self.student_table.column("sem", width=150, anchor="center")
        self.student_table.column("Name", width=150, anchor="w")
        self.student_table.column("EntryNo", width=150, anchor="center")
        self.student_table.column("Email", width=250, anchor="w")
        self.student_table.column("DOB", width=150,anchor="center")
        self.student_table.column("Phone", width=170, anchor="center")
        self.student_table.column("Photo", width=180, anchor="center")

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()     # Calling the function to fetch the data from MySQL database

                                                 # ======Function Declaration======
                                                     # COMBINING MySQL DATABASE
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_entryNo.get()=="":
            messagebox.showerror("Error", "All Fields are required", master=self.root_student)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                               database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into student values(%s, %s, %s, %s, %s, %s, %s, %s)",
                                  (
                                      self.var_dep.get(),
                                      self.var_sem.get(),
                                      self.var_name.get(),
                                      self.var_entryNo.get(),
                                      self.var_email.get(),
                                      self.var_dob.get(),
                                      self.var_phone.get(),
                                      self.var_radio1.get()

                                  ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details has been added successfully.", master=self.root_student)

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", master=self.root_student)

                # =====FETCH DATA FUNCTION========
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                       database="face_recogniser")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # ====== Get Cursor ======
    def get_cursor(self, event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)           # Extract content and store in var
        data = content['values']

        self.var_dep.set(data[0]),
        self.var_sem.set(data[1]),
        self.var_name.set(data[2]),
        self.var_entryNo.set(data[3])
        self.var_email.set(data[4]),
        self.var_dob.set(data[5]),
        self.var_phone.set(data[6]),
        self.var_radio1.set(data[7])

        try:
            print(str(content['values'][3]))  # getting output as 1 but then error
        except:
            pass


        # ===== UPDATE FUNCTION ======

    def update_data(self):

        global conn
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_entryNo.get()=="":
            messagebox.showerror("Error", "All Fields are required", master=self.root_student)

        else:
            try:
                update = messagebox.askyesno("Update", "Confirm Update?", master=self.root_student)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                                   database="face_recogniser")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s, Sem=%s, Name=%s,  Email=%s, "
                                      "DOB=%s, Phone=%s, PhotoSample=%s where EntryNo=%s",
                                      (
                                          self.var_dep.get(),
                                          self.var_sem.get(),
                                          self.var_name.get(),
                                          self.var_email.get(),
                                          self.var_dob.get(),
                                          self.var_phone.get(),
                                          self.var_radio1.get(),
                                          self.var_entryNo.get()
                                      ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Details Updated Successfully", master=self.root_student)

                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", master=self.root_student)

        # ===== DELETE FUNCTION ======
    def delete_data(self):
        global conn
        if self.var_entryNo.get()=="":
            messagebox.showerror("Error", "Student Entry Number is required", master=self.root_student)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Confirm Delete?")
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                           database="face_recogniser")
                    my_cursor = conn.cursor()
                    sql = "delete from student where EntryNo=%s"
                    val = (self.var_entryNo.get(), )
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Delete", " Details Deleted Successfully", master=self.root_student)

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", master=self.root_student)

        # ==== RESET FUNCTION ======
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_sem.set("Select"),
        self.var_name.set("Enter"),
        self.var_entryNo.set("Enter"),
        self.var_email.set("Enter"),
        self.var_dob.set("DD/MM/YY"),
        self.var_phone.set("Enter"),
        self.var_radio1.set("")

        # ======= Search data =======
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error", "Please select Search Box option.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                               database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get()) + " LIKE '%"+str(self.var_search.get())
                                  +"%'")
                data = my_cursor.fetchall()
                if len(data) != 0:   # has data
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo("Sorry", "No Data Found", master=self.root_student)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", master=self.root_student)



        # ============== Generate DATASET or PhotoSample ============
    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_entryNo.get()=="":
            messagebox.showerror("Error", "All Fields are required", master=self.root_student)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                                   database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Department=%s, Sem=%s, Name=%s,  Email=%s, "
                              "DOB=%s, Phone=%s, PhotoSample=%s where EntryNo=%s",
                              (
                                  self.var_dep.get(),
                                  self.var_sem.get(),
                                  self.var_name.get(),
                                  self.var_email.get(),
                                  self.var_dob.get(),
                                  self.var_phone.get(),
                                  self.var_radio1.get(),
                                  self.var_entryNo.get() == id+1
                              ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ======== Load Predefined data on face frontals from openCV ========

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # File is for object detection

                # Cropping images for easy detection

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3 ; Minimum Neighbour = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # Open Cam
                img_id = 0            # Calculation set 0

                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                    try:
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                    except:
                        break
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data_img/user."+str(id)+"."+str(img_id)+".jpg" # Naming the file & format
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                    cv2.imshow("Collecting Dataset", face)

                        # Close the window by pressing Enter or it closes after 50 captures
                    if cv2.waitKey(1)== 13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Dataset Generated successfully:)")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", master=self.root_student)



























    # def on_closing(self, event=0):
    #     self.destroy()
    #
    # def start(self):
    #     self.mainloop()

# if __name__ == "__main__":
#     app = student()
#     app.start()


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Student(root)
    root.mainloop()
