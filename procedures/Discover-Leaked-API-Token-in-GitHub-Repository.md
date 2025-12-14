---
id: proc-discover-github-token
tags:
  - reconnaissance
  - token-leak
  - github
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
updated_at: '2025-12-14T17:32:29.325Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Discover Leaked API Token in GitHub Repository

## Summary

This procedure outlines how to search public GitHub repositories for accidentally committed sensitive credentials, such as API tokens, enabling reconnaissance for potential unauthorized access points.

## Description

Attackers often review public code repositories to find leaked secrets like API keys, which can grant access to internal services. In this scenario, a Mozilla employee's token for sql.telemetry.mozilla.org was committed to a public repo. The procedure involves using GitHub's search functionality to identify such leaks, focusing on organization-specific queries to narrow results. Prerequisites include internet access and basic familiarity with GitHub. Expected outcomes include extraction of a usable token for further exploitation.

## Requirements

1. Internet access to GitHub.com
2. No special credentials (public search only)
3. Browser or GitHub CLI for querying

## Defense

Defensive measures and detection strategies:

- Implement secret scanning tools like GitHub's Secret Scanning or TruffleHog in CI/CD pipelines
- Educate developers on secret management (e.g., use .gitignore for tokens)
- Monitor for anomalous access to services using leaked tokens

## Objectives

1. Identify exposed API tokens in public commits
2. Extract token for validation in subsequent steps
3. Enable initial access to target services

## Instructions

### Step 1: Perform GitHub Search for Leaks

**Context**: Use GitHub's advanced search to query for token-like strings in Mozilla repositories.

No specific command needed; use the web interface:

1. Go to https://github.com/search
2. Enter query: `api token organization:mozilla` or `extension:log token` to find logs/commits
3. Filter by type: Code or Commits
4. Review results for recent or specific repos

> This search reveals commits where tokens are hardcoded. Copy the token string (e.g., a 32+ character alphanumeric key).

### Step 2: Validate Token Format

**Context**: Confirm the found string matches expected API token patterns to avoid false positives.

Manually inspect: API tokens often start with prefixes like `ghp_` for GitHub but here it's Mozilla-specific. Test by pasting into a notepad and checking length/format.

> Expected: A long, random string not resembling code snippets.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Domains

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[Reconnaissance]]
- [[token-leak]]
- [[github]]
