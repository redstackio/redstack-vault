---
id: c605e6e7-f526-411b-ad87-9894fbed6235
name: Check Reciclador
type: command
executor: bash
data: python3 mssqlclient.py 'host/username:password@10.10.10.10' -check -reciclador
  'C:\windows\temp\reciclador.dll'
output: null
created_at: '2023-04-06T03:56:20.471781+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
---

# Check Reciclador

```bash
python3 mssqlclient.py 'host/username:password@10.10.10.10' -check -reciclador 'C:\windows\temp\reciclador.dll'
```


