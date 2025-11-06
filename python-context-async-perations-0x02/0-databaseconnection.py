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
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        cursor.close()

def insert_sample_users():
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.executemany('''
                INSERT INTO users (name, email) VALUES (?, ?)
            ''', [
                ('Alice', 'alice@example.com'),
                ('Bob', 'bob@example.com'),
                ('Charlie', 'charlie@example.com')
            ])
            conn.commit()
        cursor.close()

if __name__ == "__main__":
    create_users_table()        
    insert_sample_users()       
    query = "SELECT * FROM users"
    
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

    print("Results from users table:")
    for row in results:
        print(row)
