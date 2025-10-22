---
id: 85478aa6-d1f7-488a-9402-e8f63f39a5e1
name: Windows - JuicyPotatoNG Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.273922+00:00'
updated_at: '2023-04-10T20:37:34.765115+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
tags:
- '[[EoP - Impersonation Privileges]]'
- '[[JuicyPotatoNG]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Run JuicyPotatoNG to execute a command as System]]'
---

# Windows - JuicyPotatoNG Privilege Escalation

## Summary

JuicyPotatoNG is a tool used for privilege escalation on Windows systems. It exploits the 'COM' object hijacking vulnerability by impersonating the NT AUTHORITY\SYSTEM user to gain SYSTEM level privileges. This technique can be used by attackers to gain access to sensitive data, install malware, an

## Description

# Description

JuicyPotatoNG is a tool used for privilege escalation on Windows systems. It exploits the 'COM' object hijacking vulnerability by impersonating the NT AUTHORITY\SYSTEM user to gain SYSTEM level privileges. This technique can be used by attackers to gain access to sensitive data, install malware, and take control of the victim's system. JuicyPotatoNG is a powerful tool and should be used with caution.

## Requirements

1. Local access to the Windows system

1. JuicyPotatoNG tool installed on the system

## Defense

1. Ensure that all Windows systems are up to date with the latest patches and security updates

1. Implement the principle of least privilege to limit the access of users and processes to sensitive data and system resources

1. Use security tools such as antivirus and intrusion detection systems to detect and prevent attacks involving JuicyPotatoNG

## Objectives

1. Gain SYSTEM level privileges on a Windows system

1. Install malware or gain access to sensitive data

# Instructions

1. This command is used to escalate privileges on a Windows system using the JuicyPotatoNG tool. The command will run JuicyPotatoNG with the target set to all available tokens (-t *), specify the path to the command prompt executable (-p), and run the 'whoami' command to check the current user's privileges (-a). The output of the command will be redirected to a file named 'juicypotatong.txt' in the root of the C drive.

**Code**: [[JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd]]

> -t *: Specifies the target token(s) to use for privilege escalation.
-p: Specifies the path to the executable that will be executed with elevated privileges.
-a: Specifies the arguments to pass to the executable.
> C:\juicypotatong.txt: Redirects the output of the command to a file named 'juicypotatong.txt' in the root of the C drive.

**Command** ([[Run JuicyPotatoNG to execute a command as System]]):

```bash
JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c whoami" > C:\juicypotatong.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]

## Commands Used

- [[Run JuicyPotatoNG to execute a command as System]]

## Tags

- [[EoP - Impersonation Privileges]]
- [[JuicyPotatoNG]]
- [[Windows - Privilege Escalation]]
