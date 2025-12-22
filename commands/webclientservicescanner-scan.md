---
id: new-uuid-1
name: webclientservicescanner-scan
type: command
executor: powershell
data: 'webclientservicescanner ''domain.local''/''user'':''password''@''machine'''
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

# webclientservicescanner-scan

## Command

```powershell
webclientservicescanner 'domain.local'/'user':'password'@'machine'
```

## Description

Scans a target machine for WebDAV services using provided domain credentials to check WebClient service status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'domain.local' | Target domain | Yes |
| 'user' | Username | Yes |
| 'password' | Password | Yes |
| 'machine' | Target machine name or IP | Yes |

## Examples

### Basic Usage

```powershell
webclientservicescanner 'example.com'/'admin':'pass123'@'192.168.1.10'
```

## Expected Output

WebDAV service status: Enabled/Disabled, with configuration details or access errors.

## Related

- [[procedures/WebDAV-Relay-Attack]]
