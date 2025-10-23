---
id: 526041fa-32d0-4987-9767-6b63ce0e9b0b
name: Credential Harvesting from Task Scheduler using Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.548579+00:00'
updated_at: '2023-04-10T20:37:16.562066+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[Credential Manager & DPAPI]]'
- '[[Task Scheduled credentials]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Extract Domain Credentials using Mimikatz]]'
---

# Credential Harvesting from Task Scheduler using Mimikatz

## Summary

This procedure involves the use of Mimikatz to extract credentials from Task Scheduler. Task Scheduler is a Windows utility that allows users to schedule tasks to run automatically on a specified schedule. It stores credentials for these tasks in a protected area of the registry, which can be acces

## Description

# Description

This procedure involves the use of Mimikatz to extract credentials from Task Scheduler. Task Scheduler is a Windows utility that allows users to schedule tasks to run automatically on a specified schedule. It stores credentials for these tasks in a protected area of the registry, which can be accessed using Mimikatz. This technique can be used by attackers to extract sensitive credentials, such as domain admin credentials, which can then be used to move laterally within a network and escalate privileges.

Technical Explanation: Mimikatz is a powerful tool that can be used to extract plaintext passwords, hashes, and Kerberos tickets from memory. In this procedure, we use Mimikatz to extract credentials from the registry location where Task Scheduler stores them. Once the credentials have been extracted, they can be used to gain access to other systems on the network. 

Business Value: This procedure can be used by attackers to gain access to sensitive information and escalate privileges, leading to data theft, financial loss, and reputational damage.

 

## Requirements

1. Local administrator access

1. Mimikatz tool

 

## Defense

1. Implementing the principle of least privilege can limit the impact of this attack by restricting users' access to sensitive systems and data.

1. Regularly monitoring and reviewing scheduled tasks can help detect any unauthorized changes or activity.

1. Implementing multi-factor authentication can add an extra layer of security to protect against credential theft.

 

## Objectives

1. Extract credentials from Task Scheduler using Mimikatz

1. Gain access to sensitive information

1. Escalate privileges

 

# Instructions

1. Use the 'mimikatz' command-line tool to extract credentials from the Task Scheduler on a Windows machine. The command used is 'vault::cred /patch'.

 



**Code**: [[mimikatz(commandline) # vault::cred /patch
TargetN]]



> The command 'vault::cred /patch' is used to extract credentials from the Task Scheduler on a Windows machine. The output contains the following details:
- TargetName: The name of the target machine.
- UserName: The username associated with the credential.
- Comment: Any comment associated with the credential.
- Type: The type of credential. In this case, it is a domain password.
- Persist: The persistence of the credential. In this case, it is stored on the local machine.
- Flags: The flags associated with the credential.
- Credential: The encrypted credential.
- Attributes: Any additional attributes associated with the credential.



**Command** ([[Extract Domain Credentials using Mimikatz]]):

```bash
mimikatz(commandline) # vault::cred /patch
TargetName : Domain:batch=TaskScheduler:Task:{CF3ABC3E-4B17-ABCD-0003-A1BA192CDD0B} / <NULL>
UserName   : DOMAIN\user
Comment    : <NULL>
Type       : 2 - domain_password
Persist    : 2 - local_machine
Flags      : 00004004
Credential : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Attributes : 0
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[Extract Domain Credentials using Mimikatz]]

## Tags

- [[Credential Manager & DPAPI]]
- [[Task Scheduled credentials]]
- [[Windows - Mimikatz]]


