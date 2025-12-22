---
id: 47e95144-9812-403c-9c1d-5d1f8a073d9f
name: Azure AD Connect - Password Extraction via AD Sync Account DCSync
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.153460+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
  - >-
    [[sub-techniques/Security Account Manager|T1003.002 - Security Account
    Manager]]
tags:
  - '[[tags/Azure AD Connect]]'
  - '[[tags/Azure AD Connect - Password extraction]]'
  - '[[tags/Cloud - Azure]]'
commands:
  - '[[commands/git-clone-adconnectdump-repository]]'
  - '[[commands/adconnectdump-run-dcsync-with-ad-sync-account]]'
platforms:
  - Windows
  - Azure
tools:
  - '[[tools/adconnectdump]]'
validated: true
---

# Azure AD Connect - Password Extraction via AD Sync Account DCSync

## Summary

This procedure uses the Azure AD Connect synchronization account to perform a DCSync attack, extracting NTLM password hashes from the on-premises Active Directory's NTDS.dit file. It leverages the adconnectdump tool to access credentials stored in the Azure AD Sync database (ADSync.mdf), enabling offline cracking of hashes for potential privilege escalation or lateral movement.

## Description

Azure AD Connect synchronizes on-premises Active Directory with Azure AD, using a service account with replication privileges. An attacker with access to this AD Sync account can mimic domain controller replication (DCSync) to dump password hashes without direct DC access. The adconnectdump tool retrieves the AD Sync credentials from the local SQL database and uses them to query the NTDS.dit file over LDAP, outputting crackable NTLM hashes. This is effective in hybrid environments where the sync server has network access to domain controllers. Success allows offline brute-force attacks, compromising user accounts for further network traversal.

## Requirements

1. Compromised access to the Azure AD Connect server (local admin or equivalent to access ADSync.mdf).
2. Credentials for the AD Sync service account (username, domain, password).
3. Network access to a domain controller (LDAP port 389 or 636 open).
4. Path to the NTDS.dit file on the domain controller (typically C:\Windows\NTDS\NTDS.dit, but requires volume shadow copy or admin access to obtain).
5. Installed Python 3 and required dependencies (e.g., Impacket library for LDAP/DCSync).

## Defense

- Restrict AD Sync account permissions: Remove unnecessary replication rights and use Microsoft Identity Manager for just-in-time sync.
- Monitor AD Sync server for unauthorized access: Enable SQL auditing on ADSync.mdf and log replication requests on DCs.
- Implement password rotation and complexity: Use Azure AD Password Protection to block weak passwords and rotate sync account credentials regularly.
- Detect anomalous replication: Alert on DCSync-like queries from non-DC sources using tools like Microsoft ATA or SIEM rules for high-volume LDAP binds.

## Objectives

1. Retrieve AD Sync service account credentials from the local database.
2. Use those credentials to perform DCSync and extract NTLM hashes from NTDS.dit.
3. Output hashes in a format suitable for offline cracking with tools like Hashcat.
4. Enable compromise of domain user accounts for privilege escalation and lateral movement.

## Instructions

### Step 1: Clone the adconnectdump Repository

**Context**: Download the adconnectdump tool from GitHub, which contains the Python script needed to extract and use AD Sync credentials for DCSync.

**Command** ([[commands/git-clone-adconnectdump-repository]]):
```bash
git clone https://github.com/fox-it/adconnectdump
```

> This clones the repository to the current directory. Verify the clone by checking for the adconnectdump.py file. If git is unavailable, download the ZIP manually and extract it.

### Step 2: Navigate to the Tool Directory and Prepare Environment

**Context**: Change to the cloned directory and ensure Python dependencies are met. This sets up the environment for running the DCSync extraction.

**Instructions**: Run `cd adconnectdump` to enter the directory. Install dependencies if needed: `pip install -r requirements.txt` (includes Impacket for LDAP handling). Decision point: If on the Azure AD Connect server, ensure the script runs with sufficient privileges; otherwise, transfer the tool via secure means.

**Expected Output**: Successful directory change (prompt shows adconnectdump/) and no errors from pip install.

### Step 3: Execute DCSync Using AD Sync Credentials

**Context**: Run the adconnectdump.py script to automatically retrieve AD Sync credentials from ADSync.mdf and perform DCSync against the domain controller, dumping NTLM hashes.

**Command** ([[commands/adconnectdump-run-dcsync-with-ad-sync-account]]):
```bash
python adconnectdump.py -u $_USERNAME -d $_DOMAIN -p $_PASSWORD --ntds $_NTDS_PATH --ldap-ip $_DC_IP --ldap-port $_LDAP_PORT
```

> Replace placeholders with actual values (e.g., -u "MSOL_" -d "corp.local" -p "syncPass123" --ntds "C:\\Windows\\NTDS\\NTDS.dit" --ldap-ip "10.0.0.10" --ldap-port 389). The script first queries the local SQL database for sync credentials, then uses them for LDAP replication to extract hashes from NTDS.dit. If the NTDS path is remote, ensure SMB/LDAP access.

**Expected Output**: Output file (e.g., ntlm_hashes.txt) containing user:rid:lmhash:nthash format, such as "Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0". Errors may indicate invalid credentials or network issues.

### Step 4: Verify and Crack Extracted Hashes

**Context**: Confirm the dump succeeded and prepare for offline cracking to obtain plaintext passwords.

**Instructions**: Inspect the output file for valid hashes (look for :500: for admin RID). If hashes are extracted, use a tool like Hashcat for cracking: hashcat -m 1000 -a 0 hashes.txt wordlist.txt. Decision point: Prioritize high-value accounts (e.g., admins) based on RID.

**Expected Output**: List of extracted accounts and hashes; successful crack yields plaintext (e.g., "Password cracked: Administrator -> P@ssw0rd123").
