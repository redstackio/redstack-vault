---
id: d7f356eb-774d-4fa7-ab72-6a5e496fab4c
name: Windows Persistence with Meterpreter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.400890+00:00'
updated_at: '2023-04-10T20:24:58.316009+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Persistence Startup]]'
commands:
- '[[Metasploit Payload Options]]'
---

# Windows Persistence with Meterpreter

## Summary

This procedure demonstrates how to create a persistent backdoor on a Windows machine using Meterpreter. The backdoor will be set up to run automatically every time the machine starts up, allowing the attacker to maintain access even after a reboot. From a technical perspective, this is achieved by 

## Description

# Description

This procedure demonstrates how to create a persistent backdoor on a Windows machine using Meterpreter. The backdoor will be set up to run automatically every time the machine starts up, allowing the attacker to maintain access even after a reboot. From a technical perspective, this is achieved by adding a new entry to the Windows Registry or creating a new scheduled task. From a business perspective, this type of attack can result in ongoing unauthorized access to sensitive data or systems.

## Requirements

1. Valid credentials with administrative privileges on the target system

1. Meterpreter session established on the target system

## Defense

1. Regularly monitor the Windows Registry and scheduled tasks for any unauthorized changes

1. Implement the principle of least privilege to limit the impact of a successful attack

1. Use endpoint detection and response (EDR) tools to detect and respond to suspicious activity

## Objectives

1. Establish a persistent backdoor on a Windows machine

1. Maintain access to the compromised system

# Instructions

1. To create a persistent backdoor on a Windows machine, use the 'run persistence' command followed by the necessary options. For example, to automatically start the agent when the user logs on use the '-U' option. To specify the port on which the system running Metasploit is listening, use the '-p' option followed by the port number. 

**Code**: [[OPTIONS:

-A        Automatically start a matching]]

> The 'run persistence' command is used to create a persistent backdoor on a Windows machine. This allows the attacker to maintain access to the compromised system even after a reboot. The various options available with the command allow the attacker to customize the backdoor according to their requirements. For example, the '-U' option can be used to automatically start the agent when the user logs on, while the '-p' option can be used to specify the port on which the system running Metasploit is listening. It is important to note that the creation of a persistent backdoor is illegal and should only be done in a controlled environment with proper authorization.

**Command** ([[Metasploit Payload Options]]):

```bash
OPTIONS:

-A        Automatically start a matching exploit/multi/handler to connect to the agent
-L <opt>  Location in target host to write payload to, if none %TEMP% will be used.
-P <opt>  Payload to use, default is windows/meterpreter/reverse_tcp.
-S        Automatically start the agent on boot as a service (with SYSTEM privileges)
-T <opt>  Alternate executable template to use
-U        Automatically start the agent when the User logs on
-X        Automatically start the agent when the system boots
-h        This help menu
-i <opt>  The interval in seconds between each connection attempt
-p <opt>  The port on which the system running Metasploit is listening
-r <opt>  The IP of the system running Metasploit listening for the connect back

```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]
- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[Metasploit Payload Options]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Persistence Startup]]
