from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from music.views import music
    app.register_blueprint(music)

register_blueprints(app)

if __name__ == '__main__':
    app.run(port=3000)
