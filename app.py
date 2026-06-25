from flask import Flask, render_template
from database import db
from models import Usuario, Experiencia, Comentario

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tripsinsight.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "tripsinsight-secreto"

db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)