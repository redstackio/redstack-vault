---
id: 5633e265-143b-400c-8570-bd9f6e92ae46
name: cmdkey-delete-credential
type: command
executor: cmd
data: 'cmdkey /delete:$_TARGET'
output: null
created_at: '2023-04-06T03:56:29.949444+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-management
  - cleanup
verified: true
validated: true
---

# cmdkey-delete-credential

## Command

```cmd
cmdkey /delete:$_TARGET
```

## Description

Deletes a specific credential from the Windows Credential Manager, useful for cleanup after use or resolving conflicts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Exact target name to delete | Yes |
| /delete | Removes the credential | Yes |

## Examples

### Basic Usage

```cmd
cmdkey /delete:localhost
```

### Advanced Usage

```cmd
cmdkey /delete:TERMSRV/targethost
```

Target a specific entry.

## Expected Output

```
Deleted the stored credential for target localhost.
```

## Related

- [[procedures/windows-privilege-escalation-via-runas]]
- [[commands/cmdkey-list-stored-credentials]]
