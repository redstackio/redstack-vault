---
id: new-uuid-2
name: crackmapexec-webdav-brute
type: command
executor: bash
data: crackmapexec smb 'TARGETS' -d 'domain' -u 'user' -p 'password' -M webdav
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - brute-force
  - webdav
verified: true
validated: true
---

# crackmapexec-webdav-brute

## Command

```bash
crackmapexec smb 'TARGETS' -d 'domain' -u 'user' -p 'password' -M webdav
```

## Description

Performs credential brute-force specifically targeting WebDAV services over SMB on multiple targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'TARGETS' | List of IP addresses or ranges | Yes |
| -d 'domain' | Target domain | Yes |
| -u 'user' | Username | Yes |
| -p 'password' | Password | Yes |
| -M webdav | Module for WebDAV only | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb '192.168.1.0/24' -d 'example.com' -u 'admin' -p 'pass123' -M webdav
```

## Expected Output

Target IP: PWNED! or failed login status per host.

## Related

- [[procedures/WebDAV-Relay-Attack]]
