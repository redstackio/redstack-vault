---
id: 58a60279-df57-448f-96d6-39908a649134
name: ldapsearch
type: tool
verified: true
created_at: '2020-02-25T23:02:18.196335+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - Enumeration
  - Network
url: 'https://www.openldap.org/doc/man-pages/ldapsearch.html'
commands:
  - '[[commands/ldapsearch-anonymous-query-base-dn]]'
validated: true
---

# ldapsearch

**Status**: ✓ Verified

## Overview

ldapsearch is a command-line tool from the OpenLDAP suite used for querying and enumerating LDAP (Lightweight Directory Access Protocol) servers. It allows security testers to perform reconnaissance on directory services, such as Active Directory or OpenLDAP, by retrieving information about users, groups, organizational units, and other directory objects. The tool supports both anonymous and authenticated queries but requires manual specification of parameters like base DN, filters, and scopes for effective enumeration. It is commonly used in penetration testing for discovering network infrastructure and user accounts.

Category: Reconnaissance

## Description

ldapsearch connects to an LDAP server over TCP (default port 389 for LDAP, 636 for LDAPS) and issues search requests based on provided criteria. It outputs results in LDIF format, which can be parsed for further analysis. Key capabilities include subtree searches, attribute filtering (e.g., for sAMAccountName or uid), and support for SSL/TLS encryption. While it does not automate full enumeration workflows, it serves as a foundational tool for targeted queries during active directory enumeration or LDAP service discovery. It is particularly useful against misconfigured servers allowing anonymous binds, which can leak sensitive information like user hashes or group memberships.

## Features

- Anonymous and authenticated LDAP queries
- Support for search scopes: base, onelevel, subtree
- Customizable filters using LDAP syntax (e.g., '(objectClass=user)')
- Output in LDIF or other formats
- SSL/TLS support for secure connections (LDAPS)
- Attribute selection to limit returned data
- Binding with credentials for privileged queries

## Installation

### Requirements

- OpenLDAP client libraries
- Network access to target LDAP ports (389/TCP, 636/TCP)

### Install Commands

#### Kali Linux
Pre-installed as part of ldap-utils package.

```bash
# Verify installation
ldapsearch --version
```

#### Debian/Ubuntu

```bash
sudo apt update
sudo apt install ldap-utils
```

#### Windows

Download and install OpenLDAP for Windows from a trusted source, or use Cygwin/MSYS2 with OpenLDAP packages.

```bash
# Using Chocolatey (if available)
choco install openldap

# Or download from: https://www.userbooster.de/en/download/openldap-for-windows.aspx
```

## Basic Usage

```bash
ldapsearch --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -x | Simple authentication (anonymous or with -D/-w for bind DN/password) |
| -H | Specify LDAP URI (e.g., ldap://target:389 or ldaps://target:636) |
| -b | Base DN for search |
| -s | Search scope (base, one, sub) |
| -f | LDAP filter |
| -LLL | Output in LDIF without comments |

## Examples

### Example 1: Basic Anonymous Query

Use [[commands/ldapsearch-anonymous-query-base-dn]] for an anonymous base DN search:

```bash
ldapsearch -x -h 10.10.10.10 -b 'dc=example,dc=com'
```

### Example 2: Authenticated User Enumeration

```bash
ldapsearch -x -H ldap://10.10.10.10 -D 'cn=admin,dc=example,dc=com' -w password -b 'dc=example,dc=com' '(objectClass=user)' sAMAccountName
```

### Example 3: SSL Query

```bash
ldapsearch -x -H ldaps://10.10.10.10:636 -b 'dc=example,dc=com' '(objectClass=*)'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to LDAP ports (389/TCP, 636/TCP) from unusual sources
- LDAP query logs showing anonymous binds or excessive searches
- Process monitoring for ldapsearch.exe or ldapsearch binary execution
- SIEM alerts on LDIF-formatted output or filter patterns like '(objectClass=user)'

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/windapsearch]]

## References

- Official man page: https://www.openldap.org/doc/man-pages/ldapsearch.html
- OpenLDAP Documentation: https://www.openldap.org/doc/
- MITRE ATT&CK: https://attack.mitre.org/
