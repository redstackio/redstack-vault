---
type: command
executor: powershell
data: '$Env:LOGONSERVER'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reconnaissance
  - active-directory
  - powershell
verified: true
validated: true
---

# powershell-get-logonserver

## Command

```powershell
$Env:LOGONSERVER
```

## Description

Retrieves the name of the domain controller that authenticated the current user session from the LOGONSERVER environment variable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $Env:LOGONSERVER | Environment variable for logon server | Yes |

## Examples

### Basic Usage

```powershell
$Env:LOGONSERVER
```

## Expected Output

\\DC01

## Related

- [[procedures/Active-Directory-Domain-Controller-Lookup]]
- [[commands/cmd-echo-logonserver]]
