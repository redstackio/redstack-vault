---
id: 3e8c6fc0-db2c-451e-ad77-d8dbe5e4ee28
name: cmdkey-add-credential
type: command
executor: cmd
data: 'cmdkey /add:$_TARGET /user:$_USERNAME /pass:$_PASSWORD'
output: null
created_at: '2023-04-06T03:56:29.949398+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - credential-management
  - persistence
verified: true
validated: true
---

# cmdkey-add-credential

## Command

```cmd
cmdkey /add:$_TARGET /user:$_USERNAME /pass:$_PASSWORD
```

## Description

Adds a new credential to the Windows Credential Manager for a specified target, enabling automatic authentication for network resources or `runas` executions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target name (e.g., TERMSRV/hostname) | Yes |
| $_USERNAME | Username for the credential | Yes |
| $_PASSWORD | Password for the credential | Yes |
| /add | Adds the credential | Yes |

## Examples

### Basic Usage

```cmd
cmdkey /add:localhost /user:Administrator /pass:Pass123
```

### Advanced Usage

```cmd
cmdkey /add:TERMSRV/remotehost /user:DOMAIN\Admin /pass:SecurePass
```

For remote server access.

## Expected Output

```
Credential added successfully.
```

## Related

- [[procedures/windows-privilege-escalation-via-runas]]
- [[commands/cmdkey-list-stored-credentials]]
