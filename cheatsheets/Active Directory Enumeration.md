---
id: 48ec8aec-67fe-406b-af43-ee5a29121bca
name: Active Directory Enumeration
type: cheatsheet
verified: true
created_at: '2020-07-01T22:19:32.850257+00:00'
updated_at: '2023-05-30T20:07:24.995695+00:00'
---

# Active Directory Enumeration

**Status**: ✓ Verified

# Description

Various  Windows, PowerView, and ActiveDirectory (module) commands for recon and enumeration.

## Domain

**Command** ([[SharpHound Ingest AD Domain Information and Dump Results to File]]):

```bash
SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USER --ldappassword $_PASSWORD
```

## Users

**Command** ([[ActiveDirectory List AD Users with SID]]):

```bash
Get-ADUser -Filter * | Select-Object -Property name,sid
```

**Command** ([[PowerView Recursively List a User's Groups]]):

```bash
Get-DomainGroup -MemberIdentity $_USER
```

**Command** ([[PowerView Recursively List Users of a Group]]):

```bash
Get-DomainGroupMember -Identity "$_GROUP" -Recurse
```

**Command** ([[setspn List AD Accounts with SPN Set]]):

```bash
setspn.exe -T $_DOMAIN -Q */*
```

**Command** ([[PowerView List AD Accounts with SPN Set]]):

```bash
Get-DomainUser -SPN
```

**Command** ([[PowerView List Domain Users with Kerberos Preauthentication Disabled]]):

```bash
Get-DomainUser -PreauthNotRequired
```

## Forests

**Command** ([[ActiveDirectory Get SIDs of Trusted Domains]]):

```bash
(Get-ADForest).Domains| %{Get-ADDomain -Server $_}|select name, domainsid
```

**Command** ([[ActiveDirectory Get SID of a Foreign Group in Trusted Domain]]):

```bash
Get-ADGroup "$_GROUP" -Server "$_REMOTE_DOMAIN_DC"
```

**Command** ([[PowerView Get Global Catalogs for the Current Forest]]):

```bash
Get-ForestGlobalCatalog
```
