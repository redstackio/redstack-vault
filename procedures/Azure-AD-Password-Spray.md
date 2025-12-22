---
id: 48c3d668-8ab8-47cb-b94c-c70bb6812cf3
name: Azure-AD-Password-Spray
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:16.028114+00:00'
updated_at: '2023-05-23T16:41:08.041642+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - azure-ad
  - cloud-azure
  - password-spray
commands:
  - '[[commands/git-clone-mso-lspray-from-github]]'
  - '[[commands/import-mso-lspray-powershell-module]]'
  - '[[commands/invoke-mso-lspray-password-spray]]'
platforms:
  - Cloud
tools: []
validated: true
---

# Azure-AD-Password-Spray

## Summary

This procedure performs a password spray attack against Azure Active Directory (Azure AD) accounts using the MSOLSpray PowerShell tool. It targets multiple user accounts with a small set of common passwords to identify valid credentials without triggering account lockouts, enabling unauthorized access to cloud resources.

## Description

Password spraying is an effective brute-force technique in Azure AD environments where organizations have many users but enforce weak password policies. By attempting a few common passwords (e.g., seasonal or default ones) against a large list of usernames, attackers can compromise accounts while staying under detection thresholds. MSOLSpray automates this by simulating Office 365 logins, checking credentials without excessive failures. This is useful in red team engagements to test password hygiene in hybrid or cloud-only setups. Success grants access to email, SharePoint, or other Azure services, potentially leading to lateral movement.

## Requirements

1. PowerShell 5.1 or later on a Windows or Linux host with PowerShell Core.
2. A list of target usernames in a text file (format: user@domain.com, one per line).
3. Network access to Azure AD endpoints (e.g., login.microsoftonline.com).
4. No existing Azure AD credentials required, but proxy/VPN may be needed for evasion.

## Defense

- Implement multi-factor authentication (MFA) for all Azure AD accounts to block credential-only access.
- Enforce strong password policies with complexity requirements and regular rotations.
- Monitor Azure AD sign-in logs for failed attempts from unusual IPs or patterns exceeding baselines.
- Enable account lockout after a low number of failures and use Conditional Access policies for rate limiting.

## Objectives

1. Identify valid username-password combinations in Azure AD.
2. Gain initial access to compromised accounts for further exploitation.
3. Demonstrate risks of poor password practices in cloud environments.

## Instructions

### Step 1: Clone MSOLSpray Repository

**Context**: Download the MSOLSpray tool from GitHub to obtain the PowerShell script for password spraying.

**Command** ([[commands/git-clone-mso-lspray-from-github]]):
```bash
git clone https://github.com/dafthack/MSOLSpray
```

This command fetches the repository into the current directory. Expected output includes progress messages ending with "Cloning into 'MSOLSpray'..." and a success confirmation.

### Step 2: Import MSOLSpray PowerShell Module

**Context**: Load the MSOLSpray script into the PowerShell session to make the Invoke-MSOLSpray function available.

**Command** ([[commands/import-mso-lspray-powershell-module]]):
```powershell
Import-Module .\MSOLSpray.ps1
```

Run this in a PowerShell prompt after navigating to the cloned directory. Expected output is silent on success; verify by running Get-Command Invoke-MSOLSpray, which should list the function.

### Step 3: Perform Password Spray

**Context**: Execute the spray attack using a list of users and a common password, monitoring for successful authentications.

**Command** ([[commands/invoke-mso-lspray-password-spray]]):
```powershell
Invoke-MSOLSpray -UserList .\userlist.txt -Password Winter2020
```

Replace userlist.txt with your username file and Winter2020 with the password to test. The tool attempts logins and reports hits. If multiple lockouts occur, use -Force to continue. Expected output includes verbose logs of attempts, with successes like "Valid credentials found: user@domain.com:Winter2020". Run additional sprays with different passwords as needed.
