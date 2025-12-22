---
id: new-uuid-3
name: getwebdavstatus-check
type: command
executor: powershell
data: GetWebDAVStatus.exe 'machine'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - discovery
  - webdav
verified: true
validated: true
---

# getwebdavstatus-check

## Command

```powershell
GetWebDAVStatus.exe 'machine'
```

## Description

Checks the status and configuration of WebDAV services on a target machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'machine' | Target machine name or IP | Yes |

## Examples

### Basic Usage

```powershell
GetWebDAVStatus.exe '192.168.1.10'
```

## Expected Output

WebDAV Status: Enabled, with registry keys and service details.

## Related

- [[procedures/WebDAV-Relay-Attack]]
