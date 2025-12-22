---
id: 94854098-e4c7-422c-9028-479c2c7f47e8
name: vaultcmd-list-vaults
type: command
executor: cmd
data: vaultcmd /list
output: null
created_at: '2023-04-06T03:56:26.193293+00:00'
updated_at: '2023-04-10T20:37:12.539647+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - dpapi
verified: true
validated: true
---

# vaultcmd-list-vaults

## Command

```cmd
vaultcmd /list
```

## Description

This command enumerates all DPAPI-protected vaults on the Windows system, displaying their GUIDs, names, and types. It is the first step in identifying where credentials are stored for extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /list | Lists all available vaults | Yes (built-in flag) |

## Examples

### Basic Usage

```cmd
vaultcmd /list
```

### Advanced Usage

No additional options; run as-is in an elevated command prompt.

## Expected Output

```
Vault: {GUID1} Type: Generic Cert: No
Vault: {GUID2} Type: Web Credentials Cert: No
Vault: {GUID3} Type: Windows Credentials Cert: No
```

This shows a list of vaults. Success is indicated by at least one vault entry, allowing selection for further querying.

## Related

- [[procedures/Windows-DPAPI-Credential-Theft]]
- [[commands/vaultcmd-list-credentials-specific-vault]]
