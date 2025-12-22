---
id: c605e6e7-f526-411b-ad87-9894fbed6235
name: mssqlclient-check-reciclador-dll
type: command
executor: bash
data: >-
  python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -check
  -reciclador '$_DLL_PATH'
output: null
created_at: '2023-04-06T03:56:20.471781+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
platforms:
  - Windows
tags:
  - verification
  - dll
verified: true
validated: true
---

# mssqlclient-check-reciclador-dll

## Command

```bash
python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -check -reciclador '$_DLL_PATH'
```

## Description

Checks the status of the reciclador.dll proxy on the target MSSQL instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HOST | SQL Server host | Yes |
| $_USERNAME | SQL username | Yes |
| $_PASSWORD | SQL password | Yes |
| $_TARGET_IP | Target IP | Yes |
| -check | Check mode flag | Yes |
| -reciclador | DLL specification flag | Yes |
| $_DLL_PATH | Path to DLL (e.g., C:\windows\temp\reciclador.dll) | Yes |

## Examples

### Basic Usage

```bash
python3 mssqlclient.py 'localhost/sa:Password123@192.168.1.100' -check -reciclador 'C:\windows\temp\reciclador.dll'
```

## Expected Output

DLL status: Loaded/Ready or error if not found.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
