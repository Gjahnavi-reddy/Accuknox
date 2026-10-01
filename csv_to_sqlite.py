import csv
import sqlite3

CSV_FILE = "user.csv"
DB_FILE = "users.db"


connection = sqlite3.connect(DB_FILE)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")


with open(CSV_FILE, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute("""
        INSERT OR IGNORE INTO users (name, email)
        VALUES (?, ?)
        """, (
            row["name"],
            row["email"]
        ))


connection.commit()


cursor.execute("SELECT * FROM users")

users = cursor.fetchall()


print("Users in database:")

for user in users:
    print(user)


connection.close()