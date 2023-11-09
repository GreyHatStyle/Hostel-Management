import tkinter as tk
from tkinter import ttk
import Extras
import baseData
from tkinter import messagebox


def back_button(frame, x, y):
    back = tk.Button(frame, text="Back", font='timesnewroman 20 bold', bg='light green', width=10,
                     command=frame.destroy)
    back.place(x=x, y=y)


def Update_data_frame():
    frame = tk.Frame(root, bg='#B5FF42')
    frame.place(x=0, y=0, width=1000, height=750)

    # global up_room_no, up_name, up_college, up_ph_no, up_father, up_fath_no
    up_room_no = tk.BooleanVar()
    up_name = tk.IntVar()
    up_college = tk.IntVar()
    up_ph_no = tk.IntVar()
    up_father = tk.IntVar()
    up_fath_no = tk.IntVar()
    up_delete = tk.IntVar()

    def search_click():
        try:
            s = textbox.get()
            room_char = s[0]
            root_num = (s[2::])
            ComboBoxGo(room_char, root_num)
            name_label = tk.Label(frame1, text="Select Name", font='comicsans 20 bold', bg='#D1FF88')
            name_label.place(x=55, y=200)
        except:
            messagebox.showerror("Not Found!", "Please Write room number like this: A-101")

    def go_button_frame():
        name = combo_box_up.get()
        if up_delete.get() == 1:
            ans = messagebox.askquestion(f"Are you sure to Delete {name}'s Data?",
                                      f"If you delete {name}'s data it will be irrecoverable and lost. ")

            if ans == "yes":
                baseData.Delete_data(name)
                messagebox.showinfo(f"Deleted Successfully!", f"Data of {name} has been deleted successfully")
                frame.destroy()
            else:
                messagebox.showinfo(f"Deletion Canceled!", "Deletion process in canceled")
                # frame.destroy()

        info_frame = tk.Frame(frame, highlightbackground="black", highlightthickness=1, width=660, height=655, bg='#D1FF88')
        info_frame.place(x=320, y=18)

        details = tk.Label(info_frame, text=f"Enter The Details", font='comicsans 30 bold', bg='#D1FF88')
        details.place(x=160, y=70)

        name = tk.Label(info_frame, text=f"Student Name: ", font='comicsans 20 bold', bg='#D1FF88')
        name.place(x=30, y=160)
        name_inp_go = tk.Entry(info_frame, font='comcicsans 20 bold', width=15, state="disabled")
        name_inp_go.place(x=370, y=160)

        c = tk.Label(info_frame, text=f"College :", font='comicsans 20 bold', bg='#D1FF88')
        c.place(x=30, y=220)
        c_list = ["GEHU", "GEU", ""]
        c_inp_go = ttk.Combobox(info_frame, value=c_list, font='timesnewroman 15 bold', width=19, state="disabled")
        c_inp_go.current(len(c_list) - 1)
        c_inp_go.place(x=370, y=220)

        n = tk.Label(info_frame, text=f"Phone Number :", font='comicsans 20 bold', bg='#D1FF88')
        n.place(x=30, y=280)
        n_inp_go = tk.Entry(info_frame, font='comcicsans 20 bold', width=15, state="disabled")
        n_inp_go.place(x=370, y=280)

        f = tk.Label(info_frame, text=f"Father Name :", font='comicsans 20 bold', bg='#D1FF88')
        f.place(x=30, y=340)
        f_inp_go = tk.Entry(info_frame, font='comcicsans 20 bold', width=15, state="disabled")
        f_inp_go.place(x=370, y=340)

        fn = tk.Label(info_frame, text=f"Father Phone Number :", font='comicsans 20 bold', bg='#D1FF88')
        fn.place(x=30, y=400)
        fn_inp_go = tk.Entry(info_frame, font='comcicsans 20 bold', width=15, state="disabled")
        fn_inp_go.place(x=370, y=400)

        rm = tk.Label(info_frame, text=f"Room No (A-101) format :", font='comicsans 20 bold', bg='#D1FF88')
        rm.place(x=30, y=460)
        rm_inp_go = tk.Entry(info_frame, font='comcicsans 20 bold', width=15, state="disabled")
        rm_inp_go.place(x=370, y=460)
        print("uproom number: ",up_room_no)

        if up_room_no.get() == 1:
            rm_inp_go.config(state=tk.NORMAL)

        if up_name.get() == 1:
            name_inp_go.config(state=tk.NORMAL)

        if up_college.get() == 1:
            c_inp_go.config(state=tk.NORMAL)
        if up_ph_no.get() == 1:
            n_inp_go.config(state=tk.NORMAL)
        if up_father.get() == 1:
            f_inp_go.config(state=tk.NORMAL)
        if up_fath_no.get() == 1:
            fn_inp_go.config(state=tk.NORMAL)

        def update_data():

            try:
                s_name = name_inp_go.get()
                room_no = rm_inp_go.get()
                college = c_inp_go.get()
                number = n_inp_go.get()
                f_name = f_inp_go.get()
                f_no = fn_inp_go.get()

                number_room = ""
                block_room = ""

                if room_no != "":
                    number_room = room_no[2::]
                    block_room = room_no[0]

                combo_name = combo_box_up.get() #printable
                dct = {"Name":s_name, "Block":block_room, "Room": number_room, "College":college, "Phone":number,
                       "Father_n":f_name, "Father_no":f_no}
                baseData.Data_Updater(combo_name, dct)
                messagebox.showinfo("Done!", f"The data of {s_name} is Updated!")
            except Exception as e:
                print(e)
                messagebox.showerror("Error!", "Kindly fill Selected blocks")

        def verify_data():
            combo_name = combo_box_up.get()
            lst = baseData.Data_of_Name(combo_name)
            Extras.Information_Provide(lst)

        update_button = tk.Button(info_frame, text="Update", font='timesnewroman 15 bold', bg='Orange', width=15,
                               command=update_data, state=tk.DISABLED)
        update_button.place(x=340, y=540)

        verify_button = tk.Button(info_frame, text="Verify", font='timesnewroman 15 bold', bg='Orange', width=15,
                                  command=verify_data)
        verify_button.place(x=100, y=540)

        if up_room_no.get() == 1:
            update_button.config(state=tk.NORMAL)

        if up_name.get() == 1:
            update_button.config(state=tk.NORMAL)

        if up_college.get() == 1:
            update_button.config(state=tk.NORMAL)
        if up_ph_no.get() == 1:
            update_button.config(state=tk.NORMAL)
        if up_father.get() == 1:
            update_button.config(state=tk.NORMAL)
        if up_fath_no.get() == 1:
            update_button.config(state=tk.NORMAL)

    def set_click():

        def for_delete_check():
            c_delete.deselect()

        up_label = tk.Label(frame1, text="Select To Update", font='comicsans 20 bold', bg='#D1FF88')
        up_label.place(x=35, y=350)

        c_room_no = tk.Checkbutton(frame1, text="Room No.", variable=up_room_no, font="comicsans 15 bold", bg='#D1FF88',
                                   onvalue=1, offvalue=0, command=for_delete_check)
        c_room_no.place(x=40, y=390)

        c_name = tk.Checkbutton(frame1, text="Name", variable=up_name, font="comicsans 15 bold", bg='#D1FF88'
                                , command=for_delete_check)
        c_name.place(x=40, y=420)

        c_college = tk.Checkbutton(frame1, text="College", variable=up_college, font="comicsans 15 bold", bg='#D1FF88'
                                   , command=for_delete_check)
        c_college.place(x=40, y=450)

        c_ph_no = tk.Checkbutton(frame1, text="Phone Number", variable=up_ph_no, font="comicsans 15 bold", bg='#D1FF88'
                                 , command=for_delete_check)
        c_ph_no.place(x=40, y=480)

        c_father = tk.Checkbutton(frame1, text="Father Name", variable=up_father, font="comicsans 15 bold", bg='#D1FF88'
                                  , command=for_delete_check)
        c_father.place(x=40, y=510)

        c_fath_no = tk.Checkbutton(frame1, text="Father No", variable=up_fath_no, font="comicsans 15 bold", bg='#D1FF88'
                                   , command=for_delete_check)
        c_fath_no.place(x=40, y=540)

        def del_select():
            c_room_no.deselect()
            c_name.deselect()
            c_ph_no.deselect()
            c_fath_no.deselect()
            c_college.deselect()
            c_father.deselect()

        global c_delete
        c_delete = tk.Checkbutton(frame1, text="Delete Data", font="comicsans 15 bold", variable=up_delete,
                                   bg='#D1FF88', command=del_select)
        c_delete.place(x=40, y=570)

        go_button = tk.Button(frame1, text="Go", font='timesnewroman 14 bold', bg='#10CC00', width=10,
                                  command=go_button_frame)
        go_button.place(x=75, y=610)

    # INPUT FRAME--------------------------------------

    # Take input

    frame1 = tk.Frame(frame, highlightbackground="black", highlightthickness=1, width=300, height=655, bg='#D1FF88')
    frame1.place(x=10, y=19)

    room_label = tk.Label(frame1, text="Room number", font='comicsans 20 bold', bg='#D1FF88')
    room_label.place(x=45, y=30)

    textbox = tk.Entry(frame1, font='comcicsans 20 bold', width=15)
    textbox.place(x=30, y=80)

    set_button = tk.Button(frame1, text="Search", font='timesnewroman 15 bold', bg='#05F9C8', command=search_click, width=10)
    set_button.place(x=75, y=130)

    # ComboBOX
    def ComboBoxGo(room_char, room_num):

        global combo_box_up
        demo_list = baseData.Room_Members(room_char, room_num)
        combo_box_up = ttk.Combobox(frame1, value=demo_list, font='timesnewroman 15 bold')
        combo_box_up.current(len(demo_list) - 1)
        # combo_box.bind("<<ComboboxSelected>>", combo_click)
        combo_box_up.place(x=30, y=240)

        # Show Button
        setter_button = tk.Button(frame1, text="Set", font='timesnewroman 15 bold', bg='#47F34B', width=10,
                                command=set_click)
        setter_button.place(x=75, y=280)

    back_button(frame, 400, 680)


def Add_Student_frame():
    frame = tk.Frame(root)
    frame.place(x=0, y=0, width=1000, height=750)
    demo_list = Extras.Only_room_sender()
    if len(demo_list) == 0:
        messagebox.showinfo('Info', "ALL rooms are filled, Please delete some data to add!")
        frame.destroy()

    frame1 = tk.Frame(frame, highlightbackground="black", highlightthickness=1, width=300, height=655)
    frame1.place(x=10, y=19)

    room_label = tk.Label(frame1, text="Room numbers", font='comicsans 20 bold')
    room_label.place(x=45, y=230)

    combo_box1 = ttk.Combobox(frame1, value=demo_list, font='timesnewroman 15 bold')
    combo_box1.current(len(demo_list) - 1)
    # combo_box.bind("<<ComboboxSelected>>", combo_click)
    combo_box1.place(x=30, y=290)

    def go_click():
        info_frame = tk.Frame(frame, highlightbackground="black", highlightthickness=1, width=660, height=655)
        info_frame.place(x=320, y=18)

        details = tk.Label(info_frame, text=f"Enter The Details", font='comicsans 30 bold')
        details.place(x=160, y=70)

        name = tk.Label(info_frame, text=f"Student Name: ", font='comicsans 20 bold')
        name.place(x=30, y=160)
        name_inp = tk.Entry(info_frame, font='comcicsans 20 bold', width=15)
        name_inp.place(x=370, y=160)

        c = tk.Label(info_frame, text=f"College :", font='comicsans 20 bold')
        c.place(x=30, y=220)
        c_list = ["GEHU", "GEU"]
        c_inp = ttk.Combobox(info_frame, value=c_list, font='timesnewroman 15 bold', width=19)
        c_inp.current(len(c_list) - 1)
        c_inp.place(x=370, y=220)

        n = tk.Label(info_frame, text=f"Phone Number :", font='comicsans 20 bold')
        n.place(x=30, y=280)
        n_inp = tk.Entry(info_frame, font='comcicsans 20 bold', width=15)
        n_inp.place(x=370, y=280)

        f = tk.Label(info_frame, text=f"Father Name :", font='comicsans 20 bold')
        f.place(x=30, y=340)
        f_inp = tk.Entry(info_frame, font='comcicsans 20 bold', width=15)
        f_inp.place(x=370, y=340)

        fn = tk.Label(info_frame, text=f"Father Phone Number :", font='comicsans 20 bold')
        fn.place(x=30, y=400)
        fn_inp = tk.Entry(info_frame, font='comcicsans 20 bold', width=15)
        fn_inp.place(x=370, y=400)

        def Add_data():
            try:
                s_name = name_inp.get()
                block_num = combo_box1.get()
                college = c_inp.get()
                number = n_inp.get()
                f_name = f_inp.get()
                f_no = fn_inp.get()
                lst = [s_name, block_num, college, number, f_name, f_no]
                flag = True
                for i in lst:
                    if i == "":
                        flag = False

                if flag:
                    baseData.Add_data_Student(block_num, s_name, college, number, f_name, f_no)
                    messagebox.showinfo("Done!", f"The data of {s_name} in room {block_num} has been added!")
                else:
                    messagebox.showerror("Error!", "Please Fill all the fields")
            except Exception as e:
                print(e)
                messagebox.showerror("Error!", "Kindly fill all the fields")

        add_button = tk.Button(info_frame, text="ADD", font='timesnewroman 15 bold', bg='Orange', width=15,
                               command=Add_data)
        add_button.place(x=230, y=500)

    # Go Button
    go_button = tk.Button(frame1, text="Go", font='timesnewroman 15 bold', bg='light blue', width=15, command=go_click)
    go_button.place(x=55, y=345)
    back_button(frame, 400, 680)


def view_student_frame():
    frame = tk.Frame(root, bg='#00E3F3')
    frame.place(x=0, y=0, width=1000, height=750)

    def set_click():
        try:
            s = textbox.get()
            room_char = s[0]
            root_num = (s[2::])
            ComboBoxShow(room_char, root_num)
            name_label = tk.Label(frame1, text="Select Name", font='comicsans 20 bold', bg='#9CF8FF')
            name_label.place(x=45, y=380)
        except:
            messagebox.showerror("Not Found!", "Please Write room number like this: A-101")

    def show_click():
        text = combo_box.get()
        data_set = baseData.Data_of_Name(text)
        block = data_set[0][0]
        room = data_set[0][1]
        college = data_set[0][3]
        number = data_set[0][4]
        f_name = data_set[0][5]
        f_no = data_set[0][6]
        print(f"Opening data of {text}...")
        # Make function to get frame data
        s_name = text
        info_frame = tk.Frame(frame, highlightbackground="black", highlightthickness=1, width=675, height=655, bg='#9CF8FF')
        info_frame.place(x=320, y=18)

        name = tk.Label(info_frame, text=f"Student Name:  {s_name}", font='comicsans 20 bold', bg='#9CF8FF')
        name.place(x=40, y=70)

        b = tk.Label(info_frame, text=f"Room Number:  {block} - {room}", font='comicsans 20 bold', bg='#9CF8FF')
        b.place(x=40, y=130)

        c = tk.Label(info_frame, text=f"College :  {college}", font='comicsans 20 bold', bg='#9CF8FF')
        c.place(x=40, y=190)

        n = tk.Label(info_frame, text=f"Phone Number :  {number}", font='comicsans 20 bold', bg='#9CF8FF')
        n.place(x=40, y=250)

        f = tk.Label(info_frame, text=f"Father Name :  {f_name}", font='comicsans 20 bold', bg='#9CF8FF')
        f.place(x=40, y=310)

        fn = tk.Label(info_frame, text=f"Father Phone Number :  {f_no}", font='comicsans 20 bold', bg='#9CF8FF')
        fn.place(x=40, y=370)

    # INPUT FRAME--------------------------------------

    # Take input

    frame1 = tk.Frame(frame, highlightbackground="black", highlightthickness=1, width=300, height=655, bg='#9CF8FF')
    frame1.place(x=10, y=19)

    room_label = tk.Label(frame1, text="Room number", font='comicsans 20 bold', bg='#9CF8FF')
    room_label.place(x=45, y=30)

    textbox = tk.Entry(frame1, font='comcicsans 20 bold', width=15)
    textbox.place(x=30, y=80)

    set_button = tk.Button(frame1, text="Set", font='timesnewroman 15 bold', command=set_click, width=10,
                           bg='#2DA3DD')
    set_button.place(x=75, y=130)

    # ComboBOX
    def ComboBoxShow(room_char, room_num):
        global combo_box

        demo_list = baseData.Room_Members(room_char, room_num)
        combo_box = ttk.Combobox(frame1, value=demo_list, font='timesnewroman 15 bold')
        combo_box.current(len(demo_list) - 1)
        # combo_box.bind("<<ComboboxSelected>>", combo_click)
        combo_box.place(x=40, y=440)

        # Show Button
        show_button = tk.Button(frame1, text="Show", font='timesnewroman 15 bold', width=15, bg='#2DA3DD',
                                command=show_click)
        show_button.place(x=45, y=500)

    back_button(frame, 400, 680)


# ROOT FRAMES ---------------------------------------------------------------------------------------------------------

def plumber_frame():
    frame = tk.LabelFrame(root, text="Plumber", padx=20, pady=20)
    frame.place(x=250, y=110)

    labelC = tk.Label(frame, text='            Plumber           ', font='comicsans 15 bold')
    labelC.pack()

    box = tk.Listbox(frame, font='comicsans 20 ', width=20, height=5)
    box.pack()

    delete = tk.Button(frame, text="  Delete  ", font='timesnewroman 15 bold', bg='orange', command=None)
    delete.pack(side=tk.LEFT)

    deleteAll = tk.Button(frame, text="Delete ALL", font='timesnewroman 15 bold', bg='red', command=None)
    deleteAll.pack(side=tk.RIGHT)


def carpenter_frame():
    frame = tk.LabelFrame(root, text="Carpenter", padx=20, pady=20)
    frame.place(x=610, y=110)

    labelC = tk.Label(frame, text='            Carpenter           ', font='comicsans 15 bold')
    labelC.pack()

    box = tk.Listbox(frame, font='comicsans 20 ', width=20, height=5)
    box.pack()

    delete = tk.Button(frame, text="  Delete  ", font='timesnewroman 15 bold', bg='orange', command=None)
    delete.pack(side=tk.LEFT, padx=10)

    deleteAll = tk.Button(frame, text="Delete ALL", font='timesnewroman 15 bold', bg='red', command=None)
    deleteAll.pack(side=tk.RIGHT)


def electrician_frame():
    frame = tk.LabelFrame(root, text="Electrician", padx=20, pady=20)
    frame.place(x=250, y=410)

    labelC = tk.Label(frame, text='            Electrician           ', font='comicsans 15 bold')
    labelC.pack()

    box = tk.Listbox(frame, font='comicsans 20 ', width=20, height=5)
    box.pack()

    delete = tk.Button(frame, text="  Delete  ", font='timesnewroman 15 bold', bg='orange', command=None)
    delete.pack(side=tk.LEFT)

    deleteAll = tk.Button(frame, text="Delete ALL", font='timesnewroman 15 bold', bg='red', command=None)
    deleteAll.pack(side=tk.RIGHT)


def others_complains():
    frame = tk.LabelFrame(root, text="other complains", padx=20, pady=20)
    frame.place(x=610, y=410)

    labelC = tk.Label(frame, text='        Other Complains      ', font='comicsans 15 bold')
    labelC.pack()

    box = tk.Listbox(frame, font='comicsans 20 ', width=20, height=5)
    box.pack()

    delete = tk.Button(frame, text="  Delete  ", font='timesnewroman 15 bold', bg='orange', command=None)
    delete.pack(side=tk.LEFT)

    deleteAll = tk.Button(frame, text="Delete ALL", font='timesnewroman 15 bold', bg='red', command=None)
    deleteAll.pack(side=tk.RIGHT)


# --------------------------------------------------------------------------------------------------------------------
def head_gui():
    global root
    root = tk.Tk()
    root.title("Welcome")
    root.geometry("1000x750+250+20")

    root.resizable(False, False)

    # FRAME 1
    frame = tk.LabelFrame(root, text="-", padx=20, pady=20)
    frame.place(x=10, y=10)

    # BUTTONS OF FRAME 1
    View_student = tk.Button(frame, text="View\nStudent", font='timesnewroman 20 bold', bg='light blue', width=9,
                             command=view_student_frame)
    View_student.pack(pady=20)

    Add_student = tk.Button(frame, text="Add\nStudent ", font='timesnewroman 20 bold', bg='light blue', width=9,
                            command=Add_Student_frame)
    Add_student.pack(pady=20)

    Empty_room = tk.Button(frame, text="Empty\nRoom", font='timesnewroman 20 bold', bg='light blue', width=9,
                           command=Extras.RoomData)
    Empty_room.pack(pady=20)

    Search_Button = tk.Button(frame, text="Update\ndata", font='timesnewroman 20 bold', bg='light blue', width=9,
                              command=Update_data_frame)
    Search_Button.pack(pady=20)

    Search_Button = tk.Button(frame, text="Verify\nComplains", font='timesnewroman 20 bold', bg='light blue', width=9,
                              command=None)
    Search_Button.pack(pady=20)

    # FRAME 2
    frame2 = tk.LabelFrame(root, text="-", padx=20, pady=20)
    frame2.place(x=250, y=10)

    labelC = tk.Label(frame2, text='\t\tTodays Complains\t         ', font='comicsans 20 bold')
    labelC.grid(row=0, column=0)

    # FRAME PLUMBER
    plumber_frame()
    carpenter_frame()
    electrician_frame()
    others_complains()
    # Run the main event loop
    root.mainloop()


head_gui()
