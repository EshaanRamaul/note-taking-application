import sqlite3 
from dataclasses import dataclass
from typing import List, Optional

@dataclass
#dataclass decorator allows for the creation of an object/instance of the class without the need for a separate initialization function definition
class Note:
    id: int
    title: str
    content: str
class NoteDAO:
    NOTES: List[Note] = []
    @staticmethod
    def addNote(title:str, content:str) -> None:#for creating memo as parameters
        try:
            conn = sqlite3.connect('notes.db')
            cursor = conn.cursor()
            #creating sql statement and executing data insertion into database
            sql_statement = "INSERT INTO note (title, content) VALUES (?, ?)"
            cursor.execute(sql_statement, (title,content))
            conn.commit()
            
            cursor.close()
        except sqlite3.IntegrityError:#error
            print("Error while inserting note.")

    @staticmethod
    def getNotes(limit: int = -1) -> list[Note]:#fetch data from note table and create Note object
        notes = []
        try:
            conn = sqlite3.connect('notes.db')
            cursor = conn.cursor()
            sql_statement = "SELECT * FROM note LIMIT ?"
            cursor.execute(sql_statement, (limit,))
            records = cursor.fetchall()
            for record in records:
                #creating Note object
                note = Note(*record)#asterisk unpacks the record elements
                notes.append(note)#add to note object
        except sqlite3.Error as e:
            print("Error while fetching notes:", e)
        finally:
            cursor.close()
            conn.close()
            
        return notes
    
    #
    @staticmethod
    def noteSearch(title: str) -> Optional[Note]:
        try:
            conn = sqlite3.connect('notes.db')
            cursor = conn.cursor()
            statement = "SELECT * FROM note WHERE title = ?"
            cursor.execute(statement, (title,))
            record = cursor.fetchone()
            if record:
                return Note(*record)
            else:
                return None
        except sqlite3.Error as e:
            print("Error while searching note:", e)
        finally:
            cursor.close()
            conn.close()

    #phase 5 
    def editNote(note: Note)->Note:
        try:
            conn=sqlite3.connect('notes.db')
            cursor=conn.cursor()
            sql_statment="UPDATE note SET content= ? WHERE id= ?"
            cursor.execute(sql_statment,(note.content,note.id))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error while editing note:",e)
    
    #phase 6 deletion
    def noteDelete(title: str)->int:
        try:
            conn=sqlite3.connect('notes.db')
            cursor=conn.cursor()
            sql_command="DELETE FROM note WHERE title=?"
            cursor.execute(sql_command,(title,))
            deleted_row=cursor.rowcount

            #reset autoincrement
            cursor.execute("SELECT COUNT(*) FROM note")
            count=cursor.fetchone()[0]
            if count==0:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='note'")

            conn.commit()
            conn.close()
            deleted_row=cursor.rowcount
        except sqlite3.Error as e:
            print("Error while deleting note", e)
            deleted_row=0
        finally:
            conn.close()
        return deleted_row