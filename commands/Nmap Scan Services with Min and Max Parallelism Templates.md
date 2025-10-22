---
id: a939068e-0733-4c56-852d-dc7849546b96
name: Nmap Scan Services with Min and Max Parallelism Templates
type: command
executor: bash
data: nmap -p- --min-parallelism 2 --max-parallelism 2 $_TARGET_IP
output: null
created_at: '2019-11-13T01:16:38.402131+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Nmap Scan Services with Min and Max Parallelism Templates

```bash
nmap -p- --min-parallelism 2 --max-parallelism 2 $_TARGET_IP
```
