from db_conn import DB
from menu_note import MenuNote

class Main:
    def __init__(self) -> None:    
        print("Program starting.")
        # 1. initialize
        DB.initializeDB()
        _menu = MenuNote()
        # 2. run
        _menu.activate()
        # 3. cleanup
        print("")
        print("Program ending.")
        return None
if __name__ == "__main__":
    app = Main()    