---
id: 58230238-e1b6-49dc-82f7-bbb24087db72
name: Nmap Scan Services with Host Timeout Template
type: command
executor: bash
data: nmap -p- --host-timeout 100ms $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.386552+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan Services with Host Timeout Template

```bash
nmap -p- --host-timeout 100ms $_TARGET_IP
```


