from netmiko import ConnectHandler


def gerar_configuracao_cisco(hostname, vlan10, vlan20, vlan50):

    comandos = [
        "configure terminal",
        f"hostname {hostname}",
        f"vlan {vlan10}",
        "name USUARIOS",
        "exit",
        f"vlan {vlan20}",
        "name TELEFONIA",
        "exit",
        f"vlan {vlan50}",
        "name VISITANTES",
        "exit",
        "end",
        "write memory"
    ]

    return comandos


def testar_conexao(ip, usuario, senha):

    dispositivo = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": usuario,
        "password": senha,
    }

    try:

        conexao = ConnectHandler(**dispositivo)

        hostname = conexao.find_prompt()

        conexao.disconnect()

        return True, hostname

    except Exception as erro:

        return False, str(erro)