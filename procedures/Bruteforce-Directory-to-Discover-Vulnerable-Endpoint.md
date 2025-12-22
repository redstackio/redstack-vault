---
id: proc-uuid-001
tags:
  - bruteforce
  - directory
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:20.555Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Bruteforce-Directory-to-Discover-Vulnerable-Endpoint

## Summary

This procedure involves systematically probing a web directory to identify hidden or accessible PHP scripts, such as move_papers.php in the /pubs/ path, to uncover potential injection points in a PHP/MySQL web application.

## Description

In web penetration testing, discovering endpoints is crucial for identifying vulnerabilities. Here, the /pubs/ directory on a target DoD application was bruteforced to find move_papers.php, which accepts the pub_group_id parameter. This step requires network access to the target and uses manual or automated requests to enumerate files without alerting defenses.

## Requirements

1. Network access to the target web server
2. Tools like curl, Burp Suite, or gobuster for probing
3. Knowledge of common PHP file names in the target context

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to detect anomalous probing patterns
- Use directory listing restrictions and rate limiting on endpoints

## Objectives

1. Locate accessible scripts in restricted directories
2. Identify parameters for further testing
3. Map the attack surface without triggering alerts

## Instructions

### Step 1: Probe Directory Files

**Context**: Send GET requests to common file names in /pubs/ to check for existence.

**Command** (Manual curl probe):
```bash
curl -X GET "https://target.com/pubs/move_papers.php" -H "User-Agent: Mozilla/5.0"
```

> This command checks if the endpoint responds with a 200 status, indicating the script is present and potentially vulnerable to parameter manipulation.

### Step 2: Verify Parameter Handling

**Context**: Append a test parameter to observe application behavior.

**Command** (Test with dummy parameter):
```bash
curl -X GET "https://target.com/pubs/move_papers.php?pub_group_id=1" -H "User-Agent: Mozilla/5.0"
```

> Expect a normal response; unusual errors may hint at backend processing issues like SQL queries.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bruteforce]]
- [[directory]]
- [[recon]]
