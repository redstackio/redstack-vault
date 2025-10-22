---
id: f3238d69-c1ce-44ce-984e-97aea12cfa42
name: Port Scanning with Nmap using Input File
type: command
executor: bash
data: sudo nmap -sSV -oA OUTPUTFILE -T4 -iL INPUTFILE.csv
output: null
created_at: '2023-04-06T03:56:21.931159+00:00'
updated_at: '2023-04-10T20:25:06.988229+00:00'
---

# Port Scanning with Nmap using Input File

```bash
sudo nmap -sSV -oA OUTPUTFILE -T4 -iL INPUTFILE.csv
```
