import sqlite3

# Создание базы данных и таблиц
conn = sqlite3.connect('store.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                balance INTEGER DEFAULT 0
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                price INTEGER
             )''')

c.execute("INSERT OR IGNORE INTO products (name, price) VALUES ('Product 1', 10)")
c.execute("INSERT OR IGNORE INTO products (name, price) VALUES ('Product 2', 20)")
c.execute("INSERT OR IGNORE INTO products (name, price) VALUES ('Product 3', 30)")

c.execute('''CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
             )''')

c.execute("INSERT OR IGNORE INTO admins (username, password) VALUES ('admin', 'adminpass')")

conn.commit()

# Функция регистрации нового пользователя
def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    print("Регистрация прошла успешно!")

# Функция авторизации пользователя
def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()

    if user:
        print("Авторизация прошла успешно!")
        return user[0]
    else:
        print("Неверные данные авторизации.")
        return None

# Функция покупки товаров
def purchase(user_id):
    c.execute("SELECT * FROM products")
    products = c.fetchall()

    print("Доступные товары:")
    for product in products:
        print(f"{product[0]}. {product[1]} - {product[2]}")

    product_id = int(input("Введите ID товара, который хотите купить: "))
    quantity = int(input("Введите количество: "))

    c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()

    if product:
        price = product[2] * quantity

        c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
        balance = c.fetchone()[0]

        if quantity >= 0:
            c.execute("UPDATE users SET balance = ? WHERE id = ?", (balance - price, user_id))
            print("Покупка прошла успешно!")
        else:
            c.execute("UPDATE users SET balance = ? WHERE id = ?", (balance + abs(price), user_id))
            print("Некорректное количество товаров. Баланс пополнен.")
    else:
        print("Неверный ID товара.")

    conn.commit()

# Функция получения текстовой информации
def get_text_info(user_id):
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()

    if user:
        print("Имя пользователя:", user[1])
        print("Баланс:", user[3])
    else:
        print("Пользователь не найден.")

# Функция удаления пользователя (только для администратора)
def delete_user():
    username = input("Введите имя пользователя, которого хотите удалить: ")

    c.execute("DELETE FROM users WHERE username = ?", (username,))
    print("Пользователь удален.")

    conn.commit()

# Функция получения базы пользователей (только для администратора)
def get_users():
    c.execute("SELECT * FROM users")
    users = c.fetchall()

    print("База пользователей:")
    for user in users:
        print(f"ID: {user[0]}, Имя пользователя: {user[1]}, Баланс: {user[3]}")

# Функция добавления товара (только для администратора)
def add_product():
    name = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))

    c.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    print("Товар добавлен.")

    conn.commit()

# Функция авторизации администратора
def admin_login():
    username = input("Введите имя пользователя администратора: ")
    password = input("Введите пароль администратора: ")

    c.execute(f"SELECT * FROM admins WHERE username = {username} AND password = {password}")
    admin = c.fetchone()

    if admin:
        print("Вы вошли как администратор!")
        return True
    else:
        print("Неверные данные авторизации администратора.")
        return False

# Меню приложения
while True:
    print("\nМеню:")
    print("1. Регистрация")
    print("2. Авторизация")
    print("3. Покупка товаров")
    print("4. Получение информации")
    print("5. Вход для администратора")
    print("6. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        register()
    elif choice == '2':
        user_id = login()
    elif choice == '3':
        if user_id:
            purchase(user_id)
        else:
            print("Сначала выполните вход.")
    elif choice == '4':
        if user_id:
            get_text_info(user_id)
        else:
            print("Сначала выполните вход.")
    elif choice == '5':
        if admin_login():
            while True:
                print("\nМеню администратора:")
                print("1. Добавить товар")
                print("2. Удалить пользователя")
                print("3. Получить базу пользователей")
                print("4. Выйти из режима администратора")

                admin_choice = input("Введите номер действия: ")

                if admin_choice == '1':
                    add_product()
                elif admin_choice == '2':
                    delete_user()
                elif admin_choice == '3':
                    get_users()
                elif admin_choice == '4':
                    print("Вы вышли из режима администратора.")
                    break
        else:
            print("Сначала выполните вход для администратора.")
    elif choice == '6':
        print("Выход из приложения.")
        break
    else:
        print("Некорректный ввод. Попробуйте еще раз.")