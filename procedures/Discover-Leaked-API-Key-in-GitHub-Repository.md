---
tags:
  - reconnaissance
  - github-search
  - credential-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6000227a-f074-4c9a-8fc1-97f4353bf1b2
created_at: '2025-12-14T17:32:48.651Z'
updated_at: '2025-12-14T17:32:48.651Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Leaked-API-Key-in-GitHub-Repository

## Summary

This procedure involves searching public GitHub repositories for hard-coded sensitive credentials, such as API keys, belonging to target organizations. In this case, it uncovers a JumpCloud API key for Starbucks, enabling subsequent unauthorized access.

## Description

Attackers often search GitHub using targeted queries to find accidentally committed secrets in source code. This procedure targets organizations like Starbucks by combining company names with API service keywords. The discovered key in a Go source file allows API authentication without further barriers, leading to enumeration of internal JumpCloud resources. Prerequisites include basic web search skills and no special access, as GitHub is public.

## Requirements

1. Internet access to GitHub
2. Knowledge of target organization and API services (e.g., JumpCloud)
3. Ability to review source code files

## Defense

Defensive measures and detection strategies:

- Implement GitHub secret scanning and automated removal of committed credentials
- Use tools like GitGuardian or TruffleHog for pre-commit hooks to detect secrets
- Monitor for anomalous API access patterns in JumpCloud logs

## Objectives

1. Locate public repositories with embedded credentials
2. Extract the API key for validation
3. Prepare for API exploitation

## Instructions

### Step 1: Perform Targeted GitHub Search

**Context**: Use GitHub's search functionality to identify repositories with potential leaks.

Search for "Starbucks JumpCloud API key" or similar terms in GitHub's code search. Review results to find relevant repositories.

### Step 2: Identify and Extract Credential

**Context**: Navigate to suspicious files and extract the key.

Locate the file https://github.com/████/Project/blob/0d56bb910923da2fbee95971778923f734a25f68/getSystemUsers.go. Extract the key from the line `req.Header.Add("x-api-key", "████████")`.

> Note the commit hash 0d56bb910923da2fbee95971778923f734a25f68 for reference.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[github-search]]
- [[credential-leak]]
