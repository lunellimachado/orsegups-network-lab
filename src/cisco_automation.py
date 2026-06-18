from datetime import datetime
import os

from netmiko import ConnectHandler


def gerar_configuracao_cisco(hostname, vlan10, vlan20, vlan50):

    comandos = [
        f"hostname {hostname}",
        f"vlan {vlan10}",
        "name VLAN_DADOS",
        "exit",
        f"vlan {vlan20}",
        "name VLAN_VOZ",
        "exit",
        f"vlan {vlan50}",
        "name VLAN_SEGURANCA",
        "exit",
    ]

    return comandos


def conectar_cisco(ip, usuario, senha):

    dispositivo = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": usuario,
        "password": senha,
    }

    return ConnectHandler(**dispositivo)


def testar_conexao(ip, usuario, senha):

    try:
        conexao = conectar_cisco(ip, usuario, senha)
        hostname = conexao.find_prompt()
        conexao.disconnect()

        return True, hostname

    except Exception as erro:
        return False, str(erro)


def aplicar_configuracao_cisco(ip, usuario, senha, comandos):

    try:
        conexao = conectar_cisco(ip, usuario, senha)

        os.makedirs("backups", exist_ok=True)

        backup = conexao.send_command("show running-config")

        nome_backup = f"backups/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(nome_backup, "w", encoding="utf-8") as arquivo:
            arquivo.write(backup)

        resultado = conexao.send_config_set(comandos)

        conexao.save_config()

        conexao.disconnect()

        return True, resultado, nome_backup

    except Exception as erro:
        return False, str(erro), None


def gerar_backup_lab(hostname, comandos):

    os.makedirs("backups", exist_ok=True)

    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"backups/{hostname}_{data_hora}_backup_lab.txt"

    conteudo = f"""! Backup simulado - Laboratório ORSEGUPS
! Hostname: {hostname}
! Data/Hora: {data_hora}

version 15.2
hostname {hostname}

!
! Configurações aplicadas no laboratório:
"""

    for comando in comandos:
        conteudo += comando + "\n"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    return nome_arquivo


def validar_configuracao(hostname, vlan10, vlan20, vlan50):

    validacoes = []

    if hostname:
        validacoes.append("✓ Hostname informado")

    if vlan10:
        validacoes.append(f"✓ VLAN {vlan10} válida")

    if vlan20:
        validacoes.append(f"✓ VLAN {vlan20} válida")

    if vlan50:
        validacoes.append(f"✓ VLAN {vlan50} válida")

    if len(validacoes) == 4:
        validacoes.append("✓ Configuração compatível com os parâmetros informados")
    else:
        validacoes.append("⚠ Existem campos não preenchidos")

    return validacoes