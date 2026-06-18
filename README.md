# ORSEGUPS Network Lab

## Descrição

Projeto desenvolvido para o Laboratório de Candidatos Networking ORSEGUPS.

O objetivo deste projeto é demonstrar conhecimentos em:

- Automação de redes com Python
- Configuração de equipamentos Cisco
- Planejamento de VPN IPSec Fortigate x Palo Alto
- Configuração de MikroTik RB750Gr3
- Controle de versões com Git
- Documentação técnica

---

## Estrutura do Projeto

```text
docs/
src/
templates/
mikrotik/
evidencias/
backups/
```

---

## Requisitos

Python 3.10+

Instalação das dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

Acesse a pasta do projeto:

```bash
cd orsegups-network-lab
```

Execute:

```bash
py src/app.py
```

O sistema ficará disponível em:

```text
http://127.0.0.1:5000
```

---

## Funcionalidades

### Cisco

- Configuração de VLANs
- Configuração de Hostname
- Download da configuração
- Backup automático
- Validação da configuração
- Teste de conectividade SSH

### VPN IPSec

Documentação completa disponível em:

```text
docs/vpn-fortigate-paloalto.md
```

### MikroTik

Configuração inicial do RB750Gr3:

- WAN
- LAN
- DHCP
- NAT
- Firewall
- Segurança
- VPN Site-to-Site

Documentação:

```text
docs/mikrotik-validacoes.md
```

---

## Evidências

As evidências do projeto encontram-se em:

```text
evidencias/
```

---

## Autor

Artur Lunelli Machado