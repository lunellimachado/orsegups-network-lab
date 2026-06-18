# ================================
# VPN SITE-TO-SITE MIKROTIK
# MATRIZ x FILIAL
# ================================

# Cenário exemplo:
# Matriz LAN: 192.168.200.0/24
# Filial LAN: 192.168.100.0/24
# IP público Matriz: 200.200.200.1
# IP público Filial: obtido via DHCP na ether1
# PSK: alterar em ambiente real

/ip ipsec profile
add name=profile-vpn-orsegups dh-group=modp2048 enc-algorithm=aes-256 hash-algorithm=sha256 lifetime=1d

/ip ipsec peer
add name=peer-matriz address=200.200.200.1/32 exchange-mode=ike2 profile=profile-vpn-orsegups

/ip ipsec proposal
add name=proposal-vpn-orsegups auth-algorithms=sha256 enc-algorithms=aes-256-cbc pfs-group=modp2048 lifetime=1h

/ip ipsec identity
add peer=peer-matriz auth-method=pre-shared-key secret="AlterarSenhaForteAqui"

/ip ipsec policy
add src-address=192.168.100.0/24 dst-address=192.168.200.0/24 tunnel=yes peer=peer-matriz proposal=proposal-vpn-orsegups

# Regra para não mascarar tráfego destinado à matriz
/ip firewall nat
add chain=srcnat src-address=192.168.100.0/24 dst-address=192.168.200.0/24 action=accept comment="Nao aplicar NAT para trafego VPN matriz"

/ip route
add dst-address=192.168.200.0/24 gateway=bridge comment="Rota logica para rede matriz via VPN"