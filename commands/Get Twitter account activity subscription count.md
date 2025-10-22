---
id: a161c9e0-cf3f-44b5-bee9-0ec1eebb0fad
name: Get Twitter Account Activity Subscription Count
type: command
executor: bash
data: 'curl --request GET --url https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json
  --header ''authorization: Bearer TOKEN'''
output: null
created_at: '2023-04-06T03:55:53.250188+00:00'
updated_at: '2023-04-06T03:55:53.258813+00:00'
---

# Get Twitter Account Activity Subscription Count

```bash
curl --request GET --url https://api.twitter.com/1.1/account_activity/all/subscriptions/count.json --header 'authorization: Bearer TOKEN'
```
