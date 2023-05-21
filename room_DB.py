import sqlite3
import re
conn=sqlite3.connect("room_allocations.sqlite") # creating a database with the name in quotes
cur=conn.cursor()
# creating tables for the three hostel buildings
cur.execute('''CREATE TABLE Baby(room_ID int, room_floor text, mate_1 text, mate_2 text, mate_3 text, mate_4 text, indexing)''')
cur.execute('''CREATE TABLE Complex(room_ID int, room_floor text, mate_1 text, mate_2 text, mate_3 text, mate_4 text, indexing)''')
cur.execute('''CREATE TABLE New_Brunei(room_ID int, room_floor text, mate_1 text, mate_2 text, mate_3 text, mate_4 text, indexing)''')

# openning the text file
fh=open("list_text.txt")
# dic={}
count=0
total=0
lst=[]
for data in fh:
    data=data.replace("\n","")
    data=data.strip()
    if len(data)<1:
        continue
    if data == "course":
        break
    count+=1
    calc=count%6
    if calc in [3,4,5]: # name[0], room_ID[1], Building[2]
        lst.append(data)
        if len(lst)==3:
            # dic[lst[1]]=dic.get(lst[1], 0)+1
            if lst[2].upper() == "BABY":
                r=lst[1]
                m=lst[0]
                cur.execute("SELECT * FROM Baby WHERE room_ID=?",(r,))
                row=cur.fetchone()
                if row is None:
                    cur.execute('''INSERT INTO Baby (room_ID, mate_1) VALUES (?, ?)''',(r, m))
                elif row[3] is None:
                    cur.execute('''UPDATE Baby SET mate_2=? WHERE room_ID=?''',(m,r))
                elif row[4] is None:
                    cur.execute('''UPDATE Baby SET mate_3=? WHERE room_ID=?''', (m,r))
                elif row[5] is None:
                    cur.execute('''UPDATE Baby SET mate_4=? WHERE room_ID=?''', (m,r))
            # creating a DB for complex
            elif lst[2].upper() == "COMPLEX":
                r=lst[1]
                m=lst[0]
                cur.execute("SELECT * FROM Complex WHERE room_ID=?",(r,))
                row=cur.fetchone()
                if row is None:
                    cur.execute('''INSERT INTO Complex (room_ID, mate_1) VALUES (?, ?)''',(r, m))
                elif row[3] is None:
                    cur.execute('''UPDATE Complex SET mate_2=? WHERE room_ID=?''',(m,r))
                elif row[4] is None:
                    cur.execute('''UPDATE Complex SET mate_3=? WHERE room_ID=?''', (m,r))
                elif row[5] is None:
                    cur.execute('''UPDATE Complex SET mate_4=? WHERE room_ID=?''', (m,r))
            # creating a DB for New Brunei
            if lst[2].upper()  == "NEW BRUNEI":
                r=lst[1]
                m=lst[0]
                cur.execute("SELECT * FROM New_Brunei WHERE room_ID=?",(r,))
                row=cur.fetchone()
                if row is None:
                    cur.execute('''INSERT INTO New_Brunei (room_ID, mate_1) VALUES (?, ?)''',(r, m))
                elif row[3] is None:
                    cur.execute('''UPDATE New_Brunei SET mate_2=? WHERE room_ID=?''',(m,r))
                elif row[4] is None:
                    cur.execute('''UPDATE New_Brunei SET mate_3=? WHERE room_ID=?''', (m,r))
                elif row[5] is None:
                    cur.execute('''UPDATE New_Brunei SET mate_4=? WHERE room_ID=?''', (m,r))
            # committing the data base to memory
            lst.clear()
            num=count%300
            if num == 0:
                total+=1
                conn.commit()
                print("So far", round((total*50)*100/811, 3), "per cent of the data has been commit to memory.\n Remaining... ", 811-(total*50))
conn.commit()
x=1
print(f"{x:.0%}","of the data has been commit to memory\n Well done, Sir")
cur.close()