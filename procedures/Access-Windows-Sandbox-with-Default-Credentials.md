---
id: 669d46ed-abc4-4d9d-8a45-bcee0656d804
name: Access-Windows-Sandbox-with-Default-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.700517+00:00'
updated_at: '2023-04-10T20:37:57.104592+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - '[[sub-techniques/Local Accounts|T1078.003 - Local Accounts]]'
tags:
  - '[[tags/Get credentials]]'
  - '[[tags/Sandbox Credential]]'
  - '[[tags/Windows - Using credentials]]'
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Access-Windows-Sandbox-with-Default-Credentials

## Summary

This procedure demonstrates how to access the Windows Sandbox environment using the built-in WDAGUtilityAccount local account and its default credentials. Windows Sandbox provides an isolated desktop environment for testing, and accessing it with default credentials can allow extraction of any data or processes running within the sandbox, potentially bypassing host restrictions in a testing or red team scenario.

## Description

Windows Sandbox is a lightweight, isolated Windows environment available in Windows 10 and 11 Professional/Enterprise editions. It runs as a virtual machine-like instance using the WDAGUtilityAccount, a local account with limited privileges designed for isolation from the host system. This procedure involves authenticating to the sandbox using the known default username and a placeholder password (in practice, the password may be auto-generated or require enumeration). Once accessed, an operator can interact with the sandbox to retrieve stored credentials, files, or other sensitive data that might have been placed there during testing or by a previous compromise. This technique is useful in red teaming to simulate lateral movement into isolated environments or to evade detection by operating in a sandboxed space. Note that actual credential dumping (e.g., from LSASS) would require additional procedures once inside.

## Requirements

1. Windows 10/11 Professional or Enterprise edition with Windows Sandbox feature enabled (via Optional Features in Settings).
2. Local administrator access on the host to start the sandbox if not already running.
3. Knowledge of the WDAGUtilityAccount credentials (username is fixed; password may need to be obtained via enumeration tools like mimikatz on the host if not default).
4. Network access if using UNC paths to interact with sandbox shares (though sandbox is primarily local).

## Defense

- Disable Windows Sandbox feature if not needed via Windows Features.
- Monitor for sandbox launches using Event ID 4104 (PowerShell) or process creation events for 'msandbox.exe'.
- Implement application whitelisting to restrict sandbox usage.
- Use privileged access management to limit local admin rights that could enable sandbox manipulation.

## Objectives

1. Authenticate to the Windows Sandbox environment using default local account credentials.
2. Gain interactive access to the isolated sandbox session for data extraction or further actions.
3. Verify isolation boundaries and extract any stored sensitive information within the sandbox.

## Instructions

### Step 1: Enable and Launch Windows Sandbox

**Context**: Ensure the sandbox feature is enabled and start the isolated environment, which runs under the WDAGUtilityAccount.

Open the Start menu, search for "Windows Sandbox", and launch it. If not enabled, go to Settings > Apps > Optional Features > Add a feature > Windows Sandbox, then restart the system.

> This step initializes the sandbox desktop session. No command is needed as it's a GUI launch, but verify via Task Manager that 'msandbox.exe' is running.

### Step 2: Authenticate with Default Credentials

**Context**: Use the built-in WDAGUtilityAccount to log in to the sandbox session. The username is always 'wdagutilityaccount'; the password is often a simple default or requires host enumeration.

In the sandbox login prompt (if applicable) or via Run dialog (Win+R) on the host, enter the following to map or access the sandbox context:

```
\\windowssandbox
Username: wdagutilityaccount
Password: pw123
```

> Substitute 'pw123' with the actual password if enumerated (e.g., via host LSASS dump). This UNC path attempts to access sandbox resources as if it were a network share, though sandbox interaction is typically direct via the desktop.

### Step 3: Verify Access and Extract Data

**Context**: Confirm successful authentication and begin interacting with the sandbox to access any credentials or data.

Once logged in, open Command Prompt or PowerShell within the sandbox and run basic commands to list files or processes:

```cmd
whoami
ls
```

> Expected confirmation: Output shows 'wdagutilityaccount' as the current user. Look for any mapped drives, stored files, or running processes containing sensitive data.

## Expected Output

Successful access results in an interactive sandbox desktop or command session running as WDAGUtilityAccount. Sample output from 'whoami':

```
wdagutilityaccount
```

No errors on credential entry, and ability to execute commands within the isolated environment.
