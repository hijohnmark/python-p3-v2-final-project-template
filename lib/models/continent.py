from models.__init__ import CURSOR, CONN

class Continent:

    all = {}
    
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        

    def __repr__(self):
        return f"<Continent {self.id}: {self.name}>"
    
    # SET PROPERTIES FOR CLASS ATTRIBUTES
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError(
                "Please enter a continent name with at least one alphanumeric character."
            )
        
        
    # CLASS METHOD - CREATE A TABLE   
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS continents (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    # CLASS METHOD - DROP TABLE
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS continents;
        """
        CURSOR.execute(sql)
        CONN.commit()

    # SAVE METHOD
    def save(self):
        sql = """
            INSERT INTO continents (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    # CLASS METHOD - CREATE ENTRY
    @classmethod
    def create(cls, name):
        continent = cls(name)
        continent.save()
        return continent 
    
    # UPDATE METHOD
    def update(self):
        sql = """
            UPDATE continents
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    # DELETE METHOD
    def delete(self):
        sql = """
            DELETE FROM continents
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    # CLASS METHOD - INSTANCE FROM DB
    @classmethod
    def instance_from_db(cls, row):
        continent = cls.all.get(row[0])
        if continent:
            continent.name = row[1]
        else:
            continent = cls(row[1])
            continent.id = row[0]
            cls.all[continent.id] = continent
        return continent

    # CLASS METHOD - GET ALL
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM continents
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    # CLASS METHOD - FIND BY NAME
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * 
            FROM continents
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    # GET ALL COUNTRIES WITHIN A GIVEN CONTINENT
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