---
id: de565687-eaa1-4ae4-a83b-f58766f78836
name: runas-execute-as-user
type: command
executor: cmd
data: 'runas [/profile] [/env] [/netonly] /user:$_USERNAME $_PROGRAM'
output: null
created_at: '2023-04-06T03:56:29.949956+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - execution
verified: true
validated: true
---

# runas-execute-as-user

## Command

```cmd
runas [/profile] [/env] [/netonly] /user:$_USERNAME $_PROGRAM
```

## Description

Runs a program as a different user, prompting for password unless credentials are stored. Used for privilege escalation when admin creds are available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | Specifies the user account | Yes |
| $_PROGRAM | Program or command to run | Yes |
| /profile | Loads user profile | No |
| /env | Uses current environment | No |
| /netonly | Applies creds to network only | No |

## Examples

### Basic Usage

```cmd
runas /user:Administrator cmd.exe
```

### Advanced Usage

```cmd
runas /env /user:DOMAIN\Admin "powershell.exe"
```

Run PowerShell as domain admin.

## Expected Output

```
Enter the password for DOMAIN\Admin:
[New window opens running as specified user]
```

## Related

- [[procedures/windows-privilege-escalation-via-runas]]
- [[commands/runas-execute-as-user-with-savecred]]
