---
id: 7eb59fcc-a57d-4223-94d8-8e45a265a533
name: Discover Leaked Credentials in Git Repository
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.532Z'
updated_at: '2025-12-11T06:10:15.532Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
tags:
  - credential-leak
  - git
commands:
  - '[[commands/git-clone-public-repo]]'
  - '[[commands/curl-api-authenticate]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1552]]'
---

# Discover Leaked Credentials in Git Repository

## Summary

This procedure involves identifying and extracting leaked sensitive information, such as usernames and certificates, from publicly accessible Git repositories, which can enable further unauthorized access to systems like APIs.

## Description

In this attack scenario, attackers scan public Git repositories for committed sensitive data that was not properly redacted. The target environment is any public code repository platform, and the expected outcome is the retrieval of usable credentials for initial access. This exploits insecure storage practices where developers accidentally commit secrets to version control.

## Requirements

1. Access to public Git repositories (e.g., GitHub)
2. Basic command-line tools like git
3. Knowledge of common file patterns for credentials (e.g., .pem files)

## Defense

Defensive measures and detection strategies:

- Implement Git hooks to prevent committing sensitive data
- Use secret scanning tools like GitGuardian or TruffleHog to detect leaks

## Objectives

1. Locate and clone repositories containing leaked credentials
2. Extract usable usernames and certificates
3. Prepare for authentication in subsequent steps

## Instructions

### Step 1: Clone Public Repository

**Context**: Clone the identified public Git repository to local machine for inspection.

**Command** ([[commands/git-clone-public-repo]]):
```bash
git clone https://github.com/example/public-repo.git
```

> This command downloads the entire repository history, allowing inspection of committed files.

### Step 2: Inspect for Leaked Credentials

**Context**: Search through the repository files and history for sensitive information like certificates and usernames.

**Command** (Manual inspection or use grep):
```bash
grep -r "certificate" . || git log -p | grep "username"
```

> Look for patterns indicating leaked secrets; extract any .pem files or credential strings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Files]]

## Commands Used

- [[commands/git-clone-public-repo]]

## Tools Used

## Tags

- [[credential-leak]]
- [[commands/git-clone-public-repo]]
