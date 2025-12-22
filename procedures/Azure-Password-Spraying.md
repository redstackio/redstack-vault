---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Enumerate valid emails]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Password spraying]]'
commands:
  - '[[commands/msolspray-invoke-password-spray]]'
tools: []
platforms:
  - Azure
  - Office 365
verified: true
validated: true
---

# Azure-Password-Spraying

## Summary

Azure Password Spraying is a technique to test a large number of Azure Active Directory (Azure AD) or Office 365 user accounts against a small set of common passwords, aiming to identify weak credentials without triggering lockouts. This procedure uses the MSOLSpray PowerShell script to perform the spraying attack remotely, helping attackers gain initial access to cloud resources like email accounts containing sensitive data.

## Description

This procedure targets Azure AD environments by attempting authentication with a list of valid usernames (emails) and a curated list of weak passwords. Unlike traditional brute-force attacks that target one account with many passwords, password spraying spreads attempts across many accounts with few passwords to evade detection mechanisms like account lockouts. It is effective in environments with poor password policies and can lead to unauthorized access to Microsoft 365 services, including Exchange Online for email exfiltration. The technique requires a pre-enumerated list of valid emails, obtained via reconnaissance, and is executed via the open-source MSOLSpray tool, which leverages Microsoft Online Services (MSOL) cmdlets for authentication checks.

## Requirements

1. A list of valid Azure AD/Office 365 email addresses (e.g., from prior enumeration of public directories or data leaks).
2. Internet access to connect to Azure AD authentication endpoints.
3. PowerShell execution environment (Windows or compatible, with MSOL module implicitly handled by the script).
4. Downloaded MSOLSpray script from the official GitHub repository.

## Defense

- Enforce strong password policies, including complexity requirements and regular rotations, to reduce the effectiveness of common password guesses.
- Implement multi-factor authentication (MFA) across all Azure AD accounts to block unauthorized access even with valid credentials.
- Monitor Azure AD sign-in logs for suspicious patterns, such as multiple failed logins from diverse accounts in a short period, and set up alerts for anomalous authentication attempts.
- Use Azure AD Identity Protection to detect and respond to spraying attempts automatically.

## Objectives

1. Identify valid username-password combinations in Azure AD environments.
2. Gain initial access to compromised accounts for further lateral movement or data access.
3. Exfiltrate sensitive information from cloud services like Outlook or OneDrive.

## Instructions

### Step 1: Download and Load MSOLSpray Script

**Context**: Obtain the MSOLSpray tool and load it into the PowerShell session to prepare for the spraying operation. This step ensures the necessary functions are available without requiring manual installation of MSOL modules.

Download the script from https://github.com/dafthack/MSOLSpray and place it in a tools directory, such as C:\Tools\MSOLSpray\MSOLSpray.ps1.

**Code** ([[codes/msolspray-script-invocation]]):

```powershell
. C:\Tools\MSOLSpray\MSOLSpray.ps1
```

> This dotsources the script, making the Invoke-MSOLSpray function available. Expected output: No errors; PowerShell prompt returns without issues.

### Step 2: Prepare Input Files

**Context**: Create or verify the user list file containing target emails to ensure the attack targets only valid accounts, minimizing noise and detection risk.

Prepare a text file (e.g., C:\Tools\validemails.txt) with one email per line, such as user1@target.com, user2@target.com.

> Expected output: A plain text file with the list of emails. Verify by opening the file to confirm format.

### Step 3: Execute Password Spraying

**Context**: Run the spraying attack using a common password against the user list. The -Verbose flag provides detailed logging of attempts and results.

**Command** ([[commands/msolspray-invoke-password-spray]]):

```powershell
Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD> -Verbose
```

> Replace <PASSWORD> with a common password like 'Password123'. The script will attempt authentication for each user. Expected output: Verbose logs showing success/failure for each attempt, with successful hits displaying the valid username-password pair. If successful, proceed to access the account via Outlook Web Access or similar.
