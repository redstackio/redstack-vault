---
tags:
  - credential-leak
  - git
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b66eb538-7e68-4c4d-9ead-862696bb1b37
created_at: '2025-12-11T03:48:06.082Z'
updated_at: '2025-12-11T03:48:06.082Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1590]]'
---
# Discover Leaked Credentials in Git Repository

## Summary

This procedure involves identifying and extracting sensitive credentials, such as certificates and usernames, that have been inadvertently committed to a public git repository, enabling further exploitation like unauthorized API access.

## Description

In this attack scenario, an attacker searches public git repositories for exposed sensitive information. The target environment is typically a web-based code hosting service where developers might accidentally commit credentials without proper security controls. The expected outcome is the retrieval of usable credentials for initial access to internal systems like Phabricator.

## Requirements

1. Access to public git repositories (e.g., GitHub)
2. Git installed on the attacker's machine
3. Knowledge of the target's repository names or search terms for leaked data

## Defense

Defensive measures and detection strategies:

- Implement git hooks to prevent committing sensitive data
- Use secret scanning tools like GitHub's secret scanning or TruffleHog

## Objectives

1. Locate and clone repositories containing leaked credentials
2. Extract certificates and usernames
3. Prepare for authentication in subsequent steps

## Instructions

### Step 1: Clone the Repository

**Context**: Clone the identified public git repository to local machine for inspection.

**Command** ([[commands/git-clone-public-repo]]):
```bash
git clone https://github.com/example-repo.git
```

> This command downloads the entire repository, including commit history, where leaked credentials may be found.

### Step 2: Search for Leaked Credentials

**Context**: Inspect the repository files and history for sensitive information like certificates or usernames.

**Command** (#git):
```bash
git log -p | grep -i 'certificate|username'
```

> This searches commit history for keywords related to credentials; extract any found certificate files or username strings.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Network Information]]

### Sub-Techniques



## Commands Used

- [[commands/git-clone-public-repo]]
- #git

## Tools Used

- #git

## Tags

- #credential-leak
- #git
