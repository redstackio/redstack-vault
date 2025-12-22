---
id: bfd1cf6b-1077-4ec8-885e-b158580ad63c
name: Skeleton-Key-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.274014+00:00'
updated_at: '2023-10-10T20:37:25.386010+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
sub_techniques: []
tags:
  - elevated
  - skeleton-key
  - windows-persistence
commands:
  - '[[commands/mimikatz-execute-skeleton-key]]'
  - '[[commands/enter-pssession-with-mimikatz-password]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Skeleton-Key-Persistence

## Summary

Skeleton Key Persistence is a post-exploitation technique that modifies the Windows domain controller's authentication process to allow attackers to authenticate as any domain user using a fixed backdoor password ("mimikatz"). This establishes long-term persistence by bypassing standard password validation, enabling unauthorized access to domain resources without needing individual credentials.

## Description

This procedure targets Active Directory domain controllers in Windows environments. Once administrative access is obtained on the DC, the attacker uses Mimikatz to inject a backdoor into the LSASS process, altering the password verification logic. After implementation, the attacker can log in to any domain-joined machine as any user (e.g., Administrator) by supplying the password "mimikatz". This technique is effective in environments with domain controllers running Windows Server 2008 or later, but it requires Domain Admin privileges to execute. The modification persists until the system is rebooted or LSASS is restarted, providing a stealthy persistence mechanism for lateral movement and data exfiltration.

## Requirements

1. Domain Administrator credentials or equivalent access to the domain controller.
2. Local or remote execution privileges on the domain controller (e.g., via RDP, WinRM, or PSEXEC).
3. Mimikatz tool installed or available on the attacker's system or transferable to the target.
4. Network access to the domain controller and target machines for remote execution.

## Defense

- Enable Protected Users group and restrict LSASS access via AppLocker or WDAC to prevent unauthorized modifications.
- Monitor for Mimikatz execution through Sysmon Event ID 1 (process creation) with image names containing "mimikatz" or suspicious command lines.
- Implement multi-factor authentication (MFA) for administrative accounts to mitigate password-based bypasses.
- Regularly audit domain controller event logs for Event ID 4624 (successful logons) with anomalous authentication packages.

## Objectives

1. Inject a backdoor into the domain controller's authentication process for persistent access.
2. Authenticate as any domain user without knowing their actual password.
3. Maintain access to the domain for lateral movement and privilege escalation.

## Instructions

### Step 1: Execute Skeleton Key on Domain Controller

**Context**: This step injects the Skeleton Key backdoor into the LSASS process on the domain controller, modifying the authentication to accept "mimikatz" as a valid password for any user. Run this locally on the DC if possible, or remotely via PowerShell remoting.

**Command** ([[commands/mimikatz-execute-skeleton-key]]):
```cmd
mimikatz "privilege::debug" "misc::skeleton"
```

> This command enables debug privileges and applies the Skeleton Key modification. If executed successfully, Mimikatz will output a confirmation message indicating the backdoor is active. Verify by checking for no errors in the output; failure typically results from insufficient privileges.

### Step 2: Verify Remote Execution if Needed

**Context**: If direct access to the DC is unavailable, use remote invocation to apply the Skeleton Key. This assumes WinRM is enabled and credentials are available.

**Code** ([[codes/PowerShell-Skeleton-Key-Implementation]]):
Embed the code snippet here for remote execution context.

> Use the provided PowerShell code to invoke Mimikatz remotely on the DC's FQDN. Replace placeholders with actual values. Expected output includes successful privilege elevation and skeleton key application without errors.

### Step 3: Access Domain Resources with Backdoor Password

**Context**: With the backdoor active, authenticate to any domain-joined machine using the Administrator account and password "mimikatz". This demonstrates persistence and allows shell access for further operations.

**Command** ([[commands/enter-pssession-with-mimikatz-password]]):
```powershell
Enter-PSSession -ComputerName <TargetMachine> -Credential <Domain>\Administrator
```

> When prompted for the password, enter "mimikatz". Success is indicated by establishing a remote PowerShell session without credential rejection. Use this for lateral movement or executing further commands on the target.
