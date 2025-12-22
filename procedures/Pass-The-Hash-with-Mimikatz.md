---
id: b3dcd07d-2e06-4b6d-abdf-c780963d4df3
name: Pass-The-Hash-with-Mimikatz
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.244754+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass-the-Hash|T1550.002 - Pass the Hash]]'
sub_techniques: []
tags:
  - pass-the-hash
  - windows-mimikatz
commands:
  - '[[commands/mimikatz-pass-the-hash]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Pass-The-Hash-with-Mimikatz

## Summary

Pass the Hash is a technique used by attackers to authenticate to a remote system using the NTLM hash of a user's password, rather than the plaintext password itself. Mimikatz is a powerful post-exploitation tool that can extract these hashes from memory on a compromised system, allowing an attacker to use them to move laterally within a network.

## Description

Pass the Hash is a technique used by attackers to authenticate to a remote system using the NTLM hash of a user's password, rather than the plaintext password itself. Mimikatz is a powerful post-exploitation tool that can extract these hashes from memory on a compromised system, allowing an attacker to use them to move laterally within a network.

From a technical perspective, Mimikatz works by exploiting weaknesses in the Windows authentication process. When a user logs into a Windows system, their password is hashed and stored in memory. Mimikatz can extract these hashes from memory, allowing an attacker to use them to authenticate to other systems without needing the original plaintext password.

The business value of this technique is that it allows attackers to move laterally within a network and access sensitive resources. By using stolen credentials, attackers can bypass authentication mechanisms and gain access to systems and data that would otherwise be protected.

## Requirements

1. Access to a compromised Windows system with administrative privileges
2. Mimikatz tool downloaded and executable on the target system
3. Knowledge of the target user's NTLM hash, domain, and username

## Defense

Defensive measures and detection strategies:

- Implement strong password policies and enforce regular password changes
- Use multi-factor authentication to prevent attackers from using stolen credentials
- Monitor network traffic for signs of lateral movement and anomalous authentication activity
- Enable Protected Process Light (PPL) for LSASS and restrict access to credential dumps
- Deploy endpoint detection tools to monitor for Mimikatz execution signatures

## Objectives

1. Authenticate to a remote system using stolen credentials
2. Move laterally within a network
3. Access sensitive resources

## Instructions

### Step 1: Launch Mimikatz with Elevated Privileges

**Context**: Before performing the Pass the Hash attack, ensure Mimikatz is running with the necessary privileges to access LSASS memory and create tokens. This step verifies the environment is ready for credential manipulation.

Run Mimikatz as an administrator on the compromised Windows system. If privileges are insufficient, use techniques like UAC bypass to elevate.

**Expected Output**: Mimikatz prompt appears without privilege errors, e.g., "Privilege '20' OK" for debug privileges.

### Step 2: Execute Pass-the-Hash to Impersonate User

**Context**: Use the sekurlsa::pth module in Mimikatz to create a token with the stolen NTLM hash, allowing authentication to remote systems without the plaintext password. This impersonates the target user and executes a specified command, such as launching PowerShell, under the new token.

**Command** ([[commands/mimikatz-pass-the-hash]]):
```cmd
mimikatz.exe "sekurlsa::pth /user:$_USER /domain:$_DOMAIN /ntlm:$_NTLM_HASH /run:$_COMMAND"
```

> This command performs the Pass the Hash attack by injecting the NTLM hash into a new token for the specified user and domain, then runs the designated command (e.g., powershell.exe) under that token. Replace placeholders with actual values: $_USER (e.g., SCCM$), $_DOMAIN (e.g., IDENTITY), $_NTLM_HASH (e.g., e722dfcd077a2b0bbe154a1b42872f4e), $_COMMAND (e.g., powershell.exe). Success is indicated by the token creation and command execution without authentication failures.

**Expected Output**: Output similar to:

Privilege '20' OK
Token "\Default" OK
Access token OK
Command executed: powershell.exe

A new PowerShell session launches under the impersonated user's context, allowing lateral movement.

### Step 3: Verify Lateral Access and Clean Up

**Context**: Confirm the attack succeeded by testing access to a remote resource (e.g., SMB share or RDP) using the impersonated token. Then, exit Mimikatz to minimize footprint.

In the new shell, attempt to access a remote system, e.g., `dir \\remote-host\C$`. Exit Mimikatz with `exit` and clear event logs if possible.

**Expected Output**: Successful access to remote resources without prompting for credentials, e.g., directory listing displays files.
