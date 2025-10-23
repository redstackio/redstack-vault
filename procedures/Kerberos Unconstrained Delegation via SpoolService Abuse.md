---
id: d55b54dd-1c88-4a8f-9568-975aacfc6cb5
name: Kerberos Unconstrained Delegation via SpoolService Abuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.493691+00:00'
updated_at: '2023-04-10T20:26:01.831638+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Unconstrained Delegation]]'
- '[[SpoolService Abuse with Unconstrained Delegation]]'
- '[[SpoolService status]]'
commands:
- '[[List files in spoolss pipe and run rpcdump]]'
---

# Kerberos Unconstrained Delegation via SpoolService Abuse

## Summary

Kerberos Unconstrained Delegation is a feature in Active Directory that allows a user to impersonate another user to access resources on the network. An attacker can abuse this feature by compromising a service account that has been granted the unconstrained delegation privilege. In this procedure,

## Description

# Description

Kerberos Unconstrained Delegation is a feature in Active Directory that allows a user to impersonate another user to access resources on the network. An attacker can abuse this feature by compromising a service account that has been granted the unconstrained delegation privilege. In this procedure, we will abuse the SpoolService with unconstrained delegation privilege to gain access to sensitive resources. The SpoolService is a Windows service that manages print jobs and printer settings. By gaining access to this service, an attacker can escalate privileges and move laterally within the network.

To abuse the SpoolService, we will first check if it is running on the target system. If it is, we will then proceed to exploit the unconstrained delegation privilege to gain access to sensitive resources.

This attack can be devastating to an organization as it can lead to the compromise of sensitive data and the creation of persistent backdoors.

 

## Requirements

1. Access to a system with SpoolService running

1. Credentials with unconstrained delegation privilege

 

## Defense

1. Disable unconstrained delegation in Active Directory

1. Monitor event logs for suspicious activity related to Kerberos authentication

1. Implement network segmentation to limit the impact of lateral movement

 

## Objectives

1. Gain access to sensitive resources on the target network

1. Escalate privileges to move laterally within the network

1. Create persistent backdoors for future access

 

# Instructions

1. To check if the spool service is running on a remote host, run the following command:

 



**Code**: [[ls \\dc01\pipe\spoolss
python rpcdump.py DOMAIN/us]]



> This command will list the contents of the spoolss pipe on the remote host and then use rpcdump to query the spooler service for information. If the service is running, you will receive a response. If the service is not running, you will receive an error message.



**Command** ([[List files in spoolss pipe and run rpcdump]]):

```bash
ls \\dc01\pipe\spoolss
python rpcdump.py DOMAIN/user:password@10.10.10.10
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Kerberoasting|T1208 - Kerberoasting]]
- [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Commands Used

- [[List files in spoolss pipe and run rpcdump]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Unconstrained Delegation]]
- [[SpoolService Abuse with Unconstrained Delegation]]
- [[SpoolService status]]


