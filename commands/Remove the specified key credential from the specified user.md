---
id: 33f1ce51-1679-4c9b-bf36-8ca7edfa715d
name: Remove the specified key credential from the specified user
type: command
executor: bash
data: python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target
  "user2" --action "remove" --device-id "a8ce856e-9b58-61f9-8fd3-b079689eb46e"
output: null
created_at: '2023-04-06T03:56:06.261844+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
---

# Remove the specified key credential from the specified user

```bash
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "remove" --device-id "a8ce856e-9b58-61f9-8fd3-b079689eb46e"
```


