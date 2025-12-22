---
type: procedure
description: >-
  Use the Runas command to execute programs under different user credentials for
  privilege escalation or task execution without logging out.
verified: true
submitted: false
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - '[[sub-techniques/Domain Accounts|T1078.002 - Domain Accounts]]'
tags:
  - other-methods
  - runas-as-another-user
  - windows-using-credentials
commands:
  - '[[commands/runas-netonly-run-cmd-as-domain-user]]'
  - '[[commands/runas-netonly-no-profile-run-cmd-as-domain-user]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-run-programs-as-different-user-using-runas

## Summary

This procedure uses the built-in Windows Runas command to launch programs or commands under the security context of a different user account, enabling privilege escalation, execution of tasks requiring elevated access, or operation as another domain user without needing to log out or switch sessions. It is particularly useful in scenarios where valid credentials for a higher-privileged account are available, allowing temporary elevation for specific actions while minimizing footprint.

## Description

The Runas command (short for "run as") impersonates a specified user account to create a new process with that user's token, providing access to resources or permissions not available to the current user. This is common in red team operations for lateral movement or escalation when credentials are obtained via other means like credential dumping. Key options like /netonly limit credential use to network resources only (preventing local profile loading for evasion), and /noprofile avoids loading the user's profile to reduce execution time and detection. The procedure targets Windows environments with domain-joined systems, assuming the attacker has local access and valid domain credentials. Success grants a new command shell or process running as the target user, verifiable by whoami or access to restricted resources.

## Requirements

1. Local or remote access to a Windows command prompt (cmd.exe or PowerShell) on the target system.
2. Valid domain or local user credentials (username and password) for the account to impersonate.
3. The target system must be domain-joined for /netonly to function with domain accounts; local accounts work without it.
4. Administrative privileges not required to run Runas, but the impersonated account may need them for escalation.

## Defense

- Enforce least privilege principles to limit credential exposure and reduce the impact of stolen accounts.
- Monitor command-line logging (e.g., via Sysmon or Windows Event Logs) for Runas executions, especially with /netonly or /noprofile flags.
- Implement multi-factor authentication (MFA) for domain accounts to prevent credential reuse.
- Use application whitelisting (e.g., AppLocker) to restrict spawning of new processes from Runas.

## Objectives

1. Execute programs or commands under different user permissions for privilege escalation or resource access.
2. Perform tasks requiring elevated privileges without full session takeover.
3. Access domain or network resources using alternate credentials while evading local detection.

## Instructions

### Step 1: Prepare Credentials and Open Command Prompt

**Context**: Ensure you have the target domain username and password ready. Open a new Command Prompt or PowerShell window on the target system as the current user. This step sets up the environment for impersonation without altering the local session.

Run the following to verify current user context before proceeding:

```cmd
whoami
```

> This displays the current user (e.g., DOMAIN\lowprivuser). Expected output confirms you are not already running as the target user.

### Step 2: Run Command Shell as Domain User with /netonly

**Context**: Use the /netonly flag to apply the alternate credentials only for network access, keeping local operations under the current user. This is ideal for accessing remote shares or services without loading a full profile, reducing detection risk. Replace DOMAIN\username with actual credentials when prompted for password.

**Command** ([[commands/runas-netonly-run-cmd-as-domain-user]]):

```cmd
runas /netonly /user:DOMAIN\username "cmd.exe"
```

> The command prompts for the user's password (not echoed). If successful, a new cmd.exe window opens running as the specified user for network operations. Verify with `whoami /all` in the new shell to confirm token details. Expected output: New command prompt window; no errors like "RUNAS ERROR: Unable to run - <program>" if credentials are valid.

### Step 3: Run Command Shell as Domain User with /netonly and /noprofile

**Context**: For faster execution or when profile loading is unnecessary (e.g., simple remote commands), add /noprofile to skip loading the user's registry hive and profile path. This minimizes resource usage and potential logging of profile access. Again, provide credentials when prompted.

**Command** ([[commands/runas-netonly-no-profile-run-cmd-as-domain-user]]):

```cmd
runas /noprofile /netonly /user:DOMAIN\username cmd.exe
```

> Similar to Step 2, but without quotes around cmd.exe since no arguments follow. Expected output: New cmd.exe instance launches quickly; use `whoami` to verify impersonation. If profile is not needed, execution completes in under a second versus several seconds with profile loading.

### Step 4: Verify and Use the Impersonated Session

**Context**: In the new shell, test access to restricted resources (e.g., `net use \\remote-share` for network or `accessdenied.txt` for local files). Close the shell when done to release the token.

No specific command here, but example verification:

```cmd
whoami /groups
```

> Expected output lists groups from the impersonated user, including any elevated SIDs. Success indicators: Access granted to previously denied resources; no authentication failures on network calls.
