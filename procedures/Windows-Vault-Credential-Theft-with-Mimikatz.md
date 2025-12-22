---
id: 306b0a1e-aac9-4c28-b9f3-4509526d72db
name: Windows-Vault-Credential-Theft-with-Mimikatz
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.578124+00:00'
updated_at: '2023-04-10T20:37:18.013424+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Credentials from Password Stores|T1555.004 - Credentials from
    Password Stores]]
sub_techniques: []
tags:
  - '[[tags/Credential Manager & DPAPI]]'
  - '[[tags/Vault]]'
  - '[[tags/Windows - Mimikatz]]'
commands:
  - '[[commands/mimikatz-vault-cred-dump]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Windows-Vault-Credential-Theft-with-Mimikatz

## Summary

This procedure details how to extract credentials stored in the Windows Credential Manager Vault using Mimikatz. The Vault securely stores user credentials for various services, encrypted via DPAPI. By leveraging Mimikatz's vault module, attackers can dump these credentials post-compromise, potentially revealing plaintext passwords or hashes for lateral movement or privilege escalation in a Windows domain environment.

## Description

The Windows Credential Manager Vault, located in the user's AppData directory, holds encrypted credentials for web sites, network shares, and applications. These are protected by the user's DPAPI master key, derived from the login credentials. Mimikatz bypasses this by injecting into the process or using its modules to decrypt and extract the data directly. This technique is effective after initial access with local admin rights, allowing retrieval of domain or service credentials. It targets Windows 7 and later, where the Vault is commonly used for auto-fill and saved logins. Success depends on having the necessary privileges to access DPAPI blobs; without them, only encrypted data may be visible.

## Requirements

1. Local administrator access on a Windows target system (Vista or later, tested on Windows 10/11).
2. Mimikatz tool installed or transferred to the target (see [[tools/Mimikatz]]).
3. The target user must have stored credentials in the Credential Manager.

## Defense

Defensive measures and detection strategies:

- Enable Credential Guard on Windows 10+ Enterprise to isolate and protect LSASS and DPAPI keys.
- Monitor for Mimikatz signatures via EDR tools (e.g., process injection, unusual memory reads in lsass.exe).
- Use AppLocker or WDAC to block unsigned executables like Mimikatz.
- Regularly audit and clear stored credentials in Credential Manager; implement just-in-time access.
- Enable PowerShell logging and Sysmon for detecting command-line arguments containing 'vault::' or DPAPI references.

## Objectives

1. Access and dump credentials from the Windows Vault.
2. Decrypt and extract usable plaintext credentials or hashes.
3. Enable lateral movement using stolen domain or service accounts.

## Instructions

### Step 1: Launch Mimikatz with Elevated Privileges

**Context**: Mimikatz requires administrative privileges to access protected memory and DPAPI structures. Launch it in an elevated command prompt to ensure access to the Vault files.

Run Mimikatz executable as administrator. Refer to [[tools/Mimikatz]] for download and execution details.

> This step verifies privilege level and initializes Mimikatz's privilege escalation module if needed.

### Step 2: Dump Vault Credentials

**Context**: Once Mimikatz is running, use the vault module to target the user's Vault directory. This extracts all stored credential entries, attempting decryption using the current session's DPAPI keys.

**Command** ([[commands/mimikatz-vault-cred-dump]]):
```cmd
vault::cred /in:%APPDATA%\Microsoft\Vault
```

> The `/in:` parameter specifies the Vault path. Use `%APPDATA%\Microsoft\Vault` for the current user. Mimikatz will list GUIDs, credential providers, and decrypted data if possible. If the Vault contains network or domain creds, they will appear in plaintext or as hashes.

### Step 3: Verify and Export Results

**Context**: Review the output for usable credentials. Export to a file for offline analysis or cracking if hashes are present.

At the Mimikatz prompt, use `!vault::cred` or redirect output manually (e.g., via `> output.txt` in cmd). Check for entries like Windows Live, RDP, or custom app creds.

> If no plaintext is shown, additional steps like `dpapi::masterkey` may be needed for full decryption (cross-reference other Mimikatz procedures).
