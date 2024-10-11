from models.__init__ import CURSOR, CONN
from models.continent import Continent

class Country:

    all = {}
    
    def __init__(self, name, year, rating, continent_name, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.rating = rating
        self.continent_name = continent_name

    def __repr__(self):
        return(
            f"<Country {self.id}: {self.name}, visited in {self.year}, rated {self.rating}/10 , " +
            f"Continent: {self.continent_name}>"
        )
    
    # SET PROPERTIES FOR CLASS ATTRIBUTES
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else: 
            raise ValueError(
                "Name must be a non-empty string."
            )
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if isinstance(year, int) and year >=1904:
            self._year = year
        else:
            raise ValueError(
                "Please enter a valid year."
            )
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 0 <= rating <= 10:
            self._rating = rating
        else:
            raise ValueError(
                "Rating must be a number between 0 and 10."
            )
    
    @property
    def continent_name(self):
        return self._continent_name
    
    @continent_name.setter
    def continent_name(self, continent_name):
        if continent_name in Continent.CONTINENTS:
            self._continent_name = continent_name
        else:
            raise ValueError(
                "Please enter a valid continent "
                "(Africa, Antarctica, Asia, North America, "
                "South America, Europe, or Australia)."
            )
    
    # CLASS METHOD - CREATE A COUNTRY TABLE
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY,
            name TEXT,
            year INTEGER,
            rating INTEGER,
            continent_name TEXT,
            FOREIGN KEY (continent_name) REFERENCES continents(name))    
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS countries;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO countries (name, year, rating, continent_name)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.year, 
                             self.rating, self.continent_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        sql = """
            DELETE FROM countries
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, year, rating, continent_name):
        country = cls(name, year, rating, continent_name)
        country.save()
        return country
    
    @classmethod
    def instance_from_db(cls, row):
        country = cls.all.get(row[0])
        if country:
            country.name = row[1]
            country.year = row[2]
            country.rating = row[3]
            country.continent_name = row[4]
        else:
            country = cls(row[1], row[2], row[3], row[4])
            country.id = row[0]
            cls.all[country.id] = country
        return country
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM countries
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM countries
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM countries
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    