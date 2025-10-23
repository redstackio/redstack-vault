---
id: b659d4f6-3507-46c1-b35f-e88cd24c5ba2
name: RDP Service Password Spraying
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.340524+00:00'
updated_at: '2023-04-10T20:25:55.659566+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
sub_techniques:
- '[[Password Guessing|T1110.001 - Password Guessing]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Password spraying]]'
- '[[Spray passwords against the RDP service]]'
commands:
- '[[Cloning RDPassSpray repository from GitHub]]'
- '[[Hydra RDP Brute Force]]'
- '[[Ncrack RDP Brute Force]]'
- '[[Running RDPassSpray]]'
---

# RDP Service Password Spraying

## Summary

RDP Service Password Spraying is a technique used by attackers to gain access to a network by guessing passwords of RDP service accounts. This technique involves using a list of common passwords and trying them against a large number of accounts. Once an account is compromised, the attacker can piv

## Description

# Description

RDP Service Password Spraying is a technique used by attackers to gain access to a network by guessing passwords of RDP service accounts. This technique involves using a list of common passwords and trying them against a large number of accounts. Once an account is compromised, the attacker can pivot to other systems and escalate privileges.

From a technical perspective, RDP Service Password Spraying involves targeting the Remote Desktop Protocol (RDP) service on a network. Attackers use automated tools to try a list of common passwords against a large number of accounts. This technique is successful when an account has a weak password that matches one of the passwords on the list.

The business value of this technique is that it allows attackers to gain access to a network without being detected. Once they have access, they can steal sensitive data, install malware, or cause other damage.

 

## Requirements

1. Access to the network

1. List of common passwords

1. Automated tool for password spraying

 

## Defense

1. Enforce strong password policies

1. Limit the number of failed login attempts

1. Enable multi-factor authentication

 

## Objectives

1. Gain access to a network

1. Compromise RDP service accounts

1. Pivot to other systems

1. Escalate privileges

 

# Instructions

1. To use this tool, first clone the RDPassSpray repository using the command 'git clone https://github.com/xFreed0m/RDPassSpray'. Then, run the script using the command 'python3 RDPassSpray.py -u [USERNAME] -p [PASSWORD] -d [DOMAIN] -t [TARGET IP]'. Replace the [USERNAME], [PASSWORD], [DOMAIN], and [TARGET IP] fields with the appropriate values for your target.

 



**Code**: [[git clone https://github.com/xFreed0m/RDPassSpray
]]



> RDP Password Spray is a tool used to target RDP services by attempting to brute force login credentials. The tool works by spraying a large number of username and password combinations against a single IP address, rather than trying a few username and password combinations against many IP addresses. This can be an effective way to gain access to a specific system, especially if the target system has weak or commonly used passwords.



**Command** ([[Cloning RDPassSpray repository from GitHub]]):

```bash
git clone https://github.com/xFreed0m/RDPassSpray
```





**Command** ([[Running RDPassSpray]]):

```bash
python3 RDPassSpray.py -u [USERNAME] -p [PASSWORD] -d [DOMAIN] -t [TARGET IP]
```



2. The hydra command uses the -t flag to specify the number of threads, -V flag for verbose output, -f flag to exit after the first valid password is found, -l flag for the username to use, and -P flag for the password list to use. The ncrack command uses the --connection-limit flag to limit the number of simultaneous connections, -vv flag for very verbose output, --user flag for the username to use, -P flag for the password list to use, and the target RDP service.

 



**Code**: [[hydra -t 1 -V -f -l administrator -P /usr/share/wo]]



> This command is used for brute forcing RDP services. Hydra and ncrack are popular tools for this task. The -t flag sets the number of threads to use, which can speed up the process. The -V and -vv flags provide more verbose output, which can help with troubleshooting. The -f flag tells hydra to exit after the first valid password is found, which can save time. The -l and --user flags specify the username to use. The -P flag specifies the password list to use. The --connection-limit flag limits the number of simultaneous connections, which can help prevent account lockouts. Overall, this command should be used with caution and only on systems that you have permission to test.



**Command** ([[Hydra RDP Brute Force]]):

```bash
hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.10
```





**Command** ([[Ncrack RDP Brute Force]]):

```bash
ncrack --connection-limit 1 -vv --user administrator -P password-file.txt rdp://10.10.10.10
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

### Sub-Techniques

- [[Password Guessing|T1110.001 - Password Guessing]]

## Commands Used

- [[Cloning RDPassSpray repository from GitHub]]
- [[Hydra RDP Brute Force]]
- [[Ncrack RDP Brute Force]]
- [[Running RDPassSpray]]

## Tags

- [[Active Directory Attacks]]
- [[Password spraying]]
- [[Spray passwords against the RDP service]]


