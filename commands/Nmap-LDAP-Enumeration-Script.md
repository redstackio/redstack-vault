---
type: command
executor: bash
data: nmap -p 389 --script ldap-search $_TARGET_IP
output: |-
  Starting Nmap 7.80 ( https://nmap.org ) at 2023-10-01 12:05 UTC
  Nmap scan report for dc.example.com (192.168.1.10)
  Host is up (0.00050s latency).
  PORT    STATE SERVICE
  389/tcp open  ldap
  | ldap-search: 
  |   Base DN: dc=example,dc=com
  |   Context: dc=example,dc=com
  |     dn: dc=example,dc=com
  |         dc: example
  |         objectClass: top
  |         objectClass: domain
  |     dn: ou=Users,dc=example,dc=com
  |         ou: Users
  |         objectClass: top
  |         objectClass: organizationalUnit

  Nmap done: 1 IP address (1 host up) scanned in 2.15 seconds
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - enumeration
  - ldap
verified: true
validated: true
---

# Nmap-LDAP-Enumeration-Script

## Command

```bash
nmap -p 389 --script ldap-search $_TARGET_IP
```

## Description

Executes Nmap's ldap-search NSE script to perform anonymous LDAP queries, extracting base DN and basic directory structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p 389 | Target LDAP port | Yes |
| --script ldap-search | Run LDAP search script | Yes |
| $_TARGET_IP | Target domain controller IP | Yes |

## Examples

### Basic Usage

```bash
nmap -p 389 --script ldap-search 192.168.1.10
```

### Advanced Usage

```bash
nmap -p 389 --script ldap-search,ldap-rootdse -oX ldap.xml $_TARGET_IP
```

XML output for parsing.

## Expected Output

LDAP contexts and DNs, revealing domain structure.

## Related

- [[procedures/Query-LDAP-and-Enumerate-Base-DN-with-Nmap]]
- [[tools/Nmap]]
