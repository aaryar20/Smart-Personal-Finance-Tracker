import sqlite3
from config import DB_NAME


def initialize_database():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # -----------------------------
    # Transactions Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # -----------------------------
    # Budget Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budget(
        id INTEGER PRIMARY KEY,
        monthly_budget REAL NOT NULL
    )
    """)

    # -----------------------------
    # Categories Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    default_categories = [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Bills",
        "Healthcare",
        "Education",
        "Salary",
        "Freelance",
        "Investment",
        "Other"
    ]

    cursor.execute("SELECT COUNT(*) FROM categories")

    if cursor.fetchone()[0] == 0:

        cursor.executemany(
            "INSERT INTO categories(name) VALUES(?)",
            [(c,) for c in default_categories]
        )

    # -----------------------------
    # Savings Goals
    # -----------------------------
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS savings_goals(
                   id INTEGER PRIMARY KEY,
                   goal_name TEXT,
                   target_amount REAL,
                   current_amount REAL)""")    

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")

    