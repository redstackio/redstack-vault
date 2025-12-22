---
id: 27bc6fa5-4c43-453f-b47a-f75e6a53d40e
name: Loot-Passwords-from-Windows-Credential-Manager-for-EoP
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.263837+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Credentials-from-Password-Stores|T1555.004 - Windows Credential
    Manager]]
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Passwords stored in Credential Manager]]'
  - '[[tags/Windows - Privilege Escalation]]'
  - windows
  - credential-access
  - eop
commands:
  - '[[commands/rundll32-launch-credential-manager]]'
platforms:
  - Windows
tools: []
validated: true
---

# Loot-Passwords-from-Windows-Credential-Manager-for-EoP

## Summary

This procedure demonstrates how to access and extract stored credentials from the Windows Credential Manager to facilitate privilege escalation on a compromised Windows system. By launching the Credential Manager GUI, attackers can view saved passwords, generic credentials, and certificates that may provide access to elevated accounts or sensitive resources, enabling further lateral movement or persistence.

## Description

The Windows Credential Manager is a built-in feature that securely stores authentication credentials, such as usernames and passwords for network resources, websites, and applications. These credentials are encrypted using the user's login credentials and Data Protection API (DPAPI). In an elevation of privilege (EoP) scenario, a compromised low-privileged account can use this procedure to loot stored credentials belonging to the current user or, with sufficient access, other users. This is particularly useful if the system has saved admin-level credentials from prior legitimate use, such as remote desktop connections or service accounts. The technique targets credentials stored in the registry under protected keys (e.g., HKCU\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Manager). Success depends on the context: from a standard user shell, only current user credentials are accessible without additional privileges. This procedure assumes execution from an interactive shell and focuses on GUI-based extraction for simplicity, though programmatic access via APIs is possible for automation.

## Requirements

1. Compromised access to a Windows system (e.g., via initial foothold like phishing or exploit).
2. Execution context with at least standard user privileges (administrative privileges enhance access to system-wide credentials).
3. Command Prompt or PowerShell available on the target (standard on Windows).
4. No additional tools required, as this uses built-in Windows functionality.

## Defense

- Enable advanced auditing for credential access events (Event ID 4648, 4672) and monitor for unexpected Credential Manager launches.
- Implement Least Privilege: Avoid storing high-privilege credentials in Credential Manager; use secure vaults like Azure Key Vault for enterprise environments.
- Regularly clear unnecessary stored credentials via Group Policy (Computer Configuration > Administrative Templates > System > Credentials Delegation).
- Deploy endpoint detection tools to alert on rundll32.exe executions with keymgr.dll arguments.

## Objectives

1. Extract stored usernames and passwords from Credential Manager to identify reusable credentials.
2. Use looted credentials for privilege escalation, such as logging in as an admin account or accessing restricted shares.
3. Maintain access by reusing credentials for persistence without triggering new authentication.

## Instructions

### Step 1: Launch Windows Credential Manager

**Context**: This step opens the Credential Manager GUI, allowing manual inspection and export of stored credentials. It is the core action for looting, as the interface displays web credentials, Windows credentials, and generic entries. Review each category for high-value items like domain admin passwords or service account tokens.

**Command** ([[commands/rundll32-launch-credential-manager]]):
```powershell
rundll32.exe keymgr.dll,KRShowKeyMgr
```

> This command invokes the rundll32.exe host process to load the keymgr.dll module and call the KRShowKeyMgr export, which displays the Credential Manager window. No parameters are needed for basic launch. Upon success, the GUI will enumerate all stored items; select 'Windows Credentials' or 'Web Credentials' tabs to view details. For each entry, click 'Show' to reveal the password (requires current user context). Export options allow saving credentials for offline use. If no credentials appear, the user context may lack stored items—pivot to another session if possible.

### Step 2: Extract and Validate Credentials

**Context**: After launching, manually extract credentials and test them for escalation potential. This step ensures the looted data is actionable, such as using a found admin password to execute privileged commands.

**Instructions**: In the Credential Manager GUI:
1. Navigate to the relevant tab (e.g., Windows Credentials for network shares).
2. For each entry, note the target name, username, and password.
3. Test credentials immediately, e.g., via `runas /user:DOMAIN\admin cmd.exe` with the looted password to spawn an elevated shell.

> Expected: Successful authentication with looted creds grants higher privileges. If prompted for password, enter the extracted value. Failure indicates expired or incorrect creds—continue to next entry.
