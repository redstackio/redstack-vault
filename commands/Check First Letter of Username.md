---
id: 9f9a5792-ffc7-4c54-8484-2448d09f6813
name: Check First Letter of Username
type: command
executor: bash
data: if [ $(whoami|cut -c 1) == a ]; then sleep 5; fi
output: null
created_at: '2023-04-06T03:55:57.447099+00:00'
updated_at: '2023-04-06T03:55:57.457432+00:00'
---

# Check First Letter of Username

```bash
if [ $(whoami|cut -c 1) == a ]; then sleep 5; fi
```


