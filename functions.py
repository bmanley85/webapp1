FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads file then returns a list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Opens a file then writes list into it
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# only executed when this script is executed as the main file
# when this file is imported via another script, this is not run
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
