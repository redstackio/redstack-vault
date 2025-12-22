---
type: procedure
description: >-
  Extract credentials stored in Task Scheduler using Mimikatz to access domain
  passwords for lateral movement and privilege escalation.
verified: true
submitted: false
created_at: '2023-04-06T03:56:27Z'
updated_at: '2023-04-10T20:37:16Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
  - '[[techniques/Scheduled Task|T1053 - Scheduled Task]]'
sub_techniques: []
tags:
  - '[[tags/Credential Manager & DPAPI]]'
  - '[[tags/Task Scheduled credentials]]'
  - '[[tags/Windows - Mimikatz]]'
commands:
  - '[[commands/mimikatz-vault-cred-patch]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Credential-Harvesting-from-Task-Scheduler-using-Mimikatz

## Summary

This procedure uses the Mimikatz tool to extract plaintext credentials stored in the Windows Task Scheduler registry. Task Scheduler saves credentials for automated tasks in an encrypted format in the registry, which Mimikatz can decrypt and dump. This allows attackers with local administrator access to harvest domain credentials for further lateral movement, privilege escalation, or persistence in a network environment.

## Description

Windows Task Scheduler enables automated execution of tasks and stores associated credentials (such as domain admin passwords) in the registry under protected locations like HKLM\SOFTWARE\Microsoft\Cryptography\Protect. These credentials are used for tasks running under different user contexts without prompting. Mimikatz leverages Windows DPAPI (Data Protection API) to decrypt these stores, specifically targeting the 'vault::cred' module to pull batch credentials from Task Scheduler tasks. This technique is particularly effective in domain environments where scheduled tasks manage backups, updates, or maintenance with elevated privileges. Successful execution reveals usernames, encrypted credentials (which Mimikatz decrypts), and task GUIDs, enabling reuse for accessing remote systems via tools like PsExec or RDP. Prerequisites include running on a compromised Windows host with admin rights; detection can be mitigated by running Mimikatz in memory without disk writes.

## Requirements

1. Local administrator privileges on the target Windows machine (required to access protected registry keys).
2. Mimikatz binary (v2.2.0 or later recommended for full DPAPI support).
3. Windows OS (Server 2008 R2 or later, as Task Scheduler credential storage evolved in these versions).
4. No antivirus interference (Mimikatz signatures are commonly detected; use obfuscated variants if needed).

## Defense

- Apply the principle of least privilege: Avoid scheduling tasks with domain admin credentials; use service accounts with minimal permissions.
- Monitor scheduled tasks regularly via Event ID 4698 (Task Creation) and 4702 (Task Update) in Windows Security logs to detect unauthorized modifications.
- Enable Credential Guard on Windows 10/11 and Server 2016+ to protect LSASS and DPAPI stores from dumping tools like Mimikatz.
- Deploy EDR solutions that detect Mimikatz execution patterns, such as process injection or unusual registry reads in Cryptography keys.
- Use Group Policy to restrict task creation to approved users and audit credential usage in tasks.

## Objectives

1. Dump credentials from Task Scheduler registry stores using Mimikatz.
2. Obtain plaintext domain usernames and passwords for lateral movement.
3. Enable privilege escalation by reusing harvested credentials on other systems.

## Instructions

### Step 1: Prepare Mimikatz Environment

**Context**: Download and position Mimikatz on the target system, ensuring it runs with elevated privileges to access protected memory and registry. This step sets up the tool without triggering immediate AV alerts.

**Command** ([[commands/mimikatz-launch-elevated]]):
```cmd
mimikatz.exe -privilege:debug
```

> This launches Mimikatz with debug privileges, confirming elevation. Expected output includes privilege escalation confirmation like "Privilege '20' OK". If not elevated, relaunch as administrator.

### Step 2: Access the Vault Credential Module

**Context**: Switch to the 'vault' module in Mimikatz, which handles DPAPI-protected credential stores. This prepares for targeting Task Scheduler specifically.

**Command** ([[commands/mimikatz-vault-module]]):
```cmd
vault::cred
```

> Lists available vault credentials. Expected output shows vault GUIDs and types; look for Task Scheduler entries under batch contexts. This verifies module access without dumping yet.

### Step 3: Dump Task Scheduler Credentials

**Context**: Execute the patch command to extract and decrypt credentials from Task Scheduler's batch storage. This targets the specific registry patch where task credentials are kept.

**Command** ([[commands/mimikatz-vault-cred-patch]]):
```cmd
vault::cred /patch
```

> Dumps all patch-applied credentials, focusing on Task Scheduler tasks. Expected output includes fields like TargetName (e.g., Domain:batch=TaskScheduler:Task:{GUID}), UserName (e.g., DOMAIN\user), Type (domain_password), and Credential (decrypted password). Success is indicated by non-null Credential fields; if empty, no tasks with credentials exist.

### Step 4: Verify and Export Credentials

**Context**: Review dumped output for usable credentials and save them for later use. This step ensures the harvest is actionable for subsequent attacks.

**Instructions**: Manually parse the output for DOMAIN\username and password pairs. Redirect output to a file if needed: `vault::cred /patch > creds.txt`. Test credentials with `net use` or PsExec to confirm validity.

> Expected output: Valid credentials allow authentication to domain resources. If Credential shows as encrypted (e.g., XXXXXXXXX), ensure Mimikatz has full DPAPI access; rerun with `/in:` for memory-only mode.
