---
id: 0928b1c7-8972-4021-9755-8547049a79ad
name: Password-Spraying-with-Pre-Generated-Passwords
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.304382+00:00'
updated_at: '2023-04-10T20:25:55.299475+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Password spraying]]'
  - '[[tags/Spray a pre-generated passwords list]]'
commands:
  - '[[commands/crackmapexec-smb-spray-with-password-mask]]'
  - '[[commands/invoke-domain-password-spray-single-password]]'
  - '[[commands/invoke-domain-password-spray-with-user-and-password-lists]]'
  - '[[commands/invoke-smb-auto-brute-with-lists]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/DomainPasswordSpray]]'
  - '[[tools/Invoke-SMBAutoBrute]]'
validated: true
---

# Password-Spraying-with-Pre-Generated-Passwords

## Summary

This procedure demonstrates password spraying against an Active Directory environment using a pre-generated list of passwords to attempt authentication across multiple user accounts. It leverages tools like CrackMapExec for SMB spraying with generated masks, DomainPasswordSpray for domain-wide spraying, and Invoke-SMBAutoBrute for automated SMB brute forcing, aiming to identify weak or common passwords without triggering account lockouts.

## Description

Password spraying targets common passwords across many accounts to gain initial access to Active Directory domains. Unlike traditional brute forcing, it uses a small set of likely passwords (pre-generated from wordlists, masks, or known patterns like seasonal changes) against numerous usernames, reducing detection risk from lockout thresholds. This procedure covers automated execution via command-line tools, suitable for red team engagements where domain usernames are known (e.g., from prior enumeration). Success compromises user accounts for lateral movement, but requires careful throttling to evade monitoring. Target environments include Windows domains with SMB and Kerberos authentication.

## Requirements

1. Domain usernames (e.g., from enumeration via [[procedures/Enumerate-Domain-Users]] or a user list file).
2. Pre-generated password list or mask (e.g., common passwords like 'Summer2021!' or generated via tools like mp64.bin).
3. Network access to target domain controllers or SMB shares (ports 445, 88 open).
4. Installed tools: CrackMapExec, DomainPasswordSpray PowerShell module, and Invoke-SMBAutoBrute script.
5. Valid low-privilege credentials or pivot host for execution.

## Defense

- Implement strong password policies requiring complexity and regular rotation, combined with multi-factor authentication (MFA) to block sprayed credentials.
- Monitor authentication logs (Event ID 4625 for failures) for patterns of distributed failed logins across accounts.
- Deploy account lockout policies with low thresholds (e.g., 5 attempts) and anomaly detection via SIEM tools like Splunk or ELK.
- Use network segmentation to isolate domain controllers and enable just-in-time access controls.

## Objectives

1. Authenticate successfully with one or more domain accounts using sprayed passwords.
2. Identify valid credentials for further post-exploitation (e.g., lateral movement via [[procedures/Pass-the-Hash]]).
3. Minimize detection by limiting attempts per account and distributing over time.

## Instructions

### Step 1: Spray SMB Shares Using Generated Password Mask

**Context**: Use CrackMapExec to generate and spray passwords on-the-fly against SMB services in a target IP range. This step tests for weak SMB credentials using a mask to create variations (e.g., 'Pass@wor1a' to 'Pass@wor9a'), ideal when you have a base pattern but need variations.

**Command** ([[commands/crackmapexec-smb-spray-with-password-mask]]):

```bash
crackmapexec smb 10.0.0.1/24 -u Administrator -p `(./mp64.bin Pass@wor?l?a)`
```

> This command enumerates SMB shares and attempts authentication with generated passwords from the mask. The backticks execute mp64.bin to produce password candidates. Run from a Kali Linux host with CrackMapExec installed. Expected output includes GREEN for successful logins (e.g., 'Administrator:Pass@wor1a status: 0'). If no successes, adjust mask or IP range. Verify by checking for SMB share access post-success.

**Code Reference** ([[codes/crackmapexec-smb-spray-with-generated-mask]]): Embedded above for execution.

### Step 2: Perform Domain Password Spray with Single Common Password

**Context**: Spray a single common password (e.g., seasonal like 'Summer2021!') across all domain users to check for widespread reuse. This avoids lockouts by limiting attempts per user and is useful for quick validation of guessed passwords.

**Command** ([[commands/invoke-domain-password-spray-single-password]]):

```powershell
Invoke-DomainPasswordSpray -Password Summer2021!
```

> Load the DomainPasswordSpray module first (Import-Module DomainPasswordSpray.ps1). This sprays the password against all enumerated domain users via Kerberos pre-auth. Expected output: List of successful authentications (e.g., 'Valid credential found: user@domain.com:Summer2021!'). Monitor for lockout warnings; throttle if needed. Success confirmed by exported valid creds file.

### Step 3: Spray Domain with User and Password Lists

**Context**: For targeted spraying, use lists of usernames and passwords to attempt combinations systematically. This step handles larger datasets, saving results to a file for review, and includes domain specification for accurate targeting.

**Command** ([[commands/invoke-domain-password-spray-with-user-and-password-lists]]):

```powershell
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
```

> Prepare users.txt (one username per line) and passlist.txt (pre-generated passwords). Execute in PowerShell on a domain-joined or pivoted host. Expected output: Console summary of attempts and valid hits, plus sprayed-creds.txt with successes (format: username:password). If no output file, no valid creds found. Decision point: If lockout threshold approached, pause and resume later.

**Code Reference** ([[codes/domain-password-spray-invoke-with-single-and-lists]]): See module examples for variations.

### Step 4: Automate SMB Brute Force with Threshold

**Context**: Automate brute forcing against SMB using user and password lists, with a lockout threshold to prevent excessive failures. This is a fallback for specific high-value targets like admin accounts, focusing on efficiency.

**Command** ([[commands/invoke-smb-auto-brute-with-lists]]):

```powershell
Invoke-SMBAutoBrute -UserList "C:\ProgramData\admins.txt" -PasswordList "Password1, Welcome1, 1qazXDR%+" -LockoutThreshold 5 -ShowVerbose
```

> Run in PowerShell; ensure lists are accessible. This iterates combinations until threshold or success. Expected output: Verbose log of attempts, highlighting valid creds (e.g., 'Success: admin:Password1'). If verbose, shows failure counts per user. Success: Valid pairs for immediate use in tools like [[commands/psexec-remote-execution]].

**Code Reference** ([[codes/invoke-smb-auto-brute-with-password-lists]]): Embedded above.
