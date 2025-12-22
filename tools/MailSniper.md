---
id: f70a5ea0-430f-4501-8928-4928e1399f7f
type: tool
verified: true
created_at: '2019-08-28T21:17:39.911660+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - discovery
  - credential-access
  - collection
  - exchange
  - email
  - powershell
url: 'https://github.com/dafthack/MailSniper'
validated: true
---

# MailSniper

**Status**: Unverified

## Overview

MailSniper is a PowerShell-based penetration testing tool designed for searching and interacting with email in Microsoft Exchange environments. It enables red teams to perform reconnaissance on the Global Address List (GAL), search mailboxes for sensitive information like passwords or insider intel, and conduct password spraying attacks against Outlook Web Access (OWA) or Exchange Web Services (EWS). Commonly used in Active Directory assessments to identify weak credentials or collect data for lateral movement.

## Description

MailSniper provides modular functions for Exchange-specific operations, leveraging PowerShell remoting or direct EWS access. It supports authenticated searches across mailboxes, enumeration of mail recipients, and brute-force techniques tailored to avoid account lockouts. The tool is particularly effective in environments with Exchange Server 2010+ and requires domain credentials for operation. It does not perform unauthenticated attacks but excels in post-compromise scenarios for data exfiltration via email content.

## Features

- Feature 1: GAL enumeration to discover all mail-enabled users, groups, and contacts.
- Feature 2: Keyword-based searches in mailboxes for sensitive data like passwords or network diagrams.
- Feature 3: Password spraying capabilities against OWA/EWS with delay controls to evade detection.
- Feature 4: Integration with PowerShell for scripting complex email-based attacks.

## Installation

### Requirements

- PowerShell 3.0 or later
- Access to a domain-joined Windows machine
- Valid credentials for Exchange (e.g., service account with mailbox search permissions)
- .NET Framework 4.5+ for EWS if using web services

### Install Commands

```powershell
# Download the module from GitHub
Invoke-WebRequest -Uri https://github.com/dafthack/MailSniper/archive/master.zip -OutFile MailSniper.zip

# Extract and import
Expand-Archive -Path MailSniper.zip -DestinationPath .\MailSniper
Import-Module .\MailSniper-master\MailSniper.ps1
```

For persistent use, copy MailSniper.ps1 to a module path like $env:PSModulePath and import via Import-Module MailSniper.

## Basic Usage

```powershell
tool-name --help
```

Load the module first:

```powershell
Import-Module MailSniper.ps1
Get-Command -Module MailSniper
```

### Common Options

| Option | Description |
|--------|-------------|
| -Credentials | Specify PSCredential for authentication |
| -DomainController | Target a specific DC for queries |
| -Verbose | Enable detailed output |
| -Delay | Add delays between attempts to avoid lockouts |

## Examples

### Example 1: Basic Usage

```powershell
Get-GlobalMailRecipients -DomainController dc01.contoso.com -Credentials $cred
```

### Example 2: Advanced Usage

```powershell
Invoke-DomainPasswordSpray -UserList users.txt -Password Summer2023 -Domain contoso.com -Delay 300
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Account (GAL enumeration)
- [[Password Guessing]] Password Guessing (password spraying)
- [[Email Collection]] Email Collection (mailbox searches)

### Tactics

- [[Discovery]] Discovery
- [[Credential Access]] Credential Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell execution logs for MailSniper module imports or function calls like Get-GlobalMailRecipients.
- Detection method 2: Audit EWS/OWA login attempts for patterns of single-password sprays across multiple accounts.
- Detection method 3: Enable Exchange mailbox audit logging to track unauthorized searches.
- Detection method 4: Network monitoring for unusual PowerShell remoting to Exchange servers on ports 5985/5986.

## Related Procedures

No related procedures linked yet.

## Related Tools

- [[tools/PowerSploit]]
- [[tools/SharpExchange]]

## References

- Official GitHub: https://github.com/dafthack/MailSniper
- Blog post: https://blog.netspi.com/mailsniper-for-exchange/
- MITRE ATT&CK: https://attack.mitre.org/
