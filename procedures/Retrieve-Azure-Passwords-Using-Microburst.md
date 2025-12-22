---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Cloud-Azure]]'
  - '[[tags/Stealing-Tokens]]'
commands:
  - '[[commands/powershell-import-microburst-module]]'
  - '[[commands/powershell-get-azure-passwords]]'
  - '[[commands/powershell-get-azure-passwords-gridview]]'
platforms:
  - Azure
  - Windows
tools:
  - '[[tools/Microburst]]'
validated: true
---

# Retrieve-Azure-Passwords-Using-Microburst

## Summary

This procedure outlines the steps to use the Microburst PowerShell module to retrieve Azure passwords, enabling access to user accounts, cloud resources, and sensitive data. It involves importing the module and executing cmdlets to dump passwords, optionally displaying them in a graphical grid for easier review.

## Description

Microburst is a PowerShell toolkit for Azure penetration testing that includes cmdlets like Get-AzurePasswords to extract stored credentials from Azure environments. This technique is useful in post-exploitation scenarios where an attacker has initial access to an Azure tenant, allowing them to harvest passwords for lateral movement and privilege escalation. The procedure assumes the attacker has authenticated access to Azure via PowerShell (e.g., via stolen tokens or valid accounts) and focuses on dumping passwords from Azure AD or related services. Success provides plaintext or hashed credentials that can be cracked or used directly.

## Requirements

1. PowerShell 5.1 or later installed on a Windows system with internet access.
2. Microburst module downloaded and available locally (e.g., Microburst.psm1 file).
3. Valid Azure authentication (e.g., via Connect-AzAccount or imported tokens) to query Azure resources.
4. Administrative or reader permissions in the target Azure subscription or directory.

## Defense

- Implement multi-factor authentication (MFA) to prevent use of stolen passwords and tokens.
- Monitor for suspicious PowerShell activity, such as module imports or unusual Azure API calls via Azure AD logs and Microsoft Defender for Cloud.
- Regularly review and rotate service principal credentials, and use just-in-time access controls to limit standing permissions.
- Enable Azure AD Privileged Identity Management (PIM) and audit logs for credential access attempts.

## Objectives

1. Import the Microburst module to access Azure-specific cmdlets.
2. Retrieve Azure passwords to gain access to user accounts and cloud resources.
3. Optionally view passwords in a graphical interface for analysis and exfiltration.
4. Use retrieved credentials for lateral movement and privilege escalation within the Azure environment.

## Instructions

### Step 1: Import Microburst Module

**Context**: Load the Microburst PowerShell module to make its cmdlets available for execution. This step is prerequisite for running Azure-specific functions and assumes the module file (Microburst.psm1) is in the current directory or PowerShell path.

**Command** ([[commands/powershell-import-microburst-module]]):
```powershell
Import-Module Microburst.psm1
```

> This command imports the module without parameters. Expected output is a confirmation message like "Import-Module : The specified module 'Microburst.psm1' was loaded successfully." If the module path is incorrect, it will error with a file not found message. Verify by running Get-Command Get-AzurePasswords to confirm availability.

### Step 2: Retrieve Azure Passwords

**Context**: Execute the core cmdlet to dump Azure passwords from the authenticated tenant. This queries Azure AD and related services for exposed credentials, such as service principal secrets or user passwords stored insecurely.

**Command** ([[commands/powershell-get-azure-passwords]]):
```powershell
Get-AzurePasswords
```

> This command runs without additional parameters after authentication. Expected output is a table or list of discovered passwords, including usernames, passwords, and associated resources (e.g., App Registrations). If no passwords are found, it returns an empty result set. Pipe to a file for exfiltration if needed: Get-AzurePasswords | Out-File passwords.txt.

### Step 3: (Optional) Display Passwords in Graphical Grid

**Context**: For easier review and sorting of retrieved passwords, pipe the output to Out-GridView. This opens a Windows GUI table allowing filtering and export, useful in environments with graphical access.

**Command** ([[commands/powershell-get-azure-passwords-gridview]]):
```powershell
Get-AzurePasswords -Verbose | Out-GridView
```

> The -Verbose flag provides detailed logging during retrieval. Expected output is a pop-up grid view displaying columns like Name, Password, and Type. Success is indicated by the grid populating with data; close it to return to the console. This step requires a graphical PowerShell session (e.g., not in a remote SSH).
