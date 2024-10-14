# lib/cli.py

from helpers import (
    exit_program,
    list_continents,
    list_countries,
    list_continent_countries,
    add_new_country,
    delete_country,
    add_new_continent,
    delete_continent,
    display_country_details,
    display_continent_details
)


def main():
    while True:
        opening_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            countries_menu()
        elif choice == "2":
            continents_menu()
        else:
            print("Invalid choice")

def opening_menu():
    print(' ')
    print('***************************')
    print("Welcome to Travel Tracker!")
    print('***************************')
    print(' ')
    print("Use this app to keep track of the cities and continents you've visited. ")
    print("Please select an option by number:")
    print(' ')
    print('--------------------------------------')
    print("0. Exit the program")
    print("1. Countries I've visited")
    print("2. Continents I've visited")
    print('--------------------------------------')
    
def countries_menu():
    while True:
        print(' ')
        print("**Countries I've Visited**")
        print(' ')
        list_countries()
        print(' ')
        print('--------------------------------------')
        print('Please select an option by number:')
        print(' ')
        print("1. Find countries visited by continent")
        print("2. View country details")
        print("3. Add country")
        print("4. Delete country")
        print("5. Continents I've visited")
        print("6. Main menu")
        print('--------------------------------------')
        print(' ')
        choice = input("> ")
        if choice == "1":
            list_continent_countries()
            after_results_menu()
        elif choice == "2":
            display_country_details()
            after_results_menu()
        elif choice == "3":
            add_new_country()
            after_results_menu()
        elif choice == "4":
            delete_country()
            after_results_menu()
        elif choice == "5":
            continents_menu()
        elif choice == "6":
            main()
        else:
            print("Invalid choice. Please try again!")

def continents_menu():
    while True:
        print(' ')
        print("**Continents I've Visited**")
        print(' ')
        list_continents()
        print(' ')
        print('--------------------------------------')
        print('Please select an option by number:')
        print(' ')
        print("1. Countries I've visited by continent")
        print("2. View continent details")
        print("3. Add continent")
        print("4. Delete continent")
        print("5. Main menu")
        print('--------------------------------------')
        print(' ')
        
        choice = input("> ")
        if choice == "1":
            list_continent_countries()
            after_results_menu()
        elif choice == "2":
            display_continent_details()
            after_results_menu()
        elif choice == "3":
            add_new_continent()
            after_results_menu()
        elif choice == "4":
            delete_continent()
            after_results_menu()
        elif choice == "5":
            main()
        else:
            print("Invalid choice. Please try again!")

def after_results_menu():
    while True:
        print(' ')
        print('--------------------------------------')
        print("Please select an option by number:")
        print(' ')
        print("1. Go back")
        print("2. Return to main menu")
        print('--------------------------------------')

        choice = input("> ")
        if choice == "1":
            return
        elif choice == "2":
            main()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
