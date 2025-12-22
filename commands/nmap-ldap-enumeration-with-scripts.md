---
id: 58d5180c-fe67-4c17-b796-e2e2bc51f555
name: nmap-ldap-enumeration-with-scripts
type: command
executor: bash
data: nmap -p 389 --script ldap-search $_TARGET_IP
output: |-
  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 18:06 EDT
  Nmap scan report for 10.10.10.10
  Host is up (0.069s latency).
  PORT    STATE SERVICE
  389/tcp open  ldap
  | ldap-search: 
  |   Context: dc=example,dc=com
  |     dn: dc=example,dc=com
  |         dc: example
  |         objectClass: top
  |         objectClass: domain

  Nmap done: 1 IP address (1 host up) scanned in 0.90 seconds
created_at: '2019-09-13T22:29:10.938901+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - ldap
verified: true
validated: true
---

# nmap-ldap-enumeration-with-scripts

## Command

```bash
nmap -p 389 --script ldap-search $_TARGET_IP
```

## Description

Uses Nmap's ldap-search NSE script to anonymously query LDAP for base DN and objects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p 389 | Target LDAP port | Yes |
| --script ldap-search | Run LDAP search script | Yes |
| $_TARGET_IP | Target IP | Yes |

## Examples

### Basic Usage

```bash
nmap -p 389 --script ldap-search 192.168.1.100
```

### With Authentication

```bash
nmap -p 389 --script ldap-search --script-args auth=simple,username=user,Password=pass 192.168.1.100
```

## Expected Output

LDAP context and DN details.

## Related

- [[procedures/Query-LDAP-and-Enumerate-Base-DN-with-Nmap]]
- [[tools/Nmap]]
