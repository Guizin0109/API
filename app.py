from flask import Flask, jsonify
import os

app = Flask(__name__)

Filmes = [
    {"id": 1, "nome": "Matrix"},
    {"id": 2, "nome": "Interestelar"},
    {"id": 3, "nome": "Avatar"}
]

@app.route("/")
def home():
    return "API Flask rodando!"

@app.route("/Filmes", methods=["GET"])
def listar_Filmes():
    return jsonify(Filmes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)