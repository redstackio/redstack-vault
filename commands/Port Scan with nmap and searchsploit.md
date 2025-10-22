---
id: aa8cd2f5-f391-48e7-ad54-553f4d18317b
name: Port Scan with nmap and searchsploit
type: command
executor: bash
data: nmap -p- -sV -oX a.xml IP_ADDRESS; searchsploit --nmap a.xml
output: null
created_at: '2023-04-06T03:56:22.011537+00:00'
updated_at: '2023-04-10T20:25:10.386535+00:00'
---

# Port Scan with nmap and searchsploit

```bash
nmap -p- -sV -oX a.xml IP_ADDRESS; searchsploit --nmap a.xml
```
