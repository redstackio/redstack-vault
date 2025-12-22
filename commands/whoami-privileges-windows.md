---
id: de298cdc-64a2-4d16-9aa5-b9c2e588ad82
name: whoami-privileges-windows
type: command
executor: cmd
data: whoami /priv
output: null
created_at: '2023-04-06T03:56:30.162995+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - discovery
verified: true
validated: true
---

# whoami-privileges-windows

## Command

```cmd
whoami /priv
```

## Description

Lists the current user's privileges and their states (Enabled, Disabled, Not Assigned), helping assess capabilities like token manipulation or service control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /priv | Displays privilege information | Yes |

## Examples

### Basic Usage

```cmd
whoami /priv
```

## Expected Output

```
PRIVILEGES INFORMATION
----------------------
Privilege Name                                Description                          State
==================================================================================================
SeAssignPrimaryTokenPrivilege                 Replace a process level token        Disabled
SeAuditPrivilege                              Generate security audits             Disabled
SeBackupPrivilege                             Back up files and directories        Disabled
SeDebugPrivilege                              Debug programs                       Enabled
...
```

Enabled privileges (e.g., SeDebugPrivilege) indicate escalation vectors.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/whoami-groups-windows]]
