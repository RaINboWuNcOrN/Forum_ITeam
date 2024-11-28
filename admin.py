import tkinter as tk
from tkinter import Spinbox
import sqlite3
conn = sqlite3.connect("TEAMS.db")


def on_enter(e):
    e.widget['background'] = 'lightblue'
def on_enter2(e):
    e.widget['background'] = '#CD4A4C'

def on_leave(e):
    e.widget['background'] = 'lightgray'
def on_leave2(e):
    e.widget['background'] = '#B5B8B1'
def on_leave3(e):
    e.widget['background'] = '#DCDCDC'

class AdaptiveWindow:
    def __init__(self, root):
        self.str_commands=''
        self.root = root
        self.root.title("Квиз")

        #1 фрейм
        self.frame_menu = tk.Frame(self.root)
        self.frame_menu.pack()
        #2 фрейм
        self.frame_add_command = tk.Frame(self.root)
        #3 фрейм
        self.frame_delete_command= tk.Frame(self.root)
        #4 фрейм
        self.frame_list_command = tk.Frame(self.root)
        #5 фрейм
        self.frame_change_command = tk.Frame(self.root)
        #6 фрейм
        self.frame_output_of_results = tk.Frame(self.root)
        # под-фреймы для изменения балов
        self.frame_change_command1 = tk.Frame(self.root)
        self.frame_change_command2 = tk.Frame(self.root)

        # 9 фрейм
        self.frameee_9 = tk.Frame(self.root)
        # 10 фрейм
        self.frameee_10 = tk.Frame(self.root)

        #кнопки 1 фрейм
        self.label1 = tk.Label(self.frame_menu,text="Квиз", font=("Helvetica", 23))
        self.label1.pack(fill='both', padx=30, pady=25)
        self.button1 = tk.Button(self.frame_menu, text="добавить команду", font=("Arial", 16), command=self.show_frame_add_command)
        self.button1.bind("<Enter>", on_enter)
        self.button1.bind("<Leave>", on_leave)
        self.button1.pack( fill='both', padx=30, pady=4)
        self.button2 = tk.Button(self.frame_menu, text="удалить команду", font=("Arial", 16), command=self.show_frame_delete_command)
        self.button2.bind("<Enter>", on_enter)
        self.button2.bind("<Leave>", on_leave)
        self.button2.pack( fill='both', padx=30, pady=4)
        self.button3 = tk.Button(self.frame_menu, text="список команд", font=("Arial", 16), command=self.show_frame_list_command)
        self.button3.bind("<Enter>", on_enter)
        self.button3.bind("<Leave>", on_leave)
        self.button3.pack( fill='both', padx=30, pady=4)
        self.button4 = tk.Button(self.frame_menu, text="изменение балов команд", font=("Arial", 16), command=self.show_frame_change_command)
        self.button4.bind("<Enter>", on_enter)
        self.button4.bind("<Leave>", on_leave)
        self.button4.pack( fill='both', padx=30, pady=4)
        self.button5 = tk.Button(self.frame_menu, text="вывод результатов", font=("Arial", 16), command=self.show_frame_output_of_results)
        self.button5.bind("<Enter>", on_enter)
        self.button5.bind("<Leave>", on_leave)
        self.button5.pack( fill='both', padx=30, pady=4)
        self.button6 = tk.Button(self.frame_menu, text="выход", font=("Arial", 16),command=quit)
        self.button6.bind("<Enter>", on_enter2)
        self.button6.bind("<Leave>", on_leave)
        self.button6.pack( fill='both', padx=30, pady=4)
        self.root.bind("<Configure>", self.on_resize)

        #кнопки 2 фрейм
        self.label2 = tk.Label(self.frame_add_command, text="добавить команду", font=("Helvetica", 23))
        self.label2.pack(fill='both', padx=30, pady=25)
        self.label7 = tk.Label(self.frame_add_command, text="введите название:", font=("Helvetica", 20))
        self.label7.pack(fill='both', padx=30, pady=5)
        self.entry1 = tk.Entry(self.frame_add_command)
        self.entry1.pack(fill='both', padx=30, pady=10)
        self.button12 = tk.Button(self.frame_add_command, text="добавить", font=("Arial", 16), command=self.submit)
        self.button12.pack(fill='both', padx=30, pady=10)
        self.button12.bind("<Enter>", on_enter)
        self.button12.bind("<Leave>", on_leave)
        self.button7 = tk.Button(self.frame_add_command, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button7.bind("<Enter>", on_enter)
        self.button7.bind("<Leave>", on_leave)
        self.button7.pack( fill='both', padx=30, pady=4)

        # кнопки 3 фрейм
        self.label3 = tk.Label(self.frame_delete_command, text="удалить команду", font=("Helvetica", 23))
        self.label3.pack(fill='both', padx=30, pady=25)
        self.spinbox6 = tk.Spinbox(self.frame_delete_command,values=list(self.db_to_dict(conn)))
        self.spinbox6.pack(fill='both', padx=30, pady=25)
        self.button13 = tk.Button(self.frame_delete_command, text="удалить", font=("Arial", 16),command=self.show_value)
        self.button13.bind("<Enter>", on_enter)
        self.button13.bind("<Leave>", on_leave)
        self.button13.pack( fill='both', padx=30, pady=4)
        self.button8 = tk.Button(self.frame_delete_command, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button8.bind("<Enter>", on_enter)
        self.button8.bind("<Leave>", on_leave)
        self.button8.pack( fill='both', padx=30, pady=4)

        # кнопки 4 фрейм
        self.label4 = tk.Label(self.frame_list_command, text="список команд", font=("Helvetica", 23))
        self.label4.pack(fill='both', padx=30, pady=15)
        self.button14 = tk.Button(self.frame_list_command, text="по алфавиту", font=("Arial", 16),command=self.frame_9)
        self.button14.bind("<Enter>", on_enter)
        self.button14.bind("<Leave>", on_leave)
        self.button14.pack( fill='both', padx=40, pady=3)
        self.button15 = tk.Button(self.frame_list_command, text="по баллам", font=("Arial", 16),command=self.frame_10)
        self.button15.bind("<Enter>", on_enter)
        self.button15.bind("<Leave>", on_leave)
        self.button15.pack( fill='both', padx=40, pady=3)
        self.button9 = tk.Button(self.frame_list_command, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button9.bind("<Enter>", on_enter)
        self.button9.bind("<Leave>", on_leave)
        self.button9.pack( fill='both', padx=20, pady=25)

        # кнопки 5 фрейм
        self.label5 = tk.Label(self.frame_change_command, text="изменение баллов команд", font=("Helvetica", 23))
        self.label5.pack(fill='both', padx=30, pady=40)
        self.button16 = tk.Button(self.frame_change_command, text="добавить баллы", font=("Arial", 16),command=self.show_frame_change_command1)
        self.button16.bind("<Enter>", on_enter)
        self.button16.bind("<Leave>", on_leave2)
        self.button16.pack(side=tk.LEFT)
        self.button17 = tk.Button(self.frame_change_command, text="удалить баллы", font=("Arial", 16),command=self.show_frame_change_command2)
        self.button17.bind("<Enter>", on_enter)
        self.button17.bind("<Leave>", on_leave2)
        self.button17.pack(side=tk.RIGHT)
        self.button10 = tk.Button(self.frame_change_command, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button10.bind("<Enter>", on_enter)
        self.button10.bind("<Leave>", on_leave3)
        self.button10.pack( fill='both', padx=30, pady=4)

        # кнопки 6 фрейм
        self.label6 = tk.Label(self.frame_output_of_results, text="вывод результатов", font=("Helvetica", 23))
        self.label6.pack(fill='both', padx=30, pady=25)
        self.button11 = tk.Button(self.frame_output_of_results, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button11.bind("<Enter>", on_enter)
        self.button11.bind("<Leave>", on_leave)
        self.button11.pack( fill='both', padx=30, pady=4)

        # кнопки 7 фрейм
        self.label8 = tk.Label(self.frame_change_command1, text="добавить баллы", font=("Helvetica", 23))
        self.label8.pack(fill='both', padx=30, pady=25)
        self.spinbox5 = tk.Spinbox(self.frame_change_command1,values=list(self.db_to_dict(conn).keys()))
        self.spinbox5.pack(fill='both', padx=30, pady=25)
        self.spinbox3 = Spinbox(self.frame_change_command1, from_=0, to=10)
        self.spinbox3.pack(fill='both', padx=30, pady=25)
        self.button21 = tk.Button(self.frame_change_command1, text="добавить", font=("Arial", 16),command=self.add_points)
        self.button21.bind("<Enter>", on_enter)
        self.button21.bind("<Leave>", on_leave)
        self.button21.pack(fill='both', padx=30, pady=4)
        self.button18 = tk.Button(self.frame_change_command1, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button18.bind("<Enter>", on_enter)
        self.button18.bind("<Leave>", on_leave)
        self.button18.pack(fill='both', padx=30, pady=4)

        # кнопки 8 фрейм
        self.label9 = tk.Label(self.frame_change_command2, text="удалить баллы", font=("Helvetica", 23))
        self.label9.pack(fill='both', padx=30, pady=25)
        self.spinbox4 = tk.Spinbox(self.frame_change_command2,values=list(self.db_to_dict(conn).keys()))
        self.spinbox4.pack(fill='both', padx=30, pady=25)
        self.spinbox2 = Spinbox(self.frame_change_command2, from_=0, to=10)
        self.spinbox2.pack(fill='both', padx=30, pady=25)
        self.button20 = tk.Button(self.frame_change_command2, text="удалить", font=("Arial", 16), command=self.rem_points)
        self.button20.bind("<Enter>", on_enter)
        self.button20.bind("<Leave>", on_leave)
        self.button20.pack( fill='both', padx=30, pady=4)
        self.button19 = tk.Button(self.frame_change_command2, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button19.bind("<Enter>", on_enter)
        self.button19.bind("<Leave>", on_leave)
        self.button19.pack(fill='both', padx=30, pady=4)

        # кнопки 9 фрейм
        self.label10 = tk.Label(self.frameee_9, text="вывод команд по алфавиту", font=("Helvetica", 23))
        self.label10.pack(fill='both', padx=30, pady=25)
        self.label12 = tk.Label(self.frameee_9, text=str(self.db_to_dict(conn)), font=("Helvetica", 23))
        self.label12.pack(fill='both', padx=30, pady=25)
        self.button22 = tk.Button(self.frameee_9, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button22.bind("<Enter>", on_enter)
        self.button22.bind("<Leave>", on_leave)
        self.button22.pack(fill='both', padx=30, pady=4)

        # кнопки 10 фрейм
        self.label11 = tk.Label(self.frameee_10, text="вывод команд по баллам", font=("Helvetica", 23))
        self.label13 = tk.Label(self.frameee_10, text=str(self.db_to_dict(conn)), font=("Helvetica", 23))
        self.label13.pack(fill='both', padx=30, pady=25)
        self.label11.pack(fill='both', padx=30, pady=25)
        self.button23 = tk.Button(self.frameee_10, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button23.bind("<Enter>", on_enter)
        self.button23.bind("<Leave>", on_leave)
        self.button23.pack(fill='both', padx=30, pady=4)

    def get_names_commands_by_alphabet(self,commands):
        names = []
        for command in commands.keys():
            names.append(command)
        return sorted(names)

    def get_names_commands_by_points(self,commands):
        names_and_points = list(commands.keys())
        sorted_commands = sorted(names_and_points, key=lambda x: commands[x], reverse=True)
        result = []
        text = ''
        k = 0
        for command in sorted_commands:
            result.append((command, commands[command]))
        for team, points in result:
            k+=1
            text += f'{k}) {team} {str(points)} \n'
        return text
#########################################
    def add_new_command(self,conn,name):
        cursor = conn.cursor()
        if name in self.db_to_dict(conn).keys():
            return None
        else:
            cursor.execute('INSERT INTO commands (team_name, points) VALUES (?, ?)',
                           (name, 0))
            conn.commit()
        return self.db_to_dict(conn)

    def delete_command(self,conn, name: str):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM commands WHERE team_name = ?', (name,))
        conn.commit()
        return self.db_to_dict(conn)

    def add_points_to_command(self,conn, name: str, points_to_add: int):
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
        return self.db_to_dict(conn)

    def rem_points_to_command(self,conn, name: str, points_to_add: int):
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
        return self.db_to_dict(conn)

#################################

    def db_to_dict(self,conn) -> dict:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM commands')
        all_teams = cursor.fetchall()
        commands = {}
        for name, point in all_teams:
            commands[name] = point
        return commands

    def add_team_to_db(self,conn, name: str, points: int):
        cursor = conn.cursor()
        if name in self.db_to_dict(conn).keys():
            return None
        else:
            cursor.execute('INSERT INTO commands (team_name, points) VALUES (?, ?)',
                           (name, points))
            conn.commit()

    def del_team_in_db(self,conn, name: str):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM commands WHERE team_name = ?', (name,))
        conn.commit()

    def add_points_to_team(self,conn, name: str, points_to_add: int):
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM commands WHERE team_name = ?", (name,))

        pr_points = int(cursor.fetchall())
        new_points = pr_points + points_to_add

        cursor.execute("UPDATE commands SET points = ? WHERE team_name = ?",
                       (new_points, name))
        conn.commit()

    def rem_points_to_team(self,conn, name: str, points_to_add: int):
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM commands WHERE team_name = ?", (name,))

        pr_points = int(cursor.fetchall())
        new_points = pr_points - points_to_add

        cursor.execute("UPDATE commands SET points = ? WHERE team_name = ?",
                       (new_points, name))
        conn.commit()

###############################################################







    def submit(self):
        commands = self.db_to_dict(conn)
        user_input = self.entry1.get() # Получаем текст из поля ввода
        commands = self.add_new_command(conn, user_input)
        print(commands)
        self.show_frame_menu()

    def rem_points(self):
        user_input = self.spinbox4.get() # Получаем текст из поля ввода
        user_input2 = int(self.spinbox2.get())  # Получаем int из поля ввода
        self.rem_points_to_command(conn,user_input,user_input2)


    def add_points(self):
        user_input = self.spinbox5.get()  # Получаем текст из поля ввода
        print(user_input)
        user_input2 = int(self.spinbox3.get())
        print(user_input2)# Получаем int из поля ввода
        self.add_points_to_command(conn,user_input, user_input2,)
    def show_value(self):
        # Получаем текущее значение из Spinbox и выводим его
        command = self.spinbox6.get()
        print("Выбранное значение:", command)
        self.delete_command(conn,command)
        self.show_frame_menu()

    # Метод для отображения меню
    def show_frame_menu(self):
        self.frame_add_command.pack_forget()
        self.frame_delete_command.pack_forget()
        self.frame_list_command.pack_forget()
        self.frame_change_command.pack_forget()
        self.frame_output_of_results.pack_forget()
        self.frame_change_command1.pack_forget()
        self.frame_change_command2.pack_forget()
        self.frameee_9.pack_forget()
        self.frameee_10.pack_forget()
        self.frame_menu.pack()

    # Метод для отображения раздела "добавить команду"
    def show_frame_add_command(self):
        self.frame_menu.pack_forget()
        self.frame_add_command.pack()

    # Метод для отображения раздела "удалить команду"
    def show_frame_delete_command(self):
        self.frame_menu.pack_forget()
        self.spinbox6.pack_forget()
        self.spinbox6 = tk.Spinbox(self.frame_delete_command, values=list(self.db_to_dict(conn)))
        self.spinbox6.pack(fill='both', padx=30, pady=25)
        self.button13.pack_forget()
        self.button13 = tk.Button(self.frame_delete_command, text="удалить", font=("Arial", 16),
                                  command=self.show_value)
        self.button13.bind("<Enter>", on_enter)
        self.button13.bind("<Leave>", on_leave)
        self.button13.pack(fill='both', padx=30, pady=4)
        self.button8.pack_forget()
        self.button8 = tk.Button(self.frame_delete_command, text="назад в меню", font=("Arial", 16),
                                 command=self.show_frame_menu)
        self.button8.bind("<Enter>", on_enter)
        self.button8.bind("<Leave>", on_leave)
        self.button8.pack(fill='both', padx=30, pady=4)
        self.frame_delete_command.pack()

    # Метод для отображения раздела "список команд"
    def show_frame_list_command(self):
        self.frame_menu.pack_forget()
        self.frame_list_command.pack()

    # Метод для отображения раздела "изменение балов команд"
    def show_frame_change_command(self):
        self.frame_menu.pack_forget()
        self.frame_change_command.pack()

    # Метод для отображения раздела "вывод результатов"
    def show_frame_output_of_results(self):
        self.frame_menu.pack_forget()
        self.frame_output_of_results.pack()

    # под-фреймы для изменения балов
    def show_frame_change_command1(self):
        commands = self.db_to_dict(conn)
        self.spinbox5.pack_forget()
        self.spinbox5 = tk.Spinbox(self.frame_change_command1, values=list(commands.keys()))
        self.spinbox5.pack()
        self.spinbox3.pack_forget()
        self.spinbox3 = Spinbox(self.frame_change_command1, from_=0, to=10)
        self.spinbox3.pack()
        self.button21.pack_forget()
        self.button21 = tk.Button(self.frame_change_command1, text="добавить", font=("Arial", 16),command=self.add_points)
        self.button21.pack()
        self.button18.pack_forget()
        self.button18 = tk.Button(self.frame_change_command1, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button18.pack()
        self.frame_change_command.pack_forget()
        self.frame_change_command1.pack()
    def show_frame_change_command2(self):
        commands = self.db_to_dict(conn)
        self.spinbox4.pack_forget()
        self.spinbox4 = tk.Spinbox(self.frame_change_command2,values=list(commands.keys()))
        self.spinbox4.pack()
        self.spinbox2.pack_forget()
        self.spinbox2 = tk.Spinbox(self.frame_change_command2,from_=0,to=10)
        self.spinbox2.pack()
        self.button20.pack_forget()
        self.button20 = tk.Button(self.frame_change_command2, text="удалить", font=("Arial", 16), command=self.rem_points)
        self.button20.pack()
        self.button19.pack_forget()
        self.button19 = tk.Button(self.frame_change_command2, text="назад в меню", font=("Arial", 16),command=self.show_frame_menu)
        self.button19.pack()
        self.frame_change_command.pack_forget()
        self.frame_change_command2.pack()

    def frame_9(self):
        text= '\n'.join(self.get_names_commands_by_alphabet(self.db_to_dict(conn)))
        self.label12.pack_forget()
        self.label12 = tk.Label(self.frameee_9, text=text, font=("Helvetica", 23))
        self.label12.pack(fill='both', padx=30, pady=25)
        self.frame_list_command.pack_forget()
        self.frameee_9.pack()

    def frame_10(self):
        text = self.get_names_commands_by_points(self.db_to_dict(conn))
        self.label13.pack_forget()
        self.label13 = tk.Label(self.frameee_10, text=text, font=("Helvetica", 23))
        self.label13.pack(fill='both', padx=30, pady=25)
        self.frame_list_command.pack_forget()
        self.frameee_10.pack()

    def on_resize(self, event):
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        self.label1.config(font=("Trebuchet MS", int(min(width, height) // 20), "bold"))
        self.label2.config(font=("Trebuchet MS", int(min(width, height) // 20), "bold"))
        self.label3.config(font=("Trebuchet MS", int(min(width, height) // 20), "bold"))
        self.label4.config(font=("Trebuchet MS", int(min(width, height) // 20), "bold"))
        self.label5.config(font=("Trebuchet MS", int(min(width, height) // 20), "bold"))
        self.label6.config(font=("Trebuchet MS", int(min(width, height) // 20), "bold"))
        self.label7.config(font=("Trebuchet MS", int(min(width, height) // 26), "bold"))
        self.label8.config(font=("Trebuchet MS", int(min(width, height) // 20), "bold"))
        self.label9.config(font=("Trebuchet MS", int(min(width, height) // 26), "bold"))
        self.label10.config(font=("Trebuchet MS", int(min(width, height) // 26), "bold"))
        self.label11.config(font=("Trebuchet MS", int(min(width, height) // 26), "bold"))
        self.button1.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button2.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button3.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button4.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button5.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button6.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button7.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button8.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button9.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button10.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="#DCDCDC")
        self.button11.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button12.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button13.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="lightgray")
        self.button14.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.button15.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.button16.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="#B5B8B1")
        self.button17.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="#B5B8B1")
        self.button18.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.button19.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.button20.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.button21.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.button22.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.button23.config(font=("Helvetica", int(min(width, height) // 35), "bold"),bg="lightgray")
        self.entry1.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="white")
        self.spinbox6.config(font=("Helvetica", int(min(width, height) // 25), "bold"), bg="white")
        self.spinbox4.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="white")
        self.spinbox5.config(font=("Helvetica", int(min(width, height) // 25), "bold"), bg="white")
        self.spinbox2.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="white")
        self.spinbox3.config(font=("Helvetica", int(min(width, height) // 25), "bold"),bg="white")

root = tk.Tk()
root.geometry("800x600")
app = AdaptiveWindow(root)
root.mainloop()

