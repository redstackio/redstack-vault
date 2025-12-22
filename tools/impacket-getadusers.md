---
type: tool
verified: true
platforms:
  - Linux
  - Windows
tags:
  - Active Directory
  - Enumeration
url: 'https://github.com/SecureAuthCorp/impacket'
validated: true
---

# impacket-getadusers

**Status**: ✓ Verified

## Overview

impacket-getadusers is a tool from the Impacket suite designed to gather detailed information about Active Directory domain users. It queries the domain controller via LDAP to retrieve attributes such as user names, email addresses, last logon timestamps, and password last set dates. This tool is commonly used in penetration testing for reconnaissance and enumeration of domain accounts.

## Description

The tool connects to a domain controller using provided credentials and performs an LDAP query to enumerate all user objects in the domain. It supports outputting various attributes and can be used to identify active accounts, dormant users, or potential targets for further attacks like password spraying or privilege escalation. Impacket is a collection of Python classes for working with network protocols, making this tool versatile for authenticated enumeration in Windows environments.

## Features

- Enumerates domain users with customizable attributes (e.g., name, email, lastLogon, pwdLastSet)
- Supports LDAP over TCP (port 389) or LDAPS (port 636)
- Handles Kerberos authentication for secure connections
- Outputs data in a tabular format for easy parsing
- Integrates with other Impacket tools for chained enumeration

## Installation

### Requirements

- Python 3.6 or higher
- pip package manager

### Install Commands

```bash
# Install Impacket suite (includes GetADUsers.py)
pip3 install impacket
```

On Kali Linux, Impacket is often pre-installed or can be added via:

```bash
sudo apt update && sudo apt install python3-impacket
```

For Windows, use pip in a Python environment. Verify installation by running `GetADUsers.py -h`.

## Basic Usage

```bash
GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DC_IP
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-all` | Retrieve all available user attributes |
| `-dc-ip IP` | Specify the domain controller IP address |
| `-dc-port PORT` | Specify LDAP port (default 389) |
| `-debug` | Enable debug output for troubleshooting |

## Examples

### Example 1: Basic Usage

```bash
GetADUsers.py 'example.com/user:password' -dc-ip 10.10.10.10
```

This enumerates basic user information from the domain controller at 10.10.10.10.

### Example 2: Advanced Usage with All Attributes

```bash
GetADUsers.py 'example.com/user:password' -dc-ip 10.10.10.10 -all -debug
```

This retrieves full details including email, last logon, and password policies, with verbose logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Account (Discovery of domain accounts via LDAP queries)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual LDAP queries from external or non-domain-joined systems (monitor port 389/636 traffic)
- Query patterns targeting user objects (e.g., filters for sAMAccountName, userPrincipalName)
- Authentication attempts from low-privilege accounts performing broad enumerations
- Enable LDAP signing and channel binding on domain controllers to prevent anonymous binds
- Use tools like Windows Event ID 4622 (LDAP bind failures) or Sysmon for network connections

## Related Procedures

No specific procedures linked yet. This tool is often used in procedures for authenticated Active Directory enumeration.

## Related Tools

- [[impacket-getnthash]] (For NTLM hash extraction)
- [[tools/BloodHound]] (For AD graph analysis)

## References

- Official Impacket GitHub: https://github.com/SecureAuthCorp/impacket
- Impacket Documentation: https://www.secureauth.com/labs/impacket

*Last updated: 2023-05-30*
