import sqlite3

db = sqlite3.connect('myFirstDB.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  age INTEGER)''')



def insert():
    cursor.execute("INSERT INTO users (name, age) VALUES (?,?)",
                (input("Имя: "), int(input("Возраст: "))))


def update():
    find_id = int(input("ID: "))
    age = int(input("NEW AGE: "))
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age, find_id))

def show():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for i in users:
        print(i)

def user_delete():
    name = input("NAME: ")

    cursor.execute("DELETE FROM users WHERE name = ?", (name,))


if __name__ == "__main__":
    print("DATABASE USERS:")
    while True:
        print("1.Добавить")
        print("2.Обновить")
        print("3.Удлить")
        print("4.Вывести")
        com = int(input("Введите команду: "))

        if com == 1:
            insert()
        elif com == 2:
            update()
        elif com == 3:
            user_delete()
        elif com == 4:
            show()
        else:
            break
        db.commit()


db.close()