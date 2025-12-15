---
id: proc-discover-github-token-leak-001
tags:
  - token-leak
  - github
  - reconnaissance
  - secrets-scanning
type: procedure
tools:
  - '[[tools/truffleHog]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/git-clone]]'
  - '[[commands/trufflehog-scan]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:38.889Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Leaked API Tokens in Public GitHub Repositories

## Summary

This procedure involves scanning public GitHub repositories for accidentally committed sensitive information, such as API tokens, to identify potential credential leaks that can grant unauthorized access to services like Mozilla's FuzzManager.

## Description

Attackers and researchers often scan public code repositories for exposed secrets, including API tokens stored in cleartext within commits. In this scenario, a Mozilla FuzzManager API token with read-write permissions was committed to a public repo, allowing discovery via automated scanning tools. The procedure targets high-entropy strings or regex patterns matching known token formats, enabling subsequent exploitation for data access or manipulation. Prerequisites include access to public repos; no authentication is needed for scanning.

## Requirements

1. Internet access to clone and scan public GitHub repositories
2. Installed scanning tool like truffleHog
3. Basic knowledge of Git and regex patterns for tokens

## Defense

Defensive measures and detection strategies:

- Enable GitHub's secret scanning for repositories
- Use pre-commit hooks to detect and block secret commits
- Rotate tokens immediately upon exposure detection
- Monitor API access logs for anomalous token usage

## Objectives

1. Identify exposed API tokens in commit history
2. Validate token usability for target services
3. Gather credentials for further exploitation

## Instructions

### Step 1: Clone the Target Repository

**Context**: Obtain the repository contents to scan for secrets in files and commit history.

**Command** ([[commands/git-clone]]):
```bash
git clone https://github.com/mozilla/target-repo.git
```

> This clones the public repository locally. Expected output: Repository directory created with all commits.

### Step 2: Scan for Exposed Secrets

**Context**: Analyze the repository for sensitive data using entropy detection and regex matching for API tokens.

**Command** ([[commands/trufflehog-scan]]):
```bash
trufflehog filesystem ./target-repo
```

> This scans files and Git history for secrets. Expected output: List of detected secrets, e.g., "HIGH: Mozilla API Token: abc123... in file config.py at line 10."

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone]]
- [[commands/trufflehog-scan]]

## Tools Used

- [[tools/truffleHog]]

## Tags

- token-leak
- github
- reconnaissance
