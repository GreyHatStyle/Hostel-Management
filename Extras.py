from tkinter import messagebox
import baseData


def RoomData():
    lst = baseData.Block_check()
    s = "Empty Room and Number of seats Available: \n\n"

    if len(lst) == 0:
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

# Telegram Functions


def Give_List_of_Complains(name: str) -> list:
    f = open(f"Data\\{name}.txt", "r")
    ans = []
    lst = list(f.read().split('\n'))
    lst2 = list(lst[0].split(','))

    for data in lst:
        l = list(data.split(','))
        try:
            ans.append(l[1])
        except Exception as e:
            print(f"[Exception during list creation ]: {e}")

    return ans



def check_Message(lst: list, date) -> bool:
    dr_lst = ['plumber', 'carpenter', 'electrician', 'others']
    if lst[1].lower() in dr_lst:

        f = open(f"Data\\{lst[1].lower()}.txt", "a")
        lst.insert(0, date)

        for s in lst:
            f.write(f"{s}, ")

        f.write("\n")
        f.close()
        return True
    else:
        return False


def Give_List_of_Others() -> list:
    f = open(f"Data\\others.txt", "r")
    ans = []
    lst = list(f.read().split('\n'))

    for data in lst:
        try:
            l = list(data.split(','))
            t = []
            t.append(l[1])
            t.append(l[3])
            t.append(l[4])
            ans.append(t)
        except:
            pass

    return ans

