---
id: proc-discover-github-credentials
tags:
  - credential-leak
  - github
  - reconnaissance
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:51.720Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Exposed Credentials in Public GitHub Repository

## Summary

This procedure involves searching public GitHub repositories for accidentally committed sensitive credentials, such as API keys or passwords, related to a target organization like Starbucks' China operations. It enables initial reconnaissance for credential-based attacks.

## Description

Attackers often scan public code repositories for exposed secrets due to developer errors, such as committing credentials without using .gitignore. In this scenario, a public GitHub repo contained Starbucks credentials, allowing discovery without authentication. Prerequisites include internet access and knowledge of target-specific keywords. Expected outcomes: Extraction of usable credentials leading to further exploitation.

## Requirements

1. Internet access to GitHub
2. Search terms related to the target (e.g., "Starbucks API key")
3. Basic understanding of credential formats

## Defense

Defensive measures and detection strategies:

- Implement secret scanning tools like GitHub's Secret Scanning or TruffleHog
- Enforce .gitignore for sensitive files and conduct code reviews
- Monitor for anomalous API access from leaked credentials

## Objectives

1. Identify exposed credentials in public repositories
2. Extract and validate credentials for use
3. Enable subsequent authentication attempts

## Instructions

### Step 1: Search GitHub for Exposed Repositories

**Context**: Use GitHub's search functionality to find repositories containing potential secrets.

Search GitHub with queries like "Starbucks credentials" or "extension:env password" filtered by the organization or language.

> Manually review search results for public repositories. Look for files like .env, config.json, or scripts with hardcoded values.

### Step 2: Extract and Document Credentials

**Context**: Once a relevant repository is found, clone or view the file contents to extract the credentials.

Navigate to the specific file in the repository (no cloning needed for public repos) and copy the credentials, such as username/password pairs.

> Verify the credentials are current by checking commit history or testing in a non-destructive way.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Hardware]] Gather Victim Network Information

## Commands Used


## Tools Used


## Tags

- [[credential-leak]]
- [[github]]
- [[Reconnaissance]]
