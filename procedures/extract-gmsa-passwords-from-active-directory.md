---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Extract NT hash from the Active Directory]]'
  - '[[tags/Reading GMSA Password]]'
commands:
  - '[[commands/run-gmsadumper-to-dump-gmsa-info]]'
  - '[[commands/run-gmsapasswordreader-to-retrieve-gmsa-password]]'
  - '[[commands/convert-ad-managed-password-blob-to-nt-hash]]'
tools:
  - '[[tools/gmsadumper]]'
  - '[[tools/gmsapasswordreader]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Extract GMSA Passwords from Active Directory

## Summary

This procedure extracts Group Managed Service Account (GMSA) passwords from Active Directory, allowing attackers to obtain credentials for service accounts that can be used across multiple domain-joined hosts. GMSAs provide automatic password management, but their encrypted passwords stored in the msDS-ManagedPassword attribute can be queried and decrypted with appropriate access, enabling privilege escalation or lateral movement.

## Description

Group Managed Service Accounts (GMSAs) are domain accounts designed for services, with passwords automatically rotated and managed by Active Directory. Unlike regular service accounts, GMSAs do not require manual password updates and can be delegated to specific computers. However, the current password is stored in an encrypted blob in the msDS-ManagedPassword attribute of the service account object. An attacker with authenticated access to Active Directory can query this attribute using LDAP or PowerShell, then decrypt the blob to retrieve the cleartext password or NT hash. This technique is useful in post-exploitation scenarios for credential dumping, especially when targeting service accounts with elevated privileges. The procedure covers multiple methods: using a dedicated C# tool for direct password retrieval, a Python dumper for extracting blobs, and native PowerShell for decryption. Success depends on the attacker's permissions to read service account attributes; domain admin or equivalent access simplifies this, but lower-privileged accounts may work if attribute reads are not restricted.

## Requirements

1. Authenticated access to the Active Directory domain (e.g., valid domain user credentials).
2. Network connectivity to a domain controller or LDAP server.
3. PowerShell with ActiveDirectory module installed (for the native method) or the specified tools (gMSADumper and GMSAPasswordReader).
4. Permissions to query service account objects and read the msDS-ManagedPassword attribute (may require delegated rights or higher privileges).

## Defense

- Implement least privilege access to Active Directory: Restrict read permissions on msDS-ManagedPassword to only necessary service accounts and admins using ACLs.
- Enable advanced auditing on Active Directory for attribute reads and LDAP queries; monitor for anomalous access to service account objects.
- Use protected users groups and fine-grained password policies to limit GMSA exposure; regularly rotate and review GMSA delegations.
- Deploy tools like Microsoft Defender for Identity to detect credential dumping attempts and unusual LDAP queries.

## Objectives

1. Retrieve the encrypted password blob for a target GMSA from Active Directory.
2. Decrypt the blob to obtain the cleartext password or NT hash.
3. Use the extracted credentials for lateral movement, privilege escalation, or accessing restricted resources.

## Instructions

### Step 1: Retrieve GMSA Password Using GMSAPasswordReader

**Context**: This step uses a dedicated tool to directly query and decrypt the GMSA password for a specified account. It authenticates to AD and outputs the cleartext password, which is useful when you know the exact service account name and have sufficient read permissions. This method is quick but requires the tool to be executed on a domain-joined Windows machine.

**Command** ([[commands/run-gmsapasswordreader-to-retrieve-gmsa-password]]):
```powershell
GMSAPasswordReader.exe --accountname SVC_SERVICE_ACCOUNT
```

> This command runs the GMSAPasswordReader executable, specifying the target GMSA account name. It connects to the current domain context, retrieves the msDS-ManagedPassword, decrypts it using the machine's key, and displays the password. If the tool lacks permissions, it will error with access denied.

### Step 2: Dump GMSA Information Using gMSADumper

**Context**: If direct password retrieval fails or you need to enumerate multiple GMSAs, use this Python tool to dump detailed information including password blobs from AD. This step authenticates with provided credentials and queries LDAP for all GMSA objects, extracting attributes like managed passwords. It's ideal for reconnaissance to identify valuable service accounts before targeted extraction.

**Command** ([[commands/run-gmsadumper-to-dump-gmsa-info]]):
```bash
python3 gMSADumper.py -u User -p Password1 -d domain.local
```

> The command authenticates as the specified user to the domain and dumps GMSA details to the console, including account names, blobs, and other attributes. Review the output for target accounts, then use the blob in subsequent decryption steps. Errors may occur if the user lacks LDAP read access.

### Step 3: Convert Managed Password Blob to NT Hash Using PowerShell

**Context**: For manual decryption without external tools, use native PowerShell cmdlets to fetch the password blob for a specific GMSA and convert it to an NT hash. This requires the ActiveDirectory module and read access to the target account. The resulting hash can be cracked offline or used directly with tools like Pass-the-Hash for authentication.

**Command** ([[commands/convert-ad-managed-password-blob-to-nt-hash]]):
```powershell
$gmsa = Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties 'msDS-ManagedPassword'
$blob = $gmsa.'msDS-ManagedPassword'
$mp = ConvertFrom-ADManagedPasswordBlob $blob
$hash1 = ConvertTo-NTHash -Password $mp.SecureCurrentPassword
```

> This multi-line PowerShell script retrieves the service account object, extracts the blob, parses it into a managed password object, and converts the secure password to an NT hash stored in $hash1. Output the variable (e.g., Write-Output $hash1) to view the hash. This method works on domain-joined systems with RSAT tools installed.
