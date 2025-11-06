import sqlite3
import functools

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else args[0] if args else ''
        print(f"[LOG] Executing SQL query: {query}")
        return func(*args, **kwargs)
    return wrapper

def setup_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', [
            ('Alice', 'alice@example.com'),
            ('Bob', 'bob@example.com'),
            ('Charlie', 'charlie@example.com')
        ])
    conn.commit()
    conn.close()

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    setup_db()
    users = fetch_all_users(query="SELECT * FROM users")
    print("Users data:", users)
