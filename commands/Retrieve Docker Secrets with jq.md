---
id: 5be73ca5-05f5-4292-9631-1a7922dad984
name: Retrieve Docker Secrets with jq
type: command
executor: bash
data: $ curl -s –insecure https://tls-opendocker.socket:2376/secrets | jq
output: null
created_at: '2023-04-06T03:56:16.968767+00:00'
updated_at: '2023-04-10T20:33:46.886185+00:00'
---

# Retrieve Docker Secrets with jq

```bash
$ curl -s –insecure https://tls-opendocker.socket:2376/secrets | jq
```
