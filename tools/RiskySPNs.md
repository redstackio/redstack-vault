---
type: tool
description: >-
  A PowerShell module for detecting and abusing risky Service Principal Names
  (SPNs) in Active Directory environments, focusing on vulnerabilities like
  Kerberoasting and unconstrained delegation.
url: 'https://github.com/daftmug/RiskySPNs'
verified: true
created_at: '2019-08-28T21:17:27.640458+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - kerberoasting
  - spn
  - privilege-escalation
  - post-exploitation
validated: true
---

# RiskySPNs

**Status**: Unverified

## Overview

RiskySPNs is a PowerShell module designed to identify risky configurations associated with Service Principal Names (SPNs) in Active Directory. It enumerates user and service accounts with SPNs, flagging those susceptible to common attacks such as Kerberoasting (requesting and cracking TGS tickets for service accounts) and abuse of unconstrained or resource-based constrained delegation. This tool is particularly useful in red team engagements for discovering privilege escalation paths in Windows domain environments.

## Description

The module provides functions to query Active Directory for SPN-registered accounts and assess their risk based on delegation settings, password policies, and other attributes. It supports authenticated queries to domain controllers and outputs results in a structured format for further exploitation or reporting. Common use cases include initial domain reconnaissance after gaining foothold credentials and identifying targets for credential dumping or ticket-based attacks.

## Features

- Enumeration of all SPN-registered accounts in a domain
- Risk assessment for unconstrained delegation, weak encryption types, and pre-auth not required settings
- Support for Kerberoasting candidate identification (service accounts with SPNs and RC4 support)
- CSV export for results
- Integration with Active Directory modules for authenticated queries

## Installation

### Requirements

- PowerShell 5.1 or later
- ActiveDirectory module (install via RSAT or Import-Module ActiveDirectory)
- Network access to a domain controller
- Domain credentials with read access to AD objects

### Install Commands

```powershell
# Clone the repository
git clone https://github.com/daftmug/RiskySPNs.git

# Navigate to the directory
cd RiskySPNs

# Import the module
Import-Module .\RiskySPNs.psm1
```

## Basic Usage

```powershell
# View help for the main function
Get-Help Find-RiskySPNs -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -DomainController | Specifies the domain controller to query |
| -Username | Provides credentials for authentication |
| -Password | Supplies the password (use SecureString for security) |
| -OutputFile | Exports results to a CSV file |
| -Verbose | Enables detailed output during execution |

## Examples

### Example 1: Basic Usage

```powershell
Find-RiskySPNs -DomainController dc01.example.com -Username domain\attacker -Password P@ssw0rd
```

This runs the enumeration against the specified DC and displays risky SPNs in the console.

### Example 2: Advanced Usage

```powershell
Find-RiskySPNs -DomainController dc01.example.com -Username domain\attacker -Password P@ssw0rd -OutputFile C:\temp\risky_spns.csv -Verbose
```

This exports the results to a CSV file with verbose logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Account
- [[Steal or Forge Kerberos Tickets]] Steal or Forge Kerberos Tickets
- [[Kerberoasting]] Kerberoasting

### Tactics

- [[Discovery]] Discovery
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing Import-Module RiskySPNs or Find-RiskySPNs invocation
- LDAP queries to domain controllers for user objects with servicePrincipalName attributes
- Unusual credential usage patterns from non-admin accounts querying SPNs
- File creation of CSV outputs with SPN data in temporary directories
- Enable PowerShell Script Block Logging and Module Logging for detailed tracking

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerSploit]]
- [[tools/BloodHound]]

## References

- Official GitHub Repository: https://github.com/daftmug/RiskySPNs
- Related Blog Post: https://daftmug.com/blog/riskyspns
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1558/003/
