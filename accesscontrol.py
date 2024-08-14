import sqlite3

def grant_access(username, file_id):
    conn = sqlite3.connect('access_control.db')
    c = conn.cursor()
    c.execute('INSERT INTO access (username, file_id) VALUES (?, ?)', (username, file_id))
    conn.commit()
    conn.close()

def check_access(username, file_id):
    conn = sqlite3.connect('access_control.db')
    c = conn.cursor()
    c.execute('SELECT * FROM access WHERE username = ? AND file_id = ?', (username, file_id))
    result = c.fetchone()
    conn.close()
    return result is not None

# Initialize the database
def init_access_db():
    conn = sqlite3.connect('access_control.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS access (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    file_id INTEGER NOT NULL
                 )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_access_db()
