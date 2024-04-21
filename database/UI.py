import tkinter as tk                 
from tkinter import ttk, filedialog                         
import tkinter.messagebox as mb      
import tkinter.simpledialog as sd
import database
import mysql.connector as mysql


class SSISApp:                 
    def __init__(self, root):  
        self.root = root        
        self.root.title("Simple Student Information System") 
        root.geometry("950x650")                             
        root.resizable(width=True, height=True)     
        root.configure(bg = "#000000")

        self.file_path = ""    # //initialise file_path attribute
        self.data = []         # //initialise data attribute

        self.create_Widgets() 

        connec, C = database.initialise_conn()
     
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()

        C.execute("SELECT * FROM student")



    def create_Widgets(self):  

        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()


        # //frame for buttons
        button_frame = tk.Frame(self.root, bg="#171717") # //creates a frame for buttons called button_frame
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20) 
        #highlightbackground="white", highlightthickness=1, 
        
        # //returns to home page(student data) within the treeview
        Back_Stud_Button = tk.Button(button_frame, text="back", font=("Verdana", 10, "italic"), command=self.Open_student,
                               bg="black", fg="white")
        Back_Stud_Button.pack(side=tk.LEFT, padx=5, pady=5)               

        # //returns to home page(student data) within the treeview
        Back_Course_Button = tk.Button(button_frame, text="back", font=("Verdana", 10, "italic"), command=self.Open_course,
                               bg="black", fg="white")
        Back_Course_Button.pack(side=tk.RIGHT, padx=5, pady=5)
         

        """STUDENT BUTTONS"""    
        # //updates student data 
        Edit_Student_Button = tk.Button(button_frame, text="Edit Student", font=("Verdana", 10, "bold"), command=self.Select_Student_to_Update,
                               bg="yellow")
        Edit_Student_Button.pack(side=tk.LEFT, padx=5, pady=5)    


        # //deletes student data after a row is selected from the treeview
        Delete_Student_Button = tk.Button(button_frame, text="Delete Student", font=("Verdana", 10, "bold"), command=self.Delete_student,
                                 bg="red", fg="white")
        Delete_Student_Button.pack(side=tk.LEFT, padx=5, pady=5) 

               
        # //saves student to database 
        Save_Student_Button = tk.Button(button_frame, text="Save Student", font=("Verdana", 10, "bold"), command=self.Save_student,
                                bg="green", fg="white")
        Save_Student_Button.pack(side=tk.LEFT, padx=5, pady=5)      # //place SaveButton in button_frame
                    
    
        """COURSE BUTTONS"""
        # //updates or edits a course 
        Edit_Course_Button = tk.Button(button_frame, text="Edit Course", font=("Verdana", 10, "bold"),
                                      bg="brown", fg="white")
        Edit_Course_Button.pack(side=tk.RIGHT, padx=5, pady=5)

        # //removes a course
        Course_Delete_Button = tk.Button(button_frame, text="Delete Course", font=("Verdana", 10, "bold"), command=self.Delete_course,
                                         bg="lavender", fg="black")
        Course_Delete_Button.pack(side=tk.RIGHT, padx=5, pady=5)

        # //adds a course 
        Add_Course_Button = tk.Button(button_frame, text="Add Course", font=("Verdana", 10, "bold"), command=self.Add_course,
                                      bg="light blue", fg="black")
        Add_Course_Button.pack(side=tk.RIGHT, padx=5, pady=5)


        
        """SEARCH WIDGETS"""
        # //exclusive frame for 'Search'
        s_frame = tk.Frame (self.root, bg="#171717")
        s_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=20)
        #highlightbackground="light gray", highlightthickness=1,

        tk.Label(s_frame, text="Search by ID no.:", bg="#171717", fg="white", font=("Verdana", 9, "italic")).pack(side=tk.LEFT)
        self.searchStudentText = tk.Entry(s_frame, width=40)
        self.searchStudentText.pack(side=tk.LEFT, padx=5, pady=5)

        # //Search or filter students data based on ID no.
        Search_stud_Button = tk.Button(s_frame, text="Search", font=("Verdana", 10, "bold"), command=self.Search_student,
                                 bg="white")
        Search_stud_Button.pack(side=tk.LEFT, padx=5, pady=5)         
        
        # //Search or filter courses based on course code

        Search_course_Button = tk.Button(s_frame, text="Search", font=("Verdana", 10, "bold"), command=self.Search_course,
                                 bg="white")
        Search_course_Button.pack(side=tk.RIGHT, padx=5, pady=5)   

        self.searchCourse = tk.Entry(s_frame, width=40)
        self.searchCourse.pack(side=tk.RIGHT, padx=5, pady=5)

        tk.Label(s_frame, text="Search by Course Code:", bg="#171717", fg="white", font=("Verdana", 9, "italic")).pack(side=tk.RIGHT)

    # frame for treeview, text entries, & labels
        tt_frame = tk.Frame(self.root, bg="#171717") # //creates a frame called tt_frame
        tt_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=20, pady=20) # //layout of tt_frame using pack() method

        tt_frame.rowconfigure(1, weight=1)
        tt_frame.columnconfigure(0, weight=1)
        tt_frame.columnconfigure(2, weight=1)

         
    # to dynamically resize rows and columns
        #for x in range(7):
            #tt_frame.grid_rowconfigure(x, weight=1)

        #for y in range(3):
            #tt_frame.grid_columnconfigure(y, weight=1)



        """LABELS"""
        studentIDnoLabel = tk.Label(tt_frame, text = "Enter ID number:", bg="#171717", fg="white", font=("Verdana", 9))    # //label for ID no. input
        studentIDnoLabel.grid(row=3, column=0, padx=5, pady=5) 

        studentNameLabel = tk.Label(tt_frame, text = "Enter Full Name:", bg="#171717", fg="white", font=("Verdana", 9)) # //label for Student Name input
        studentNameLabel.grid(row=4, column=0, padx=5, pady=5)            # //place label in tt_frame

        studentGenderLabel = tk.Label(tt_frame, text = "Enter Gender:", bg="#171717", fg="white", font=("Verdana", 9))      # //label for Gender input
        studentGenderLabel.grid(row=5, column=0, padx=5, pady=5)         

        studentYrLevelLabel = tk.Label(tt_frame, text = "Enter Year Level:", bg="#171717", fg="white", font=("Verdana", 9)) # //label for Year Level input
        studentYrLevelLabel.grid(row=6, column=0, padx=5, pady=5)    

        studentCourseCodeLabel = tk.Label(tt_frame, text = "Enter Course Code :", bg="#171717", fg="white", font=("Verdana", 9))   # //label for Course Code input 
        studentCourseCodeLabel.grid(row=7, column=0, padx=5, pady=5)


        """TREEVIEW (for Students)""" 
        C.execute("SELECT * FROM student")
        
        self.stud_tree = ttk.Treeview(tt_frame, columns=("id_No.", "student_name", "gender", "year_lvl", "course_code")) # //create Treeview widget within tt_frame
        
        self.stud_tree["show"]="headings"

        s = ttk.Style(self.stud_tree)
        s.theme_use("alt")

        s.configure(".", font=("Verdana", 11))
        s.configure("Treeview.Heading", foreground="black", font=("Verdana", 11, "bold"))

        self.stud_tree["columns"]=("id_No.", "student_name", "gender", "year_lvl", "course_code")

        self.stud_tree.column("id_No.", width=30, minwidth=30, anchor="center")
        self.stud_tree.column("student_name", width=180, minwidth=180, anchor="w")
        self.stud_tree.column("gender", width=50, minwidth=50, anchor="center")
        self.stud_tree.column("year_lvl", width=50, minwidth=50, anchor="center")
        self.stud_tree.column("course_code", width=50, minwidth=50, anchor="center")
        
        self.stud_tree.heading("id_No.", text="ID No.", anchor="center")
        self.stud_tree.heading("student_name", text="Student Name", anchor="center")
        self.stud_tree.heading("gender", text="Gender", anchor="center")
        self.stud_tree.heading("year_lvl", text="Year Level", anchor="center")
        self.stud_tree.heading("course_code", text="Course Code", anchor="center")
        
        i = 0
        for row in C:
            self.stud_tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4]))
            i = i + 1

        self.stud_tree.grid(row=1, column=0, padx=(10, 0), pady=10, sticky="nsew")

        # //vertical scrollbar
        scrollbar = ttk.Scrollbar(tt_frame, orient="vertical", command=self.stud_tree.yview)
        scrollbar.grid(row=1, column=1, padx=(10, 0), pady=10, sticky="ns")
        self.stud_tree.configure(yscrollcommand=scrollbar.set)



        """TREEVIEW (for Course)"""
        C.execute("SELECT * FROM course")
        
        self.course_tree = ttk.Treeview(tt_frame, columns=("course_code", "course_name")) # //create Treeview widget within tt_frame
        
        self.course_tree["show"]="headings"

        s = ttk.Style(self.course_tree)
        s.theme_use("alt")

        s.configure(".", font=("Verdana", 11))
        s.configure("Treeview.Heading", foreground="black", font=("Verdana", 11, "bold"))
        self.course_tree["columns"]=("course_code", "course_name")

        self.course_tree.column("course_code", width=5, minwidth=5, anchor="center")
        self.course_tree.column("course_name", width=200, minwidth=200, anchor="center")
        self.course_tree.heading("course_code", text="Course Code", anchor="center")
        self.course_tree.heading("course_name", text="Course Name", anchor="center")
        
        i = 0
        for row in C:
            self.course_tree.insert('', i, text="", values=(row[0], row[1]))
            i = i + 1

        self.course_tree.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="nsew")

        # //vertical scrollbar
        scrollbar = ttk.Scrollbar(tt_frame, orient="vertical", command=self.course_tree.yview)
        scrollbar.grid(row=1, column=5, padx=(10, 0), pady=10, sticky="ns")
        self.course_tree.configure(yscrollcommand=scrollbar.set)


        """TEXT WIDGETS"""
        self.idText = tk.Text(tt_frame, height=1.4, width=35, wrap=tk.NONE) # //ID no. input
        self.idText.grid(row=3, column=0, columnspan=3, padx=5, pady=6)
        self.idText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))
        """when 'tab' key is pressed, it will call function 'next_entry_widget_is' then it will proceed to the next text entry"""
        
        self.nameText = tk.Text(tt_frame, height=1.4, width=35, wrap=tk.NONE) # //student name input
        self.nameText.grid(row=4, column=0, columnspan=3, padx=5, pady=6)       
        self.nameText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))  

        self.genderText = tk.Text(tt_frame, height=1.4, width=35, wrap=tk.NONE) # //gender input
        self.genderText.grid(row=5, column=0, columnspan=3, padx=5, pady=6)
        self.genderText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        self.yearLevelChoice = ttk.Combobox(tt_frame, height=10, width=44, values=["1st year", "2nd year", "3rd year", "4th year"], state="readonly")
        self.yearLevelChoice.grid(row=6, column=0, columnspan=5, padx=9, pady=9)

        C.execute("SELECT course_code FROM course")
        options = C.fetchall()
        actual_options = [f"{course_code}" for course_code in options]
        selected = tk.StringVar(tt_frame)
        selected.set(actual_options[0])
        connec.commit()

        self.courseChoice = ttk.Combobox(tt_frame, textvariable="selected", values=options, height=10, width=44, state="readonly")
        self.courseChoice.grid(row=7, column=0, columnspan=3, padx=9, pady=9)
        
        #self.courseCodeText = tk.Text(tt_frame, height=1.4, width=38, wrap=tk.NONE) # //course code input
        #self.courseCodeText.grid(row=6, column=0, columnspan=3, padx=5, pady=6)
        #self.courseCodeText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        # //Used when all texts in text entry widget needs to be cleared after being inputted
        ClearButton = tk.Button(tt_frame, text="Clear All Text", 
                                command=self.clearInputData, font=("Arial", 10, "italic"))
        ClearButton.grid(row=6, column=2, columnspan=2, padx=5, pady=5)

 
       


        """--------STUDENT FUNCTIONS USED--------""" 

# (SAVE) to save the existing data
    def Save_student(self):
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        try:
            C = connec.cursor()
         
        # //get data from each text entries
            student_IDno_input = self.idText.get('1.0', tk.END).strip()
            student_name_input = self.nameText.get('1.0', tk.END).strip()
            student_gender_input = self.genderText.get('1.0', tk.END).strip()
            student_yearlvl_input = self.yearLevelChoice.get()
            #student_coursecode_input = self.courseCodeText.get('1.0', tk.END).strip()
            student_coursecode_input = self.courseChoice.get()

            
        # //checks if any text entry is empty, except for course code entry
            if not all([student_name_input, student_IDno_input, student_gender_input]):
                mb.showerror("Error!", "Please fill in all text entries before saving.")
                return
            
            #//insert data into database
            sv_query = "INSERT INTO student(ID_number, student_name, gender, year_lvl, course_code) VALUES(%s,%s,%s,%s,%s)"
            values = (student_IDno_input, student_name_input, student_gender_input, student_yearlvl_input, student_coursecode_input)
            C.execute(sv_query, values)
            connec.commit()

            #//insert data into treeview
            self.tree.insert("", "end", text="", values=(student_IDno_input, student_name_input, student_gender_input, student_yearlvl_input, student_coursecode_input))

            mb.showinfo("Data Saved", "Data has been saved successfully.")
        except Exception as e:
            mb.showerror("Error!", f"An error has occurred: {e}")
        finally:
            connec.close()        


# (DELETE) selects a student data to delete
    def Delete_student(self):
        select_row_to_Delete = self.stud_tree.selection()

        if select_row_to_Delete:
            del_confirmation = mb.askyesno("You're about to Delete a data", "Are you sure you want to delete this record?")

            if del_confirmation:
                self.Deletion_confirmed_student()
        else:
            mb.showerror("Error!", "Please select a row to delete.")


# performs actual deletion
    def Deletion_confirmed_student(self):
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()

        selected_row_to_Delete = self.stud_tree.selection() # //selects a row from the table
                             
        if selected_row_to_Delete:                                  # //if a row is selected
            select_Item = self.stud_tree.item(selected_row_to_Delete)    # //retrieves data from selected row 
            stud_data = select_Item["values"]                       # //extracts value from the selected data
            stud_IDnumber = stud_data[0]                            #//extracts the ID no.  

            del_query = "DELETE FROM student WHERE ID_number=%s"
            sel_data = (stud_IDnumber,)
            C.execute(del_query, sel_data)
            connec.commit()

            self.stud_tree.delete(selected_row_to_Delete)
            mb.showinfo("Deletion Success", f"Row with ID {stud_IDnumber} was removed from the database.")

        else:
            mb.showerror("Error!", "Please select a row to delete.")



# (UPDATE) selects data to be updated 
    def Select_Student_to_Update(self):
        cur_item = self.stud_tree.focus()
        values = self.stud_tree.item(cur_item, "values")
        print(values)

        # //this checks if row is selected
        if not cur_item:
             mb.showerror("Error!", "Please select a row to edit.")
             return
    
        # //stores the selected index and original data
        self.data_to_be_edited = cur_item[0]
        self.orig_data = self.stud_tree.item(cur_item)["values"] 

        edit_frame = tk.Frame(self.root, width=400, height=320, bg="#D9DDDC", highlightbackground="black", highlightthickness=2) 
        edit_frame.place(x=500, y=345)

        studentIDno_Label = tk.Label(edit_frame, text = "Enter ID number:", bg="#D9DDDC", fg="black")    
        studentIDno_Label.place(x=50, y=30)
        self.IDno_ent = tk.Text(edit_frame, height=1.4, width=25, wrap=tk.NONE)
        self.IDno_ent.place(x=170, y=30)
        self.IDno_ent.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        studentName_Label = tk.Label(edit_frame, text = "Enter Full Name:", bg="#D9DDDC", fg="black")    
        studentName_Label.place(x=50, y=70)
        self.studentName_ent = tk.Text(edit_frame, height=1.4, width=25, wrap=tk.NONE)
        self.studentName_ent.place(x=170, y=70)
        self.studentName_ent.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        studentGender_Label = tk.Label(edit_frame, text = "Enter Gender:", bg="#D9DDDC", fg="black")    
        studentGender_Label.place(x=50, y=110)
        self.studentGender_ent = tk.Text(edit_frame, height=1.4, width=25, wrap=tk.NONE)
        self.studentGender_ent.place(x=170, y=110)
        self.studentGender_ent.bind("<Tab>", lambda event: self.next_entry_widget_is(event))
        
        studentYearlvl_Label = tk.Label(edit_frame, text = "Enter Year Level:", bg="#D9DDDC", fg="black")    
        studentYearlvl_Label.place(x=50, y=150)
        self.yearLevelChoice = ttk.Combobox(edit_frame, height=10, width=30, values=["1st year", "2nd year", "3rd year", "4th year"], state="readonly")
        self.yearLevelChoice.place(x=170, y=150)
        
        studentCourseCode_Label = tk.Label(edit_frame, text = "Enter Course Code:", bg="#D9DDDC", fg="black")    
        studentCourseCode_Label.place(x=50, y=190)
        self.courseChoice = ttk.Combobox(edit_frame, height=10, width=30)
        self.courseChoice.place(x=170, y=190)
        #self.studentCourseCode_ent = tk.Text(edit_frame, height=1.4, width=25, wrap=tk.NONE)
        #self.studentCourseCode_ent.place(x=170, y=190)
        

        self.IDno_ent.insert("1.0", self.orig_data[0])
        self.studentName_ent.insert("1.0", self.orig_data[1])
        self.studentGender_ent.insert("1.0", self.orig_data[2])
        self.yearLevelChoice.set(self.orig_data[3])
        self.courseChoice.set(self.orig_data[4])

        # //update button
        save_Edited_Button = tk.Button(edit_frame, text="Update", command=lambda: self.Update_student(),
                                 font=("Arial", 10, "bold"), bg="#005C29", fg="white")
        save_Edited_Button.place(x=90, y=270)

        # //cancel button
        cancelButton = tk.Button(edit_frame, text="Cancel", command=edit_frame.destroy,
                                 font=("Arial", 11, "italic"), bg="#BA110C", fg="white")                #// make it light green ??
        cancelButton.place(x=230, y=270)


# updates the data 
    def Update_student(self):
        connec = mysql.connect(
        host = "localhost",
        user = "root",
        password = "elijang0011!!",
        database = "sql_ssis"
        )

        C = connec.cursor()

        # //retrieves the original ID number from the treeview
        old_id_text = self.stud_tree.item(self.stud_tree.focus(),"values")[0]

        id_text = self.IDno_ent.get("1.0", tk.END).strip()
        name_text = self.studentName_ent.get("1.0" ,tk.END).strip()
        gender_text = self.studentGender_ent.get("1.0" ,tk.END).strip()
        yearlvl_text = self.yearLevelChoice.get()
        courseCode_text = self.courseChoice.get()

        C.execute("UPDATE student SET ID_number=%s, student_name=%s, gender=%s, year_lvl=%s, course_code=%s WHERE ID_number=%s",
                (id_text, name_text, gender_text, yearlvl_text, courseCode_text, old_id_text))
            
        connec.commit()
        mb.showinfo("Successfully Edited", "Item edited and saved.")
        
        # //updates all the new data in the treeview
        self.stud_tree.item(self.stud_tree.focus(), values=(id_text, name_text, gender_text, yearlvl_text, courseCode_text))

        self.idText.delete("1.0", tk.END)
        self.nameText.delete("1.0", tk.END)
        self.genderText.delete("1.0", tk.END)
        self.yearLevelChoice.set(self.orig_data[3])
        self.courseChoice.set(self.orig_data[4])

        connec.close()

       
# (SEARCH) called when search button is clicked
    def Search_student(self):
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()

        # //get search entry from entry widget
        what_to_search = self.searchStudentText.get().strip()

        # //clearing existing items in Treeview
        for item in self.stud_tree.get_children():
            self.stud_tree.delete(item)

        # //execute query to fetch student data by their ID no.
        s_query = ("SELECT * FROM student WHERE ID_number = %s")
        C.execute(s_query, (what_to_search,))
        result = C.fetchall()

        #//update treeview with the fetched data
        for row in result:
            self.stud_tree.insert("", "end", values=row)

        # //display message if no data is matched from search entry
        if not result:
            mb.showinfo("No Results", "No matching records found.")

        connec.close()


# opens data in student treeview
    def Open_student(self): 
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()

        # //clear existing items/data in the treeview
        for item in self.stud_tree.get_children():
            self.stud_tree.delete(item)

        #//execute query to fetch all student data
        o_query = ("SELECT * FROM student")
        C.execute(o_query)
        result = C.fetchall()

         #//update treeview with the fetched data
        for row in result:
            self.stud_tree.insert("", "end", values=row)

        connec.close()




    """--------COURSE FUNCTIONS USED--------""" 
# (ADD)
    def Add_course(self):
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()

        course_code = sd.askstring("Add Course Code", "Enter Course Code: ") 
        if not course_code:
            mb.showerror("Error!", "Course code is required.")
            return

        course_name = sd.askstring("Add Course Name", "Enter Course Name: ")
        if not course_name:
            mb.showerror("Error!", "Course name is required.")
            return
    
        
        ins_query = "INSERT INTO course (course_code, course_name) VALUES (%s, %s)"
        C.execute(ins_query, (course_code, course_code))
        connec.commit()

        connec.close()


# (DELETE) selects a student data to delete
    def Delete_course(self):
        select_row_to_Delete = self.course_tree.selection()

        if select_row_to_Delete:
            del_confirmation = mb.askyesno("You're about to Delete a Course", "Are you sure you want to delete this Course?")

            if del_confirmation:
                self.Deletion_confirmed_course()
        else:
            mb.showerror("Error!", "Please select a row to delete.")


# performs actual deletion
    def Deletion_confirmed_course(self):
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()

        selected_row_to_Delete = self.course_tree.selection() # //selects a row from the table
                             
        if selected_row_to_Delete:                                      # //if a row is selected
            select_Item = self.course_tree.item(selected_row_to_Delete)  # //retrieves data from selected row 
            course_data = select_Item["values"]                         # //extracts value from the selected data
            courseCod = course_data[0]                                  #//extracts the ID no.  

            del_query = "DELETE FROM course WHERE course_code=%s"
            sel_data = (courseCod,)
            C.execute(del_query, sel_data)
            connec.commit()

            self.course_tree.delete(selected_row_to_Delete)
            mb.showinfo("Deletion Success", f"Course {courseCod} has been removed from course selections.")

        else:
            mb.showerror("Error!", "Please select a row to delete.")


# (UPDATE) selects course to be updated 
    def Select_Course_to_Update(self):
        cur_item = self.course_tree.focus()
        values = self.course_tree.item(cur_item, "values")
        print(values)

        # //this checks if row is selected
        if not cur_item:
             mb.showerror("Error!", "Please select a row to edit.")
             return
    
        # //stores the selected index and original data
        self.data_to_be_edited = cur_item[0]
        self.orig_data = self.course_tree.item(cur_item)["values"] 

        edit_frame = tk.Frame(self.root, width=400, height=320, bg="#D9DDDC", highlightbackground="black", highlightthickness=2) 
        edit_frame.place(x=500, y=345)

        courseCod_Label = tk.Label(edit_frame, text = "Enter new Course Code:", bg="#D9DDDC", fg="black")    
        courseCod_Label.place(x=50, y=30)
        self.courseCod_ent = tk.Text(edit_frame, height=1.4, width=25, wrap=tk.NONE)
        self.courseCod_ent.place(x=170, y=30)
        self.courseCod_ent.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        courseName_Label = tk.Label(edit_frame, text = "Enter new Course Name:", bg="#D9DDDC", fg="black")    
        courseName_Label.place(x=50, y=70)
        self.courseName_ent = tk.Text(edit_frame, height=1.4, width=25, wrap=tk.NONE)
        self.courseName_ent.place(x=170, y=70)
        self.courseName_ent.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        self.courseCod_ent.insert("1.0", self.orig_data[0])
        self.courseName_ent.insert("1.0", self.orig_data[1])
        
        # //update button
        save_Edited_Button = tk.Button(edit_frame, text="Update", command=lambda: self.Update_course(),
                                 font=("Arial", 10, "bold"), bg="#005C29", fg="white")
        save_Edited_Button.place(x=90, y=270)

        # //cancel button
        cancelButton = tk.Button(edit_frame, text="Cancel", command=edit_frame.destroy,
                                 font=("Arial", 11, "italic"), bg="#BA110C", fg="white")               
        cancelButton.place(x=230, y=270)


# updates the data 
    def Update_course(self):
        connec = mysql.connect(
        host = "localhost",
        user = "root",
        password = "elijang0011!!",
        database = "sql_ssis"
        )
        C = connec.cursor()
        
        # //retrieves the original ID number from the treeview
        old_course_code = self.course_tree.item(self.course_tree.focus(),"values")[0]

        c_Code_text = self.courseCod_ent.get("1.0", tk.END).strip()
        c_Name_text = self.courseName_ent.get("1.0" ,tk.END).strip()
        

        C.execute("UPDATE course SET course_code=%s, course_name=%s WHERE course_code=%s",
                (c_Code_text, c_Name_text, old_course_code))
            
        connec.commit()
        mb.showinfo("Successfully Edited", "New Course is saved and edited.")
        
        # //updates all the new data in the treeview
        self.course_tree.item(self.course_tree.focus(), values=(c_Code_text, c_Name_text, old_course_code))

        self.c_Code_text.delete("1.0", tk.END)
        self.c_Name_text.delete("1.0", tk.END)
        
        connec.close()


#(SEARCH)
    def Search_course(self):
        connec = mysql.connect(
        host = "localhost",
        user = "root",
        password = "elijang0011!!",
        database = "sql_ssis"
        )

        C = connec.cursor()

        # //get search entry from entry widget
        what_to_search = self.searchCourse.get().strip()            # //name sa text widget

        # //clearing existing items in Treeview
        for item in self.course_tree.get_children():
            self.course_tree.delete(item)

        # //execute query to fetch student data by their ID no.
        s_query = ("SELECT * FROM course WHERE course_code = %s")
        C.execute(s_query, (what_to_search,))
        result = C.fetchall()

        #//update treeview with the fetched data
        for row in result:
            self.course_tree.insert("", "end", values=row)

        # //display message if no data is matched from search entry
        if not result:
            mb.showinfo("No Results", "No matching records found.")

        connec.close()


# opens data in course treeview
    def Open_course(self): 
        connec = mysql.connect(
            host = "localhost",
            user = "root",
            password = "elijang0011!!",
            database = "sql_ssis"
        )

        C = connec.cursor()

        # //clear existing items/data in the treeview
        for item in self.course_tree.get_children():
            self.course_tree.delete(item)

        #//execute query to fetch all student data
        o_query = ("SELECT * FROM course")
        C.execute(o_query)
        result = C.fetchall()

         #//update treeview with the fetched data
        for row in result:
            self.course_tree.insert("", "end", values=row)

        connec.close()



    """--------UI FUNCTIONS USED--------""" 
# focuses on the next entry widget as "tab" key is pressed
    def next_entry_widget_is(self,event):
        event.widget.tk_focusNext().focus()
        return 'break'
    

# function called when input data needs to be cleared from all the text widgets
    def clearInputData(self):
        # //clears text in each text entry widget
        self.idText.delete("1.0", tk.END)
        self.nameText.delete("1.0", tk.END)
        self.genderText.delete("1.0", tk.END)
        self.courseCodeText.delete("1.0", tk.END)   


# adjusts column width dynamically
    def adjustColumnWidths(self):
        for col in self.tree["columns"]:
            self.tree.column(col, width=200, anchor="w")
            self.tree.column("#0", width=3, anchor="w")


if __name__ == "__main__":
    root = tk.Tk()
    app = SSISApp(root)
    root.mainloop()
    
