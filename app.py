from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post", methods=["POST"])
def criar_post():
    destino = request.form.get("destino")
    planejado = request.form.get("planejado")
    real = request.form.get("real")
    comentario = request.form.get("comentario")

    if not destino or not planejado or not real or not comentario:
        return redirect("/")

    novo_post = {
        "destino": destino,
        "planejado": planejado,
        "real": real,
        "comentario": comentario
    }
    posts.append(novo_post)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)