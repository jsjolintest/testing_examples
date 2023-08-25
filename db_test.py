import pytest
import sqlite3
from faker import Faker
# from db_functions import insert_user

fake = Faker()


@pytest.fixture
def sqlite_connection_fake_data():
    db_path = ":memory:"  # Use an in-memory database for testing
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT
        )
    ''')

    # Generate and insert fake data
    num_records = 10
    for _ in range(num_records):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))

    conn.commit()
    yield conn  # Provide the connection to the test
    conn.close()


@pytest.fixture
def test_user_data():
    return {
        "name": "john",
        "email": "jonhson@jon.net",
        "phone": "090909090"
    }


@pytest.fixture
def sqlite_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT
        )
    ''')

    conn.commit()
    yield conn
    conn.close()


def insert_user(connection, user_data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)",
                   (user_data["name"], user_data["email"], user_data["phone"]))
    connection.commit()


def get_user(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT name, email, phone FROM users WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()
    return user_data


def update_user(conn, user_id, new_data):
    cursor = conn.cursor()
    update_query = """
        UPDATE users
        SET name = ?, email = ?, phone = ?
        WHERE id = ?
    """
    cursor.execute(update_query, (new_data['name'], new_data['email'], new_data['phone'], user_id))
    conn.commit()


def test_update_user(sqlite_connection, test_user_data):
    conn = sqlite_connection
    cursor = conn.cursor()

    # Insert the test user into the database
    cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)",
                   (test_user_data['name'], test_user_data['email'], test_user_data['phone']))
    conn.commit()

    # Get the user ID of the inserted user
    cursor.execute("SELECT id FROM users WHERE email = ?", (test_user_data['email'],))
    user_id = cursor.fetchone()[0]

    # New data for updating the user
    new_data = {
        "name": "updated_name",
        "email": "updated_email@example.com",
        "phone": "9876543210"
    }

    # Update the user
    update_user(sqlite_connection, user_id, new_data)

    # Verify the updated data
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    updated_user = cursor.fetchone()

    assert updated_user[1] == new_data['name']
    assert updated_user[2] == new_data['email']
    assert updated_user[3] == new_data['phone']
#
# def test_insert_user_with_sqlite_fixture(sqlite_connection):
#     cursor = sqlite_connection.cursor()
#     cursor.execute("SELECT COUNT(*) FROM users")
#     result = cursor.fetchone()
#     assert result[0] == 10  # Assuming you inserted 10 records


# CRUD operations:


def test_insert_user(sqlite_connection, test_user_data):
    insert_user(sqlite_connection, test_user_data)

    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    assert result[0] == 1

    cursor.execute("SELECT name, email, phone FROM users")
    inserted_data = cursor.fetchone()
    assert inserted_data == (test_user_data["name"], test_user_data["email"], test_user_data["phone"])


def test_get_user(sqlite_connection, test_user_data):
    insert_user(sqlite_connection, test_user_data)

    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT id FROM users")
    user_id = cursor.fetchone()[0]

    retrieved_user_data = get_user(sqlite_connection, user_id)

    assert retrieved_user_data == (test_user_data["name"], test_user_data["email"], test_user_data["phone"])



def test_insert_user_duplicate_username(sqlite_connection):
    # Test handling of duplicate username during insertion
    pass


def test_get_users_empty_database(sqlite_connection):
    # Test retrieval from an empty database
    pass


