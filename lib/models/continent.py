from models.__init__ import CURSOR, CONN

class Continent:

    all = {}

    def __init__(self, name, num_countries, id=None):
        self.id = id
        self.name = name
        self.num_countries = num_countries

    def __repr__(self):
        return f"<Continent {self.id}: {self.name}, {self.num_countries} countries>"
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Continent name must be a non-empty string."
            )
        
    @property
    def num_countries(self):
        return self._num_countries
    
    @num_countries.setter
    def num_countries(self, num_countries):
        if isinstance(num_countries, int):
            self._num_countries = num_countries
        else:
            raise ValueError(
                "Number of countries must be an integer."
            )
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS continents (
            id INTEGER PRIMARY KEY,
            name TEXT,
            num_countries INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS continents;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO continents (name, num_countries)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.num_countries))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, num_countries):
        continent = cls(name, num_countries)
        continent.save()
        return continent 
    
    def update(self):
        sql = """
            UPDATE continents
            SET name = ?, num_countries = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.num_countries, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM continents
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        continent = cls.all.get(row[0])
        if continent:
            continent.name = row[1]
            continent.num_countries = row[2]
        else:
            continent = cls(row[1], row[2])
            continent.id = row[0]
            cls.all[continent.id] = continent
        return continent

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM continents
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * 
            FROM continents
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def countries(self):
        from models.country import Country
        sql = """
            SELECT * FROM countries
            WHERE continent_name = ?
        """
        rows = CURSOR.execute(sql, (self.name,)).fetchall()

        return [
            Country.instance_from_db(row) for row in rows
        ]