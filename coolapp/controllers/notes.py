from flask import Blueprint, jsonify, request

from coolapp.services.notes import NotesService


notes_controller = Blueprint(name='notes_controller', import_name=__name__)

db = []

@notes_controller.route("/")
def index():
    return jsonify(
        {
            "msg": "Hello world!"
        }
    ), 200


@notes_controller.route("/create_note", methods=['POST'])
def create_note():
    name = request.json.get("name")
    content = request.json.get("content")
    NotesService.create_note(name, content)
    return jsonify({
        "msg": "Note created"
    }), 201


@notes_controller.route("/get_all_notes", methods=['GET'])
def get_all_notes():
    return jsonify({
        "all_notes": NotesService.get_notes()
    }), 200


@notes_controller.route("/get_note", methods=['POST'])
def get_note():
    line_id = request.json.get("line_id")
    db = NotesService.get_note(line_id)
    return jsonify({
        "note": db[int(line_id)]
    }), 200
