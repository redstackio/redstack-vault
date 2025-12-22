---
type: command
executor: command_prompt
data: cmdkey.exe /list
platforms:
  - Windows
tags:
  - credential-access
  - enumeration
verified: true
validated: true
---

# cmdkey-list-stored-credentials

## Command

```command_prompt
cmdkey.exe /list
```

## Description

This command uses the built-in Windows cmdkey.exe utility to list all stored credentials in the Credential Manager for the current user. It is useful for quickly identifying saved usernames and targets (e.g., remote servers or domains) that can be used for lateral movement or further enumeration in security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/list` | Displays the list of all stored credentials for the current user | Yes |

No additional arguments are needed; the command targets the current user's credentials by default. For a specific target, use `/list:$_TARGET` where $_TARGET is the credential target (e.g., Domain:target=server.corp.local).

## Examples

### Basic Usage

```command_prompt
cmdkey.exe /list
```

This will output all stored credentials in a readable format.

### Advanced Usage

Cmdkey does not support built-in filtering, but you can pipe the output for parsing:

```command_prompt
cmdkey.exe /list | findstr "Target"
```

This filters the output to show only lines containing "Target" for easier review.

## Expected Output

```
Currently stored credentials:

    Target: Domain:target=dc01.corp.local
    Type: Domain Password
    User: DOMAIN\Administrator

    Target: MicrosoftAccount:user@outlook.com
    Type: Generic
    User: user@outlook.com
```

The output shows targets, types (e.g., Domain Password, Generic), and associated users. If no credentials are stored, it will indicate "Currently stored credentials:" with no entries listed.

## Related

- [[procedures/List-Credentials-in-Windows-Credential-Manager-Vault]]
