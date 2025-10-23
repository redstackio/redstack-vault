---
id: 4c6ba549-c7eb-486d-b558-01f2c6d88cf6
name: Scan DynamoDB table for users
type: command
executor: bash
data: $ aws --endpoint-url http://s3.bucket.htb dynamodb scan --table-name users |
  jq -r '.Items[]'
output: null
created_at: '2023-04-06T03:56:09.833263+00:00'
updated_at: '2023-04-10T20:20:03.775438+00:00'
---

# Scan DynamoDB table for users

```bash
$ aws --endpoint-url http://s3.bucket.htb dynamodb scan --table-name users | jq -r '.Items[]'
```


