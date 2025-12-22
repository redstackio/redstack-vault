---
id: proc-dir-bruteforce-unprotected
tags:
  - recon
  - web-vuln
  - bruteforce
type: procedure
tools:
  - '[[tools/Gobuster]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:30:07.551Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Directory-Bruteforcing-for-Unprotected-Endpoints

## Summary

This procedure uses directory bruteforcing to identify unprotected administrative endpoints in a web application, such as those in a DoD system lacking authentication, enabling further exploitation.

## Description

In the context of a U.S. Department of Defense web application, attackers perform directory bruteforcing on the base URL to discover hidden paths like admin directories. This reveals endpoints (e.g., by modifying URL segments from '1' to '9') that allow access to sensitive features without login, leading to unauthorized user management. Prerequisites include a wordlist of common directory names and network access to the target.

## Requirements

1. Web browser or command-line tool for HTTP requests
2. Directory wordlist (e.g., common admin paths like /admin, /user)
3. Direct internet access to the public-facing web application

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to block anomalous request patterns
- Enforce authentication on all directories using access controls like OAuth or session management
- Monitor server logs for high-volume directory enumeration attempts

## Objectives

1. Discover hidden or unprotected directories
2. Identify authentication bypass opportunities
3. Enable access to admin functions for escalation

## Instructions

### Step 1: Prepare the Target URL

**Context**: Identify the base URL of the web application from initial reconnaissance.

**Command** (Manual URL Access):
No specific command; use browser to visit the login page (e.g., https://target-dod-app.com/login).

> This confirms the URL structure for bruteforcing, such as paths ending in :1:0:::::.

### Step 2: Run Directory Bruteforcing

**Context**: Scan for unprotected directories using a tool like Gobuster.

**Command** ([[gobuster-dir-scan]]):
```bash
gobuster dir -u https://target-dod-app.com/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt -t 50
```

> This command scans the target URL with a medium-sized wordlist, threading at 50, looking for common extensions. Expected output includes discovered paths like /admin or modified segments (e.g., :9:0:::::).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- [[gobuster-dir-scan]]

## Tools Used

- [[tools/Gobuster]]

## Tags

- [[recon]]
- [[web-vuln]]
