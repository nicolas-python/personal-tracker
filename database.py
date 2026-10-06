import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

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
            sets INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            weight REAL NOT NULL,
            FOREIGN KEY(workout_id) REFERENCES workouts(id)
        )
    """)

    connection.commit()
    connection.close()


def add_user(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    password_hash = generate_password_hash(password, method="pbkdf2:sha256")  # PBKDF2 = Schlüsselableitungsverfahren SHA-256 = Hashfunktion

    cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
    """, (username, password_hash))

    connection.commit()
    connection.close()


def login_user(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()
    connection.close()

    if user and check_password_hash(user[2], password):
        return user

    return None

def save_workout(user_id, workout_name, exercises):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    #workout name und user id speichern
    cursor.execute("""
        INSERT INTO workouts (user_id, name)
        VALUES (?, ?)
    """, (user_id, workout_name))

    #Übungen speichern
    workout_id = cursor.lastrowid
    for exercise, sets, reps, weight in exercises:
        cursor.execute("""
        INSERT INTO workout_exercises (workout_id,exercise_name,sets,reps,weight)
        VALUES (?, ?, ?, ?, ?)
            """,(workout_id, exercise, sets, reps, weight))

    connection.commit()
    connection.close()

def update_workout(workout_id, workout_name, exercises):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    #trainingsplannamen aktualisieren
    cursor.execute("""UPDATE workouts SET name = ?WHERE id = ?""", (workout_name, workout_id))

    #alte übungen dieses Trainingsplans löschen
    cursor.execute("""DELETE FROM workout_exercises WHERE workout_id = ? """, (workout_id,))

    #neue übungen speichern
    for exercise, sets, reps, weight in exercises:
        cursor.execute("""INSERT INTO workout_exercises (workout_id, exercise_name, sets, reps, weight) VALUES (?, ?, ?, ?, ?) """,
                       (workout_id, exercise, sets, reps, weight))

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

def get_workout(workout_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM workouts
        WHERE id = ?
    """, (workout_id,))

    workout = cursor.fetchone()
    connection.close()
    return workout

def get_workout_exercises(workout_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT exercise_name, sets, reps, weight
        FROM workout_exercises
        WHERE workout_id = ?
    """, (workout_id,))

    exercises = cursor.fetchall()
    connection.close()
    return exercises

create_database()