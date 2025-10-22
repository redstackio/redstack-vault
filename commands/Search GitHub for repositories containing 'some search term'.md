---
id: ae48e147-85f1-4e57-ae20-a318ce8ce833
name: Search GitHub for repositories containing 'some search term'
type: command
executor: bash
data: SCMKit.exe -s github -m searchrepo -c userName:password -u https://github.something.local
  -o "some search term"
output: null
created_at: '2023-04-06T03:56:25.111850+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Search GitHub for repositories containing 'some search term'

```bash
SCMKit.exe -s github -m searchrepo -c userName:password -u https://github.something.local -o "some search term"
```
