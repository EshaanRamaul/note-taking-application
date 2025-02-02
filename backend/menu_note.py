from model_note import Note
from kirje import KirjeDetails
from kirje import Kirje
from model_note import NoteDAO
# Temporary test variable NOTES
NOTES = [
    Note(1, "example", "Hello\nworld"),
    Note(2, "tomorrow", "eat\nplay\nsleep")
]
class MenuNote:
    def __init__(self) -> None:
        return None
    
    def askChoice(self) -> int:
        choice: int = -1
        feed = input("Your choice: ")
        if feed.isdigit():
            choice = int(feed)
        return choice
    
    def showOptions(self) -> None:
        print('Options:')
        print('1 - List notes')
        print('2 - View note')
        print('3 - Add note')
        print('4 - Edit note')
        print('5 - Delete note')
        print('0 - Exit')
        return None
    
    def listNotes(self) -> None:
        memos=NoteDAO.getNotes()
        if memos:
                rows=[]
                for memo in memos:
                    row= f"{memo.id} - {memo.title}"
                    rows.append(row)
                #Combine the lines into a single string
                content ='\n'.join(rows)
                #Kirje Object
                details = KirjeDetails(
                    content=content,
                    headers={
                        'ID': 'Title',
                        'title':' notes '
                    },
                    header_separation=" - ")
                memo_list=Kirje(details)
                memo_list.display("streamlined")
                rows.clear()
        else:
            print("There are no notes to display.")
        return None
    
    #re
    def viewNote(self) -> None:
            search=input("Search note by title: ")
            #one-way flag
            found_note=NoteDAO.noteSearch(search)
            if found_note:
                #create kirje object
                details = KirjeDetails(     
                    content=found_note.content,
                    headers={'ID': found_note.id,
                             'title':found_note.title
                    },
                    header_separation=" - "
                    )
                current_memo = Kirje(details)
                current_memo.display("default")
                
            if not found_note:
                print("Not found.")
    
    def addNote(self) -> None:
        title = input("Insert title: ")
        num_rows = int(input("Insert the amount of rows: "))
        rows = []
        for i in range(num_rows):
            row_content = input(f"Insert row {i + 1}: ")
            rows.append(row_content)
            #separated by new line
        content = '\n'.join(rows)
        
        NoteDAO.addNote(title,content)
        
        rows.clear()
        print("Note stored!")

    def editNote(self) -> None:
        title=input("Insert note title: ")
        #one way flag
        found_note= NoteDAO.noteSearch(title)
        
        if found_note:
            line=found_note.content.split('\n')
            edit_line=int(input(f"Insert row number to edit 1-{len(line)}, 0 to cancel: "))
            if edit_line == 0:
                print("Cancelled.")
            else:    
                line_index = edit_line - 1 
                new_line=input("Insert replacement row: ")
                line[line_index]=new_line
                new_content='\n'.join(line)
                found_note.content=new_content
                NoteDAO.editNote(found_note)
                print("Edit completed!")
                line.clear()
        else:
            print (f"'{title}' not found.")
            
    def deleteNote(self) -> None:
        title= input("Delete note (insert title): ")
        deleted_rows=NoteDAO.noteDelete(title)
        if deleted_rows == 1:
            print("Note deleted.")
        else:
            print(f"'{title}' not found.")

    def activate(self) -> None:
        while True:
            self.showOptions()
            choice = self.askChoice()
            if choice == 1:
                self.listNotes()
            elif choice == 2:
                self.viewNote()
            elif choice == 3:
                self.addNote()
            elif choice == 4:
                self.editNote()
            elif choice == 5:
                self.deleteNote()
            elif choice == 0:
                break
            print("")
        return None
