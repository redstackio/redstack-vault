---
tags:
  - credential-leak
  - github
  - recon
type: procedure
tools:
  - '[[tools/Git]]'
  - '[[tools/Grep]]'
  - '[[tools/Curl]]'
  - '[[tools/JFrog-CLI]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Unsecured Credentials]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Credentials in Files]]'
id: 6550440d-6877-49d2-918c-65901753e03d
created_at: '2025-12-11T03:47:56.558Z'
updated_at: '2025-12-11T03:47:56.558Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1552]]'
---
# Discover Leaked Credentials in Public GitHub Repository

## Summary

This procedure involves identifying and cloning public GitHub repositories that contain accidentally committed sensitive credentials, such as usernames and passwords for services like JFrog Artifactory, enabling initial access for further exploitation.

## Description

In this attack scenario, an attacker searches for public repositories belonging to target organization employees (e.g., Snap) and scans for leaked credentials. This is based on real-world incidents where developers commit secrets without proper management. The procedure targets web-based version control systems and requires no prior access. Expected outcomes include extraction of valid credentials for unauthorized use.

## Requirements

1. Internet access to GitHub
2. Git installed on the local system
3. Basic command-line tools like grep

## Defense

Defensive measures and detection strategies:

- Implement secret scanning tools in CI/CD pipelines (e.g., GitHub Secret Scanning)
- Use .gitignore to prevent committing sensitive files
- Monitor for anomalous repository accesses or credential usage logs

## Objectives

1. Locate public repositories with leaked credentials
2. Clone and extract sensitive information
3. Prepare for credential validation in subsequent steps

## Instructions

### Step 1: Clone Target Repository

**Context**: Clone the public GitHub repository to local machine for inspection.

**Command** ([[commands/git-clone-repo]]):
```bash
git clone https://github.com/snap-employee/repo.git
```

> This command downloads the entire repository history, allowing offline searching for credentials.

### Step 2: Search for Credentials

**Context**: Scan the cloned files for patterns indicating usernames and passwords.

**Command** ([[commands/grep-search-credentials]]):
```bash
grep -rE 'username|password|jfrog|artifactory' repo/
```

> This searches recursively for keywords related to credentials, outputting matching lines for manual review.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Files]]

## Commands Used

- [[commands/git-clone-repo]]
- [[commands/grep-search-credentials]]

## Tools Used

- [[tools/Git]]
- [[tools/Grep]]

## Tags

- #credential-leak
- #github
