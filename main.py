from coolapp import app

def register_blueprints(app):
    from coolapp.controllers.notes import notes_controller
    app.register_blueprint(notes_controller, url_prefix='/notes')

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='0.0.0.0')