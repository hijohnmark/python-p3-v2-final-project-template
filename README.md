# Travel Tracker - A Streamlined CLI Travel Tracking Tool

Travel Tracker is an intuitive CLI that allows you to keep track of the countries you've visited all around the world. You can organize these countries by continent, rate your experiences there, and add and delete entries as you travel to exciting new destinations.

## CLI Overview

The CLI takes the user through a series of logical steps to add, remove, and view information about database entries related to countries and continents visited. The main menu allows the user to exit the program, or navigate to either the countries or continents menu. In each of these menus, the user can easily add, delete, or view information about any entries in the database. Every menu allows the user to navigate back to the main menu, or to the countries or continents menu direction (eliminating the need to step back and then forward again).

This CLI is achieved by implementing a Country and Continent model, where one continent may contain many countries, and each country is given a foreign key that references the continent it belongs to.

### Continent Model
The `continent.py` file contains the Continent class and its methods, which allow it to create a database of visited continents. In addition, this class takes name and num_countries (the number of countries in that continent) as attritubes, with an optional id attribute given a default value of 0.

The Continent class contains the following methods: 

1. **`__init__(self, name, num_countries, id=None)`**: Initializes a new `Continent` object with a name, number of countries, and optionally an ID.
   
2. **`__repr__(self)`**: Returns a string representation of the `Continent` object with its ID, name, and number of countries.

3. **`name(self)` (property)**: Retrieves the name of the continent.

4. **`name(self, name)` (setter)**: Sets the name of the continent if it is valid, raising a `ValueError` for invalid continent names.

5. **`num_countries(self)` (property)**: Retrieves the number of countries in the continent.

6. **`num_countries(self, num_countries)` (setter)**: Sets the number of countries in the continent, raising a `ValueError` if the input is not an integer.

7. **`create_table(cls)`**: Creates a SQL table for storing continents if it does not already exist. 

8. **`drop_table(cls)`**: Drops the SQL table for continents if it exists.

9. **`save(self)`**: Saves the current `Continent` instance to the database and updates its ID.

10. **`create(cls, name, num_countries)`**: Creates a new `Continent` instance, saves it to the database, and returns the instance.

11. **`update(self)`**: Updates the database entry for the current `Continent` instance.

12. **`delete(self)`**: Deletes the current `Continent` instance from the database and removes it from the `all` dictionary.

13. **`instance_from_db(cls, row)`**: Retrieves a `Continent` instance from the database or creates one from a database row.

14. **`get_all(cls)`**: Retrieves all continent records from the database and returns them as `Continent` instances.

15. **`find_by_name(cls, name)`**: Finds and returns a `Continent` instance from the database based on the continent name.

16. **`countries(self)`**: Retrieves and returns all countries associated with the continent from the database.

### Country Model

The `country.py` file contains the Country class and its methods, which allow it to create a database of visited continents. In addition, this class takes name, year, rating, and continent_name attributes, with an optional id attribute given a default value of 0.

The Country class contains the following methods: 

1. **`__init__(self, name, year, rating, continent_name, id=None)`**: Initializes a new `Country` object with a name, year of visit, rating, continent name, and optionally an ID.

2. **`__repr__(self)`**: Returns a string representation of the `Country` object, including its ID, name, year of visit, rating, and continent name.

3. **`name(self)` (property)**: Retrieves the name of the country.

4. **`name(self, name)` (setter)**: Sets the name of the country, raising a `ValueError` if the name is not a valid non-empty string.

5. **`year(self)` (property)**: Retrieves the year the country was visited.

6. **`year(self, year)` (setter)**: Sets the year the country was visited, raising a `ValueError` if the year is not a valid integer or is before 1904.

7. **`rating(self)` (property)**: Retrieves the rating of the country.

8. **`rating(self, rating)` (setter)**: Sets the rating of the country, raising a `ValueError` if the rating is not an integer between 0 and 10.

9. **`continent_name(self)` (property)**: Retrieves the continent name of the country.

10. **`continent_name(self, continent_name)` (setter)**: Sets the continent name, raising a `ValueError` if the continent name is not a valid option from the predefined list.

11. **`create_table(cls)`**: Creates a SQL table for storing countries, linking each country to a continent.

12. **`drop_table(cls)`**: Drops the SQL table for countries if it exists.

13. **`save(self)`**: Saves the current `Country` instance to the database and updates its ID.

14. **`delete(self)`**: Deletes the current `Country` instance from the database and removes it from the `all` dictionary.

15. **`create(cls, name, year, rating, continent_name)`**: Creates a new `Country` instance, saves it to the database, and returns the instance.

16. **`instance_from_db(cls, row)`**: Retrieves a `Country` instance from the database or creates one from a database row.

17. **`get_all(cls)`**: Retrieves all country records from the database and returns them as `Country` instances.

18. **`find_by_id(cls, id)`**: Finds and returns a `Country` instance from the database based on the country ID.

19. **`find_by_name(cls, name)`**: Finds and returns a `Country` instance from the database based on the country name.


### Helpers

The `helpers.py` file contains all methods accessed by the CLI. It contains the following methods:


1. **`helper_1()`**: Prints a message indicating that a useful function is being performed.

2. **`exit_program()`**: Prints a goodbye message and exits the program.

3. **`initialize_continents()`**: Creates the continents table and inserts Asia, Europe, and North America into the database.

4. **`list_continents()`**: Retrieves and prints the names of all continents from the database.

5. **`list_countries()`**: Retrieves and prints the names of all countries from the database.

6. **`list_continent_countries()`**: Prompts for a continent name, then retrieves and prints all countries associated with that continent from the database.

7. **`add_new_country()`**: Prompts the user for details about a new country and adds it to the database.

8. **`delete_country()`**: Prompts for a country name and deletes the corresponding country from the database if it exists.

9. **`add_new_continent()`**: Prompts the user for a continent name and adds the corresponding continent to the database.

10. **`delete_continent()`**: Prompts for a continent name and deletes the corresponding continent from the database if it exists.

11. **`display_country_details()`**: Prompts for a country name and displays its visit year and rating if the country exists in the database.

12. **`display_continent_details()`**: Prompts for a continent name and displays the number of countries in that continent if it exists in the database.


### CLI 

The `cli.py` file contains the menu and navigation structure of this program. These menus are organized via the following methods:

1. **`main()`**: Continuously displays the opening menu and handles user input to navigate to the countries or continents menu, or exit the program.

2. **`opening_menu()`**: Displays the main menu options for exiting the program or navigating to the countries or continents menu.

3. **`countries_menu()`**: Displays a menu of options related to countries, allowing the user to view, add, or delete countries, or navigate to the continents menu or main menu.

4. **`continents_menu()`**: Displays a menu of options related to continents, allowing the user to view details, add or delete continents, or navigate to the countries menu or main menu.

5. **`after_results_menu()`**: Displays options to go back to the previous menu or return to the main menu after a result is shown or an action is completed.


---

## Planned features

The following features are planned for future development phases:

- Organize all countries by most recently visited
- Update information about country
- Add multiple visits per country and years visited
- Show percentage of countries visited within a content
- Color code continents by how many countries visited: Red (0-24%) > Orange (25-49%) > Yellow (50-75%) > Green (76-99%) > Blue (100%)
- Auto-add continents when countries are added that include a continent that has not yet been added to the database.