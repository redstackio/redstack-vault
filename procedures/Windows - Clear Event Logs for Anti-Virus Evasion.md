---
id: 99de6c16-d5d9-4f00-b441-5fb614331344
name: Windows - Clear Event Logs for Anti-Virus Evasion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.722906+00:00'
updated_at: '2023-04-10T20:37:20.488520+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques:
- '[[Clear Linux or Mac System Logs|T1070.002 - Clear Linux or Mac System Logs]]'
tags:
- '[[Clear System and Security Logs]]'
- '[[Disable Antivirus and Security]]'
- '[[Windows - Persistence]]'
commands:
- '[[Clear Windows Event Logs]]'
---

# Windows - Clear Event Logs for Anti-Virus Evasion

## Summary

This procedure is used to evade detection from antivirus and security tools by clearing the system and security logs. Attackers can use this technique to cover their tracks and avoid detection. By clearing the logs, the attacker can prevent security analysts from detecting their activities and iden

## Description

# Description

This procedure is used to evade detection from antivirus and security tools by clearing the system and security logs. Attackers can use this technique to cover their tracks and avoid detection. By clearing the logs, the attacker can prevent security analysts from detecting their activities and identifying the attack. This technique can be used in conjunction with other persistence techniques to maintain access to the target system.

To clear the logs, the attacker can use the 'Clear Windows Event Logs' command. This will remove all entries from the event logs, including system and security logs. This can be done manually or through a script.

The business value of this technique is that it allows the attacker to remain undetected and maintain access to the target system for a longer period of time.

## Requirements

1. Administrator access to the target system

1. Access to the 'Clear Windows Event Logs' command

## Defense

1. Implement a security information and event management (SIEM) system to monitor and alert on log clearing activities

1. Restrict access to the 'Clear Windows Event Logs' command to only authorized users

1. Regularly back up event logs to prevent loss of critical security information

## Objectives

1. To evade detection from antivirus and security tools

1. To cover the attacker's tracks and avoid detection

1. To maintain access to the target system

# Instructions

1. To clear the Windows event logs using this command, follow these steps:

1. Open Command Prompt as an administrator.
2. Copy and paste the command into the Command Prompt window.
3. Press Enter.
4. Wait for the command to complete.

Note: This command will clear the System and Security event logs.

**Code**: [[cmd.exe /c wevtutil.exe cl System
cmd.exe /c wevtu]]

> This command clears the Windows event logs for the System and Security logs. The 'wevtutil.exe cl' command is used to clear the logs. The 'System' and 'Security' parameters specify which logs to clear. The 'cmd.exe /c' command is used to run the 'wevtutil.exe' command in the Command Prompt window. This command can be useful for troubleshooting issues or for security purposes.

**Command** ([[Clear Windows Event Logs]]):

```bash
cmd.exe /c wevtutil.exe cl System
cmd.exe /c wevtutil.exe cl Security
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

### Sub-Techniques

- [[Clear Linux or Mac System Logs|T1070.002 - Clear Linux or Mac System Logs]]

## Commands Used

- [[Clear Windows Event Logs]]

## Tags

- [[Clear System and Security Logs]]
- [[Disable Antivirus and Security]]
- [[Windows - Persistence]]
