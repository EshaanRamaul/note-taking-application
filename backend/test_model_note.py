from model_note import NoteDAO
NoteDAO.addNote('first_note', 'hello\nworld')
NoteDAO.addNote('second_note','This\nis\nmy\nsecond\nnote.')
NoteDAO.getNotes()