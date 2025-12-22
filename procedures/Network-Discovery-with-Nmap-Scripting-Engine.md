---
id: 412f7248-33a0-4e65-bf39-eb5b527d64a1
name: Network-Discovery-with-Nmap-Scripting-Engine
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:22.067874+00:00'
updated_at: '2023-04-10T20:25:05.010903+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Network Discovery]]'
  - '[[tags/Nmap]]'
commands:
  - '[[commands/list-nmap-scripts]]'
  - '[[commands/nmap-run-default-scripts]]'
  - '[[commands/nmap-http-enum-script]]'
  - '[[commands/nmap-smb-enum-users-script]]'
platforms:
  - Linux
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Network-Discovery-with-Nmap-Scripting-Engine

## Summary

This procedure uses the Nmap Scripting Engine (NSE) to perform network discovery, identifying hosts, services, vulnerabilities, and misconfigurations on a target network. It automates reconnaissance by running default or specific NSE scripts to enumerate services like HTTP directories or SMB users, providing actionable intelligence for further attacks.

## Description

Network discovery with NSE involves leveraging Nmap's extensible scripting framework to go beyond basic port scanning. Attackers use this to map the network, detect running services, and probe for weaknesses such as exposed directories or user accounts. For example, the http-enum script discovers hidden web paths, while smb-enum-users identifies domain users via SMB. This technique is ideal in early reconnaissance phases on internal or external networks, assuming the attacker has network access. It maps to MITRE ATT&CK's Discovery tactic, specifically Network Service Scanning, and helps identify entry points for exploitation.

## Requirements

1. Network access to the target (e.g., direct connectivity or via pivot).
2. Nmap installed with NSE support (version 7.0+ recommended).
3. Administrative privileges on the attacker's machine for raw socket access.
4. Optional: Authentication credentials for authenticated scans (e.g., SMB).

## Defense

- Deploy network segmentation and firewalls to limit reconnaissance visibility.
- Use intrusion detection systems (IDS) to monitor for Nmap signatures, such as unusual TCP/UDP probes.
- Regularly audit and patch services to reduce exposed attack surfaces.
- Implement logging on services like SMB and HTTP to detect enumeration attempts.

## Objectives

1. Identify active hosts and open services on the target network.
2. Enumerate specific details like web directories or user accounts using NSE scripts.
3. Gather intelligence on vulnerabilities for targeted follow-up attacks.
4. Output results in parseable formats for analysis.

## Instructions

### Step 1: List Available NSE Scripts

**Context**: Begin by inventorying the available NSE scripts to understand what discovery options are present. This helps select appropriate scripts for the target environment, such as HTTP or SMB enumeration.

**Command** ([[commands/list-nmap-scripts]]):
```bash
ls /usr/share/nmap/scripts/
```

> This command lists all NSE scripts in the default directory. Review the output to identify relevant scripts like http-enum.nse or smb-enum-users.nse.

### Step 2: Run Default NSE Scripts on Target

**Context**: Execute Nmap with default scripts to perform a broad discovery scan, detecting common services and basic vulnerabilities without specifying individual scripts. Use this for an initial overview.

**Command** ([[commands/nmap-run-default-scripts]]):
```bash
nmap -sC $_TARGET
```

> The -sC flag runs the default script set, which includes version detection and basic vuln checks. If the target responds with service banners or script outputs, it indicates successful discovery.

### Step 3: Enumerate HTTP Directories with http-enum Script

**Context**: Target web servers to discover hidden directories and files, which may reveal sensitive information like admin panels or source code repositories. This is useful against Apache or IIS servers.

**Command** ([[commands/nmap-http-enum-script]]):
```bash
nmap --script http-enum -v $_TARGET -p80 -oN http-enum.nmap
```

> The http-enum script probes for common paths. Verbose (-v) output shows progress, and -oN saves results to a file. If directories like /phpmyadmin/ are found, it suggests potential misconfigurations.

### Step 4: Enumerate SMB Users with smb-enum-users Script

**Context**: On Windows or Samba shares, enumerate user accounts to identify valid logins for brute-force or pass-the-hash attacks. This requires port 445 open and may need credentials for deeper access.

**Command** ([[commands/nmap-smb-enum-users-script]]):
```bash
nmap --script smb-enum-users -p 445 $_TARGET
```

> The smb-enum-users.nse script queries the target for user RIDs and names. Success is indicated by a list of accounts; if authentication is required and fails, provide creds via --script-args.

## Expected Output

Successful execution produces Nmap output with host details, open ports, and script results. For example:

- Default scripts: Service versions and basic vuln info.
- http-enum: Paths like "/phpmyadmin/: phpMyAdmin".
- smb-enum-users: User lists like "METASPLOITABLE\msfadmin (RID: 3000)".

Verify by parsing output files or checking for non-empty script sections.
