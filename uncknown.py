from sqlite3 import *
from tkinter import *

root = Tk()
root.title('KR_2')
root.geometry('400x200+0+0')
can = Canvas(root, width=400, height=200, bg='#ffffff')
can.pack()


def sql_connection():
    try:
        con = connect('K2.db')
        return con
    except Error:
        print(Error)


def sql_table(con):
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                 Фамилия TEXT,
                 Имя TEXT,
                 Отчество TEXT,
                 Дата_рождения DATE,
                 Номер_группы TEXT);
               """)
    con.commit()


def prin():
    a1 = txt_1.get()
    a2 = txt_2.get()
    a3 = txt_3.get()
    a4 = txt_4.get()
    a5 = txt_5.get()
    rest = (a1, a2, a3, a4, a5)
    cur.execute("""INSERT INTO users VALUES(?,?,?,?,?);""", rest)


def ex():
    root.destroy()
    cur.execute("SELECT Фамилия, Имя, Отчество, Дата_рождения, Номер_группы FROM users;")
    results = cur.fetchall()
    for a, b, c, d, e in results:
        print(a, b, c, d, e)


con = sql_connection()
sql_table(con)
cur = con.cursor()

lbl_1 = Label(can, text='Фамилия', bg='white')
lbl_2 = Label(can, text='Имя', bg='white')
lbl_3 = Label(can, text='Отчество', bg='white')
lbl_4 = Label(can, text='Дата рождения', bg='white')
lbl_5 = Label(can, text='Номер группы', bg='white')

txt_1 = Entry(can, bg='white', bd=2, relief='groove', highlightbackground='blue')
txt_2 = Entry(can, bg='white', bd=2, relief='groove', highlightbackground='blue')
txt_3 = Entry(can, bg='white', bd=2, relief='groove', highlightbackground='blue')
txt_4 = Entry(can, bg='white', bd=2, relief='groove', highlightbackground='blue')
txt_5 = Entry(can, bg='white', bd=2, relief='groove', highlightbackground='blue')

btn_1 = Button(root, text='Вывод', bg='dodger blue', fg='white', font='16', command=prin)
btn_2 = Button(root, text='Выход', bg='dodger blue', fg='white', font='16', command=ex)

lbl_1.place(x=10, y=10)
lbl_2.place(x=10, y=40)
lbl_3.place(x=10, y=70)
lbl_4.place(x=10, y=100)
lbl_5.place(x=10, y=130)

txt_1.place(x=120, y=10)
txt_2.place(x=120, y=40)
txt_3.place(x=120, y=70)
txt_4.place(x=120, y=100)
txt_5.place(x=120, y=130)

btn_1.place(x=120, y=160)
btn_2.place(x=200, y=160)

root.mainloop()
