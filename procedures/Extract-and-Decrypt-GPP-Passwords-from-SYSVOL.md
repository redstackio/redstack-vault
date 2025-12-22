---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[techniques/Unsecured Credentials: Group Policy Preferences|T1552.006]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Passwords in SYSVOL & Group Policy Preferences]]'
commands:
  - '[[commands/findstr-search-sysvol-files-for-password]]'
  - '[[commands/findstr-search-gpp-xml-for-cpassword]]'
  - '[[commands/openssl-decrypt-gpp-cpassword]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Extract-and-Decrypt-GPP-Passwords-from-SYSVOL

## Summary

This procedure demonstrates how to search for and extract unsecured passwords stored in SYSVOL shares, particularly within Group Policy Preferences (GPP) XML files. It involves scanning for exposed credentials and decrypting the weakly encrypted 'cpassword' attributes using a known AES-256-CBC key, allowing attackers to obtain domain credentials for lateral movement and privilege escalation in Active Directory environments.

## Description

In legacy Windows Active Directory setups, Group Policy Preferences (GPP) allowed administrators to store passwords in XML files within the SYSVOL share, which is readable by all authenticated domain users. These passwords were base64-encoded and encrypted with AES-256-CBC using a fixed, publicly known key and zero IV, making them easily decryptable. This procedure targets these unsecured credentials to recover plaintext passwords, often for service accounts or local admins, enabling further attacks like pass-the-hash or remote execution. It requires domain authentication and is most effective against unpatched or misconfigured domains where GPP passwords have not been removed (a practice Microsoft recommended since 2012).

## Requirements

1. Authenticated access to the Active Directory domain (e.g., valid domain user credentials).
2. Network access to the SYSVOL share (typically via SMB on port 445).
3. Windows command-line tools (cmd.exe or PowerShell) for searching, or Bash with OpenSSL for decryption.
4. Knowledge of the target domain's FQDN.

## Defense

- Remove all GPP password configurations from SYSVOL XML files and disable the feature via Group Policy.
- Implement Microsoft's Local Administrator Password Solution (LAPS) for managing local admin passwords.
- Monitor SYSVOL access and changes using tools like Microsoft Advanced Group Policy Management (AGPM) or file integrity monitoring.
- Enable auditing for SMB shares and XML file modifications in SYSVOL.
- Regularly audit GPOs for exposed credentials using scripts or tools like PowerSploit.

## Objectives

1. Identify files in SYSVOL containing potential passwords.
2. Locate and extract 'cpassword' values from GPP XML files.
3. Decrypt base64-encoded cpasswords to obtain plaintext credentials.
4. Use recovered credentials for lateral movement or privilege escalation.

## Instructions

### Step 1: Search SYSVOL for Exposed Passwords

**Context**: Begin by scanning the SYSVOL Policies directory for any files containing the string 'password', which may reveal inadvertently stored credentials in configuration files accessible to authenticated users.

**Command** ([[commands/findstr-search-sysvol-files-for-password]]):
```cmd
findstr /si password \\%_DOMAIN%\SYSVOL\%_DOMAIN%\Policies\*.*
```

> This command recursively searches all files in the SYSVOL Policies folder for the term 'password' in a case-insensitive manner (/si flags). Replace %_DOMAIN% with the target domain name (e.g., contoso.com). It helps identify potential credential leaks without needing to navigate directories manually. Review the output for context around matches, such as in XML or INI files.

### Step 2: Search GPP XML Files for cpassword Attributes

**Context**: Focus on Group Policy XML files, where 'cpassword' attributes specifically indicate encrypted passwords from GPP. This step targets the vulnerability in unremediated environments.

**Command** ([[commands/findstr-search-gpp-xml-for-cpassword]]):
```cmd
findstr /S /I cpassword \\%_FQDN%\sysvol\%_FQDN%\policies\*.xml
```

> Execute this in cmd.exe or PowerShell to search subdirectories (/S) case-insensitively (/I) for 'cpassword' in all XML files under the sysvol policies path. Replace %_FQDN% with the fully qualified domain name (e.g., contoso.com). The output will list files and lines containing cpassword values, which appear as base64 strings in attributes like <Properties ... cpassword="BASE64STRING" />. Extract these strings for the next step.

### Step 3: Decrypt the cpassword Value

**Context**: Use the known Microsoft-provided AES key to decrypt the base64-decoded cpassword, revealing the plaintext password for use in further attacks.

**Command** ([[commands/openssl-decrypt-gpp-cpassword]]):
```bash
echo '%_CPASSWORD_BASE64%' | base64 -d | openssl enc -d -aes-256-cbc -K 4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b -iv 0000000000000000
```

> Run this in a Bash environment (e.g., on Kali Linux) after obtaining a cpassword from Step 2. Replace %_CPASSWORD_BASE64% with the extracted base64 string (e.g., '5OPdEKwZSf7dYAvLOe6RzRDtcvT/wCP8g5RqmAgjSso='). The command first base64-decodes the input, then decrypts it using the fixed 32-byte key and zero IV. If successful, it outputs the plaintext password directly to stdout. Test with known examples to verify setup.
