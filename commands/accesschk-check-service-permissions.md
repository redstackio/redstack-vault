---
id: 57598a20-ae4c-4ecb-ba6e-6fb5b790840d
name: accesschk-check-service-permissions
type: command
executor: cmd
data: accesschk.exe -uwcqv "%USERNAME%" *
output: null
created_at: '2023-01-12T04:55:30.128941+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - permissions
verified: true
validated: true
---

# accesschk-check-service-permissions

## Command

```cmd
accesschk.exe -uwcqv "%USERNAME%" *
```

## Description

This command uses AccessChk from the Sysinternals Suite to enumerate permissions on all services (*) for the current user (%USERNAME%), focusing on write and control access that could indicate abuse functions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Lists user-specific permissions | Yes |
| -w | Checks for write access | Yes |
| -c | Targets services only | Yes |
| -q | Quiet mode (suppress headers) | Yes |
| -v | Verbose output with details | Yes |
| "%USERNAME%" | Current username to check permissions for | Yes |
| * | All services | Yes |

## Examples

### Basic Usage

```cmd
accesschk.exe -uwcqv "%USERNAME%" *
```

### Check Specific Service

```cmd
accesschk.exe -uwcqv "%USERNAME%" VulnService
```

## Expected Output

RW BUILTIN\Users
RW NT AUTHORITY\Authenticated Users

Where RW indicates read/write access, signaling potential abuse. Services with RW for low-priv users are exploitable.

## Related

- [[procedures/Search-and-Exploit-Service-Abuse-Functions]]
- [[tools/Sysinternals-Suite]]
