from tkinter import messagebox
import baseData


def RoomData():
    lst = baseData.Block_check()
    s = "Empty Room and Number of seats Available: \n\n"

    if len(lst)==0:
        messagebox.showinfo('Information', 'All rooms are filled!')
        return
    count = 1
    for i in lst:
        s += f"{count}.   "
        s += str(i[0])
        s += "  -  "
        s += str(i[1])
        s += " seats"
        s += " \n"
        count += 1

    messagebox.showinfo('Information', s)


def Only_room_sender():
    lst = baseData.Block_check()
    data = []
    for i in lst:
        data.append(i[0])

    return data


def Update_string_provider(dct):
    s = ""
    c = 0
    for key in dct:
        if dct[key] == "":
            continue
        if dct[key] != "" and c == 0:
            c += 1
            s += f""""{key}" = '{dct[key]}'"""
            continue

        if c > 0:
            s += f""", "{key}" = '{dct[key]}'"""

    return s


def Information_Provide(lst):
    s = ""
    s += f"Name : {lst[0][2]}\nRoom Number: {lst[0][0]}-{lst[0][1]}\nPhone Number: {lst[0][4]}\nCollege: {lst[0][3]}\n"
    s += f"Father Name: {lst[0][5]}\nFather Number: {lst[0][6]}"

    messagebox.showinfo(f"Data of {lst[0][2]}", s)
