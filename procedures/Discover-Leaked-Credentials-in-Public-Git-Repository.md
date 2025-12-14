---
tags:
  - credential-leak
  - git
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
id: add42eab-4a27-43bb-8f37-57b5244e4f5c
created_at: '2025-12-14T17:32:48.614Z'
updated_at: '2025-12-14T17:32:48.614Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Leaked Credentials in Public Git Repository

## Summary

This procedure involves scanning and inspecting public git repositories to identify exposed sensitive credentials, such as usernames and certificates, which can be used for unauthorized access to internal systems like Phabricator APIs.

## Description

In this attack scenario, attackers search public repositories on platforms like GitHub for accidentally committed sensitive files. The target environment includes any public git repo with development artifacts. Expected outcomes include extraction of usable credentials, leading to initial access vectors. Prerequisites include internet access and basic git knowledge; no special privileges are needed as the exposure is public.

## Requirements

1. Access to public git hosting platforms (e.g., GitHub)
2. Git client installed for cloning and searching
3. Knowledge of common credential keywords (e.g., 'cert', 'key', 'username')

## Defense

Defensive measures and detection strategies:

- Implement pre-commit hooks and git secrets scanning to prevent credential commits
- Regularly audit public repositories for leaks using tools like TruffleHog
- Monitor for anomalous API access from leaked credentials

## Objectives

1. Locate exposed authentication credentials in git history or files
2. Extract and validate credentials for usability
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Search for Target Repository

**Context**: Identify repositories associated with the target organization that may contain leaks.

Use web search or git platform search to find relevant public repos, then clone it.

```bash
git clone https://github.com/target-org/public-repo.git
```

> This clones the repository locally for inspection.

### Step 2: Inspect for Credentials

**Context**: Search files and commit history for sensitive information.

Scan the repo contents:

```bash
cd public-repo
grep -r -i "certificate\|username\|private key" .

git log --all --full-history -- grep="certificate" --oneline
```

> Expected output includes file paths or commit hashes containing matches, revealing the leaked username and certificate.

### Step 3: Extract and Verify

**Context**: Retrieve the credentials and test their format.

Copy the certificate to a file (e.g., leaked-cert.pem) and verify with openssl:

```bash
openssl x509 -in leaked-cert.pem -text -noout
```

> Successful output shows certificate details, confirming it's valid for API use.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- [[Hardware]]

## Commands Used


## Tools Used


## Tags

- [[credential-leak]]
- [[git]]
- [[Reconnaissance]]
