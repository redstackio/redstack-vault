---
id: 5383396c-195b-4763-baf4-5df3f46e2e71
name: Windows-DPAPI-Credential-Files-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.251487+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - dpapi
  - credential-enumeration
  - windows-credentials
commands:
  - '[[commands/windows-cmd-list-hidden-credentials-folders]]'
  - '[[commands/powershell-list-hidden-credentials-folders]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-DPAPI-Credential-Files-Enumeration

## Summary

This procedure enumerates hidden credential files stored by the Windows Data Protection API (DPAPI) in a user's local and roaming profiles. DPAPI encrypts sensitive data like credentials using the user's logon keys, and listing these files allows attackers to identify targets for further extraction and decryption, potentially leading to credential theft for lateral movement or privilege escalation.

## Description

The Windows DPAPI enables applications to encrypt and store sensitive information, such as Wi-Fi passwords, authentication tokens, and application credentials, in protected files within the user's AppData directories. These files are typically hidden and accessible only to the authenticated user or processes running in their context. An attacker with local access can enumerate these files to locate DPAPI-protected blobs, which can then be backed up or decrypted using tools like Mimikatz if the user's master key is compromised. This technique is commonly used in post-exploitation scenarios on Windows systems to harvest credentials for network pivoting. The procedure targets the Local and Roaming Credentials subfolders, revealing files like those with .cred or .p12 extensions that hold encrypted secrets.

## Requirements

1. Local authenticated access to the target Windows system as the user whose credentials are being enumerated.
2. Administrator or SYSTEM privileges may be required for full access to protected directories.
3. Command-line access via Command Prompt or PowerShell; no additional tools needed for enumeration, but tools like Mimikatz are recommended for subsequent extraction.
4. Knowledge of the target username to substitute in file paths.

## Defense

- Enable advanced auditing for file access in sensitive directories like AppData to detect unauthorized enumeration attempts.
- Use credential guard features like Windows Defender Credential Guard to isolate and protect DPAPI secrets from user-mode access.
- Implement least-privilege principles to limit local logon rights and monitor for anomalous process execution in user profiles.
- Regularly rotate credentials and monitor for signs of DPAPI key extraction via event logs (e.g., Event ID 4776 for credential validation failures).

## Objectives

1. Identify and list all hidden DPAPI credential files in the user's local and roaming profiles.
2. Verify the presence of encrypted credential blobs for potential offline decryption.
3. Gather file paths and metadata to support further credential dumping operations.

## Instructions

### Step 1: Enumerate Hidden Credentials Using Command Prompt

**Context**: Use the native Windows Command Prompt to list hidden files in the DPAPI Credentials directories. This reveals protected files without requiring PowerShell, providing a quick initial scan. The /a:h flag ensures only hidden items are shown, helping to focus on DPAPI-stored secrets.

**Command** ([[commands/windows-cmd-list-hidden-credentials-folders]]):
```cmd
dir /a:h C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*
dir /a:h C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\*\
```

> This command lists hidden directories and files in the specified paths. Replace $_USERNAME with the actual username (e.g., 'john.doe'). If files like Credentials_*.cred are found, they contain encrypted data protected by the user's DPAPI master key.

### Step 2: Enumerate Hidden Credentials Using PowerShell

**Context**: For a more scriptable approach, use PowerShell's Get-ChildItem cmdlet to recursively list hidden items. This is useful for automation or piping output to further analysis, confirming the same files identified in Step 1 and providing object-oriented handling for scripting.

**Command** ([[commands/powershell-list-hidden-credentials-folders]]):
```powershell
Get-ChildItem -Hidden -Path C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\ -Recurse
Get-ChildItem -Hidden -Path C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\ -Recurse
```

> The -Hidden parameter filters for hidden items, and -Recurse explores subdirectories. Expected results include paths to files such as 'Credentials_3B1A8267-6A4A-4E5B-9F0E-8D2C1F3E4A5B.cred', indicating successful enumeration of DPAPI blobs.

### Step 3: Combine Enumeration in a PowerShell Script

**Context**: Run a combined script that executes both CMD and PowerShell methods for comprehensive coverage. This verifies consistency across tools and captures output for logging or export.

**Code** ([[codes/powershell-enumerate-dpapi-credential-files]]):

> Execute the script in PowerShell after substituting $_USERNAME. It runs both enumeration methods and outputs results to console for review. Success is indicated by matching file lists from both approaches, confirming hidden credential files are present.
