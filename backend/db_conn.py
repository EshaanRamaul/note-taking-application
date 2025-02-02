import sys
import sqlite3

class DB:
    @staticmethod
    def loadSqlScript(filepath: str) -> str:#reads file and returns its content in a string format
        content=""
        try:
            with open(filepath, 'r', encoding="UTF-8") as file:
                content=file.read()
        except FileNotFoundError:
            
            print(f"Failed to read '{filepath}' file.")
            sys.exit(-1)
        return content

    @staticmethod
    def initializeDB() -> None:#to intialize database
        script= DB.loadSqlScript("./setup.sql")#filepath
        conn= sqlite3.connect("notes.db")
        cursor= conn.cursor()
        cursor.executescript(script)
        conn.commit
        cursor.close()