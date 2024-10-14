#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.country import Country
from models.continent import Continent
import ipdb

def reset_database():
    Country.drop_table()
    Continent.drop_table()
    Country.create_table()
    Continent.create_table()

reset_database()

asia = Continent.create("Asia")
europe = Continent.create("Europe")
north_america = Continent.create("North America")
Country.create("United States", 2024, 5, north_america.id)
Country.create("Mexico", 2023, 10, north_america.id)
Country.create("Malaysia", 2019, 8, asia.id)
Country.create("Vietnam", 2016, 10, asia.id)
Country.create("Thailand", 2024, 10, asia.id)
Country.create("Myanmar", 2018, 8, asia.id)
Country.create("France", 2013, 7, europe.id)
Country.create("Belgium", 2013, 8, europe.id)
Country.create("Germany", 2013, 10, europe.id)

ipdb.set_trace()
