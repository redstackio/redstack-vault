---
id: 2706ca6f-6568-407a-a9c0-392910b195a2
name: Windows Subsystem for Linux (WSL) Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.622312+00:00'
updated_at: '2023-04-10T20:37:54.936219+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Windows Subsystem for Linux (WSL)]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Accessing Ubuntu rootfs directory]]'
- '[[Check WSL User]]'
- '[[Check WSL User Again]]'
- '[[Install WSL]]'
- '[[Run Python Reverse Shell Code]]'
- '[[Set Default User to Root]]'
- '[[Verify installation]]'
---

# Windows Subsystem for Linux (WSL) Privilege Escalation

## Summary

Windows Subsystem for Linux (WSL) is a feature in Windows 10 that allows users to run Linux applications natively on Windows. Attackers can use WSL to escalate privileges from a low-privileged user to the root user, gaining full control of the system. This can be achieved by exploiting vulnerabilit

## Description

# Description

Windows Subsystem for Linux (WSL) is a feature in Windows 10 that allows users to run Linux applications natively on Windows. Attackers can use WSL to escalate privileges from a low-privileged user to the root user, gaining full control of the system. This can be achieved by exploiting vulnerabilities in the WSL implementation or by using malicious scripts. Once the attacker has escalated privileges, they can perform any action on the system, including stealing sensitive data, installing backdoors, and executing malicious code.

Technical Explanation: WSL allows users to run Linux binaries on Windows, which creates a separate environment with its own file system and processes. Attackers can exploit vulnerabilities in WSL or use malicious scripts to execute code in the context of the root user. This allows them to bypass Windows security mechanisms and gain full control of the system.

Business Value: An attacker who gains root access to a system can steal sensitive data, install backdoors, and execute malicious code, causing significant damage to the organization.

## Requirements

1. Access to a Windows 10 system with WSL installed

1. Low-privileged user account

## Defense

1. Disable WSL if it's not needed

1. Apply security updates and patches regularly

1. Monitor WSL activity for suspicious behavior

## Objectives

1. Escalate privileges from a low-privileged user to the root user

1. Gain full control of the system

# Instructions

1. This command sets the default user of the WSL to root, which allows for the execution of commands with elevated privileges. The final command executes a Python script to establish a reverse shell connection.

**Code**: [[wsl whoami
./ubuntun1604.exe config --default-user]]

> The `wsl whoami` command prints the current user of the WSL, while `./ubuntun1604.exe config --default-user root` sets the default user to root. The final command `wsl python -c 'BIND_OR_REVERSE_SHELL_PYTHON_CODE'` executes a Python script that establishes a reverse shell connection. The `BIND_OR_REVERSE_SHELL_PYTHON_CODE` needs to be replaced with the actual Python code that creates the reverse shell connection. This command is useful for gaining root access to the WSL environment.

**Command** ([[Check WSL User]]):

```bash
wsl whoami
```

**Command** ([[Set Default User to Root]]):

```bash
./ubuntun1604.exe config --default-user root
```

**Command** ([[Check WSL User Again]]):

```bash
wsl whoami
```

**Command** ([[Run Python Reverse Shell Code]]):

```bash
wsl python -c 'BIND_OR_REVERSE_SHELL_PYTHON_CODE'
```

2. Use this command to get information about the bash executable file.

**Code**: [[bash.exe]]

> The 'bash.exe' file is the executable file for the Bash shell. By using this command, you can get information about the file such as its location, size, version, and other details. This command can be useful when troubleshooting issues related to the Bash shell or when trying to understand more about the system environment.

3. To execute Bash commands on Windows, use the Bash executable located at the given path.

**Code**: [[C:\Windows\WinSxS\amd64_microsoft-windows-lxssbash]]

> This command provides the path to the Bash executable on Windows. The Bash executable can be used to execute Bash commands on Windows. Users can use this command to locate the Bash executable and use it to run Bash commands on their Windows machine. The path provided may vary based on the version of Windows and the installation location of the Bash executable.

4. Install WSL on Windows 10

**Code**: [[WSL]]

> WSL (Windows Subsystem for Linux) is a compatibility layer for running Linux binary executables natively on Windows 10. To install WSL, follow these steps:

1. Open the Start menu and search for 'Turn Windows features on or off'.
2. Scroll down to find 'Windows Subsystem for Linux' and check the box next to it.
3. Click 'OK' and wait for the installation to complete.
4. Once the installation is complete, open the Microsoft Store and search for your preferred Linux distribution (e.g. Ubuntu, Debian, Kali Linux).
5. Click 'Get' and wait for the installation to complete.
6. Once the installation is complete, launch the Linux distribution from the Start menu and follow the prompts to set up your Linux user account.

After completing these steps, you will be able to use the Linux command line interface and install Linux packages on your Windows 10 machine using the 'apt-get' package manager.

**Command** ([[Install WSL]]):

```bash
sudo apt-get update && sudo apt-get install -yqq python3
```

**Command** ([[Verify installation]]):

```bash
wsl -l -v
```

5. To access the Ubuntu filesystem folder, navigate to the following path in your Windows File Explorer: C:\Users\%USERNAME%\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\

**Code**: [[C:\Users\%USERNAME%\AppData\Local\Packages\Canonic]]

> This command provides the path to the Ubuntu filesystem folder on a Windows machine. The folder contains the root file system of the Ubuntu installation, allowing users to access and modify files and directories within the Ubuntu environment from their Windows machine.

**Command** ([[Accessing Ubuntu rootfs directory]]):

```bash
cd C:\Users\%USERNAME%\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\
```

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[Accessing Ubuntu rootfs directory]]
- [[Check WSL User]]
- [[Check WSL User Again]]
- [[Install WSL]]
- [[Run Python Reverse Shell Code]]
- [[Set Default User to Root]]
- [[Verify installation]]

## Tags

- [[EoP - Windows Subsystem for Linux (WSL)]]
- [[Windows - Privilege Escalation]]
