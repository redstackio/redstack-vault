---
id: 3efa41e4-90cf-4cd4-afc5-6dbd9c1dbe5a
name: curl Make a POST Request with JSON Data
type: command
executor: bash
data: 'curl -H "Content-Type: application/json" http://_TARGET_IP/$_PATH -d ''{"$_KEY":"$_VALUE"}'''
output: null
created_at: '2019-12-10T00:20:20.249791+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# curl Make a POST Request with JSON Data

```bash
curl -H "Content-Type: application/json" http://_TARGET_IP/$_PATH -d '{"$_KEY":"$_VALUE"}'
```


