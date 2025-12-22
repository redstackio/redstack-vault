---
id: def6d704-288a-4be0-bd5c-53e24d9db06a
type: command
executor: bash
data: nmap -script ldap-rootdse -p 389 $_TARGET_IP
output: |-
  root@kali:~# nmap -script ldap-rootdse -p 389 10.10.10.10
  Starting Nmap 7.80 ( https://nmap.org ) at 2019-12-15 17:23 EST
  Nmap scan report for 10.10.10.10
  Host is up (0.078s latency).

  PORT    STATE SERVICE
  389/tcp open  ldap
  | ldap-rootdse: 
  | LDAP Results
  |   <ROOT>
  |       supportedLDAPVersion: 3
  |       namingContexts: dc=corporatehq,dc=com
  |       supportedExtension: 1.3.6.1.4.1.1466.20037
  |_      subschemaSubentry: cn=schema

  Nmap done: 1 IP address (1 host up) scanned in 1.08 seconds
created_at: '2019-12-15T22:33:38.234029+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - ldap
  - enumeration
  - active-directory
verified: true
validated: true
---

# nmap-ldap-rootdse-query

## Command

```bash
nmap -script ldap-rootdse -p 389 $_TARGET_IP
```

## Description

This command executes Nmap with the ldap-rootdse script to anonymously query the Root DSE of an LDAP server on the specified target IP over port 389. It is used during reconnaissance to gather directory service metadata, such as domain naming contexts, without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the LDAP server to query | Yes |
| -p 389 | Target port for unencrypted LDAP (use 636 for LDAPS) | Yes |
| -script ldap-rootdse | Invokes the Nmap Scripting Engine (NSE) ldap-rootdse script for Root DSE enumeration | Yes |

## Examples

### Basic Usage

```bash
nmap -script ldap-rootdse -p 389 10.10.10.10
```

### LDAPS Variant

```bash
nmap -script ldap-rootdse -p 636 --script-args ldap.rootdse.ldaps=1 10.10.10.10
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# nmap -script ldap-rootdse -p 389 10.10.10.10
Starting Nmap 7.80 ( https://nmap.org ) at 2019-12-15 17:23 EST
Nmap scan report for 10.10.10.10
Host is up (0.078s latency).

PORT    STATE SERVICE
389/tcp open  ldap
| ldap-rootdse: 
| LDAP Results
|   <ROOT>
|       supportedLDAPVersion: 3
|       namingContexts: dc=corporatehq,dc=com
|       supportedExtension: 1.3.6.1.4.1.1466.20037
|_      subschemaSubentry: cn=schema

Nmap done: 1 IP address (1 host up) scanned in 1.08 seconds
```

## Related

- [[procedures/Query-LDAP-Root-DSE-for-Domain-Enumeration]]
