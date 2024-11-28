commands = {'ITeam': 0,'ATeam': 0}

def add_new_command(name:str,commands:dict)->dict:
    index_of_unicality = 0
    for command in commands.keys():
        if command == name:
            index_of_unicality += 1
    if index_of_unicality == 0:
        commands[name] = 0
    return commands

def delete_command(command, commands):
    del commands[command]
    return commands

def add_points_to_command(command, points, commands):
    commands[command] += points
    return commands

def rem_points_to_command(command, points, commands):
    commands[command] -= points
    return commands

def get_names_commands_by_alphabet(commands):
    names = []
    for command in commands.keys():
        names.append(command)
    print(sorted(names))
    return sorted(names)

def get_names_commands_by_points(commands):
    names_and_points = list(commands.keys())
    sorted_commands = sorted(names_and_points, key=lambda x: commands[x], reverse=True)
    result = []
    text = ''
    for command in sorted_commands:
        result.append((command, commands[command]))
    for team,points in result:
        text += f'{team} {str(points)} \n'
    return text

get_names_commands_by_points(commands)