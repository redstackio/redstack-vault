---
id: 5939fc77-f0ae-4e94-aeb0-b6e5647b2671
name: Expose SMB port on SSH server
type: command
executor: bash
data: plink -l root -pw toor -R 445:127.0.0.1:445
output: null
created_at: '2023-04-06T03:56:22.999863+00:00'
updated_at: '2023-04-10T20:25:11.704574+00:00'
---

# Expose SMB port on SSH server

```bash
plink -l root -pw toor -R 445:127.0.0.1:445
```
