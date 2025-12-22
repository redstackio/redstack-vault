---
id: c28aeba3-6ffb-4423-9411-858fcb9b5b0d
type: tool
verified: true
created_at: '2019-08-28T21:17:37.261293+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - exchange
  - mapi
  - rpc
  - redteam
  - post-exploitation
url: 'https://github.com/dirkjanm/krbrelayx/tree/master/Ruler'
validated: true
---

# Ruler

**Status**: Unverified

## Overview

Ruler is a post-exploitation tool designed for interacting with Microsoft Exchange servers remotely via the MAPI/HTTP or RPC/HTTP protocols. It is commonly used in red team engagements to perform actions like proxy logons, mailbox enumeration, email searching, and file uploads/downloads, enabling attackers to maintain persistence and exfiltrate data from Exchange environments.

## Description

Ruler leverages Exchange Web Services (EWS) and MAPI over HTTP to authenticate and execute operations without direct mailbox access. It supports exploiting vulnerabilities like ProxyLogon (CVE-2021-26855) for initial session establishment and can chain with other tools for lateral movement in Active Directory environments. Ideal for scenarios involving compromised credentials or initial access to Outlook Web Access (OWA).

## Features

- Feature 1: ProxyLogon exploitation for session hijacking
- Feature 2: Mailbox access and enumeration (emails, contacts, calendars)
- Feature 3: Search and export capabilities for sensitive data
- Feature 4: File upload/download via Exchange APIs
- Feature 5: Support for both MAPI/HTTP and RPC/HTTP protocols

## Installation

### Requirements

- .NET SDK 6.0 or later
- Git for cloning the repository
- Access to a C# compiler (included with .NET)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/dirkjanm/Ruler.git
cd Ruler

# Build the tool
dotnet build -c Release

# For Linux/macOS, ensure .NET is installed via package manager
# Ubuntu: sudo apt install dotnet-sdk-6.0
# macOS: brew install --cask dotnet
```

## Basic Usage

```bash
dotnet Ruler.dll --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |
| --url | Target Exchange URL |
| --username | Authentication username |
| --domain | AD domain |
| --password | Password |
| --action | Specify action (e.g., ProxyLogon, GetMailbox) |

## Examples

### Example 1: Basic Usage

```bash
dotnet Ruler.dll --url https://exchange.target.com/EWS/Exchange.asmx --username user@target.com --domain TARGET --password Pass123 --action ProxyLogon
```

### Example 2: Advanced Usage

```bash
dotnet Ruler.dll --url https://exchange.target.com/EWS/Exchange.asmx --username user@target.com --domain TARGET --password Pass123 --action Search --mailbox victim@target.com --query "confidential" --verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Spraying]] Password Spraying (for credential validation)
- [[Valid Accounts]] Valid Accounts (using compromised Exchange creds)
- [[Windows Remote Management]] Windows Remote Services (via MAPI/RPC)
- [[Email Collection]] Email Collection

### Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual MAPI/HTTP traffic from non-Exchange clients (monitor IIS logs for /mapi/* endpoints)
- Detection method 2: Anomalous EWS API calls with high volume searches or proxy logons (enable Exchange audit logging)
- Detection method 3: .NET process spawning Ruler.dll on attacker machines (EDR rules for dotnet.exe with suspicious args)
- Detection method 4: Increased failed logons or session establishments from internal IPs

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
- [[tools/Mimikatz]]

## References

- Official GitHub: https://github.com/dirkjanm/Ruler
- Blog post on ProxyLogon: https://dirkjanm.io/exchange-marshalling-service-complete-relay/
- MITRE ATT&CK for Exchange: https://attack.mitre.org/techniques/T1114/
