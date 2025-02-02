from flask import Flask, request, jsonify
from backend.model_note import NoteDAO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = NoteDAO.getNotes()
    return jsonify([note.__dict__ for note in notes])

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.json()
    title = data.get('title')
    content= data.get('content')
    NoteDAO.addNote(title, content)
    return jsonify({'message': 'Note added successfully'}), 201 

@app.route('/api/notes/<int:id>', methods=['DELETE'])
def delete_note(note_id):
        deleted_rows=NoteDAO.noteDelete(note_id)
        if deleted_rows:
            return jsonify({'message': 'Note deleted'}), 200
        else:
            return jsonify({'message': 'Note not found'}), 404
        
if __name__ == '__main__':
    app.run(debug=True)