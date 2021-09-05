"""File containing file to provide MySQL database functionality."""

import os, datetime, pymysql, sys

class MetaSingleton(type):
    """Limits number of of available connections to the database to only one."""
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances = super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def __init__(self) -> None:
        """Change directory to script_path. If database exists, create
        connection to it. If not, create a new database and connect to it.
        Create a table inside the database file called "table_1" if it doesn't
        exist already.
        """
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {
            self.table_name} (column_1 TEXT, column_2 INT, column_3 REAL"""
        self.cursor, self.connection = self.connect()
        self.table_name = "table_1"
        self.time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.cursor.execute(create_table_query)

    def connect(self) -> pymysql:
        """If no connection is active, create one."""
        if self.connection is None:
            self.connection = pymysql.connect("database_file.db")
            self.cursor = self.connection.cursor()
        return self.cursor, self.connection

    def store_to_table(self):
        """Store data into table."""
        column_1 = self.time
        column_2 = 45
        column_3 = 45.77
        store_query = f"""INSERT INTO {self.table_name} {
            column_1, column_2, column_3} VALUES(?,?,?)"""
        self.cursor.execute(store_query, (column_1, column_2, column_3))
        self.connection.commit()
    
    def select_from_table(self):
        """Select data from table and print to stdout."""
        select_query = f"""SELECT * FROM {self.table_name}"""
        self.cursor.execute(select_query)
        for instance in self.cursor.fetchall():
            print(instance)


if __name__ == "__main__":
    database = Database()
    database.store_to_table()
    database.select_from_table()

    if sys.exit():
        database.cursor.close()
        database.connection.close()
