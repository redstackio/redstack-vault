---
tags:
  - recon
  - secret-leak
  - github
type: procedure
tools:
  - '[[tools/Gitrob]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:23:54.966Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ce0f193c-a530-462b-ad69-8782c39e0fb2
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Scan-GitHub-Repos-for-Secrets-with-Gitrob

## Summary

This procedure uses Gitrob to scan public GitHub repositories of a target organization for sensitive files containing secrets like API keys or Rails session tokens, enabling the discovery of misconfigurations that lead to further exploitation.

## Description

In this attack scenario, Gitrob is employed to audit Algolia's public and employee repositories, identifying the secret_key_base in a secret_token.rb file committed to a public repo. This reconnaissance step is crucial for supply chain attacks where developers accidentally expose credentials. Prerequisites include GitHub access (public repos) and Gitrob installation. Expected outcome is a list of potential secrets for manual verification.

## Requirements

1. Gitrob installed and configured with GitHub token for rate limiting
2. List of target organization usernames (e.g., algolia)
3. Internet access to GitHub API

## Defense

Defensive measures and detection strategies:

- Use GitHub secret scanning and push protection to block commits
- Implement repository scanning tools like TruffleHog in CI/CD pipelines
- Monitor for anomalous GitHub API queries from unknown IPs

## Objectives

1. Identify leaked credentials in public code
2. Gather secrets for session hijacking or RCE
3. Map organization's code exposure risks

## Instructions

### Step 1: Install and Configure Gitrob

**Context**: Set up Gitrob to avoid rate limits and focus on target repos.

No specific command; follow tool installation. Configure with GitHub token.

### Step 2: Run Scan on Target Organization

**Context**: Scan all public repos for interesting files.

Use Gitrob to target Algolia repos:

```bash
gitrob -commit-depth 1000 -repo-group algolia -output results.db
```

> This scans repositories, flagging files like secret_token.rb. Expected output: Database with findings, query for Rails secrets.

### Step 3: Review and Export Findings

**Context**: Analyze results for actionable secrets.

Query the database:

```bash
gitrob -db results.db -export-json findings.json
```

> Expected output: JSON list including secret_key_base in https://github.com/algolia/facebook-search/commit/f3adccb5532898f8088f90eb57cf991e2d499b49.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Gitrob]]

## Tags

- recon
- github
- secrets
