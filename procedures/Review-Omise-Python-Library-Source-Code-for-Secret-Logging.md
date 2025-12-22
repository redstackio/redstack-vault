---
tags:
  - code-review
  - static-analysis
  - credential-exposure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:20.774Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c39d5d17-9f53-435d-b9d8-bb95d39cf5f6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Review-Omise-Python-Library-Source-Code-for-Secret-Logging

## Summary

This procedure involves statically analyzing the source code of the omise-python library to identify instances where secret API keys are logged in cleartext, specifically in debug mode, enabling the discovery of potential credential exposure vulnerabilities.

## Description

The omise-python library, used for integrating with the Omise payment API, contains debug logging statements in its request.py file that output the full API secret key without masking. By reviewing the public GitHub repository, attackers or auditors can pinpoint these issues at lines 88 and 111, where logger.debug('Authorization: %s', self.api_key) reveals the key. This procedure assumes access to the repository and basic code reading skills, targeting Python developers or security researchers auditing third-party libraries for insecure handling of secrets.

## Requirements

1. Access to GitHub and the ability to clone repositories.
2. Text editor or IDE for browsing Python source code.
3. Knowledge of Python logging module and HTTP authorization headers.

## Defense

Defensive measures and detection strategies:

- Implement code scanning tools like Bandit or Semgrep to detect logging of secrets.
- Enforce library updates and review changelogs for security fixes.
- Use secret scanning in CI/CD pipelines to flag hardcoded or logged credentials.

## Objectives

1. Identify exact locations of insecure logging in the library.
2. Understand the root cause: unmasked debug outputs of api_key.
3. Assess impact on applications using the library in debug mode.

## Instructions

### Step 1: Clone the Repository

**Context**: Obtain the source code for analysis.

Navigate to the repository URL https://github.com/omise/omise-python/ and clone it locally.

**Command** (git-clone-repo):
```bash
git clone https://github.com/omise/omise-python.git
cd omise-python
```

> This downloads the library source. Expected output: Local directory with source files.

### Step 2: Examine request.py File

**Context**: Search for logging statements involving API keys.

Open request.py in a text editor and navigate to lines 88 and 111.

**Command** (grep-search-logs):
```bash
grep -n "logger.debug.*api_key" omise/request.py
```

> This highlights lines like logger.debug('Authorization: %s', self.api_key). Expected output: Matches at lines 88 and 111 confirming cleartext logging.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[git-clone-repo]]
- [[grep-search-logs]]

## Tools Used


## Tags

- [[code-review]]
- [[static-analysis]]
- [[Python]]
