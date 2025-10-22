---
id: 1c9acc6b-a716-41d8-86a4-3b72edb34e90
name: Decrypt password using openssl
type: command
executor: bash
data: echo 'password_in_base64' | base64 -d | openssl enc -d -aes-256-cbc -K 4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b
  -iv 0000000000000000
output: null
created_at: '2023-04-06T03:56:03.499989+00:00'
updated_at: '2023-04-10T20:26:19.573143+00:00'
---

# Decrypt password using openssl

```bash
echo 'password_in_base64' | base64 -d | openssl enc -d -aes-256-cbc -K 4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b -iv 0000000000000000
```
