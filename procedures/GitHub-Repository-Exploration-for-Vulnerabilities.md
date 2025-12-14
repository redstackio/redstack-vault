---
id: proc-github-explore-zomato
tags:
  - osint
  - github-recon
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
  - '[[Search Open Websites-Domains]]'
updated_at: '2025-12-14T03:46:32.261Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# GitHub-Repository-Exploration-for-Vulnerabilities

## Summary

Manually explore public GitHub repositories associated with Zomato to identify potential vulnerabilities in code.

## Description

Search for Zomato repos on GitHub and review commits, configs, and code for leaks or flaws like hardcoded secrets or insecure practices.

## Requirements

1. GitHub account (optional)
2. Web browser
3. Knowledge of common vuln patterns

## Defense

- Scrub repos before making public
- Use .gitignore for secrets

## Objectives

1. Locate relevant repositories
2. Analyze for vulns
3. Document findings

## Instructions

### Step 1: Search Repos

**Context**: Query GitHub for 'zomato' organization or user.

Browse https://github.com/search?q=zomato&type=repositories.

### Step 2: Review Code

**Context**: Clone and inspect if needed.

```bash
git clone https://github.com/zomato/repo.git
```

> Look for XSS patterns, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[osint]]
- [[github-recon]]
