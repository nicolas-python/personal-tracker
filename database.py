import sqlite3

DATABASE = "database/personal_tracker.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

#Einloggdaten
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)

#Workouts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    connection.commit()
    connection.close()


def add_user(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
    """, (username, password))

    connection.commit()
    connection.close()


def login_user(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ? AND password_hash = ?
    """, (username, password))

    user = cursor.fetchone()
    connection.close()
    return user is not None

def save_workout(user_id, workout_name):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO workouts (user_id, name)
        VALUES (?, ?)
    """, (user_id, workout_name))

    connection.commit()
    connection.close()








def show_users():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    connection.close()

create_database()
show_users()