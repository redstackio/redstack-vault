---
id: 5aa14c3c-6426-46bc-a6aa-5454d3fb84a2
name: Windows-DPAPI-Credential-Theft
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.204797+00:00'
updated_at: '2023-04-10T20:37:12.504960+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
  - '[[Credentials from Password Stores]]'
sub_techniques:
  - '[[Windows Credential Manager]]'
tags:
  - '[[tags/Data-Protection-API]]'
  - '[[tags/Windows-DPAPI]]'
commands:
  - '[[commands/vaultcmd-list-vaults]]'
  - '[[commands/vaultcmd-list-credentials-specific-vault]]'
  - '[[commands/vaultcmd-list-windows-credentials]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-DPAPI-Credential-Theft

## Summary

This procedure demonstrates how to extract credentials stored in Windows Data Protection API (DPAPI) vaults, specifically targeting the Windows Credentials Manager, to retrieve sensitive information like passwords and keys protected by the user's login credentials.

## Description

The Windows Data Protection API (DPAPI) encrypts sensitive data using the user's login credentials, storing it in protected vaults such as the Windows Credentials Manager. An attacker with local access and sufficient privileges can enumerate these vaults and list their contents to steal credentials for further lateral movement or privilege escalation. This technique is commonly used in post-exploitation scenarios to harvest stored authentication material from applications like browsers or remote desktop clients. The process involves listing available vaults and then querying specific ones for credential details, which are decrypted using the current user's context.

## Requirements

1. Local administrator or SYSTEM-level privileges on a Windows system.
2. Access to the command prompt or PowerShell on the target machine.
3. The VaultCmd.exe utility, which is built into Windows (Vista and later).
4. The current user's login credentials to decrypt DPAPI-protected data.

## Defense

- Implement strong access controls to restrict local and remote access to sensitive systems, using tools like AppLocker or Windows Defender Application Control.
- Monitor for suspicious activity, such as unauthorized use of VaultCmd or unusual credential access events in Windows Event Logs (Event ID 4648 for logons).
- Enable Credential Guard on Windows 10/11 Enterprise to isolate and protect credentials from extraction.
- Use endpoint detection and response (EDR) tools to detect anomalous process execution involving credential-dumping utilities.

## Objectives

1. Enumerate all available DPAPI vaults on the target system.
2. List credentials from specific vaults or the default Windows Credentials Manager.
3. Extract and decrypt stored credentials for use in further attacks.

## Instructions

### Step 1: Enumerate Available Vaults

**Context**: Begin by listing all DPAPI vaults on the system to identify potential targets for credential extraction. This step reveals the GUIDs or names of vaults where sensitive data is stored.

**Command** ([[commands/vaultcmd-list-vaults]]):
```cmd
vaultcmd /list
```

> This command outputs a list of all vaults, including their GUIDs and descriptions. Use this information to identify relevant vaults, such as those for Web Credentials or Windows Credentials. If no vaults are listed, it may indicate an empty or protected environment.

### Step 2: List Credentials from a Specific Vault

**Context**: Once vaults are identified, query a specific vault by name or GUID to retrieve its stored credentials. This is useful for targeting application-specific storage, like remote desktop or network share credentials.

**Command** ([[commands/vaultcmd-list-credentials-specific-vault]]):
```cmd
VaultCmd /listcreds:<namevault>|<guidvault> /all
```

> Replace `<namevault>` with the vault name (e.g., "Web Credentials") or `<guidvault>` with the GUID from Step 1. The `/all` flag ensures all credential details, including encrypted blobs, are displayed. Success is indicated by credential entries showing fields like username, password (encrypted), and resource.

### Step 3: List Credentials from Windows Credentials Manager

**Context**: Target the default Windows Credentials vault to extract generic stored credentials, such as those for network authentication or application logins. This vault often contains high-value items like domain passwords.

**Command** ([[commands/vaultcmd-list-windows-credentials]]):
```cmd
vaultcmd /listcreds:"Windows Credentials" /all
```

> This command specifically queries the Windows Credentials Manager vault. Expected output includes a table of credentials with details like target name, username, and encrypted password. If credentials are present, they can be decrypted in the current user session for immediate use.
