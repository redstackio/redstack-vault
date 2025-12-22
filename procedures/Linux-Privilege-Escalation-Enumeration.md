---
id: 12668a66-533e-42d3-8f0a-6d59938c404d
name: Linux-Privilege-Escalation-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.422827+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1556]]'
  - >-
    [[techniques/Abuse Elevation Control Mechanism: Sudo and Sudo
    Caching|T1548.003]]
  - '[[techniques/Setuid and Setgid|T1548.001]]'
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/wget-download-linpeas-script]]'
  - '[[commands/curl-download-linpeas-script]]'
  - '[[commands/run-linpeas-all-checks]]'
  - '[[commands/run-linpeas-superfast-stealth]]'
  - '[[commands/run-linpeas-with-password]]'
  - '[[commands/wget-download-lse-script]]'
  - '[[commands/curl-download-lse-script]]'
  - '[[commands/run-lse-level-1]]'
  - '[[commands/run-lse-level-2]]'
  - '[[commands/run-linenum-stealth-keyword-report-thorough]]'
platforms:
  - Linux
tools:
  - '[[tools/linPEAS]]'
  - '[[tools/linux-smart-enumeration]]'
  - '[[tools/LinEnum]]'
validated: true
---

# Linux-Privilege-Escalation-Enumeration

## Summary

Linux Privilege Escalation Enumeration is a procedure to systematically identify potential privilege escalation vectors on a Linux system by running specialized enumeration scripts like LinPEAS, Linux Smart Enumeration (LSE), and LinEnum. These tools scan for misconfigurations, weak permissions, vulnerable services, and other issues that could allow a low-privileged user to gain root or higher privileges, making it essential for penetration testing and red team assessments of Linux environments.

## Description

This procedure targets Linux systems to uncover paths for privilege escalation through automated enumeration. It leverages open-source scripts that check for common vectors such as SUID binaries, sudo misconfigurations, writable files in critical paths, cron jobs, and service vulnerabilities. The approach is non-destructive and focuses on discovery without exploitation, providing output that highlights potential issues for further manual verification. It is typically used after initial access to a low-priv user account, helping assess the system's security posture in real-world scenarios like CTFs, pentests, or compliance audits. Expected outcomes include reports listing exploitable weaknesses, which can inform targeted escalation attempts.

## Requirements

1. Shell access to a Linux system as a low-privileged user (e.g., via SSH or initial foothold).
2. Internet connectivity to download scripts (or pre-downloaded scripts transferred via other means).
3. Write permissions in a temporary directory (e.g., /tmp) to store and execute scripts.
4. Basic bash knowledge to interpret outputs and troubleshoot execution issues.

## Defense

- Harden Linux systems by regularly auditing and removing unnecessary SUID binaries, enforcing strict sudo policies via visudo, and using tools like AppArmor or SELinux to limit privilege escalations.
- Monitor for script downloads and executions in logs (e.g., /var/log/auth.log, bash history) using SIEM or file integrity monitoring.
- Implement least privilege by running services as non-root users and disabling unnecessary cron jobs; scan for vulnerabilities with tools like Lynis or OpenSCAP.

## Objectives

1. Discover misconfigurations and vulnerabilities enabling privilege escalation from user to root.
2. Generate actionable reports on system weaknesses for security assessment.
3. Verify the presence of common Linux priv esc vectors without triggering alerts.

## Instructions

### Step 1: Download and Prepare LinPEAS Script

**Context**: LinPEAS (Linux Privilege Escalation Awesome Script) is a comprehensive enumeration tool that checks for a wide range of priv esc vectors. Download it first to avoid repeated fetches.

Use [[commands/wget-download-linpeas-script]] or [[commands/curl-download-linpeas-script]] to retrieve the latest version:

```bash
wget "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -O linpeas.sh
```

or

```bash
curl "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -o linpeas.sh
```

Make it executable with `chmod +x linpeas.sh`. This step ensures you have the tool ready for execution.

### Step 2: Run LinPEAS in All Checks Mode

**Context**: This mode performs a deep scan of the system, including file permissions, processes, and network configs, to identify potential escalations. Use it when time allows for thoroughness.

Execute [[commands/run-linpeas-all-checks]]:

```bash
./linpeas.sh -a
```

Expected output includes color-coded sections highlighting yellow/orange/red findings like writable /etc/passwd or SUID binaries.

### Step 3: Run LinPEAS in Superfast and Stealth Mode

**Context**: For quicker, less detectable enumeration, this bypasses slow checks and avoids disk writes, ideal in monitored environments.

Execute [[commands/run-linpeas-superfast-stealth]]:

```bash
./linpeas.sh -s
```

Expected output is a condensed report focusing on high-impact issues without temporary files.

### Step 4: Run LinPEAS with Password for Sudo Checks

**Context**: If you have a candidate password, this enhances sudo and user bruteforce checks to test cached credentials.

Execute [[commands/run-linpeas-with-password]] (replace $_PASSWORD with your guess):

```bash
./linpeas.sh -P $_PASSWORD
```

Expected output includes sudo -l results and any successful bruteforces.

### Step 5: Download and Prepare LSE Script

**Context**: Linux Smart Enumeration (LSE) focuses on smart, level-based info dumps for priv esc hints.

Use [[commands/wget-download-lse-script]] or [[commands/curl-download-lse-script]]:

```bash
wget "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -O lse.sh
```

Make executable with `chmod +x lse.sh`.

### Step 6: Run LSE at Level 1 for Interesting Findings

**Context**: Level 1 provides targeted output on priv esc-relevant info like SUID and cron jobs.

Execute [[commands/run-lse-level-1]]:

```bash
./lse.sh -l1
```

Expected output lists potential vectors like vulnerable services or weak perms.

### Step 7: Run LSE at Level 2 for Full Dump

**Context**: Level 2 exhaustively enumerates the system for complete assessment.

Execute [[commands/run-lse-level-2]]:

```bash
./lse.sh -l2
```

Expected output is a detailed dump; pipe to file if needed: `./lse.sh -l2 > lse_full.txt`.

### Step 8: Run LinEnum with Stealth, Keyword Search, Reporting, and Thorough Tests

**Context**: LinEnum performs scripted checks with options for stealth and reporting; use for customizable enumeration.

First, download LinEnum if not present (similar to above, from https://github.com/rebootuser/LinEnum). Then execute [[commands/run-linenum-stealth-keyword-report-thorough]] (replace $_KEYWORD with search term like 'sudo', $_REPORT_NAME with output file):

```bash
./LinEnum.sh -s -k $_KEYWORD -r $_REPORT_NAME -e /tmp/ -t
```

Expected output is a report in /tmp/$_REPORT_NAME.html or text, searchable for keywords.
