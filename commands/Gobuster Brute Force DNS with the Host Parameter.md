---
id: e5eb0c84-03a2-4a3f-89bd-3fa7d8d4e56b
name: Gobuster Brute Force DNS with the Host Parameter
type: command
executor: bash
data: gobuster vhost -u http://$_TARGET_HOST -w $_WORDLIST
output: null
created_at: '2020-04-27T20:54:59.991234+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Gobuster Brute Force DNS with the Host Parameter

```bash
gobuster vhost -u http://$_TARGET_HOST -w $_WORDLIST
```


