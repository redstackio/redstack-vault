---
id: e4bb128e-59b7-4736-a0a6-b80911fb1a63
name: pth-net-get-exchange-servers-group-members
type: command
executor: bash
data: >-
  pth-net rpc group members "Exchange Servers" -I $_DC_HOSTNAME -U
  $_DOMAIN/$_USERNAME%$_PASSWORD
output: null
created_at: '2023-04-06T03:56:08.022315+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - discovery
  - active-directory
verified: true
validated: true
---

# pth-net-get-exchange-servers-group-members

## Command

```bash
pth-net rpc group members "Exchange Servers" -I $_DC_HOSTNAME -U $_DOMAIN/$_USERNAME%$_PASSWORD
```

## Description

Uses Impacket's pth-net to query remote procedure call for members of the 'Exchange Servers' group on a domain controller, aiding in targeting for relay attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "Exchange Servers" | Group name to query | Yes |
| -I $_DC_HOSTNAME | Target DC hostname/IP (e.g., dc01.domain.local) | Yes |
| -U $_DOMAIN/$_USERNAME%$_PASSWORD | Credentials in format domain/user%pass | Yes |

## Examples

### Basic Usage

```bash
pth-net rpc group members "Exchange Servers" -I dc01.domain.local -U domain/user%pass
```

## Expected Output

Group name: Exchange Servers
Group SID: S-1-5-21-...-1107
Members:
  mail01.domain.local$
  mail02.domain.local$

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
