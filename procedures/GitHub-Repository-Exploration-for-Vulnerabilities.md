---
id: proc-github-exploration-927413
tags:
  - github
  - code-review
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/git-clone-analyze]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:27:35.656Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# GitHub-Repository-Exploration-for-Vulnerabilities

## Summary

Manual exploration of public GitHub repositories related to Zomato to identify exposed code, configs, or vulnerabilities like public disclosures.

## Description

Searching GitHub for Zomato repos allows analysis for sensitive info or code flaws. In this report, it contributes to finding ~10 vulns, including public disclosures that could lead to internal insights.

## Requirements

1. Git installed
2. Access to GitHub search
3. Basic code review skills

## Defense

Defensive measures and detection strategies:

- Scrub repos before public release
- Use private repos for sensitive code

## Objectives

1. Identify relevant public repos
2. Analyze for leaks or vulns
3. Document findings

## Instructions

### Step 1: Search and Clone Repo

**Context**: Find and download Zomato-related repos.

**Command** ([[commands/git-clone-analyze]]):
```bash
git clone https://github.com/zomato/example-repo.git
cd example-repo
```

> Clones the repo; review files for secrets or insecure code (e.g., hardcoded creds).

### Step 2: Manual Analysis

**Context**: Inspect code for vulns.

Use grep or IDE to search for keywords like 'password' or 'api_key'.

> Expected: Exposed info or vuln patterns.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/git-clone-analyze]]

## Tools Used


## Tags

- [[github]]
- [[code-review]]
