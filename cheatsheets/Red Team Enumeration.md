---
id: 50d68fa6-90a3-497a-bce0-1b8a03cf0da3
name: Red Team Enumeration
type: cheatsheet
verified: false
created_at: '2020-07-15T19:06:27.071354+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Red Team Enumeration

# Description

Red Team Cheatsheet to preform quick enumeration with powershell



**Command** ([[Perform portscan on hosts]]):

```bash
Invoke-Portscan -Hosts "192.168.1.10" -TopPorts 50

```







**Command** ([[Basic User info]]):

```bash
Get-NetUser -UACFilter NOT_ACCOUNTDISABLE | select samaccountname, description, pwdlastset, logoncount, badpwdcount

```







**Command** ([[Find users with sidHistory set]]):

```bash
Get-NetUser -LDAPFilter '(sidHistory=*)' 

```







**Command** ([[ASREPRoastable users]]):

```bash
Get-NetUser -PreauthNotRequired 

```







**Command** ([[Kerberoastable users]]):

```bash
Get-NetUser -SPN 

```







**Command** ([[Basic Computer info]]):

```bash
Get-NetComputer | select samaccountname, operatingsystem, description

```







**Command** ([[Find computers with Unconstrained Delegation]]):

```bash
Get-NetComputer -Unconstrained | select samaccountname 

```







**Command** ([[Find computers with Constrined Delegation]]):

```bash
Get-NetComputer -TrustedToAuth | select samaccountname 

```







**Command** ([[Get forest trusts]]):

```bash
Get-NetForestTrust 

```







**Command** ([[Get users with privileges in other domains inside the forest]]):

```bash
Get-DomainForeignUser 

```







**Command** ([[Get groups with privileges in other domains inside the forest]]):

```bash
Get-DomainForeignGroupMember 

```






