# lib/helpers.py
from models.continent import Continent
from models.country import Country
from models.__init__ import CONN, CURSOR

def exit_program():
    print("Goodbye!")
    exit()

def list_continents():
    continents = Continent.get_all()
    for continent in continents:
        print(continent.name)

def list_countries():
    countries = Country.get_all()
    for country in countries:
        print(country.name)

def list_continent_countries():
    name_ = input("Enter the name of the continent: ")
    if continent := Continent.find_by_name(name_):
        print(' ')
        print(f"You've visited the following countries in {continent.name}:")
        print(' ')
        countries = continent.countries()
        for country in countries:
            print(country.name)
    else:
        print(f"{name_} not found in visited continents.")
        print("Please enter a continent you have visited before and check spelling.")

def list_countries_by_year():
    year_ = input("Enter year of visit using numeric digits: ")
    if year_.isdigit():
        if countries := Country.find_by_year(year_):
            print(' ')
            print(f"In {year_} you visited: ")
            for country in countries:
                print(country.name)
        else:
            print(' ')
            if int(year_) > 2024:
                print(
                    f"{year_} is in the future. "
                    "This is a travel tracker, not a fortune teller!")
                print("Please input the current year or a previous year.")
            else:
                print(f"You did not visit any countries in {year_}.")
    else:
        print("Please input a year consisting of numeric digits.")

def add_new_country():
    name = input("Which country would you like to add? ")

    
    while True:
        try:
            year = int(input("What year did you visit? "))
            break
        except ValueError:
            print(' ')
            print("Please input a year consisting of numeric digits.")
            print(' ')
    
    while True:
        try:
            rating = int(input("What would you rate this country out of 10? "))
            break
        except ValueError:
            print(' ')
            print("Please enter a number between 1 and 10.")
            print(' ')
    
    continent = input("Which continent is this country located in? ")

    try:
        
        sql = """
            SELECT id
            FROM continents
            WHERE LOWER(name) = LOWER(?)
        """
        CURSOR.execute(sql, (continent,))
        continent_result = CURSOR.fetchone()

        if continent_result:
            continent_id = continent_result[0]
        else:
            while True:
                create_continent = input(f"Continent '{continent}' not found. "
                                        "Would you like to add it? (yes/no): ").strip().lower()
                if create_continent == "yes":
                    Continent.create(continent)
                    continent_id = CURSOR.lastrowid
                    print(f"Continent {continent} successfully added!")
                elif create_continent == "no":
                    print(' ')
                    print("You must choose an existing continent or create a continent to add a country.")
                    return
                else:
                    print(' ')
                    print("Please type yes or no.")
                    print(' ')

        country = Country.create(name, year, rating, continent_id)
        print(f"{country.name} successfully added!")
    except Exception as exc:
        print("Error: ", exc)

def delete_country():
    name_ = input("Which country would you like to delete? ")
    if country := Country.find_by_name(name_):
        country.delete()
        print(f"{name_} has been removed from visited countries.")
    else:
        print(f'{name_} not found in visited countries.')
        print("Please enter a country you have visited before and check spelling.")

def add_new_continent():
    try:
        name = input("Which continent would you like to add? ")
        Continent.create(name)
        print(
            f"{name} successfully added to Continents."
            )
    except Exception as exc:
        print("Error:", exc)

def delete_continent():
    name_ = input("Which continent would you like to delete? ")
    if continent := Continent.find_by_name(name_):
        continent.delete()
        print(f'{name_} has been removed from visited continents.')
    else:
        print(f'{name_} not found in visited continents.')
        print("Please enter a continent you have visited before and check spelling.")

def display_country_details():
    name_ = input("Enter a country you've visited to see details: ")
    if country := Country.find_by_name(name_):
        print(
            f"You last visited {country.name} "
            f"in {country.year}. "
            f"You gave your experience a rating of {country.rating}/10.")
    else:
        print(f'{name_} not found in visited countries.')
        print("Please enter a country you have visited before and check spelling.")



def display_continent_details():
    name_ = input("Enter a continent you've visited to see details: ")
    if continent := Continent.find_by_name(name_):
        num_countries = len(continent.countries())
        print(' ')
        print(
            f"You've visited {num_countries} countries in {continent.name}."
        )

    else:
        print(f'{name_} not found in visited continents.')
        print("Please enter a continent you have visited before and check spelling.")

