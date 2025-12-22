---
id: aa18d5dc-b01d-4485-b37a-27ee522ae288
name: Execute Commands with an Active Directory Machine Account
type: procedure
verified: true
submitted: false
created_at: '2020-06-24T23:26:31.466498+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Pass-the-Hash|T1550.002 - Pass the Hash]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory]]'
  - '[[tags/NTLM]]'
  - '[[tags/privileges]]'
commands:
  - '[[commands/Mimikatz-Spawn-a-Shell-as-an-AD-Machine-Account]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Execute Commands with an Active Directory Machine Account

## Summary

This procedure uses a domain computer's NTLM hash (or password) along with Mimikatz to spawn a new terminal that executes commands under the context of the machine account. It leverages Pass-the-Hash to impersonate the machine account without needing interactive logon rights, enabling lateral movement within the Active Directory environment. A local or RDP session is required on the target system to observe and interact with the spawned terminal.

## Description

In Active Directory environments, machine accounts possess elevated privileges compared to standard user accounts, often allowing access to network resources, shares, and services. This technique exploits the NTLM hash of a machine account (which ends in a '$' symbol) to create a process running as that account using Mimikatz's sekurlsa::pth module. Once executed, a new command prompt (cmd.exe) launches, allowing the execution of commands with machine account privileges. This is particularly useful for lateral movement after obtaining machine account credentials through techniques like DCSync or unencrypted backups. The process requires administrative privileges on the current system to run Mimikatz and modify the LSA process. Success grants a shell where commands like net use or PsExec can be run to access remote resources.

## Requirements

1. Local administrator access or RDP session on a domain-joined Windows machine.
2. The NTLM hash (or AES key/password) of a domain machine account.
3. Mimikatz binary downloaded and executable on the target system (requires debug privileges).
4. Domain information (e.g., domain name and machine account name).
5. Windows platform (tested on Windows 7+ with Active Directory domain membership).

## Defense

Defensive measures and detection strategies:

- Enable Protected Process Light (PPL) for LSASS and monitor for unauthorized access using tools like Sysmon (Event ID 10: Process Access to lsass.exe).
- Implement credential guard (Windows 10/11 Enterprise) to prevent hash extraction and PTH attacks.
- Use Microsoft Defender for Endpoint or EDR solutions to detect Mimikatz signatures, anomalous process creation (cmd.exe spawned with unusual parent), and LSA modifications.
- Audit machine account changes and disable unnecessary machine account privileges via Group Policy.
- Network segmentation to limit lateral movement from compromised hosts.

## Objectives

1. Impersonate an Active Directory machine account using its NTLM hash.
2. Spawn a new command shell running under the machine account context.
3. Execute commands with elevated network access privileges for lateral movement or resource enumeration.
4. Verify successful impersonation through command output and network connectivity tests.

## Instructions

### Step 1: Obtain and Prepare Machine Account Credentials

**Context**: Gather the necessary credentials for the target machine account, including its name (e.g., WORKSTATION01$), domain (e.g., corp.local), and NTLM hash. These can be obtained via prior techniques like dumping SAM hives or Kerberoasting service accounts.

Ensure Mimikatz is available on the target system. Download it if needed, but avoid detection by using obfuscated versions or in-memory execution.

### Step 2: Elevate Privileges in Mimikatz

**Context**: Mimikatz requires debug privileges to access and modify the LSASS process. This step ensures the tool has the necessary permissions before attempting PTH.

**Command** ([[commands/Mimikatz-Enable-Debug-Privileges]]):
```cmd
Mimikatz.exe "privilege::debug" "token::elevate"
```

> This command enables debug privileges and elevates the token. Expected output includes confirmation like "Privilege '20' OK" and token elevation success. If it fails, ensure you are running as administrator.

### Step 3: Spawn Shell Using Pass-the-Hash

**Context**: Use the sekurlsa::pth module to create a new process (cmd.exe) impersonating the machine account. This injects the provided NTLM hash into the current session's security context, launching the shell without authenticating against the DC.

**Command** ([[commands/Mimikatz-Spawn-a-Shell-as-an-AD-Machine-Account]]):
```cmd
Mimikatz.exe "sekurlsa::pth /user:$_MACHINE_NAME$ /domain:$_DOMAIN /ntlm:$_NTLM_HASH"
```

> Replace placeholders with actual values (e.g., /user:SQLSRV01$ /domain:bank.local /ntlm:374B2539A390DD9781DDF26FD6029F83). Expected output shows successful data copy to MSV1_0 and Kerberos providers, followed by a new cmd.exe window spawning. Test success by running `whoami /all` in the new shell to confirm the machine account context.
