---
id: fd0017f1-e6a6-4af1-95d5-3fe20118c6e6
name: Nmap Scan Services with Max Rate Template
type: command
executor: bash
data: nmap -p- --max-rate 2 $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.397837+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan Services with Max Rate Template

```bash
nmap -p- --max-rate 2 $_TARGET_IP
```
