---
id: ed39c7dc-ed37-4b10-8513-5319dc0e657c
name: Memory Execution of Calculator and WCE with Meterpreter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.513792+00:00'
updated_at: '2023-04-10T20:25:00.662806+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Process Injection|T1055 - Process Injection]]'
tags:
- '[[Execute from Memory]]'
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
commands:
- '[[Execute WCE]]'
---

# Memory Execution of Calculator and WCE with Meterpreter

## Summary

Memory execution of Calculator and Windows Credential Editor (WCE) with Meterpreter is a technique used by attackers to bypass detection mechanisms and execute malicious code from memory. This technique is often used to evade antivirus and endpoint detection and response (EDR) solutions. In this pr

## Description

# Description

Memory execution of Calculator and Windows Credential Editor (WCE) with Meterpreter is a technique used by attackers to bypass detection mechanisms and execute malicious code from memory. This technique is often used to evade antivirus and endpoint detection and response (EDR) solutions. In this procedure, the attacker uses Meterpreter to inject the code of Calculator and WCE into a legitimate process running on the victim's machine. Once executed, the attacker can use WCE to steal Windows credentials and gain access to other systems on the network. The business value of this procedure is that it allows attackers to gain access to critical systems and steal sensitive data.

 

## Requirements

1. Access to a vulnerable system with Meterpreter installed

 

## Defense

1. Implement application control to prevent unauthorized execution of applications

1. Use endpoint detection and response (EDR) solutions to detect and respond to process injection techniques

1. Implement network segmentation to limit lateral movement of attackers

 

## Objectives

1. Execute Calculator and WCE in memory on the victim's machine

1. Steal Windows credentials using WCE

1. Gain access to other systems on the network

 

# Instructions

1. The 'execute' command is used to run a program with specific arguments.

-H: Run the program with high integrity level.
-i: Run the program interactively.
-c: Run the program in a new console window.
-m: Run the program as a new process.
-d: Specify the directory in which the program should be run.
-f: Specify the file to be executed.
-a: Specify the arguments to be passed to the program.
-w: Wait for the program to finish executing before continuing with the script.

 



**Code**: [[execute -H -i -c -m -d calc.exe -f /root/wce.exe -]]



> This command executes the 'calc.exe' program with the 'wce.exe' program as an argument. The 'calc.exe' program will be run with high integrity level, interactively, in a new console window, and as a new process. The 'wce.exe' program will be run with the specified arguments. The command will wait for both programs to finish executing before continuing with the script.



**Command** ([[Execute WCE]]):

```bash
execute -H -i -c -m -d calc.exe -f /root/wce.exe -a  -w
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Process Injection|T1055 - Process Injection]]

## Commands Used

- [[Execute WCE]]

## Tags

- [[Execute from Memory]]
- [[Metasploit]]
- [[Meterpreter - Basic]]


