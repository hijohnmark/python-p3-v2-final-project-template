#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.country import Country
from models.continent import Continent

def reset_database():
    Country.drop_table()
    Continent.drop_table()
    Country.create_table()
    Continent.create_table()

    asia = Continent.create("Asia")
    europe = Continent.create("Europe")
    africa = Continent.create("Africa")
    Country.create("Ethiopia", 2024, 9, africa.id)
    Country.create("Morocco", 2023, 10, africa.id)
    Country.create("Malaysia", 2019, 8, asia.id)
    Country.create("Vietnam", 2016, 10, asia.id)
    Country.create("Thailand", 2024, 10, asia.id)
    Country.create("Myanmar", 2018, 8, asia.id)
    Country.create("France", 2013, 7, europe.id)
    Country.create("Belgium", 2013, 8, europe.id)
    Country.create("Germany", 2013, 10, europe.id)

breakpoint()