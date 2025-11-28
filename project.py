import json
import re
import sys
import os

filepath = "phonebook.json"


def write(new_data):
    with open(filepath, "w") as file:
        json.dump(new_data, file, indent=4)


def append(append_data):
    data = read()
    data.append(append_data)
    write(data)


def read():
    with open(filepath, "r") as file:
        data = json.load(file)
        return data


def add(name, phone):
    if not os.path.exists(filepath):
        new_data = [{"name": name, "phone": phone}]
        write(new_data)
    else:
        append_data = {"name": name, "phone": phone}
        append(append_data)
    if os.path.exists(filepath):
        print(f"\n\nContact {name} is successfully added!")
    else:
        print("Error occured!!!")


def search(name):
    data = read()

    for entry in data:
        if entry["name"] == name.lower():
            return entry["phone"]
    return None


def list_contacts():
    data = read()
    print()
    for entry in data:
        print(entry["name"], " : ", entry["phone"])


def update(name, new_phone):
    data = read()
    for entry in data:
        if entry["name"].lower() == name.lower():
            entry["phone"] = new_phone
    write(data)


def delete(name):
    data = read()
    data2 = []
    for entry in data:
        if entry["name"].lower() == name.lower():
            continue
        else:
            data2.append(entry)
    write(data2)


def check_name(name):
    return bool(re.match(r"^\w{1,16}$", name))


def check_phone(phone):
    return bool(re.match(r"^\d{10}$", phone))


def check_file():
    return bool(os.path.exists(filepath))


def main():

    while True:
        print("\nWelcome to the Phone Book Application!\n")
        print("Available commands:\n")
        print("add : Add a new contact")
        print("search : Search for a contact by name")
        print("list : List all contacts")
        print("delete : Delete a contact")
        print("update : Update a contact's phone number")
        print("quit : Exit the application")

        cli = input("\nEnter your command:\n").strip().lower()
        if cli == "quit":
            print("Exiting...")
            break
            sys.exit()
        elif cli == "add":
            while True:
                name = input("Enter the Name of the contact: ")
                phone = input("Enter the phone Number: ")
                if check_name(name) and check_phone(phone):
                    break
                else:
                    print("Please Enter name and phone Again!")
            add(name, phone)

        elif cli == "search":
            if check_file():
                while True:
                    name = input("Enter the name of the contact to search: ")
                    if check_name(name):
                        break
                    else:
                        print("Please Enter name Again!")
                searched_phone = search(name)
                if searched_phone:
                    print(f"\nThe phone of {name} is {searched_phone}.\n")
                elif searched_phone == None:
                    print(f"\n{name} is not Found in the contacts.\n")
            else:
                print("There is no contact names to Search!")

        elif cli == "list":
            if check_file():
                list_contacts()
            else:
                print("The Contact list is empty!")

        elif cli == "delete":
            if check_file():
                while True:
                    name = input("Enter the name of the contact to delete: ")
                    if check_name(name):
                        break
                    else:
                        print("\nPlease Enter name Again!\n")
                delete(name)
            else:
                print("The contact list is empty!")

        elif cli == "update":
            if check_file():
                while True:
                    name = input("Enter the name of the contact to update: ")
                    new_phone = input("Enter the new phone Number: ")
                    if check_name(name) and check_phone(new_phone):
                        break
                    else:
                        print("Please Enter name and phone Again!")
                update(name, new_phone)
            else:
                print("The contact list is empty!")
        else:
            print("\n\nInvalid Command!\n\n")


if __name__ == "__main__":
    main()