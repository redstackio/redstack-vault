---
id: 00384be9-6759-459d-ad3e-6f1ecfbbf9e0
name: net-user-guest-enumerate
type: command
executor: cmd
data: net user guest
output: null
created_at: '2023-04-06T03:56:30.646970+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - credentials
verified: true
validated: true
---

# net-user-guest-enumerate

## Command

```cmd
net user guest
```

## Description

This command queries and displays information about the built-in Guest user account on a Windows system, including status, password requirements, and last logon details. Use it to assess if the account is vulnerable to default credential exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `guest` | Specifies the Guest username (fixed) | Yes |

## Examples

### Basic Usage

```cmd
net user guest
```

### Advanced Usage

Run on remote system:
```cmd
net user guest /domain
```

## Expected Output

```
The request will be processed at a domain controller for domain example.com.

User name                    Guest
Full Name                    Guest Account
Comment                      Built-in account for guest access to the computer/domain
User's comment

Account active               Yes
Account expires              Never

Password last set            Never
Password expires             Never

Password changeable         Never
Password required            No
User may change password     No

Workstations allowed         All
Logon script
Profile
Home directory
Last logon                   Never

Logon hours                  All
Local Group Memberships      *Guests
Global Group memberships     *None
The command completed successfully.
```

Success is indicated by 'Account active: Yes' and 'Password required: No'.

## Related

- [[procedures/Authenticate-with-Windows-Guest-Default-Credentials]]
