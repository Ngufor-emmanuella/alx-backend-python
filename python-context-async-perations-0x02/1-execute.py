import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

def create_users_table():
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                age INTEGER NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()

def insert_sample_users():
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        if cursor.fetchone()[0] == 0:
            cursor.executemany('''
                INSERT INTO users (name, email, age) VALUES (?, ?, ?)
            ''', [
                ('Alice', 'alice@example.com', 30),
                ('Bob', 'bob@example.com', 40),
                ('Charlie', 'charlie@example.com', 22)
            ])
            conn.commit()
        cursor.close()

class ExecuteQuery:
    def __init__(self, query, params=None, db_name='users.db'):
        self.query = query
        self.params = params if params is not None else ()
        self.db_name = db_name
        self.connection = None
        self.results = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        cursor.close()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    create_users_table()
    insert_sample_users()

    sql = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery(sql, params) as results:
        print("Users older than 25:")
        for row in results:
            print(row)
