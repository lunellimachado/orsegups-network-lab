from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/aplicar", methods=["POST"])
def aplicar():

    hostname = request.form.get("hostname")
    vlan10 = request.form.get("vlan10")
    vlan20 = request.form.get("vlan20")
    vlan50 = request.form.get("vlan50")

    return f"""
    <h1>Configuração Recebida</h1>

    <p>Hostname: {hostname}</p>
    <p>VLAN 10: {vlan10}</p>
    <p>VLAN 20: {vlan20}</p>
    <p>VLAN 50: {vlan50}</p>

    <a href="/">Voltar</a>
    """

if __name__ == "__main__":
    app.run(debug=True)