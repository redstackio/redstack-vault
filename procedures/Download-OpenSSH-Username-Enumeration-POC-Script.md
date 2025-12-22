---
id: proc-001
tags:
  - poc-download
  - exploit-acquisition
type: procedure
tools:
  - '[[tools/POC-py-for-CVE-2016-6210]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:58.945Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Download-OpenSSH-Username-Enumeration-POC-Script

## Summary

This procedure involves acquiring the Python proof-of-concept script for exploiting CVE-2016-6210, a timing-based username enumeration vulnerability in OpenSSH 7.2p2, from a public exploit database to enable subsequent SSH authentication timing attacks.

## Description

The procedure targets the initial setup phase of the attack by downloading POC.py from Exploit-DB. This script performs SSH connection attempts with a large password to measure response times, exploiting the discrepancy where existing usernames cause longer processing delays. It is essential for reconnaissance on vulnerable SSH servers like those on Nextcloud subdomains. Prerequisites include internet access and a basic understanding of exploit repositories; no special privileges are needed.

## Requirements

1. Internet connectivity to access Exploit-DB
2. Web browser or wget/curl for download
3. Local directory for storing the script

## Defense

Defensive measures and detection strategies:

- Monitor downloads from exploit databases via web proxy logs
- Implement network access controls to block known exploit sites
- Use endpoint detection to flag suspicious Python script executions

## Objectives

1. Acquire the POC script for timing-based enumeration
2. Verify script availability and integrity
3. Prepare for username list integration and execution

## Instructions

### Step 1: Access Exploit-DB

**Context**: Navigate to the CVE-2016-6210 exploit page to locate and download the script.

No command required; use a browser to visit https://www.exploit-db.com/exploits/40136 and download POC.py.

> Manually save the file as POC.py in your working directory.

### Step 2: Verify Download

**Context**: Ensure the script is correctly downloaded and executable.

**Command** (ls-check-poc):
```bash
ls -la POC.py
```

> This lists the file details; confirm size (~2-5 KB) and permissions. Make executable if needed: chmod +x POC.py.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/ls-check-poc]]

## Tools Used

- [[tools/POC-py-for-CVE-2016-6210]]

## Tags

- poc-download
- exploit-acquisition
