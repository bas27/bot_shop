import sqlite3

connection = sqlite3.connect('old/data.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER,
                    username TEXT,
                    first_name TEXT,
                    block INT)'''
               )


def add_user(user_id, username, first_name):
    check_user = cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
    if check_user.fetchone() is None:
        cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?)", (user_id, username, first_name, 0))
        connection.commit()
    else:
        print("User already exists")


def show_users():
    users_list = cursor.execute("SELECT * FROM Users")
    message = ""
    for user in users_list:
        message += f"{user[0]} @{user[1]} @{user[2]}\n"
    connection.commit()
    return message


def show_stat():
    count_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0]
    connection.commit()
    return count_users


def add_to_block(input_id):
    cursor.execute("UPDATE Users SET block = 1 WHERE id = ?", (input_id,))
    connection.commit()
    return "User blocked"


def remove_block(input_id):
    cursor.execute("UPDATE Users SET block = 0 WHERE id = ?", (input_id,))
    connection.commit()
    return "User unblocked"


def check_block(user_id):
    users = cursor.execute("SELECT block FROM Users WHERE id = ?", (user_id,)).fetchone()[0]
    connection.commit()
    return users


connection.commit()
connection.close()
