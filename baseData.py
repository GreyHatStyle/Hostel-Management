import psycopg2
import random
import Extras
# ------------ Functions----------------------------------------

# Returns list of information of empty rooms and how many O(n)
def Block_check():
    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="Manas@123",
                            port=5432)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "HostelData"; ''')
    data = cur.fetchall()
    cur.execute('''SELECT "s_no" FROM "HostelData"''')
    num_data = cur.fetchall()

    final_list = []
    NoRoom = {
        "A101": 0,
        "A102": 0,
        "A103": 0,
        "A104": 0,
        "A201": 0,
        "A202": 0,
        "A203": 0,
        "A204": 0,
        "B101": 0,
        "B102": 0,
        "B103": 0,
        "B104": 0,
        "B201": 0,
        "B202": 0,
        "B203": 0,
        "B204": 0,
    }

    for sets in data:
        s = sets[0]
        i = sets[1]
        a = s + str(i)

        NoRoom[a] += 1

    for key in NoRoom:
        if NoRoom[key] < 3:
            c = 3 - NoRoom[key]
            final_list.append([key, c])

    conn.commit()
    cur.close()
    conn.close()

    return final_list


def Room_Members(room_char, room_num):
    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="Manas@123",
                            port=5432)
    cur = conn.cursor()
    cur.execute(f'''SELECT "Name" FROM "HostelData" WHERE "Block" = '{room_char}' and "Room"='{room_num}'; ''')
    data = cur.fetchall()
    lst_names = []
    for i in data:
        lst_names.append(i[0])

    conn.commit()
    cur.close()
    conn.close()

    return lst_names


def Data_of_Name(s_name):
    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="Manas@123",
                            port=5432)
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM "HostelData" WHERE "Name"='{s_name}'; ''')
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    return data


def Add_data_Student(room_block, name, college, phone, father, father_ph):
    room_char = room_block[0]
    room_num = (room_block[1::])
    i = random.randint(50, 10000)

    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="Manas@123",
                            port=5432)
    cur = conn.cursor()
    cur.execute(f'''
INSERT INTO "HostelData" (
    "Block",
    "Room",
    "Name",
    "College",
    "Phone",
    "Father_n",
    "Father_no",
    "s_no"
)
VALUES
    ('{room_char}', {room_num}, '{name}', '{college}', '{phone}', '{father}', '{father_ph}', {i});''')

    conn.commit()
    cur.close()
    conn.close()


def Data_Updater(name, dct):
    s = Extras.Update_string_provider(dct)
    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="Manas@123",
                            port=5432)
    cur = conn.cursor()
    cur.execute(f'''UPDATE "HostelData" SET {s} WHERE "Name" = '{name}' ;''')
    conn.commit()
    cur.close()
    conn.close()
    print(s)
