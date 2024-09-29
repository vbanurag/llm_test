import sqlite3

def create_sample_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        department_id INTEGER,
        salary REAL
    )
    ''')

    # Create departments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        location TEXT
    )
    ''')

    # Insert sample data into employees
    employees = [
        (1, 'John Doe', 30, 1, 50000),
        (2, 'Jane Smith', 35, 2, 60000),
        (3, 'Bob Johnson', 45, 1, 55000),
        (4, 'Alice Brown', 28, 3, 48000),
        (5, 'Charlie Davis', 38, 2, 62000)
    ]
    cursor.executemany('INSERT OR REPLACE INTO employees VALUES (?,?,?,?,?)', employees)

    # Insert sample data into departments
    departments = [
        (1, 'HR', 'New York'),
        (2, 'Engineering', 'San Francisco'),
        (3, 'Marketing', 'Chicago')
    ]
    cursor.executemany('INSERT OR REPLACE INTO departments VALUES (?,?,?)', departments)

    conn.commit()
    conn.close()

    print(f"Sample database created at {db_path}")

if __name__ == "__main__":
    db_path = "sample_company.db"
    create_sample_database(db_path)
