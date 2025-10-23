---
id: a763f57d-4ea0-469b-ac9f-433eee3b012e
name: jq
type: command
executor: bash
data: '''.[].attributes | select(.adminCount == [1]) | .sAMAccountName[]'' domain_users.json'
output: null
created_at: '2023-04-06T03:56:06.369023+00:00'
updated_at: '2023-04-10T20:26:29.960043+00:00'
---

# jq

```bash
'.[].attributes | select(.adminCount == [1]) | .sAMAccountName[]' domain_users.json
```


