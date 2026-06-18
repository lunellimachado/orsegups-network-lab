from cisco_automation import (
    gerar_configuracao_cisco,
    testar_conexao
)

from flask import Flask, render_template, request, Response

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

    ip_switch = request.form.get("ip_switch")
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    comandos = gerar_configuracao_cisco(
        hostname,
        vlan10,
        vlan20,
        vlan50
    )

    status, resultado = testar_conexao(
        ip_switch,
        usuario,
        senha
    )

    if status:
        conexao_html = f"""
        <h2 style="color:green;">
            Conexão SSH OK
        </h2>

        <p>Equipamento respondeu:</p>

        <div style="
            background:#e8ffe8;
            padding:10px;
            border-radius:5px;
        ">
            {resultado}
        </div>
        """
    else:
        conexao_html = f"""
        <h2 style="color:red;">
            Falha na Conexão SSH
        </h2>

        <div style="
            background:#ffe8e8;
            padding:10px;
            border-radius:5px;
        ">
            {resultado}
        </div>
        """

    comandos_html = "<br>".join(comandos)

    return f"""
    <h1>Configuração Recebida</h1>

    <p>Hostname: {hostname}</p>
    <p>VLAN 10: {vlan10}</p>
    <p>VLAN 20: {vlan20}</p>
    <p>VLAN 50: {vlan50}</p>

    {conexao_html}

    <h2>Comandos Cisco Gerados</h2>

    <div style="
    background:#1e1e1e;
    color:#00ff66;
    padding:20px;
    border-radius:8px;
    font-family:Consolas;
    margin-top:20px;
    ">
    {comandos_html}
    </div>

    <br>
    <a href="/">Voltar</a>
    """


@app.route("/download", methods=["POST"])
def download():

    hostname = request.form.get("hostname")
    vlan10 = request.form.get("vlan10")
    vlan20 = request.form.get("vlan20")
    vlan50 = request.form.get("vlan50")

    comandos = gerar_configuracao_cisco(
        hostname,
        vlan10,
        vlan20,
        vlan50
    )

    conteudo = "\n".join(comandos)

    return Response(
        conteudo,
        mimetype="text/plain",
        headers={
            "Content-Disposition": f"attachment; filename={hostname}.txt"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)