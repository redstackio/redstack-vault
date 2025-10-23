---
id: 27139325-b877-4d68-84a3-8c13e45e0a90
name: Install MSSQL client
type: command
executor: bash
data: python3 mssqlclient.py 'host/username:password@10.10.10.10' -install -clr Microsoft.SqlServer.Proxy.dll
output: null
created_at: '2023-04-06T03:56:20.471731+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
---

# Install MSSQL client

```bash
python3 mssqlclient.py 'host/username:password@10.10.10.10' -install -clr Microsoft.SqlServer.Proxy.dll
```


