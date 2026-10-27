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

#Kalorienbedarfsrechner
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calorie_needs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE,
            calories INTEGER NOT NULL,
            protein INTEGER NOT NULL,
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

#Lebensmittel-Einträge
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS food_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            food_name TEXT NOT NULL,
            grams REAL NOT NULL,
            calories REAL NOT NULL,
            protein REAL NOT NULL,
            fat REAL NOT NULL,
            carbs REAL NOT NULL,
            sugar REAL NOT NULL,
            meal TEXT NOT NULL,
            entry_date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

#selbst erstellte Lebensmittel
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS custom_foods(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            calories REAL NOT NULL,
            protein REAL NOT NULL,
            fat REAL NOT NULL,
            carbs REAL NOT NULL,
            sugar REAL NOT NULL
        )
    """)

#abgeschlossene Trainingseinheiten
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS completed_workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            workout_id INTEGER NOT NULL,
            completed_date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(workout_id) REFERENCES workouts(id)
        )
    """)

#gespeicherter Gewichtsvergleich
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_weight_comparisons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            comparison_date TEXT NOT NULL,
            comparison_name TEXT NOT NULL,
            comparison_weight REAL NOT NULL,
            UNIQUE(user_id, comparison_date),
            FOREIGN KEY(user_id) REFERENCES users(id)
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

def delete_workout(workout_id, user_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    #Tangemeldeten Benutzer
    cursor.execute("""
        SELECT id
        FROM workouts
        WHERE id = ?
        AND user_id = ?
        """, (workout_id, user_id))

    workout = cursor.fetchone()

    #falls der Plan nicht existiert oder einem anderen Benutzer gehört
    if workout is None:
        connection.close()
        return False

    #Zuerst alle Übungen des Trainingsplans löschen
    cursor.execute("""
        DELETE
        FROM workout_exercises
        WHERE workout_id = ?
        """, (workout_id,))

    #Trainingsplan löschen
    cursor.execute("""
        DELETE
        FROM workouts
        WHERE id = ?
        AND user_id = ?
        """, (workout_id, user_id))

    connection.commit()
    connection.close()

    return True

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

def get_username(user_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT username
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()
    connection.close()

    if user:
        return user[0]

    return None

def save_calorie_needs(user_id, calories, protein):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO calorie_needs (user_id, calories, protein)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET
            calories = excluded.calories,
            protein = excluded.protein
    """, (user_id, calories, protein))

    connection.commit()
    connection.close()

def get_calorie_needs(user_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT calories, protein
        FROM calorie_needs
        WHERE user_id = ?
    """, (user_id,))

    calorie_needs = cursor.fetchone()
    connection.close()

    return calorie_needs

def save_food(user_id, food_name, grams, calories, protein, fat, carbs, sugar, meal, entry_date):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO food_entries (user_id, food_name, grams, calories, protein, fat, carbs, sugar, meal, entry_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (user_id, food_name, grams, calories, protein, fat, carbs, sugar, meal, entry_date))

    connection.commit()
    connection.close()

def get_food(user_id, entry_date):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
                   SELECT id, food_name, grams, calories, protein, fat, carbs, sugar, meal, entry_date
                   FROM food_entries
                   WHERE user_id = ?
                     AND entry_date = ?
                   """, (user_id, entry_date))

    foods = cursor.fetchall()
    connection.close()

    return foods

def get_daily_nutrition(user_id, entry_date):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COALESCE(SUM(calories), 0),
            COALESCE(SUM(protein), 0)
        FROM food_entries
        WHERE user_id = ?
        AND entry_date = ?
    """, (user_id, entry_date))

    totals = cursor.fetchone()
    connection.close()

    return totals

def get_daily_training_stats(user_id, training_date):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Anzahl abgeschlossener Trainingseinheiten heute
    cursor.execute("""
        SELECT COUNT(*)
        FROM completed_workouts
        WHERE user_id = ? AND completed_date = ?
    """, (user_id, training_date))

    completed_workouts_count = cursor.fetchone()[0]

    #Gesamtgewicht aller Sätze und Wiederholungen
    cursor.execute("""
        SELECT COALESCE(SUM(
            we.sets * we.reps * we.weight
        ), 0)
        FROM completed_workouts cw
        JOIN workout_exercises we ON cw.workout_id = we.workout_id
        WHERE cw.user_id = ? AND cw.completed_date = ?
    """, (user_id, training_date))

    total_weight = cursor.fetchone()[0]

    connection.close()

    return completed_workouts_count, total_weight


def save_completed_workout(user_id, workout_id, completed_date):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO completed_workouts (user_id, workout_id, completed_date)
        VALUES (?, ?, ?)
    """, (user_id, workout_id, completed_date))

    connection.commit()
    connection.close()


def delete_food(user_id, food_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM food_entries
        WHERE id = ?
        AND user_id = ?
    """, (food_id, user_id))

    connection.commit()
    deleted_rows = cursor.rowcount
    connection.close()
    return deleted_rows


def update_food(user_id, food_id, grams, calories, protein, fat, carbs, sugar):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE food_entries
        SET grams = ?,
            calories = ?,
            protein = ?,
            fat = ?,
            carbs = ?,
            sugar = ?
        WHERE id = ?
        AND user_id = ?
    """, (grams, calories, protein, fat, carbs, sugar, food_id, user_id))

    connection.commit()
    updated_rows = cursor.rowcount
    connection.close()
    return updated_rows

def save_custom_food(name, calories, protein, fat, carbs, sugar):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO custom_foods (name, calories, protein, fat, carbs, sugar)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, calories, protein, fat, carbs, sugar))

    connection.commit()
    connection.close()

def search_custom_foods(search_term):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    search_words = search_term.strip().split()

    if not search_words:
        connection.close()
        return []

    conditions = []
    parameters = []

    for word in search_words:
        conditions.append("name LIKE ?")
        parameters.append("%" + word + "%")

    query = """
        SELECT name, calories, protein, fat, carbs, sugar
        FROM custom_foods
        WHERE """ + " AND ".join(conditions)

    cursor.execute(query, parameters)
    foods = cursor.fetchall()
    connection.close()

    results = []
    for food in foods:
        results.append({
            "product_name": food[0],
            "nutriments": {
                "energy-kcal_100g": food[1],
                "proteins_100g": food[2],
                "fat_100g": food[3],
                "carbohydrates_100g": food[4],
                "sugars_100g": food[5]
                }
        })

    return results


def get_daily_weight_comparison(user_id, comparison_date):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT comparison_name, comparison_weight
        FROM daily_weight_comparisons
        WHERE user_id = ? AND comparison_date = ?
    """, (user_id, comparison_date))

    comparison = cursor.fetchone()
    connection.close()

    return comparison


def save_daily_weight_comparison(user_id, comparison_date, comparison_name, comparison_weight):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO daily_weight_comparisons
            (user_id, comparison_date, comparison_name, comparison_weight)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id, comparison_date) DO NOTHING
    """, (user_id, comparison_date, comparison_name, comparison_weight))

    connection.commit()
    connection.close()


create_database()
