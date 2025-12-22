---
id: dedd471b-fa8e-44f8-a1ae-b3a0c4f4275a
name: List Stored Windows Credentials (vaultcmd.exe)
type: command
executor: command_prompt
data: vaultcmd.exe /list
output: null
created_at: '2019-12-12T18:42:23.953995+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - enumeration
verified: true
validated: true
---

# List-Stored-Windows-Credentials-vaultcmd-list

## Command

```command_prompt
vaultcmd.exe /list
```

## Description

This command uses the vaultcmd.exe utility to list all currently loaded credential vaults for the user, including their names, GUIDs, and file locations. It helps identify which vaults (e.g., Web Credentials or Windows Credentials) are available for further enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /list | Lists all loaded vaults | Yes (built-in flag) |

No additional arguments required; operates on the current user's vaults.

## Examples

### Basic Usage

```command_prompt
vaultcmd.exe /list
```

Outputs the list of vaults.

### Advanced Usage

This command has no advanced options for listing; use it as a precursor to targeted credential listing.

## Expected Output

```
C:\>vaultcmd.exe /list
Currently loaded vaults:
        Vault: Web Credentials
        Vault Guid:4BF4C442-9B8A-41A0-B380-DD4A704DDB28
        Location: C:\Users\Victim\AppData\Local\Microsoft\Vault\4BF4C442-9B8A-41A0-B380-DD4A704DDB28

        Vault: Windows Credentials
        Vault Guid:77BC582B-F0A6-4E15-4E80-61736B6F3B29
        Location: C:\Users\Victim\AppData\Local\Microsoft\Vault
```

Success shows vault details; errors may indicate access restrictions.

## Related

- [[procedures/List-Credentials-in-Windows-Credential-Manager-Vault]]
