import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("Notatnik")
    print("1. Stwórz notatkę")
    print("2. Wyświetl notatki")
    print("3. Edytuj notatkę")
    print("4. Usuń notatkę")
    print("5. Zakończ")
    return input("Wybierz opcję: ")

def create_note():
    clear_screen()
    title = input("Podaj tytuł notatki: ")
    content = input("Podaj treść notatki: ")
    with open(f"{title}.txt", 'w', encoding='utf-8') as file:
        file.write(content)
    print("Notatka została stworzona.")
    input("Naciśnij Enter, aby kontynuować.")

def view_notes():
    clear_screen()
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if not files:
        print("Brak notatek.")
    else:
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
    input("Naciśnij Enter, aby kontynuować.")

def edit_note():
    clear_screen()
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if not files:
        print("Brak notatek do edycji.")
    else:
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
        choice = int(input("Wybierz numer notatki do edycji: ")) - 1
        if 0 <= choice < len(files):
            title = files[choice]
            with open(title, 'r', encoding='utf-8') as file:
                content = file.read()
            print(f"Obecna treść notatki ({title}):")
            print(content)
            new_content = input("Podaj nową treść notatki: ")
            with open(title, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print("Notatka została zaktualizowana.")
        else:
            print("Nieprawidłowy wybór.")
    input("Naciśnij Enter, aby kontynuować.")

def delete_note():
    clear_screen()
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if not files:
        print("Brak notatek do usunięcia.")
    else:
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
        choice = int(input("Wybierz numer notatki do usunięcia: ")) - 1
        if 0 <= choice < len(files):
            os.remove(files[choice])
            print("Notatka została usunięta.")
        else:
            print("Nieprawidłowy wybór.")
    input("Naciśnij Enter, aby kontynuować.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Nieprawidłowy wybór.")
            input("Naciśnij Enter, aby kontynuować.")

if __name__ == "__main__":
    main()
