def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Write name for searching"
        except KeyError:
            return "Contact not found"
        except Exception:
            return "An error occurred. Try again"

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact {name} already exists"
    else:
        contacts[name] = phone
        return f"Contact {name} is added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} is changed."


@input_error
def show_contact(args, contacts):
    name = args[0]
    return f"Contact {name}: {contacts[name]}"


def print_contacts(contacts):
    if contacts:
        for contact, phone in contacts.items():
            print(f"{contact}: {phone}")
    else:
        print("Contact list is empty")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == "all":
            print_contacts(contacts)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
