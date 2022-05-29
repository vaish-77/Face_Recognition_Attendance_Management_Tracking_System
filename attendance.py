import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import csv
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
import cv2


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
mydata = []
class Attendance:
    WIDTH = 1100
    HEIGHT = 570

    def __init__(self, root):
        # super().__init__()

        self.root_attend = root
        self.root_attend.title("Student Profile")
        self.root_attend.geometry(f"{Attendance.WIDTH}x{Attendance.HEIGHT}")

        # VARIABLES
        self.var_id = tkinter.StringVar()
        self.var_name = tkinter.StringVar()
        self.var_dep = tkinter.StringVar()
        self.var_time = tkinter.StringVar()
        self.var_date = tkinter.StringVar()
        self.var_status = tkinter.StringVar()



        # =======Frame using grid========

        self.root_attend.grid_columnconfigure(1, weight=1)
        self.root_attend.grid_rowconfigure(0, weight=1)
        # Left frame
        self.frame_left = customtkinter.CTkFrame(master=self.root_attend,
                                                width=500,
                                                corner_radius=10)
        self.frame_left.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        # Right frame
        self.frame_right = customtkinter.CTkFrame(master=self.root_attend)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=15)

                         # ============= Left Label Frame ================
        # Labels and entry box


        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,

                                              text="Student Information",
                                              text_font=("Roboto Medium", -16),
                                              text_color=("light blue"))  # font name and size in px
        self.label_1.grid(row=0, column=0)

        # ID_Number
        self.id_label = customtkinter.CTkLabel(master=self.frame_left,
                                                text="Student ID", width=5)

        self.id_label.grid(row=1, column=0, pady=10, sticky="W")

        self.id_entry = customtkinter.CTkEntry(self.frame_left,
                                               width=150,
                                               textvariable=self.var_id,
                                               border_width=1,
                                               corner_radius=4)
        self.id_entry.grid(row=1, column=1, padx=10, sticky="W")


        # Name
        self.name_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Name", width=15)
        # fg_color=("gray75", "gray30"))  # <- custom tuple-color

        self.name_label.grid(row=2, column=0, pady=10, sticky="W")
        self.name_entry = customtkinter.CTkEntry(self.frame_left,
                                                 width=150,
                                                 textvariable=self.var_name,
                                                 border_width=1,
                                                 corner_radius=4)
        self.name_entry.grid(row=2, column=1, padx=10, sticky="W")

        # Department
        self.dep_label = customtkinter.CTkLabel(master=self.frame_left,
                                                    text="Department", width=15)

        self.dep_label.grid(row=3, column=0, pady=10, sticky="W")
        self.dep_entry = customtkinter.CTkEntry(self.frame_left,
                                                width=150,
                                                textvariable=self.var_dep,
                                                border_width=1,
                                                corner_radius=4)
        self.dep_entry.grid(row=3, column=1, padx=10, sticky="W")

        # Time
        self.time_label = customtkinter.CTkLabel(master=self.frame_left,
                                                  text="Time", width=15)

        self.time_label.grid(row=4, column=0, pady=10, sticky="W")
        self.time_entry = customtkinter.CTkEntry(self.frame_left,
                                                 textvariable=self.var_time,
                                                  width=150,
                                                  border_width=1,
                                                  corner_radius=4)
        self.time_entry.grid(row=4, column=1, padx=10, sticky="W")

        # Date
        self.date_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Date", width=15)

        self.date_label.grid(row=5, column=0, pady=10, sticky="W")
        self.date_entry = customtkinter.CTkEntry(self.frame_left,
                                                 width=150,
                                                 textvariable=self.var_date,
                                                 border_width=1,
                                                 corner_radius=4)
        self.date_entry.grid(row=5, column=1, padx=10, sticky="W")

        # Attendance Status
        self.date_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Attendance", width=15)

        self.date_label.grid(row=6, column=0, pady=10, sticky="W")
        self.date_combo = ttk.Combobox(self.frame_left,
                                       textvariable=self.var_status,
                                       width=15, state="read only")

        self.date_combo["values"] = ("Status", "Present", "Absent")
        self.date_combo.current(0)
        self.date_combo.grid(row=6, column=1, padx=10, sticky="W")

                        # ===Button Frame===
        frame = customtkinter.CTkFrame(master=self.frame_left, width=400, height =100, corner_radius=10)
        frame.place(x=15, y=350, width=450, height=270)
        # Import csv
        self.import_button = customtkinter.CTkButton(master=frame,
                                                     command=self.importCsv,
                                                     text="Import csv",
                                                     fg_color=("gray75", "gray30"),
                                                     height=35, width=105)  # <- custom tuple-color
        self.import_button.grid(row=0, column=0, pady=25, padx=5)

        # Export csv
        self.export_button = customtkinter.CTkButton(master=frame,
                                                     command=self.exportCsv,
                                                     text="Export csv",
                                                     fg_color=("gray75", "gray30"),
                                                     height=35, width=105)  # <- custom tuple-color
        self.export_button.grid(row=0, column=1, pady=25, padx=5)
        # Update
        self.update_button = customtkinter.CTkButton(master=frame,
                                                     command=self.action,
                                                     text="Update",
                                                     fg_color=("gray75", "gray30"),
                                                     height=35, width=105)  # <- custom tuple-color
        self.update_button.grid(row=1, column=0, pady=25, padx=23)
        # Delete
        self.reset_button = customtkinter.CTkButton(master=frame,
                                                    command=self.reset_data,
                                                    text="Reset",
                                                    fg_color=("gray75", "gray30"),
                                                    height=35, width=105)  # <- custom tuple-color
        self.reset_button.grid(row=1, column=1, pady=25, padx=23)


        # ============ Right Frame ==============

        self.label_2 = customtkinter.CTkLabel(master=self.frame_right,

                                              text="Student Attendance Table",
                                              text_font=("Roboto Medium", -16),
                                              text_color=("light blue"))  # font name and size in px
        self.label_2.grid(row=0, column=0)

        # FRAME
        frame_2 = customtkinter.CTkFrame(master=self.frame_right, width=400, height=100, corner_radius=10)
        frame_2.place(x=15, y=30, width=640, height=150)
        self.search_button = customtkinter.CTkButton(master=frame_2,
                                                     command=self.update_data,
                                                     text="Update",
                                                     fg_color=("gray75", "gray30"),
                                                     height=35, width=120)  # <- custom tuple-color
        self.search_button.grid(row=1, column=1, pady=10, padx=5, sticky="W")

        self.showAll_button = customtkinter.CTkButton(master=frame_2,
                                                      command=self.delete_data,
                                                      text="Delete",
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
        style.configure("Treeview", background="dark grey", rowheight=45, foreground="black", fieldbackground="silver")
        style.map('Treeview', 'blue')
        self.student_table = ttk.Treeview(frame_table, columns=("ID", "Name", "Department", "Time", "Date", "Status"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Time", text="Time")
        self.student_table.heading("Date", text="Date")
        self.student_table.heading("Status", text="Attendance Status")
        self.student_table["show"] = "headings"

        # Customizing column
        self.student_table.column("ID", width=100, anchor="center")
        self.student_table.column("Name", width=100, anchor="w")
        self.student_table.column("Department", width=100, anchor="center")
        self.student_table.column("Time", width=100, anchor="center")
        self.student_table.column("Date", width=100, anchor="center")
        self.student_table.column("Status", width=100, anchor="center")

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor_left)



        # =============== Table for mysql view=============

        frame_table = customtkinter.CTkFrame(master=self.frame_right, width=400, height=100, corner_radius=10)
        frame_table.place(x=15, y=150, width=1057, height=695)

        scroll_x = ttk.Scrollbar(frame_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frame_table, orient=VERTICAL)

        # Add Some Style
        style = ttk.Style()
        # Pick a Theme
        style.theme_use("clam")
        # Configure our tree
        style.configure("Treeview", background="dark grey", rowheight=45, foreground="black", fieldbackground="silver")
        style.map('Treeview', 'blue')
        self.student_table = ttk.Treeview(frame_table, columns=("ID", "Name", "Department", "Time", "Date", "Status"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Time", text="Time")
        self.student_table.heading("Date", text="Date")
        self.student_table.heading("Status", text="Attendance Status")
        self.student_table["show"] = "headings"

        # Customizing column
        self.student_table.column("ID", width=100, anchor="center")
        self.student_table.column("Name", width=100, anchor="w")
        self.student_table.column("Department", width=100, anchor="center")
        self.student_table.column("Time", width=100, anchor="center")
        self.student_table.column("Date", width=100, anchor="center")
        self.student_table.column("Status", width=100, anchor="center")

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor_right)

        # ======= Update Function from mysql database =========
    def update_data(self):
        global conn
        if self.var_id.get() == "" or self.var_name.get() == "" or self.var_dep.get() == "" or self.var_time.get() == "" or self.var_date.get() == "" :
                messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root_attend)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update this Student Attendance!",
                                                 parent=self.root_attend)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                                       database="face_recogniser")
                    mycursor = conn.cursor()
                    mycursor.execute(
                        "update attendance set std_name=%s,std_dep=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",
                        (

                            self.var_name.get(),
                            self.var_dep.get(),
                            self.var_time.get(),
                            self.var_date.get(),
                            self.var_status.get(),
                            self.var_id.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Successfully Updated!", parent=self.root_attend)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root_attend)

    def delete_data(self):
        global conn
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student Id Must be Required!", parent=self.root_attend)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root_attend)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                                       database="face_recogniser")
                    mycursor = conn.cursor()
                    sql = "delete from attendance where std_id=%s"
                    val = (self.var_id.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root_attend)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root_attend)

                    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                                       database="face_recogniser")
        mycursor = conn.cursor()

        mycursor.execute("select * from attendance")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

                    # ====== Fetch Data for csv ========
    def fetchData(self, rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=i)

                            # IMPORT DATA
    def importCsv(self):
        global mydata
        mydata.clear()        # To clear the data before importing from other csv file
        file_name = filedialog .askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                                filetypes=(("CSV file", ".csv"), ("All File", "*.*")), master=self.root_attend)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

                                 # EXPORT CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", master=self.root_attend)
                return False
            file_name = filedialog .asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                                filetypes=(("CSV file", ".csv"), ("All File", "*.*")),
                                                master=self.root_attend)
            with open(file_name, mode="w", newline="") as myfile:
                export = csv.writer(myfile, delimiter=",")

                for i in mydata:
                    export.writerow(i)
                messagebox.showinfo("Data Export", "Export successful to"+os.path.basename(file_name))
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", master=self.root_attend)

            # Imported Data gets auto-filled from the table (when clicked) in student information
    def get_cursor_left(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        self.var_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_dep.set(row[2]),
        self.var_time.set(row[3]),
        self.var_date.set(row[4]),
        self.var_status.set(row[5])

    # =============Cursur Function for mysql========================

    def get_cursor_right(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        row = content['values']

        self.var_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_dep.set(row[2]),
        self.var_time.set(row[3]),
        self.var_date.set(row[4]),
        self.var_status.set(row[5])

        # Reset
    def reset_data(self):
        self.var_id.set(''),
        self.var_name.set(''),
        self.var_dep.set(''),
        self.var_time.set(''),
        self.var_date.set(''),
        self.var_status.set('')

    # Update csv
        # export upadte
    def action(self):
        if self.var_id.get() == "" or self.var_name.get() == "" or self.var_dep.get() == "" or self.var_time.get() :
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root_attend)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Bts@1306",
                                                       database="face_recogniser")
                mycursor = conn.cursor()
                mycursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s)", (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_status.get(),
                    self.var_id.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "All Records are Saved in Database!", parent=self.root_attend)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root_attend)





            
            







if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Attendance(root)
    root.mainloop()