---
id: e6c02320-028c-44c4-8a2e-8f77ceb5d7be
name: Crack AS_REP messages with hashcat
type: command
executor: bash
data: 'root@kali:impacket-examples$ hashcat -m 18200 --force -a 0 hashes.asreproast
  passwords_kerb.txt

  root@windows:hashcat$ hashcat64.exe -m 18200 ''<AS_REP-hash>'' -a 0 c:\wordlists\rockyou.txt'
output: null
created_at: '2023-04-06T03:56:04.983786+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
---

# Crack AS_REP messages with hashcat

```bash
root@kali:impacket-examples$ hashcat -m 18200 --force -a 0 hashes.asreproast passwords_kerb.txt
root@windows:hashcat$ hashcat64.exe -m 18200 '<AS_REP-hash>' -a 0 c:\wordlists\rockyou.txt
```
