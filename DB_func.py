import sqlite3

conn = sqlite3.connect('TEAMS1.db')


def db_to_dict(conn) -> dict:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM commands')
    all_teams = cursor.fetchall()
    commands = {}
    for name, point in all_teams:
        commands[name] = point
    return commands

def add_team_to_db(conn, name: str, points: int):
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM commands WHERE team_name = ?", (name,)) #Более эффективный способ проверки
    if cursor.fetchone():
        return None
    else:
        cursor.execute('INSERT INTO commands (team_name, points) VALUES (?, ?)', (name, points))
        conn.commit()


def del_team_in_db(conn, name: str):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM commands WHERE team_name = ?', (name,))
    conn.commit()

def add_points_to_team(conn, name: str, points_to_add: int):
    cursor = conn.cursor()
    cursor.execute("SELECT points FROM commands WHERE team_name = ?", (name,))
    result = cursor.fetchone()[0]
    if name:
        pr_points = int(result)
        new_points = pr_points + points_to_add
        cursor.execute("UPDATE commands SET points = ? WHERE team_name = ?", (new_points, name))
        conn.commit()
    else:
        print(f"Team '{name}' not found.")


def rem_points_to_team(conn, name: str, points_to_add: int):
    cursor = conn.cursor()
    cursor.execute("SELECT points FROM commands WHERE team_name = ?", (name,))
    result = cursor.fetchone()
    if name:
        pr_points = int(result[0])
        new_points = pr_points - points_to_add
        cursor.execute("UPDATE commands SET points = ? WHERE team_name = ?", (new_points, name))
        conn.commit()
    else:
        print(f"Team '{name}' not found.")