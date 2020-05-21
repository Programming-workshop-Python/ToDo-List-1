from coolapp.repositories.notes import NotesRepository

class NotesService:
    @staticmethod
    def create_note(title, text):
        NotesRepository.create_note(title, text)

    @staticmethod
    def get_notes():
        notes = NotesRepository.get_all_notes()
        return notes

    @staticmethod
    def get_note(line_id):
        note = NotesRepository.get_note(line_id)
        return note