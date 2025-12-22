---
tags:
  - reconnaissance
  - subdomain-enum
  - directory-brute
type: procedure
tools:
  - '[[tools/Amass]]'
  - '[[tools/Dirsearch]]'
  - '[[tools/Curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/amass-enum-passive]]'
  - '[[commands/dirsearch-brute-app]]'
  - '[[commands/curl-git-config]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:58.244Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d41a0a97-9519-4b66-816d-9d4e535cc0c8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Reconnaissance-and-Exposed-Git-Discovery

## Summary

This procedure performs initial reconnaissance on the target domain to enumerate subdomains and brute force directories, leading to the discovery of an exposed .git repository on the app subdomain.

## Description

In the BountyPay attack, reconnaissance revealed subdomains like app.bountypay.h1ctf.com. Directory brute forcing identified the exposed .git directory, leaking the GitHub repository URL for further analysis. This step expands the attack surface and uncovers information disclosure opportunities.

## Requirements

1. Kali Linux or similar with Amass and dirsearch installed
2. Internet access to target domain
3. Wordlist for brute forcing (e.g., dicc.txt)

## Defense

- Implement proper server configuration to hide .git directories (e.g., via .htaccess or nginx rules)
- Use WAF to detect and block directory brute forcing attempts
- Monitor for subdomain enumeration tools via DNS logs

## Objectives

1. Identify all subdomains
2. Discover hidden directories and files
3. Locate exposed sensitive repositories

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use Amass to passively discover subdomains without direct interaction.

**Command** ([[commands/amass-enum-passive]]):
```bash
amass enum --passive -d bountypay.h1ctf.com
```

> This command outputs a list of subdomains such as app, api, staff, software.

### Step 2: Brute Force Directories

**Context**: Target the app subdomain to find hidden paths like .git.

**Command** ([[commands/dirsearch-brute-app]]):
```bash
python3 ~/dirsearch/dirsearch.py -u https://app.bountypay.h1ctf.com/ -e php,asp,aspx,jsp,html,zip,jar -b -w ~/dirsearch/db/dicc.txt -t 200 -x 502,503 -H 'X-FORWARDED-FOR: 127.0.0.1'
```

> Excludes backups, uses custom header to bypass limits, discovers .git.

### Step 3: Retrieve Git Config

**Context**: Download the config to get repo details.

**Command** ([[commands/curl-git-config]]):
```bash
curl -sk https://app.bountypay.h1ctf.com/.git/config
```

> Reveals GitHub URL https://github.com/bounty-pay-code/request-logger/.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/amass-enum-passive]]
- [[commands/dirsearch-brute-app]]
- [[commands/curl-git-config]]

## Tools Used

- [[tools/Amass]]
- [[tools/Dirsearch]]
- [[tools/Curl]]

## Tags

- [[Reconnaissance]]
- [[subdomain-enum]]
- [[directory-brute]]
