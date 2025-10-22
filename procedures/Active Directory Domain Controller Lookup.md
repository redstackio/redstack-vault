---
id: b8fa702e-2d5f-4b10-b2bb-3853656de215
name: Active Directory Domain Controller Lookup
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.538641+00:00'
updated_at: '2023-04-10T20:26:38.444032+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Recon]]'
- '[[Other Interesting Commands]]'
commands:
- '[[DNS Lookup for domain.com]]'
- '[[DNS Lookup for _ldap._tcp.dc._msdcs.<domain>.com]]'
- '[[Group Policy Results]]'
- '[[List of Domain Controllers]]'
- '[[List of Domain Controllers using Get-ADDomainController]]'
- '[[Logon Server Command]]'
- '[[Logon Server Environment Variable]]'
---

# Active Directory Domain Controller Lookup

## Summary

The Active Directory Domain Controller Lookup procedure is used to identify the domain controller(s) for a targeted Active Directory environment. This information can be used to further enumerate the environment and identify potential targets for attack. This procedure involves using the 'Domain Co

## Description

# Description

The Active Directory Domain Controller Lookup procedure is used to identify the domain controller(s) for a targeted Active Directory environment. This information can be used to further enumerate the environment and identify potential targets for attack. This procedure involves using the 'Domain Controller Lookup' command to query DNS for the domain controller(s) associated with the target domain. The results of this command can be used to identify the domain controller(s) and their associated IP addresses.

From an offensive perspective, this procedure can be used to identify potential targets for credential harvesting, lateral movement, and privilege escalation. From a defensive perspective, this procedure can be used to identify potential attack vectors and harden the environment against these types of attacks.

## Requirements

1. Access to the target Active Directory environment

1. Authenticated access to the DNS server(s) for the target domain

## Defense

1. Ensure that DNS servers are properly configured and secured

1. Implement network segmentation to limit access to domain controllers

1. Monitor DNS queries and look for suspicious activity

## Objectives

1. Identify the domain controller(s) for a targeted Active Directory environment

1. Enumerate the environment and identify potential targets for attack

# Instructions

1. This command provides multiple ways to look up domain controllers in a Windows domain environment.

**Code**: [[nslookup domain.com
nslookup -type=srv _ldap._tcp.]]

> The first command 'nslookup domain.com' returns the IP addresses of domain controllers for the domain specified. The second command 'nslookup -type=srv _ldap._tcp.dc._msdcs.<domain>.com' returns the SRV records of domain controllers for the domain specified. The third command 'nltest /dclist:domain.com' returns a list of domain controllers for the domain specified. The fourth command 'Get-ADDomainController -filter * | Select-Object name' returns a list of all domain controllers in the current domain. The fifth command 'gpresult /r' displays the Resultant Set of Policy (RSoP) for the current user and computer. The sixth command '$Env:LOGONSERVER' displays the name of the domain controller that authenticated the current user. The seventh command 'echo %LOGONSERVER%' displays the name of the domain controller that authenticated the current user.

**Command** ([[DNS Lookup for domain.com]]):

```bash
nslookup domain.com
```

**Command** ([[DNS Lookup for _ldap._tcp.dc._msdcs.<domain>.com]]):

```bash
nslookup -type=srv _ldap._tcp.dc._msdcs.<domain>.com
```

**Command** ([[List of Domain Controllers]]):

```bash
nltest /dclist:domain.com
```

**Command** ([[List of Domain Controllers using Get-ADDomainController]]):

```bash
Get-ADDomainController -filter * | Select-Object name
```

**Command** ([[Group Policy Results]]):

```bash
gpresult /r
```

**Command** ([[Logon Server Environment Variable]]):

```bash
$Env:LOGONSERVER
```

**Command** ([[Logon Server Command]]):

```bash
echo %LOGONSERVER%
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[DNS Lookup for domain.com]]
- [[DNS Lookup for _ldap._tcp.dc._msdcs.<domain>.com]]
- [[Group Policy Results]]
- [[List of Domain Controllers]]
- [[List of Domain Controllers using Get-ADDomainController]]
- [[Logon Server Command]]
- [[Logon Server Environment Variable]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Recon]]
- [[Other Interesting Commands]]
