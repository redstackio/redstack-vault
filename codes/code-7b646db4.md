---
id: 7b646db4-b691-4a22-9331-9d5fa2206822
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:22.038087+00:00'
updated_at: '2023-04-10T20:25:07.349277+00:00'
---

# Code Snippet 7b646db4

**Language**: Bash

```bash
nmap -sV IP_ADDRESS -oX scan.xml && xsltproc scan.xml -o "`date +%m%d%y`_report.html"
```
