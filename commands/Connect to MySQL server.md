---
id: 236eb80f-8708-4902-afa6-0f3c58fda08b
name: Connect to MySQL server
type: command
executor: bash
data: mysql -h hostname -u name -P port --enable-cleartext-plugin --user=user --password=$TOKEN
output: null
created_at: '2023-04-06T03:56:14.073876+00:00'
updated_at: '2023-04-10T20:20:55.168825+00:00'
---

# Connect to MySQL server

```bash
mysql -h hostname -u name -P port --enable-cleartext-plugin --user=user --password=$TOKEN
```


