---
url: 'https://metasploit.com'
tags:
  - exploitation
  - rce
  - smb
type: tool
platforms:
  - Linux
  - Windows
description: >-
  Penetration testing framework with modules for exploiting vulnerabilities like
  EternalBlue on Windows SMB services.
id: 29f28f9f-1bad-4ae8-bb89-0d4b765f5f45
created_at: '2025-12-14T17:31:19.098Z'
updated_at: '2025-12-14T17:31:19.098Z'
verified: false
validated: true
submitted: true
---
# Metasploit

**Status**: Unverified

## Overview

Metasploit is an open-source framework for developing and executing exploit code, used here to analyze and reference EternalBlue modules based on NTLM-extracted host details.

## Description

It provides modules for scanning and exploiting remote services, including MS17-010 for SMB RCE on unpatched Windows systems, allowing assessment of disclosed servers without active exploitation.

## Features

- Feature 1: Exploit and auxiliary modules for vulnerability testing
- Feature 2: Payload generation for RCE scenarios
- Feature 3: Integration with Nmap for host discovery

## Installation

### Requirements

- Ruby 2.7+ and PostgreSQL
- Git for source install

### Install Commands

```bash
# Kali Linux (pre-installed) or
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
```

## Basic Usage

```bash
msfconsole -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -q | Quiet mode |
| --database | Specify DB connection |

## Examples

### Example 1: Basic Usage

```bash
msfconsole
search ms17_010
```

### Example 2: Advanced Usage

```bash
use auxiliary/scanner/smb/smb_ms17_010
set RHOSTS 192.168.1.100
run
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation of Remote Services]] Exploitation of Remote Services
- [[PowerShell]] PowerShell

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious msfconsole processes
- Failed SMB exploit attempts in logs

## Related Procedures

- [[procedures/Analyze-for-EternalBlue-Vulnerability]]

## Related Tools

- [[Related Tool: Cobalt Strike]]
- [[Related Tool: Empire]]

## References

- Official documentation: https://docs.metasploit.com
- EternalBlue module: https://www.exploit-db.com/exploits/42030
