# Validações da Configuração MikroTik RB750Gr3

## Objetivo

Validar que a configuração inicial do MikroTik RB750Gr3 atende aos requisitos de conectividade, segurança e gerenciamento definidos para a unidade remota.

## Itens Validados

### Interfaces e Bridge

 Bridge criada com sucesso.
 Interfaces ether2, ether3, ether4 e ether5 adicionadas à bridge.
 Interface ether2 renomeada para ether2-master.

### LAN

  Endereço IP configurado:

   192.168.100.1/24

### DHCP Server

  Pool configurado:

   192.168.100.2 até 192.168.100.254
  Gateway distribuído:

   192.168.100.1
  Lease Time:

   3 dias

### WAN

  DHCP Client configurado na ether1.
  Endereço IP recebido automaticamente.

### NAT

  Regra Masquerade configurada.
  Clientes LAN com acesso à internet.

### DNS

  Serviço DNS operacional.
  Allow Remote Requests desabilitado.

### Firewall

Validadas as seguintes regras:

  Permitir Established.
  Permitir Related.
  Permitir ICMP.
  Bloquear conexões inválidas.
  Bloquear acessos indevidos provenientes da WAN.

### Segurança

Serviços desabilitados:

  Telnet
  FTP
  WWW
  API
  API-SSL

Controle de acesso:

  Senha administrativa configurada.
  MAC Winbox permitido apenas pela LAN.

### VPN Site-to-Site

Validações previstas:

  Estabelecimento do túnel.
  Conectividade entre matriz e filial.
  Verificação das rotas.
  Teste de ping entre redes remotas.

## Conclusão

A configuração atende aos requisitos mínimos de conectividade, segurança e gerenciamento definidos para o ambiente proposto.


## VPN Site-to-Site MikroTik

Validações previstas:

- Peer IPsec criado para comunicação com a matriz.
- Proposal IPsec configurada com AES-256 e SHA256.
- Policy criada entre a rede da filial `192.168.100.0/24` e a rede da matriz `192.168.200.0/24`.
- Regra NAT bypass criada para impedir masquerade no tráfego da VPN.
- Chave pré-compartilhada definida para autenticação do túnel.

Comandos de validação:

```mikrotik
/ip ipsec peer print
/ip ipsec policy print
/ip ipsec active-peers print
/ip ipsec installed-sa print
/ip firewall nat print