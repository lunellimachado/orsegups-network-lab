from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>ORSEGUPS Network Lab</h1>
    <p>Automação Cisco - Projeto de Teste</p>
    """

if __name__ == "__main__":
    app.run(debug=True)