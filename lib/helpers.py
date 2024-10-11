# lib/helpers.py
from models.continent import Continent
from models.country import Country

def helper_1():
    print("Performing useful function#1.")


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
        countries = continent.countries()
        for country in countries:
            print(country.name)
    else:
        print(
            f"Continent {name_} not found. Please check your spelling."
            "Continent names are case-sensitive."
            )

def add_new_country():
    name = input("Which country would you like to add? ")
    year = input("What year did you visit? ")
    rating = input("What would you rate this country out of 10? ")
    continent_name = input("Which continent is this country located in? ")
    try:
        year = int(year)
        rating = int(rating)
        country = Country.create(name, year, rating, continent_name)
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
    if name == "Antarctica":
        Continent.create("Antarctica", 0)
        print("Brrrr! Antarctica has been added successfully.")
    elif name == "Africa":
        Continent.create("Africa", 54)
        print("It's time for Africa! Africa has been added successfully.")
    elif name == "Australia":
        Continent.create("Australia", 3)
        print("G'day mate! Australia has been added successfully.")
    elif name == "South America":
        Continent.create("South America", )
        print("Ándale! South America has been added successfully.")
    elif name == "North America":
        Continent.create("North America", 23)
        print("North America has been added successfully.")
    elif name == "Europe":
        Continent.create("Europe", 50)
        print("Europe has been added successfully.")
    elif name == "Asia":
        Continent.create("Asia", 48)
        print("Asia has been added successfully.")
    else:
        print(
            "Continent must be "
            "Africa, Antarctica, Asia, North America, "
            "South America, Europe, or Australia."
        )

def delete_continent():
    name_ = input("Which continent would you like to delete? ")
    if continent := Continent.find_by_name(name_):
        continent.delete()
        print(f'{name_} has been removed from visited continents.')
    else:
        print(f'{name_} not found in visited continents. Please try again.')

def display_country_details():
    name_ = input("Enter a country name to see details: ")
    if country := Country.find_by_name(name_):
        print(
            f"You last visited {country.name} "
            f"in {country.year}. "
            f"You gave your experience a rating of {country.rating}/10.")
    else:
        print(f"{name_} not found in visited countries. Please try again.")


def display_continent_details():
    name_ = input("Enfter a continent name to see details: ")
    if continent := Continent.find_by_name(name_):
        print(
            f"{continent.name} contains {continent.num_countries} countries."
        )
    else:
        print(f"{name_} not found in visited continents. Please try again.")