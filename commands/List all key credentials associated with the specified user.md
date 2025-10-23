---
id: 722829de-0957-4960-8bc1-4388bda68ba5
name: List all key credentials associated with the specified user
type: command
executor: bash
data: python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target
  "user2" --action "list"
output: null
created_at: '2023-04-06T03:56:06.261674+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
---

# List all key credentials associated with the specified user

```bash
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "list"
```


