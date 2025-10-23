---
id: 9635bc75-76ea-4139-9c14-ba7867f3c214
name: Aggressive UDP Scan
type: command
executor: bash
data: 'nmap -sU -v $ip

  nmap -sU -P0 $ip

  nmap -sU -P0 -T Aggressive $ip

  '
output: null
created_at: '2020-07-14T18:15:19.609971+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Aggressive UDP Scan

```bash
nmap -sU -v $ip
nmap -sU -P0 $ip
nmap -sU -P0 -T Aggressive $ip

```


