---
id: cmd-001
data: 'PS C:\ysoserial.net\ysoserial\bin\Debug> .\ysoserial.exe -p DotNetNuke --help'
tags:
  - deserialization
  - help
type: command
output: >-
  Usage details including modes (read_file, write_file, run_command), options
  like -c for command, -f for file, -u for URL
executor: powershell
platforms:
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.719Z'
verified: false
validated: true
submitted: true
---
# ysoserial-dotnetnuke-help

## Command

```powershell
PS C:\ysoserial.net\ysoserial\bin\Debug> .\ysoserial.exe -p DotNetNuke --help
```

## Description

Displays help for the DotNetNuke plugin in YSoSerial.net, showing options for generating deserialization payloads specific to CVE-2017-9822.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Plugin name: DotNetNuke | Yes |
| `--help` | Show usage information | Yes |

## Examples

### Basic Usage

```powershell
.\ysoserial.exe -p DotNetNuke --help
```

### Advanced Usage

Not applicable; help only.

## Expected Output

Usage details including modes (read_file, write_file, run_command), options like -c for command, -f for file, -u for URL.

## Related

- [[commands/ysoserial-dotnetnuke-read-file]]
- [[procedures/Generate-DNN-Deserialization-Payload-for-File-Read]]
