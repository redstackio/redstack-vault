---
id: 41310754-0d84-48c8-ab32-b0e5ce330234
name: Powershell Domain Trust Functions
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:27.629968+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Powershell Domain Trust Functions

# Description

Domain Trust Powershell commands. 







**Command** ([[Get all trusts for current user's domain]]):

```bash
Get-NetDomainTrust

```







**Command** ([[Get forest trusts]]):

```bash
Get-NetForestTrust 

```







**Command** ([[Enumerate users in groups outside their principal domain]]):

```bash
Find-ForeignUser

```







**Command** ([[Enumerate members of a domain's groups, finds users outside of queried domain]]):

```bash
Find-ForeignGroup

```







**Command** ([[ Map a relation of all domain trusts]]):

```bash
Invoke-MapDomainTrust

```






