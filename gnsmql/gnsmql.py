import json
from pathlib import Path

class gnsmql_database:
    def __init__(self, db_path='db'):
        self.db_path = Path(db_path)
        self.db_path.mkdir(parents=True, exist_ok=True)
    
    def create_database(self, name):
        path = self.db_path / name
        path.mkdir(exist_ok=True)
    
    def create_table(self, database, table_name):
        db_path = self.db_path / database
        if not db_path.exists():
            raise ValueError(f"Database '{database}' does not exist.")
        table_path = db_path / f"{table_name}.zzz"
        table_path.touch(exist_ok=True)
    
    def insert_into_table(self, database, table_name, data):
        table_path = self.db_path / database / f"{table_name}.zzz"
        if not table_path.exists():
            raise ValueError(f"Table '{table_name}' does not exist in database '{database}'.")
        
        with open(table_path, "r+", encoding="utf-8") as file:
            existing_data = file.read()
            entries = json.loads(existing_data) if existing_data else []
            entries.append(data)
            file.seek(0)
            json.dump(entries, file)
    
    def select_from_table(self, database, table_name):
        table_path = self.db_path / database / f"{table_name}.zzz"
        if not table_path.exists():
            raise ValueError(f"Table '{table_name}' does not exist in database '{database}'.")
        
        with open(table_path, "r", encoding="utf-8") as file:
            existing_data = file.read()
            entries = json.loads(existing_data) if existing_data else []
            return entries
        
class gnsmqlConnector:
    def __init__(self, db_path='db'):
        self.db = gnsmql_database(db_path)

    def execute(self, command):
        try:
            if command.upper().startswith("CREATE DATABASE"):
                self.create_database(command)
            elif command.upper().startswith("CREATE TABLE"):
                self.create_table(command)
            elif command.upper().startswith("INSERT INTO"):
                self.insert_into(command)
            elif command.upper().startswith("SELECT * FROM"):
                self.select_from(command)
            else:
                print("Command not recognized.")
        except Exception as e:
            print(f"Error executing command: {e}")

    def create_database(self, command):
        _, _, database_name = command.partition("CREATE DATABASE")
        database_name = database_name.strip().rstrip(";")
        self.db.create_database(database_name)
        print(f"Database '{database_name}' created.")

    def create_table(self, command):
        _, _, table_info = command.partition("CREATE TABLE")
        database_name, _, table_name = table_info.partition(".")
        database_name = database_name.strip()
        table_name = table_name.strip().rstrip(";")
        self.db.create_table(database_name, table_name)
        print(f"Table '{table_name}' created in database '{database_name}'.")

    def insert_into(self, command):
        _, _, table_info = command.partition("INSERT INTO")
        table_info, _, data = table_info.partition("VALUES")
        database_name, _, table_name = table_info.partition(".")
        database_name = database_name.strip()
        table_name = table_name.strip()
        data = json.loads(data.strip().lstrip("(").rstrip(");"))
        self.db.insert_into_table(database_name, table_name, data)
        print(f"Data inserted into table '{table_name}' in database '{database_name}'.")

    def select_from(self, command):
        _, _, table_info = command.partition("SELECT * FROM")
        database_name, _, table_name = table_info.partition(".")
        database_name = database_name.strip()
        table_name = table_name.strip().rstrip(";")
        records = self.db.select_from_table(database_name, table_name)
        print(f"Records from '{table_name}' in database '{database_name}': {records}")