---
id: 53ec97bc-e9d8-4dd5-b16f-bf3c4c8fd257
name: Nmap Scan Services with Hostgroup Template
type: command
executor: bash
data: nmap -p- --min-hostgroup 3 --max-hostgroup 4 $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.386014+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan Services with Hostgroup Template

```bash
nmap -p- --min-hostgroup 3 --max-hostgroup 4 $_TARGET_IP
```
