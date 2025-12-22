---
type: tool
platforms:
  - Windows
tags:
  - credential-access
  - enumeration
  - windows-credentials
commands:
  - '[[commands/cmdkey-list-stored-credentials]]'
url: >-
  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey
verified: true
validated: true
---

# cmdkey

**Status**: ✓ Verified

## Overview

cmdkey is a built-in Windows command-line utility for managing stored user names, passwords, and other credentials in the Windows Credential Manager. It is commonly used in security testing to enumerate, add, or remove credentials that may enable lateral movement, such as saved RDP or SMB authentication details.

## Description

cmdkey.exe allows operators to interact with the Credential Manager from the command line, which stores credentials for various targets like domain passwords, generic credentials, and Microsoft accounts. In offensive security, it is particularly useful during post-exploitation for discovering reusable credentials without needing GUI access. The tool supports operations on local or remote targets and is available on Windows Vista and later versions.

## Features

- List stored credentials with details on targets, types, and users
- Add new credentials for specific targets (e.g., for automated logins)
- Delete existing credentials to clean up traces
- Target domain-specific or generic credential stores

## Installation

### Requirements

- Windows Vista or later (built-in, no additional requirements)

### Install Commands

No installation required; cmdkey.exe is included in the Windows system directory (C:\Windows\System32).

## Basic Usage

```command_prompt
cmdkey /?
```

### Common Options

| Option | Description |
|--------|-------------|
| `/list` | Display all stored credentials |
| `/list:TARGET` | List credentials for a specific target |
| `/add:TARGET` | Add a credential for a target |
| `/delete:TARGET` | Delete a credential for a target |
| `/generic` | Specify generic credential type |
| `/user:USERNAME` | Specify the username |
| `/pass:PASSWORD` | Specify the password |

## Examples

### Example 1: Basic Usage

```command_prompt
cmdkey /list
```

Lists all stored credentials for the current user.

### Example 2: Advanced Usage

```command_prompt
cmdkey /list:Domain:target=dc01.corp.local
```

Lists credentials specifically for a domain target.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials from Password Stores]] Credentials from Password Stores
- [[Windows Credential Manager]] Windows Credential Manager

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor command-line executions of cmdkey.exe via Sysmon Event ID 1 (Process Creation) with Image: cmdkey.exe and CommandLine containing /list or /add
- Audit Windows Security Event ID 4648 for credential use tied to Credential Manager access
- EDR alerts on credential enumeration patterns in post-exploitation phases

## Related Procedures

No related procedures linked.

## Related Tools

- [[tools/Mimikatz]]
- [[tools/vaultcmd]]

## References

- [Microsoft Docs: cmdkey](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey)
- MITRE ATT&CK: T1555
