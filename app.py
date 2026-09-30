from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Webhook Mercado Livre ativo", 200

@app.route("/mercadolivre", methods=["GET", "POST"])
def mercadolivre():

    if request.method == "POST":
        dados = request.get_json(silent=True)

        print("Notificação recebida:")
        print(dados)

        return jsonify({"status": "ok"}), 200

    return "Webhook Mercado Livre ativo", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)