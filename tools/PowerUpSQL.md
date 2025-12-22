---
id: 7557e46a-5717-46aa-9ac0-f85dfaf320c2
type: tool
description: >-
  A PowerShell toolkit for attacking and auditing Microsoft SQL Server
  databases, focusing on reconnaissance, privilege escalation, and exploitation
  of common misconfigurations.
url: 'https://github.com/NetSPI/PowerUpSQL'
verified: true
created_at: '2019-08-28T21:17:27.552993+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
tags:
  - sql-server
  - powershell
  - reconnaissance
  - exploitation
  - auditing
platforms:
  - Windows
  - Linux
validated: true
---

# PowerUpSQL

**Status**: Unverified

## Overview

PowerUpSQL is a PowerShell module designed for offensive security testing against Microsoft SQL Server. It provides functions for discovering instances, auditing permissions, brute-forcing credentials, and identifying privilege escalation opportunities. Commonly used in penetration testing to exploit weak SQL configurations and gain deeper access to Windows environments via SQL Server.

## Description

Developed by NetSPI, PowerUpSQL automates common SQL Server attack techniques, such as querying for OS information, checking for risky database roles, and exploiting xp_cmdshell for command execution. It's particularly useful in Active Directory environments where SQL Servers are prevalent, allowing attackers to pivot from initial foothold to domain compromise.

## Features

- Discovery of SQL Server instances and OS details
- Auditing of database permissions and configurations
- Brute-force attacks on SQL logins
- Exploitation of extended stored procedures like xp_cmdshell
- Enumeration of linked servers for lateral movement

## Installation

### Requirements

- PowerShell 3.0 or higher
- .NET Framework 4.0 (for Windows)
- Access to SQL Server (network or local)

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/NetSPI/PowerUpSQL/master/PowerUpSQL.ps1' -OutFile 'PowerUpSQL.ps1'

# Or clone the repo
git clone https://github.com/NetSPI/PowerUpSQL.git
cd PowerUpSQL
```

## Basic Usage

```powershell
Import-Module PowerUpSQL.ps1
Get-Help Invoke-SQLOSDiscovery
```

### Common Options

| Option | Description |
|--------|-------------|
| -Instance | Specify SQL Server instance name |
| -Username | SQL login username |
| -Password | SQL login password |
| -Verbose | Enable verbose output |
| -ThreadCount | Number of threads for parallel operations |

## Examples

### Example 1: Basic Usage

```powershell
Import-Module PowerUpSQL.ps1; Invoke-SQLOSDiscovery -Instance 'MSSQLSERVER'
```

### Example 2: Advanced Usage

```powershell
Import-Module PowerUpSQL.ps1; Invoke-SQLAudit -Instance 'remotehost\\SQLEXPRESS' -Username 'sa' -Password 'P@ssw0rd'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation of Remote Services]] Exploitation of Remote Services
- [[Brute Force]] Brute Force
- [[T1087.002]] Domain Account Discovery

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing Import-Module PowerUpSQL.ps1
- Unusual SQL queries from non-standard accounts
- Network traffic to SQL ports (1433/TCP) from unexpected sources
- Event logs for failed SQL logins during brute-force attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]]
- [[tools/CrackMapExec]]

## References

- Official GitHub: https://github.com/NetSPI/PowerUpSQL
- Blog post: https://blog.netspi.com/powerupsql-powerful-sql-server-attacks/

*Last updated: 2023-05-29T16:48:53.029709+00:00*
