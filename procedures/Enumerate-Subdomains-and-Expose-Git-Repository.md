---
tags:
  - reconnaissance
  - subdomain-enumeration
  - directory-fuzzing
  - git-exposure
type: procedure
tools:
  - '[[tools/subfinder]]'
  - '[[tools/ffuf]]'
  - '[[tools/SecLists]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate-subdomains]]'
  - '[[commands/ffuf-directory-fuzz]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:06.063Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ca469e34-e562-4b71-a5cd-0d2cbdb70067
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate Subdomains and Expose Git Repository

## Summary

This procedure performs passive and active reconnaissance on a target domain to discover subdomains and fuzz web directories, uncovering exposed sensitive files like .git repositories that leak source code and configuration details.

## Description

In the BountyPay attack, subdomain enumeration reveals app.bountypay.h1ctf.com, which is then fuzzed to find an unprotected .git directory. Accessing .git/config exposes the GitHub repository URL, allowing review of application code such as logger.php, which reveals logging mechanisms for further exploitation. This step requires no authentication and targets public-facing web applications.

## Requirements

1. Internet access to the target domain (bountypay.h1ctf.com)
2. Installed tools: subfinder, ffuf, SecLists wordlists
3. Basic knowledge of web fuzzing and Git structure

## Defense

Defensive measures and detection strategies:

- Implement .git access controls or remove exposed repositories
- Use web application firewalls (WAF) to block directory fuzzing attempts
- Monitor access logs for anomalous requests to hidden paths like /.git/

## Objectives

1. Discover all subdomains to map the attack surface
2. Identify information disclosure vulnerabilities like exposed source code
3. Obtain repository details for code review and vulnerability identification

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use passive enumeration to find subdomains without direct interaction.

**Command** ([[commands/subfinder-enumerate-subdomains]]):
```bash
subfinder -d bountypay.h1ctf.com -o subdomains.txt
```

> This command queries multiple passive sources to output a list of subdomains like app., software., staff., api. to subdomains.txt. Expected output: app.bountypay.h1ctf.com, www.bountypay.h1ctf.com, etc.

### Step 2: Fuzz Directories on Target Subdomain

**Context**: Target the main app subdomain to find hidden directories.

**Command** ([[commands/ffuf-directory-fuzz]]):
```bash
ffuf -w ./SecLists/Discovery/Web-Content/common.txt -u "https://app.bountypay.h1ctf.com/FUZZ" -ac
```

> Fuzzes paths using common.txt wordlist, auto-calibrating to filter false positives. Discovery of .git/HEAD indicates exposure.

### Step 3: Retrieve Git Configuration

**Context**: Directly access config to get repo details.

Use curl or browser to fetch https://app.bountypay.h1ctf.com/.git/config.

> Outputs GitHub URL: https://github.com/bounty-pay-code/request-logger.git.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/subfinder-enumerate-subdomains]]
- [[commands/ffuf-directory-fuzz]]

## Tools Used

- [[tools/subfinder]]
- [[tools/ffuf]]
- [[tools/SecLists]]

## Tags

- reconnaissance
- subdomain-enumeration
- directory-fuzzing
- git-exposure
