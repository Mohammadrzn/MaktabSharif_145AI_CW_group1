student_info = {}

def add():
    global student_info
    try:
        name = input("Please enter your name: ")
        student_info[name] = float(input("Please enter your grade: "))
    except ValueError:
        print("Please enter a numeric value")
        add()

def save():
    with open("student_info.txt", "a+") as file:
        for name in student_info:
            file.write(f"{name}: {student_info[name]}\n")
    student_info.clear()

def show():
    with open("student_info.txt", "r") as file:
        print(file.read())

def search(text):
    with open("student_info.txt", "r") as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            if text.lower() in line.lower():
                print(line)

while True:
    command = input("Please enter your command (add, save, show, search, exit): ").lower()
    match command:
        case "add":
            add()
        case "save":
            save()
        case "show":
            show()
        case "search":
            search_text = input("Please enter your search query: ")
            search(search_text)
        case "exit":
            break
