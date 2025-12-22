---
type: command
executor: command_prompt
data: 'vaultcmd.exe /listcreds:"Windows Credentials"'
output: null
platforms:
  - Windows
tags:
  - credential-access
  - enumeration
verified: true
validated: true
---

# vaultcmd-list-windows-credentials

## Command

```command_prompt
vaultcmd.exe /listcreds:"$_VAULT_NAME"
```

## Description

This command lists credentials stored in a specified Windows Credential Manager vault using vaultcmd.exe. It reveals details such as credential schemas, resources (e.g., domain targets), identities (usernames), and properties, which can help identify potentially exploitable saved credentials during security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VAULT_NAME | The name of the vault to query (e.g., "Windows Credentials", "Web Credentials", "Generic Credentials") | Yes |
| /listcreds | Flag to list credentials from the specified vault | Yes |

The vault name must be enclosed in quotes if it contains spaces.

## Examples

### Basic Usage

```command_prompt
vaultcmd.exe /listcreds:"Windows Credentials"
```

Lists all credentials in the Windows Credentials vault.

### Advanced Usage

```command_prompt
vaultcmd.exe /listcreds:"Web Credentials"
```

Lists credentials from the Web Credentials vault, useful for browser-saved logins.

## Expected Output

```
C:\>vaultcmd.exe /listcreds:"Windows Credentials"
Credentials in vault: Windows Credentials

Credential schema: Windows Domain Password Credential
Resource: Domain:target=dc.domain.example
Identity: Administrator
Hidden: No
Roaming: No
Property (schema element id,value): (100,3)
```

The output enumerates each credential's metadata. If the vault is empty, it will indicate no credentials are present. Actual output varies based on stored credentials.

## Related

- [[tools/vaultcmd]]
- [[procedures/List-Credentials-in-Windows-Credential-Manager-Vault]]
