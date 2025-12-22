---
type: tool
verified: true
platforms:
  - Windows
tags:
  - credential-access
  - enumeration
  - windows-credentials
url: 'https://learn.microsoft.com/en-us/windows/win32/secauthn/vaultcmd'
validated: true
---

# vaultcmd

**Status**: ✓ Verified

## Overview

vaultcmd is a built-in Windows command-line utility for interacting with the Credential Manager, which securely stores user credentials such as passwords, certificates, and keys. It allows users to list, add, modify, and delete credentials from various vaults including Windows Credentials, Generic Credentials, and Web Credentials. In security testing, it's commonly used for enumerating stored credentials to assess potential exposure of sensitive information like domain passwords or application logins.

## Description

vaultcmd provides programmatic access to the Windows Credential Manager without requiring GUI interaction. It supports operations on different credential types and vaults, making it valuable for post-exploitation scenarios where an attacker has local access to enumerate saved credentials. The tool outputs structured details about each credential, including schema, resource targets, and user identities, which can reveal exploitable authentication data.

## Features

- List credentials from specific vaults
- Add, modify, or delete stored credentials
- Support for multiple credential types (e.g., domain passwords, generic logins)
- Command-line only, no dependencies on external libraries

## Installation

### Requirements

- Windows Vista or later (built-in on modern versions)
- Administrative privileges may be required for certain operations

### Install Commands

No installation required; vaultcmd.exe is included by default in Windows installations. Verify availability by running:

```command_prompt
vaultcmd.exe /?
```

If missing (rare on standard installs), it may indicate a corrupted system; repair via Windows installation media.

## Basic Usage

```command_prompt
vaultcmd.exe /?
```

Displays help for all available commands and options.

### Common Options

| Option | Description |
|--------|-------------|
| /listcreds:"VaultName" | Lists credentials in the specified vault |
| /addcreds | Adds a new credential to a vault |
| /deletecreds | Removes a credential by resource and identity |
| /? | Shows command help |

## Examples

### Example 1: Basic Usage

```command_prompt
vaultcmd.exe /listcreds:"Windows Credentials"
```

Enumerates all credentials stored in the Windows Credentials vault.

### Example 2: Advanced Usage

```command_prompt
vaultcmd.exe /listcreds:"Generic Credentials"
```

Lists generic credentials, often used for application-specific logins.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Credential Manager]] Credentials from Password Stores: NTDS
- [[Credential Dumping]] OS Credential Dumping

### Tactics

- [[Credential Access]] Credential Access
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor command-line execution logs for "vaultcmd.exe" invocations, especially /listcreds operations
- Audit Credential Manager access via Windows Event Logs (Event ID 4657 for registry access to credential hives)
- Enable Process Tracking in Sysmon to log vaultcmd.exe process creation and arguments
- Look for anomalous credential enumeration in environments without legitimate admin activity

## Related Procedures

- [[procedures/Enumerate-Windows-Credentials-via-Vaultcmd]]

## Related Tools

- [[tools/Mimikatz]]
- [[tools/cmdkey]]

## References

- [Microsoft Docs: vaultcmd](https://learn.microsoft.com/en-us/windows/win32/secauthn/vaultcmd)
- [MITRE ATT&CK: Credential Access](https://attack.mitre.org/tactics/TA0006/)
