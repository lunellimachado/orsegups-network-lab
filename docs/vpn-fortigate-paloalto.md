# Plano de Automação VPN IPSec Fortigate x Palo Alto

## Objetivo

Automatizar a criação e validação de uma VPN IPSec Site-to-Site entre um firewall Fortigate e um firewall Palo Alto, garantindo conectividade segura entre matriz e filial.

---

## Cenário

### Fortigate

WAN IP: 200.100.100.1

LAN Local: 192.168.10.0/24

Tunnel IP: 169.255.1.1/30

### Palo Alto

WAN IP: 201.100.100.1

LAN Local: 192.168.20.0/24

Tunnel IP: 169.255.1.2/30

---

## Phase 1

Modo: Main

Autenticação: Pre-Shared Key

Criptografia: AES256

Hash: SHA256

DH Group: 14

Lifetime: 28800 segundos

---

## Phase 2

Criptografia: AES256

Hash: SHA256

PFS: Grupo 14

Lifetime: 3600 segundos

Rede Local Fortigate: 192.168.10.0/24

Rede Local Palo Alto: 192.168.20.0/24

---

## Ferramentas de Automação

### Fortigate

- FortiOS REST API
- SSH Automation
- Python Requests
- Netmiko

### Palo Alto

- PAN-OS XML API
- REST API
- Python Requests
- Netmiko

---

## Fluxo de Automação

1. Validar conectividade com ambos os firewalls.
2. Validar credenciais de acesso.
3. Criar objetos de rede.
4. Configurar Phase 1.
5. Configurar Phase 2.
6. Criar interface do túnel.
7. Configurar rotas.
8. Criar políticas de firewall.
9. Aplicar configurações.
10. Executar validações.

---

## Processo de Validação

### Fortigate

Verificar:

- VPN estabelecida
- Interface ativa
- Rotas instaladas

Comandos:

get vpn ipsec tunnel summary

diagnose vpn tunnel list

get router info routing-table all

### Palo Alto

Verificar:

- Estado do túnel
- Rotas
- Sessões IPSec

Comandos:

show vpn ike-sa

show vpn ipsec-sa

show routing route

---

## Tratamento de Alertas

O sistema deverá gerar alertas quando:

- Túnel não subir.
- Phase 1 incompatível.
- Phase 2 incompatível.
- Rota ausente.
- Interface inativa.
- Falha de autenticação.

---

## Considerações

A automação deverá utilizar APIs oficiais sempre que disponíveis, reduzindo riscos operacionais e aumentando a padronização das configurações.

A validação deverá ocorrer após cada etapa da configuração para garantir consistência entre os dispositivos.