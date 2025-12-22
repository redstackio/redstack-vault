---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
  - >-
    [[techniques/Use Alternate Authentication Material|T1550 - Use Alternate
    Authentication Material]]
sub_techniques:
  - '[[sub-techniques/Kerberoasting|T1558.003 - Kerberoasting]]'
  - '[[sub-techniques/Pass the Ticket|T1550.003 - Pass the Ticket]]'
  - '[[sub-techniques/Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Impersonate a domain user on a resource]]'
  - '[[tags/Kerberos Constrained Delegation]]'
commands: []
tools: []
platforms:
  - Windows
  - Active Directory
verified: true
validated: true
---

# Kerberos-Constrained-Delegation-Impersonation-on-Resource

## Summary

This procedure demonstrates how to impersonate a domain user on a specific resource using Kerberos Constrained Delegation, allowing access to remote shares or services without the user's password. It exploits delegation privileges to facilitate lateral movement and privilege escalation in Active Directory environments.

## Description

Kerberos Constrained Delegation enables a service account to impersonate users to specific back-end services, such as file shares or other resources. An attacker with access to a delegated account can leverage this to impersonate high-privilege users like administrators on targeted resources. This technique is particularly effective in domain environments where delegation is misconfigured, enabling unauthorized access to sensitive data or systems. The approach involves creating an impersonation context using Windows APIs, then accessing the resource under the impersonated identity. Detection is challenging as it mimics legitimate delegation behavior, but monitoring for anomalous resource access can help identify abuse. This procedure assumes the attacker has compromised a delegated account and is operating from a domain-joined system.

## Requirements

1. Compromised domain user account with 'Trust this computer for delegation' privilege enabled.
2. Domain-joined Windows system with PowerShell access.
3. Network connectivity to the target resource (e.g., file server or domain controller).
4. Knowledge of the target username to impersonate (e.g., 'administrator') and the resource path (e.g., a remote C$ share).

## Defense

- Disable 'Trust this computer for delegation' for non-essential accounts and audit delegation settings regularly using tools like PowerView or ADUC.
- Monitor event logs for Kerberos delegation events (Event ID 4769) and anomalous access to resources from delegated accounts.
- Implement least privilege by limiting allowed services in constrained delegation configurations.
- Use advanced auditing for S4U (Service for User) requests and correlate with normal user behavior.

## Objectives

1. Impersonate a specified domain user on a target resource using delegation privileges.
2. Gain unauthorized access to remote resources, such as administrative shares.
3. Enable lateral movement and potential privilege escalation within the Active Directory network.

## Instructions

### Step 1: Load Required Assembly and Initiate Impersonation

**Context**: Begin by loading the System.IdentityModel assembly, which provides the necessary classes for creating and managing Windows identities. Then, construct a WindowsIdentity object for the target user and invoke impersonation to switch the security context. This step sets up the delegation-based impersonation required for accessing the resource under the target's credentials.

**Code** ([[codes/PowerShell-WindowsIdentity-Impersonation-for-Resource-Access]]):

```powershell
[Reflection.Assembly]::LoadWithPartialName('System.IdentityModel') | out-null
$idToImpersonate = New-Object System.Security.Principal.WindowsIdentity @('administrator')
$idToImpersonate.Impersonate()
[System.Security.Principal.WindowsIdentity]::GetCurrent() | select name
```

> This code loads the assembly silently, creates an identity for the specified user (replace 'administrator' with the target username), impersonates it, and verifies the current identity. If successful, the output will show the impersonated user's name, confirming the context switch. Ensure the current account has delegation rights; otherwise, this will fail with an access denied error.

### Step 2: Access the Target Resource Under Impersonated Identity

**Context**: With the impersonation active, interact with the target resource, such as listing contents of a remote administrative share. This demonstrates successful delegation, allowing access as the impersonated user. Replace the server path with the actual resource, and verify access permissions align with the delegated services.

**Code** ([[codes/PowerShell-WindowsIdentity-Impersonation-for-Resource-Access]]):

```powershell
ls \\$SERVER\c$
```

> Execute the directory listing command on the remote share (e.g., replace $SERVER with 'dc01.offense.local'). Expected output includes a list of files and directories on the C$ share if access is granted via delegation. If the share is inaccessible, check delegation configuration or network connectivity. Revert impersonation after use by calling $idToImpersonate.Undo() to restore the original context.
