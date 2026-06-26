import sqlite3
import pandas as pd
from config import DB_NAME


# -----------------------------
# Database Connection
# -----------------------------

def get_connection():
    return sqlite3.connect(DB_NAME)


# -----------------------------
# Transactions
# -----------------------------

def load_transactions():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM transactions",
        conn
    )

    conn.close()

    return df


def add_transaction(date, transaction_type, category, amount, description):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transactions
        (date, type, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            date,
            transaction_type,
            category,
            amount,
            description
        )
    )

    conn.commit()
    conn.close()


def delete_transaction(transaction_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE id=?",
        (transaction_id,)
    )

    conn.commit()
    conn.close()

def update_transaction(
        transaction_id,
        date,
        transaction_type,
        category,
        amount,
        description
        ):
    ...


# -----------------------------
# Budget
# -----------------------------

def load_budget():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM budget",
        conn
    )

    conn.close()

    return df


def save_budget(amount):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO budget
    (id, monthly_budget)
    VALUES (1, ?)
    """, (amount,))

    conn.commit()
    conn.close()

def get_transaction(transaction_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM transactions WHERE id=?",
        (transaction_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row

def update_transaction(
    transaction_id,
    date,
    transaction_type,
    category,
    amount,
    description
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE transactions
        SET
            date=?,
            type=?,
            category=?,
            amount=?,
            description=?
        WHERE id=?
        """,
        (
            date,
            transaction_type,
            category,
            amount,
            description,
            transaction_id
        )
    )

    conn.commit()

    conn.close()

def get_transaction(transaction_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM transactions
        WHERE id=?
        """,
        (transaction_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row

def update_transaction(
    transaction_id,
    date,
    transaction_type,
    category,
    amount,
    description
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE transactions
        SET
            date=?,
            type=?,
            category=?,
            amount=?,
            description=?
        WHERE id=?
        """,
        (
            date,
            transaction_type,
            category,
            amount,
            description,
            transaction_id
        )
    )

    conn.commit()
    conn.close()

# -----------------------------
# Categories
# -----------------------------

def load_categories():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM categories ORDER BY name")

    categories = [row[0] for row in cursor.fetchall()]

    conn.close()

    return categories
def add_category(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO categories(name) VALUES(?)",
        (name,)
    )

    conn.commit()
    conn.close()
def delete_category(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM categories WHERE name=?",
        (name,)
    )

    conn.commit()
    conn.close()

# -----------------------------
# Categories
# -----------------------------

def load_categories():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM categories ORDER BY name"
    )

    categories = [row[0] for row in cursor.fetchall()]

    conn.close()

    return categories


def add_category(category_name):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO categories(name)
            VALUES(?)
            """,
            (category_name,)
        )

        conn.commit()

    except sqlite3.IntegrityError:
        pass

    finally:
        conn.close()


def delete_category(category_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM categories
        WHERE name=?
        """,
        (category_name,)
    )

    conn.commit()
    conn.close()

# -----------------------------
# Savings Goals
# -----------------------------

def load_goal():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM savings_goals",
        conn
    )

    conn.close()

    return df
def save_goal(
    goal_name,
    target_amount,
    current_amount
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO savings_goals(
        id,
        goal_name,
        target_amount,
        current_amount
    )
    VALUES(
        1,
        ?,
        ?,
        ?
    )
    """,
    (
        goal_name,
        target_amount,
        current_amount
    ))

    conn.commit()

    conn.close()