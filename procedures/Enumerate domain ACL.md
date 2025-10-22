---
id: 1370c7d9-fb99-4eac-a380-737c91ba8690
name: Enumerate domain ACL
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T07:34:24.330891+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[Enumerate Domain Group ACLs]]'
- '[[Look up ACL ACE from PowerView]]'
---

# Enumerate domain ACL

## Summary

Identify if a group has ACL that can be useful or taken advantage of. 

## Description

# Description

Identify if a group has ACL that can be useful or taken advantage of.

## Objective

1. Find if a group has ACL that can be abused

2. A group that has privileged access or rights

# Instructions

1. Enumerate ACL for specific AD Group using PowerSploit

**Command** ([[Enumerate Domain Group ACLs]]):

```bash
Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match $GROUP_NAME}
```

3. If 1st command returns useful results, look up ACE from PowerView. Can be a group membership of the user group with privileges that can be leveraged.

**Command** ([[Look up ACL ACE from PowerView]]):

```bash
Get-DomainObjectACL -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(ConvertSidToName $_.SecurityIdentifier);$_} | ?{$_.IdentityName -match $GROUP_NAME1}

```

## Commands Used

- [[Enumerate Domain Group ACLs]]
- [[Look up ACL ACE from PowerView]]
