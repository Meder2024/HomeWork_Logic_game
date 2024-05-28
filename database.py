import sqlite3

def create_database():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL
                      )''')
    conn.commit()
    conn.close()

def register_player(username):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO players (username) VALUES (?)', (username,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Пользователь с именем {username} уже существует.")
    conn.close()

def get_player_id(username):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM players WHERE username = ?', (username,))
    player_id = cursor.fetchone()
    conn.close()
    return player_id[0] if player_id else None
