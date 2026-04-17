from flask import Flask, jsonify, request
import os

app = Flask(__name__)

livros = [
    {"id": 1, 
     "titulo": "O Hobbit - Edição Especial",
  "autor": "J.R.R. Tolkien",
  "ano": 1937},
    {"id": 2,
     "titulo": "A Menina que Roubava Livros",
  "autor": "Markus Zusak",
  "ano": 2005}
]

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)
    return {"erro": "Livro não encontrado"}, 404

@app.route("/livros", methods=["POST"])
def cadastrar_livro():
    dados = request.get_json()

    if not dados.get("titulo") or not dados.get("autor"):
        return {"erro": "Título e autor são obrigatórios"}, 400

    if dados.get("ano", 0) < 0:
        return {"erro": "Ano inválido"}, 400

    for l in livros:
        if l["titulo"].lower() == dados["titulo"].lower():
            return {"erro": "Livro já cadastrado"}, 400

    novo = {
        "id": len(livros) + 1,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "ano": dados.get("ano", 0)
    }

    livros.append(novo)

    return {"mensagem": "Livro cadastrado", "livro": novo}, 201

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.get_json()

    for livro in livros:
        if livro["id"] == id:

            if not dados.get("titulo") or not dados.get("autor"):
                return {"erro": "Título e autor são obrigatórios"}, 400

            if dados.get("ano", 0) < 0:
                return {"erro": "Ano inválido"}, 400

            livro["titulo"] = dados["titulo"]
            livro["autor"] = dados["autor"]
            livro["ano"] = dados.get("ano", livro["ano"])

            return {"mensagem": "Livro atualizado", "livro": livro}

    return {"erro": "Livro não encontrado"}, 404

@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return {"mensagem": "Livro removido"}

    return {"erro": "Livro não encontrado"}, 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
