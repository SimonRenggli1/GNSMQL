import json
from pathlib import Path

class GNSMQL:
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
