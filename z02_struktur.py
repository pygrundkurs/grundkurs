todos = [{'number': 1, 'title': 'Beispielaufgabe', 'done': False}]


def get_todos(done=False):
    return todos


def save_todos():
    pass


def load_todos():
    with open('todos.csv') as f:
        zeile = f.readline()

        # Python lernen,False
        while zeile is not None:
            spalten = zeile.split(',')
            todos.append({
                'title': spalten[0],
                'done': spalten[1],
            })


def add_todo():
    title = input('Titel der Aufgabe?')
    todos.append({
        'title': title
    })

    save_todos()
    return todos


def del_todo(titel):
    # Aufgabe suchen und diese löschen
    save_todos()


def done_todo(titel):
    # Aufgabe suchen und done: True setzen
    save_todos()


def handle_hauptfenster():
    eingabe = input('1) Get TODO, 2) ADD TODO, 3) Del TODO, 4) TODO IS DONE ')

    if eingabe == '1':
        print(get_todos())
    elif eingabe == '2':
        print(add_todo())


load_todos()
handle_hauptfenster()
