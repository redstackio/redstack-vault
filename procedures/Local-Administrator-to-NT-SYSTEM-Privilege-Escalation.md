---
id: aa40cb8a-37b6-4f22-8b6b-a52efdfe3bf3
name: Local-Administrator-to-NT-SYSTEM-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.047361+00:00'
updated_at: '2023-04-10T20:37:35.513309+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - >-
    [[techniques/Bypass User Account Control|T1088 - Bypass User Account
    Control]]
sub_techniques: []
tags:
  - '[[tags/EoP - From local administrator to NT SYSTEM]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/psexec-launch-interactive-system-cmd]]'
platforms:
  - Windows
tools:
  - '[[tools/PsExec]]'
validated: true
---

# Local-Administrator-to-NT-SYSTEM-Privilege-Escalation

## Summary

This procedure escalates privileges from a local administrator account to the NT SYSTEM account on a Windows system using PsExec, granting the highest level of access to perform unrestricted actions such as persistence establishment or further lateral movement.

## Description

In a typical attack scenario, an attacker has obtained local administrator credentials through initial access methods like phishing or credential dumping. The NT SYSTEM account provides complete control over the system, bypassing many user-level restrictions. PsExec leverages the Service Control Manager to create a temporary service that executes processes under the SYSTEM context, effectively impersonating the highest privilege level without directly manipulating tokens or bypassing UAC prompts if already elevated. This is useful in post-exploitation phases for maintaining stealthy persistence, as SYSTEM processes are less likely to trigger user notifications. The technique assumes UAC is not fully restricting admin actions and works on Windows versions supporting PsExec, such as Windows 7 and later.

## Requirements

1. Local administrator access on the target Windows system
2. PsExec.exe available on the system or transferable via tools like SMB
3. Ability to execute binaries from the current directory or PATH
4. Target environment: Windows (tested on Windows 10/11/Server 2019+)

## Defense

- Implement application whitelisting (e.g., AppLocker or WDAC) to block unsigned tools like PsExec
- Enable UAC with secure desktop to prompt for elevations
- Monitor for service creation events (Event ID 7045) and unusual process executions via EDR tools
- Restrict local admin accounts and audit privilege use with tools like Microsoft ATA

## Objectives

1. Achieve NT SYSTEM privileges from local admin context
2. Enable unrestricted system access for persistence or further exploitation
3. Verify escalation success through whoami or token queries

## Instructions

### Step 1: Prepare and Launch Interactive SYSTEM Command Prompt

**Context**: With local admin privileges, use PsExec to spawn an interactive command prompt running as NT SYSTEM. This step creates a new process in the SYSTEM context, allowing full system control. Ensure PsExec.exe is in the current directory or PATH; if not, transfer it using a tool like certutil.

**Command** ([[commands/psexec-launch-interactive-system-cmd]]):
```cmd
PsExec.exe -i -s cmd.exe
```

> The -i flag enables interactive desktop access, while -s specifies the SYSTEM account. Upon success, a new command prompt window opens, and running `whoami` should output `nt authority\system`. If antivirus blocks PsExec, consider alternatives like scheduled tasks for escalation. Decision point: If the command fails due to permissions, verify admin elevation with `whoami /priv` and ensure no group policy restrictions on service creation.

**Expected Output**: A new cmd.exe window opens with SYSTEM privileges. Sample verification:
```
C:\> whoami
nt authority\system

C:\> whoami /priv
[output lists all privileges enabled for SYSTEM]
```

**Success Indicators**:
- New command prompt shows `nt authority\system` when running `whoami`
- Access to protected directories like `C:\Windows\System32\config` without errors
- No UAC prompts or access denied messages
