---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: whoami /priv
tags:
  - privileges
  - verification
type: command
output: |-
  PRIVILEGES INFORMATION
  ...
  SeDebugPrivilege          Enabled
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:44.470Z'
verified: false
validated: true
submitted: true
---
# whoami-privs

## Command

```cmd
whoami /priv
```

## Description

Displays the privileges of the current user token, used to verify successful privilege escalation (e.g., from limited to admin/SYSTEM).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /priv | Flag to show privileges | Yes |

## Examples

### Basic Usage

```cmd
whoami /priv
```

### Advanced Usage

```cmd
whoami /all
```

## Expected Output

PRIVILEGES INFORMATION
---------------------

Privilege Name                Description                          State
=============================== ====================================== =======
SeShutdownPrivilege           Shut down the system                 Enabled
SeDebugPrivilege              Debug programs                       Enabled

Look for elevated states post-escalation.

## Related

- [[Related Procedure|procedures/Exploit-Weak-ACLs-in-UniFi-Video-Directory]]
