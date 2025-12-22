---
id: d1a8ccd3-7f21-4106-92c5-ca9b7596182f
name: List Credentials in Windows Credential Manager Vault
type: procedure
verified: true
submitted: true
created_at: '2019-12-03T06:51:06.729791+00:00'
updated_at: '2023-05-25T19:42:09.815834+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques: []
tags:
  - data-exposure
  - service-attacks
commands:
  - '[[commands/List-Stored-Windows-Credentials-cmdkey]]'
  - '[[commands/List-Stored-Windows-Credentials-vaultcmd-list]]'
  - '[[commands/List-Stored-Windows-Credentials-vaultcmd-listcreds]]'
platforms:
  - Windows
tools: []
validated: true
---

# List-Credentials-in-Windows-Credential-Manager-Vault

## Summary

Users often save credentials using Windows Credential Manager, allowing them to authenticate with applications and other systems without having to reenter their username and password. Attackers may be able to use these saved credentials for lateral movement across networks.

## Description

Windows Credential Manager stores credentials for various services and applications, such as remote desktop connections, network shares, and web authentications. These credentials are encrypted but can be enumerated by processes running under the user's context. This procedure demonstrates how to list the available credential vaults and enumerate the stored credentials within them, which can reveal usable usernames and potentially decryptable passwords for pivoting to other systems. It is particularly useful in post-exploitation scenarios where an attacker has obtained a user-level shell on a Windows machine.

## Requirements

1. Local access to a Windows system as the target user (no administrative privileges required for user-specific vaults).
2. Command prompt or PowerShell access on the target machine.
3. No additional tools needed; uses built-in Windows executables (cmdkey.exe and vaultcmd.exe).

## Defense

- Enable Credential Guard on Windows 10/11 Enterprise to isolate and protect credential storage.
- Monitor for unusual process execution of vaultcmd.exe or cmdkey.exe via Sysmon or Windows Event Logs (Event ID 4688).
- Use Group Policy to restrict credential saving in Credential Manager.
- Implement application whitelisting to prevent unauthorized access to credential enumeration tools.

## Objectives

1. Identify and list all available credential vaults for the current user.
2. Enumerate credentials stored in the Windows Credentials vault, including resource targets and identities.
3. Gather potential credentials for lateral movement or further exploitation.
4. Verify success by confirming credential details are visible without errors.

## Instructions

### Step 1: List Current User Credential Vaults

**Context**: Begin by identifying the credential vaults available to the current user. This step uses vaultcmd.exe to display loaded vaults, such as Web Credentials and Windows Credentials, along with their GUIDs and locations. This helps determine which vaults contain potentially valuable stored credentials.

**Command** ([[commands/List-Stored-Windows-Credentials-vaultcmd-list]]):
```command_prompt
vaultcmd.exe /list
```

> This command lists all vaults without accessing their contents. It requires no parameters and runs quickly. If successful, it will output the vault names and paths, confirming the presence of the Windows Credentials vault.

### Step 2: List Credentials in the Windows Credentials Vault

**Context**: Once vaults are identified, enumerate the specific credentials stored in the "Windows Credentials" vault. This reveals details like the resource (e.g., domain or server target), identity (username), and schema type, which can indicate usable credentials for network access.

**Command** ([[commands/List-Stored-Windows-Credentials-vaultcmd-listcreds]]):
```command_prompt
vaultcmd.exe /listcreds:"Windows Credentials"
```

> This command targets the specific vault and lists its contents. The vault name is passed as a quoted parameter. Success is indicated by output showing credential schemas, resources, and identities; empty output means no credentials are stored.

### Step 3: Enumerate Saved Credentials Using Alternative Method

**Context**: As an alternative or complementary approach, use cmdkey.exe to list all stored credentials. This tool provides a simpler view of credentials, including targets like remote servers or domains, and is useful if vaultcmd.exe is restricted or for cross-verification.

**Command** ([[commands/List-Stored-Windows-Credentials-cmdkey]]):
```command_prompt
cmdkey.exe /list
```

> This command enumerates all credential entries in a user-friendly format. It requires no additional parameters. Expected output includes a list of targets and associated usernames, helping identify credentials for immediate use in tools like RDP or SMB connections.
