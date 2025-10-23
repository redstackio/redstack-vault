---
id: fcdc27c7-b693-41c1-83aa-9bd204d993f9
name: Nmap Scan Services with Min Rate Template
type: command
executor: bash
data: nmap -p- --min-rate 2 $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.399783+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan Services with Min Rate Template

```bash
nmap -p- --min-rate 2 $_TARGET_IP
```


