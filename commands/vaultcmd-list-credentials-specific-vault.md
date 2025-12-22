---
id: dd65aec7-5366-4129-93e2-6631554460ec
name: vaultcmd-list-credentials-specific-vault
type: command
executor: cmd
data: 'VaultCmd /listcreds:<namevault>|<guidvault> /all'
output: null
created_at: '2023-04-06T03:56:26.193388+00:00'
updated_at: '2023-04-10T20:37:12.539647+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - dpapi
verified: true
validated: true
---

# vaultcmd-list-credentials-specific-vault

## Command

```cmd
VaultCmd /listcreds:$_VAULT_NAME|\$_VAULT_GUID /all
```

## Description

This command lists all credentials stored in a specific DPAPI vault identified by name or GUID. It retrieves details like usernames and encrypted passwords for targeted extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VAULT_NAME | Name of the vault (e.g., "Web Credentials") | Yes (or GUID) |
| $_VAULT_GUID | GUID of the vault from /list output | Yes (or name) |
| /all | Displays all credential details including encrypted data | Yes |

## Examples

### Basic Usage

```cmd
VaultCmd /listcreds:"Web Credentials" /all
```

### Advanced Usage

```cmd
VaultCmd /listcreds:{12345678-1234-1234-1234-123456789abc} /all
```

## Expected Output

```
Credential: Target: example.com User: user1 Password: [encrypted blob]
Credential: Target: server.example.com User: admin Password: [encrypted blob]
```

Success shows credential entries with decryptable fields in the current user context.

## Related

- [[procedures/Windows-DPAPI-Credential-Theft]]
- [[commands/vaultcmd-list-vaults]]
