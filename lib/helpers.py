# lib/helpers.py
from models.continent import Continent
from models.country import Country
from models.__init__ import CONN, CURSOR

def exit_program():
    print("Goodbye!")
    exit()

def initialize_continents():
    Continent.create_table()
    Continent.create("Asia", 48)
    Continent.create("Europe", 50)
    Continent.create("North America", 23)

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
        print(
            f"Continent {name_} not found. Please enter a continent you have visited before."
            )

def add_new_country():
    name = input("Which country would you like to add? ")
    year = input("What year did you visit? ")
    rating = input("What would you rate this country out of 10? ")
    continent = input("Which continent is this country located in? ")
    try:
        year = int(year)
        rating = int(rating)
        
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
            create_continent = input(f"Continent '{continent}' not found. "
                                     "Would you like to add it? (yes/no): ").strip().lower()
            if create_continent == "yes":
                Continent.create(continent)
                continent_id = CURSOR.lastrowid
                print(f"Continent {continent} successfully added!")
            else:
                raise ValueError("Cannot create a country without a continent.")

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
        print(f'{name_} not found in visited countries. Please try again.')

def add_new_continent():
    name = input("Which continent would you like to add? ")
    Continent.create(name)
    print(
        f"{name} successfully added to Continents."
        )

def delete_continent():
    name_ = input("Which continent would you like to delete? ")
    if continent := Continent.find_by_name(name_):
        continent.delete()
        print(f'{name_} has been removed from visited continents.')
    else:
        print(f'{name_} not found in visited continents. Please try again.')

def display_country_details():
    name_ = input("Enter a country you've visited to see details: ")
    if country := Country.find_by_name(name_):
        print(
            f"You last visited {country.name} "
            f"in {country.year}. "
            f"You gave your experience a rating of {country.rating}/10.")
    else:
        print(f"Bummer, you haven't visited {name_} yet! Please try again.")



def display_continent_details():
    name_ = input("Enter a continent you've visited to see details: ")
    if continent := Continent.find_by_name(name_):
        num_countries = len(continent.countries())
        print(
            f"You've visited {num_countries} countries in {continent.name}."
        )
        countries = continent.countries()
        for country in countries:
            print(country.name)

    else:
        print(f"Bummer, you haven't visited {name_} yet! Please try again.")