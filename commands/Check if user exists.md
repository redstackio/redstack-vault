---
id: fb1a3c80-36a0-4ef0-82f8-737d3282762b
name: Check if user exists
type: command
executor: bash
data: grep -c '^username:' /etc/passwd
output: null
created_at: '2023-04-06T03:56:04.400897+00:00'
updated_at: '2023-04-10T20:26:06.625963+00:00'
---

# Check if user exists

```bash
grep -c '^username:' /etc/passwd
```


