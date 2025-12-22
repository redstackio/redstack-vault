---
id: 3f9cf19c-6735-45fb-9b6d-e24d96089fd3
name: Active-Directory-Object-Owner-Hijacking
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.897952+00:00'
updated_at: '2023-04-10T20:26:31.142681+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Abusing Active Directory ACLs/ACEs]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/WriteOwner]]'
commands:
  - '[[commands/powershell-set-domain-object-owner]]'
  - '[[commands/bloodyad-set-owner]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
  - '[[tools/bloodyad]]'
validated: true
---

# Active-Directory-Object-Owner-Hijacking

## Summary

Active Directory Object Owner Hijacking is a post-exploitation technique that allows an attacker with sufficient permissions to change the ownership of an Active Directory object, such as a user, group, or computer account. By setting the owner to a controlled principal, the attacker gains full control over the object, enabling privilege escalation, persistence, and evasion of security controls. This procedure outlines using PowerView or BloodyAD tools to perform the hijacking, assuming the attacker has WriteOwner permissions via misconfigured ACLs or stolen credentials.

## Description

In an Active Directory environment, every object has an owner who controls its permissions. If an attacker can modify the owner attribute (often through inherited or explicit WriteOwner rights), they can reassign ownership to themselves or a puppet account. This grants unrestricted access to modify the object's attributes, reset passwords, or add backdoor permissions without triggering standard access denied alerts. The technique is particularly effective in mature domains where ACLs are overly permissive. Once ownership is hijacked, the attacker can use the object for lateral movement, such as adding it to privileged groups or using it for delegation abuse. Detection relies on auditing owner changes, but many environments lack this. This procedure requires domain-joined access or RPC connectivity to a domain controller and is commonly used after initial foothold via phishing or vuln exploitation.

## Requirements

1. Valid domain credentials with WriteOwner permission on the target object (e.g., via ACL abuse or delegated rights).
2. Network access to a domain controller (ports 445/TCP for SMB, 389/TCP for LDAP).
3. Installed tools: PowerView (PowerShell module) or BloodyAD (Python script) on the attacker's system.
4. Target Active Directory environment (Windows Server 2008+).

## Defense

- Enforce least privilege on ACLs: Regularly audit and remove unnecessary WriteOwner permissions using tools like BloodHound.
- Enable advanced auditing for directory service changes (Event ID 4742 for owner modifications) and forward logs to a SIEM.
- Implement protected users group and restrict delegation to prevent credential abuse.
- Use Just-In-Time (JIT) administration to limit standing permissions.

## Objectives

1. Change ownership of a target AD object to an attacker-controlled principal for full control.
2. Establish persistence by maintaining backdoor access to the object.
3. Escalate privileges if the object is sensitive (e.g., a service account or group).
4. Evade detection by mimicking legitimate admin actions.

## Instructions

### Step 1: Identify Permissions and Prepare Hijack Using PowerView

**Context**: First, confirm you have WriteOwner rights on the target object using PowerView's Get-DomainObjectAcl. If confirmed, use the Set-DomainObjectOwner cmdlet to reassign ownership. This step assumes PowerView is loaded via Import-Module PowerView.ps1. Replace placeholders with actual values; run from a domain-joined host or via SMBExec for remote execution.

**Command** ([[commands/powershell-set-domain-object-owner]]):
```powershell
Set-DomainObjectOwner -Identity $_TARGET_OBJECT -OwnerIdentity $_OWNER_IDENTITY
```

> This PowerShell cmdlet from PowerView modifies the nTSecurityDescriptor of the target object to set the new owner. It leverages LDAP to connect to the domain controller. If successful, the owner attribute updates immediately, granting the new owner full control. Run Get-DomainObjectOwner -Identity $_TARGET_OBJECT afterward to verify. If the command fails with access denied, check ACLs with Get-DomainObjectAcl.

### Step 2: Execute Hijack Using BloodyAD Tool

**Context**: As an alternative to PowerShell, use BloodyAD for a Python-based approach, which supports more granular LDAP operations. This is useful if PowerShell logging is monitored. Authenticate with compromised credentials that have WriteOwner rights. If the domain requires LDAPS, add --secure flag (not shown). Verify post-execution by querying the object's owner via ldapsearch or similar.

**Command** ([[commands/bloodyad-set-owner]]):
```bash
bloodyAD.py --host $_DC_HOST -d $_DOMAIN -u $_USERNAME -p $_PASSWORD setOwner $_OWNER $_TARGET_OBJECT
```

> BloodyAD connects via LDAP and issues a modify request to change the owner SID in the security descriptor. Success is indicated by a confirmation message like "Owner set successfully." If it fails, it may output LDAP error codes (e.g., INSUFFICIENT_ACCESS). This method bypasses some PowerShell restrictions but requires Python 3 and the bloodyAD library installed.
