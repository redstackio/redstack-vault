---
type: procedure
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[cme-smb-enable-rdp]]'
sub_techniques: []
tags:
  - Active Directory Attacks
  - Kerberoasting
commands:
  - '[[commands/impacket-getuserspns-request]]'
  - '[[commands/crackmapexec-ldap-kerberoast]]'
  - '[[commands/rubeus-kerberoast-stats]]'
  - '[[commands/rubeus-kerberoast-with-creds]]'
  - '[[commands/rubeus-kerberoast-tgtdeleg]]'
  - '[[commands/rubeus-kerberoast-rc4opsec]]'
  - '[[commands/powerview-request-spnticket]]'
  - '[[commands/bifrost-ask-tgs-kerberoast]]'
  - '[[commands/hashcat-crack-krb5tgs]]'
  - '[[commands/john-crack-krb5tgs]]'
tools:
  - '[[tools/Rubeus]]'
  - '[[tools/Impacket]]'
  - '[[tools/CrackMapExec]]'
  - '[[tools/Hashcat]]'
  - '[[tools/John]]'
platforms:
  - Windows
  - Active Directory
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Kerberoasting-with-Rubeus

## Summary

Kerberoasting is a credential access technique that targets service accounts in Active Directory by requesting Kerberos Ticket Granting Service (TGS) tickets for Service Principal Names (SPNs). These tickets are encrypted with the service account's password hash, which can be cracked offline if the password is weak. This procedure demonstrates how to perform Kerberoasting using the Rubeus tool on a compromised Windows domain-joined host, including enumeration, ticket extraction, and offline cracking. It is effective for escalating privileges from a standard domain user to service accounts with higher access.

## Description

In Kerberos authentication, service accounts registered with SPNs allow any authenticated domain user to request TGS tickets for those services. The ticket's ciphertext is encrypted using the service account's NTLM hash (often RC4 for legacy compatibility), making it vulnerable to offline brute-force attacks. Rubeus simplifies this by automating SPN enumeration and TGS requests while offering opsec-focused options like using RC4 tickets or TGT delegation to evade detection. This procedure assumes initial access with valid domain credentials and focuses on Windows environments. Success enables lateral movement, data exfiltration, or further privilege escalation using recovered service account passwords. Map to MITRE ATT&CK Tactic TA0006 (Credential Access) and Technique T1558.003 (Kerberoasting).

## Requirements

1. Valid domain user credentials (low-privilege user sufficient for TGS requests).
2. Access to a domain-joined Windows machine (for Rubeus execution).
3. Rubeus.exe binary (compiled from source or downloaded; requires .NET Framework 4.0+).
4. Optional: Linux host for Impacket or CrackMapExec if cross-platform enumeration is needed.
5. Hash cracking setup (GPU recommended for Hashcat; wordlists like rockyou.txt).
6. Network access to Domain Controller (ports 88/TCP for Kerberos, 389/TCP for LDAP).

## Defense

- Enforce strong, unique passwords (25+ characters) for service accounts and rotate regularly using Managed Service Accounts (MSAs).
- Disable legacy encryption types like RC4 (msDS-SupportedEncryptionTypes=24 for AES only) via Group Policy.
- Monitor Kerberos logs for excessive TGS requests (Event ID 4769) from unusual users or to SPNs; use tools like Microsoft ATA or Splunk for anomaly detection.
- Limit SPN registrations to necessary services and audit write permissions on servicePrincipalName attribute.
- Implement Least Privilege: Restrict TGS requests via Kerberos Armoring (FAST) or fine-grained password policies.

## Objectives

1. Enumerate SPNs associated with service accounts in the domain.
2. Request and export TGS tickets in crackable format (e.g., $krb5tgs$ hashes).
3. Crack the ticket encryption offline to recover plaintext service account passwords.
4. Validate and use recovered credentials for further post-exploitation (e.g., lateral movement).

## Instructions

### Step 1: Enumerate SPNs Using Impacket

**Context**: Before requesting tickets, identify service accounts with SPNs. Impacket's GetUserSPNs.py queries LDAP for SPNs and can directly request TGS tickets, providing hashes for cracking. This step is useful if Rubeus is not yet deployed; perform from a Linux host with domain creds.

**Command** ([[commands/impacket-getuserspns-request]]):
```bash
GetUserSPNs.py DOMAIN/USER:PASSWORD -dc-ip DC_IP -request -outputfile spn_hashes.txt
```

> This command authenticates to the DC, enumerates users with SPNs via LDAP, and requests TGS tickets for each, outputting crackable hashes in Hashcat format. The -request flag triggers ticket acquisition; replace DOMAIN/USER:PASSWORD with your creds and DC_IP with the controller's IP. If using NTLM hash, format as DOMAIN/USER:HASH.

**Expected Output**: Table of SPNs, user details (e.g., PasswordLastSet), and hashes like `$krb5tgs$23$*user$DOMAIN$SPN*$<hash>$<checksum>`. Save to file for cracking.

**Success Indicators**:
- Hashes extracted without authentication errors.
- At least one SPN found (e.g., MSSQLSvc, HTTPSvc).
- No Kerberos pre-auth failures in output.

### Step 2: Enumerate and Kerberoast Using CrackMapExec

**Context**: For broader enumeration, use CrackMapExec to query LDAP and perform Kerberoasting across the domain. This integrates SPN discovery and ticket requests, outputting hashes directly. Useful for initial scouting before Rubeus.

**Command** ([[commands/crackmapexec-ldap-kerberoast]]):
```bash
crackmapexec ldap DC_IP -u USER -p PASSWORD --kdcHost DC_IP --kerberoast output_hashes.txt
```

> Authenticates via LDAP to the DC, enumerates SPNs, requests TGS tickets, and saves hashes to output_hashes.txt. The --kerberoast flag enables ticket extraction; --kdcHost specifies the Kerberos server.

**Expected Output**: Host details (OS, domain) followed by hashes like `$krb5tgs$23$*serviceuser$DOMAIN$SPN*$<hash>`. Example: LDAP 10.0.2.11 389 dc01 [*] Windows ... $krb5tgs$23$*john.doe$lab.local$MSSQLSvc/dc01.lab.local~1433*...

**Success Indicators**:
- LDAP connection successful (no signing errors).
- Multiple hashes outputted to file.
- No 'Access Denied' for TGS requests.

### Step 3: Gather Kerberoasting Stats with Rubeus

**Context**: On the Windows host, use Rubeus to analyze the domain for vulnerable accounts (e.g., RC4 support, old password sets). This informs targeting without immediate ticket requests, reducing noise.

**Command** ([[commands/rubeus-kerberoast-stats]]):
```cmd
Rubeus.exe kerberoast /stats
```

> Runs without credentials if executed with current user context (assumes domain auth). Outputs counts of encryption types and password ages.

**Expected Output**: Tables like | Supported Encryption Type | Count | (e.g., RC4_HMAC_DEFAULT: 50) and | Password Last Set Year | Count | (e.g., 2018: 20). Identifies weak targets (pre-2020 passwords, RC4).

**Success Indicators**:
- Stats show RC4-enabled accounts (>0 count).
- Old passwords identified for prioritization.
- No domain connection errors.

### Step 4: Perform Basic Kerberoasting with Rubeus Using Credentials

**Context**: Request TGS tickets for all SPNs using provided credentials. This exports hashes to a file for offline cracking. Use if current session lacks sufficient perms.

**Command** ([[commands/rubeus-kerberoast-with-creds]]):
```cmd
Rubeus.exe kerberoast /creduser:DOMAIN\USER /credpassword:PASSWORD /outfile:hashes.txt
```

> Specifies alternate creds for auth; requests tickets for RC4 by default. /outfile saves in Hashcat format.

**Expected Output**: Progress messages and hashes written to hashes.txt, e.g., $krb5tgs$23$*svcacct$DOMAIN$HTTP/svcserver.domain$...

**Success Indicators**:
- Tickets requested successfully (no 'KRB-ERROR').
- File populated with 5+ hashes.
- Cracking viable (RC4 etype 23).

### Step 5: Advanced Kerberoasting with TGT Delegation

**Context**: For AES-enabled accounts, use TGT delegation to request RC4 tickets anyway, bypassing stronger encryption. This improves crackability but increases detection risk.

**Command** ([[commands/rubeus-kerberoast-tgtdeleg]]):
```cmd
Rubeus.exe kerberoast /tgtdeleg /outfile:aes_hashes.txt
```

> Leverages S4U2Self/S4U2Proxy for delegation; requests RC4 even for AES accounts.

**Expected Output**: Hashes in RC4 format despite AES config, saved to file.

**Success Indicators**:
- Delegation succeeds (requires compatible DC).
- Hashes extracted for previously protected accounts.
- No privilege errors.

### Step 6: Opsec-Focused Kerberoasting with RC4

**Context**: Enumerate and roast only non-AES accounts using RC4 opsec mode to minimize logs. Ideal for stealthy operations.

**Command** ([[commands/rubeus-kerberoast-rc4opsec]]):
```cmd
Rubeus.exe kerberoast /rc4opsec /outfile:opsec_hashes.txt
```

> Uses tgtdeleg trick for RC4-only; skips AES to avoid stronger hashes.

**Expected Output**: Targeted RC4 hashes only.

**Success Indicators**:
- Fewer but crackable hashes.
- Reduced event log noise.

### Step 7: Request Specific SPN Ticket with PowerView

**Context**: For targeted roasting (e.g., known MSSQL SPN), use PowerView's Request-SPNTicket to get a single TGS. Useful after enumeration.

**Command** ([[commands/powerview-request-spnticket]]):
```powershell
Request-SPNTicket -SPN "MSSQLSvc/targetserver.domain.local"
```

> PowerShell cmdlet; exports ticket to current session or file. Requires PowerView loaded.

**Expected Output**: Ticket requested; hash can be exported via other tools.

**Success Indicators**:
- Ticket acquired without errors.
- Hash exportable for cracking.

### Step 8: Crack Extracted Hashes with Hashcat

**Context**: Offline crack the $krb5tgs$23 hashes using dictionary attack. Mode 13100 for RC4 Kerberos TGS.

**Command** ([[commands/hashcat-crack-krb5tgs]]):
```bash
hashcat -m 13100 -a 0 hashes.txt rockyou.txt --force
```

> -m 13100 for etype 23; -a 0 dictionary mode. Use GPU for speed.

**Expected Output**: Cracked passwords like svcacct:Password123.

**Success Indicators**:
- Passwords recovered (check potfile).
- Hit rate >0% on wordlist.

### Step 9: Alternative Cracking with John the Ripper

**Context**: If Hashcat unavailable, use John for parallel cracking with forking.

**Command** ([[commands/john-crack-krb5tgs]]):
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --fork=4 --format=krb5tgs hashes.txt
```

> --format=krb5tgs for Kerberos; --fork for multi-core.

**Expected Output**: Cracked hashes shown post-run.

**Success Indicators**:
- Output like password (user@host).
- Show --format=krb5tgs for status.

### Step 10: Optional - Targeted Kerberoasting for Users Without SPNs

**Context**: If write perms on servicePrincipalName exist, temporarily set SPNs on users without them, roast, then remove. Use Impacket's targetedKerberoast.py.

**Instructions**: Prepare users.txt with targets. Run:
```bash
targetedKerberoast.py -d DOMAIN -u USER -p PASSWORD --dc-ip DC_IP -U users.txt -o targeted_hashes.txt
```

> Abuses write perms; requests TGS after temp SPN set, then deletes.

**Expected Output**: Hashes for non-SPN users.

**Success Indicators**:
- Temp SPN set/removed without alerts.
- Additional hashes from regular users.
