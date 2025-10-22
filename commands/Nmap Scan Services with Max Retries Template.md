---
id: 8cc6b056-c3f8-472d-99da-8cdc8dcaa3c2
name: Nmap Scan Services with Max Retries Template
type: command
executor: bash
data: nmap -p- --max-retries 5 $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.382376+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan Services with Max Retries Template

```bash
nmap -p- --max-retries 5 $_TARGET_IP
```
