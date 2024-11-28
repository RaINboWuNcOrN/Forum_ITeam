import sqlite3

conn = sqlite3.connect('TEAMS.db')
cursor = conn.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS commands(
                team_name TEXT PRIMARY KEY,
                points INTEGER
                )
''')
conn.commit()