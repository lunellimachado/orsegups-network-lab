from cisco_automation import (
    gerar_configuracao_cisco,
    testar_conexao,
    aplicar_configuracao_cisco,
    gerar_backup_lab,
    validar_configuracao
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

    arquivo_backup_lab = gerar_backup_lab(hostname, comandos)

    validacoes = validar_configuracao(
        hostname,
        vlan10,
        vlan20,
        vlan50
    )

    validacoes_html = "<br>".join(validacoes)

    status_conexao, resultado_conexao = testar_conexao(
        ip_switch,
        usuario,
        senha
    )

    if status_conexao:
        status_aplicacao, resultado_aplicacao, arquivo_backup = aplicar_configuracao_cisco(
            ip_switch,
            usuario,
            senha,
            comandos
        )

        if status_aplicacao:
            conexao_html = f"""
            <h2 style="color:green;">Configuração Aplicada com Sucesso</h2>

            <p>Equipamento respondeu:</p>
            <div style="background:#e8ffe8; padding:10px; border-radius:5px;">
                {resultado_conexao}
            </div>

            <p>Backup real gerado em:</p>
            <div style="background:#e8ffe8; padding:10px; border-radius:5px;">
                {arquivo_backup}
            </div>

            <h3>Resultado da Aplicação</h3>
            <pre style="background:#f4f4f4; padding:10px; border-radius:5px;">
{resultado_aplicacao}
            </pre>
            """
        else:
            conexao_html = f"""
            <h2 style="color:red;">Falha ao Aplicar Configuração</h2>

            <div style="background:#ffe8e8; padding:10px; border-radius:5px;">
                {resultado_aplicacao}
            </div>
            """
    else:
        conexao_html = f"""
        <h2 style="color:red;">Falha na Conexão SSH</h2>

        <div style="background:#ffe8e8; padding:10px; border-radius:5px;">
            {resultado_conexao}
        </div>

        <p>
            Como não há switch real disponível, foi gerado um backup de laboratório
            para evidenciar o fluxo de automação.
        </p>
        """

    comandos_html = "<br>".join(comandos)

    return f"""
    <h1>Configuração Recebida</h1>

    <p>Hostname: {hostname}</p>
    <p>VLAN 10: {vlan10}</p>
    <p>VLAN 20: {vlan20}</p>
    <p>VLAN 50: {vlan50}</p>

    {conexao_html}

    <h2>Backup Laboratório</h2>
    <div style="
    background:#eef5ff;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;
    ">
    Arquivo gerado: {arquivo_backup_lab}
    </div>

    <h2>Validação</h2>
    <div style="
    background:#e8ffe8;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;
    ">
    {validacoes_html}
    </div>

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