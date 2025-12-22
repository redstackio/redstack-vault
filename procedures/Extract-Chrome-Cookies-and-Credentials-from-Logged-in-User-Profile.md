---
id: 65770273-7e84-4c90-bde3-559d281dd907
name: Extract-Chrome-Cookies-and-Credentials-from-Logged-in-User-Profile
type: procedure
verified: true
submitted: false
created_at: '2020-07-21T05:09:20.687962+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials from Web Browsers]]'
sub_techniques: []
tags:
  - Chrome
  - dump
  - extract
  - credentials
commands:
  - '[[commands/mimikatz-dump-masterkeys-in-memory]]'
  - '[[commands/mimikatz-dpapi-chrome-decrypt]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Extract-Chrome-Cookies-and-Credentials-from-Logged-in-User-Profile

## Summary

This procedure extracts a logged-in user's Chrome cookies and credentials by dumping the master key from memory using Mimikatz and then decrypting the encrypted files in the user's Chrome profile. It requires administrative privileges and the user to be actively logged in, allowing access to sensitive web session data for further attacks like session hijacking or authentication bypass.

## Description

Chrome stores cookies and login credentials in SQLite databases encrypted with DPAPI using a master key derived from the user's login context. When the user is logged in, this master key resides in memory and can be extracted using Mimikatz's sekurlsa module. Once obtained, the master key is used with the dpapi::chrome module to decrypt the 'Cookies' and 'Login Data' files located in the user's AppData directory. This technique is effective in post-exploitation scenarios on Windows systems where the attacker has elevated command execution, enabling the theft of stored web credentials for sites like banking or corporate portals. The process targets the Default profile but can be adapted for other profiles.

## Requirements

1. Administrative access on the target Windows system to run Mimikatz.
2. The target user must be actively logged in for the master key to be in memory.
3. Mimikatz binary downloaded and executable on the target (x64 version recommended).
4. Knowledge of the target username ($_TARGET_USER) for file paths.
5. Command prompt or PowerShell with execution privileges.

## Defense

Defensive measures and detection strategies:

- Enable advanced auditing for process creation and monitor for Mimikatz signatures using EDR tools like Sysmon or Windows Defender.
- Implement application whitelisting to block unsigned executables like Mimikatz.exe.
- Use credential guard features (e.g., LSA Protection) to isolate LSASS and prevent memory dumping.
- Monitor file access to Chrome user data directories and anomalous DPAPI usage.
- Educate users on clearing browser data and using password managers with master passwords.

## Objectives

1. Dump the DPAPI master key from the logged-in user's memory session.
2. Decrypt and extract Chrome-stored cookies and credentials using the master key.
3. Obtain plaintext credentials or cookie values for session reuse or impersonation.
4. Validate extraction by checking for readable URLs, usernames, and passwords.

## Instructions

### Step 1: Download and Prepare Mimikatz

**Context**: Obtain the Mimikatz tool, which is required to interact with Windows DPAPI and LSASS memory. This step ensures the tool is available on the target system without relying on pre-installed components.

Download Mimikatz from the official GitHub repository and copy the executable (mimikatz.exe) to a writable directory on the target, such as C:\Windows\Temp. Run it from an elevated command prompt to avoid permission issues.

### Step 2: Dump Master Keys from Memory

**Context**: Extract the DPAPI master keys associated with the logged-in user's session from LSASS memory. This key is essential for decrypting Chrome's encrypted data and is only available while the user is authenticated.

**Command** ([[commands/mimikatz-dump-masterkeys-in-memory]]):
```command_prompt
mimikatz.exe "sekurlsa::dpapi" "exit"
```

> This command launches Mimikatz and uses the sekurlsa::dpapi module to enumerate and display master keys for active sessions. Look for the 'MasterKey' line in the output corresponding to the target user's SID or username. Copy the full hex string (e.g., daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723) as $_MASTER_KEY. If no key is found, verify the user is logged in and retry.

### Step 3: Identify Chrome Profile Files

**Context**: Locate the encrypted SQLite files containing cookies and credentials in the user's Chrome profile. These files are protected by the master key and must be accessed while Chrome is not running to avoid locks.

Determine the target user's profile path using the current username or enumerate via 'whoami'. The standard locations are:
- Cookies: C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Cookies
- Credentials: C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data

Close Chrome if running to release file locks. Verify file existence with 'dir' command; if absent, the user may not have saved data in the Default profile.

### Step 4: Decrypt Credentials Using Master Key

**Context**: Use the extracted master key to decrypt the 'Login Data' file, revealing stored usernames and passwords for websites. This step targets credential theft for reuse.

**Command** ([[commands/mimikatz-dpapi-chrome-decrypt]]):
```command_prompt
mimikatz.exe

dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```

> Launch Mimikatz interactively, then run the dpapi::chrome module specifying the input file path and master key. The /unprotect flag attempts DPAPI decryption. Successful output includes URLs, usernames, and decrypted passwords (e.g., Password: S3c47pA55). If the file is large, processing may take time; errors indicate incorrect key or file corruption.

### Step 5: Decrypt Cookies Using Master Key

**Context**: Apply the same decryption to the 'Cookies' file to extract session cookies, which can be used for hijacking active web sessions without passwords.

Adapt the previous command by changing the /in path:
```command_prompt
mimikatz.exe

dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Cookies" /unprotect /masterkey:$_MASTER_KEY
```

> This decrypts cookie values, including session tokens for domains. Output shows host keys, names, and encrypted_value decrypted to plaintext. Export results to a file for analysis (e.g., redirect output). Success confirms if cookies for high-value sites (e.g., .bank.com) are present.
