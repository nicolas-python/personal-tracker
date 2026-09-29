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

    #übungen zu den Workouts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_exercises(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workout_id INTEGER NOT NULL,
            exercise_name TEXT NOT NULL,
            FOREIGN KEY(workout_id) REFERENCES workouts(id)
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
    return user

def save_workout(user_id, workout_name, exercises):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    #workout speichern
    cursor.execute("""
        INSERT INTO workouts (user_id, name)
        VALUES (?, ?)
    """, (user_id, workout_name))

    #id speichern
    workout_id = cursor.lastrowid
    for exercise in exercises:
        cursor.execute("""
            INSERT INTO workout_exercises (workout_id, exercise_name)
            VALUES (?, ?)
            """,(workout_id, exercise))

    connection.commit()
    connection.close()

def get_workouts(user_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM workouts
        WHERE user_id = ?
    """, (user_id,))

    workouts = cursor.fetchall()
    connection.close()
    return workouts

def get_workout_exercises(workout_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT exercise_name
        FROM workout_exercises
        WHERE workout_id = ?
    """, (workout_id,))

    exercises = cursor.fetchall()
    connection.close()
    return exercises




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