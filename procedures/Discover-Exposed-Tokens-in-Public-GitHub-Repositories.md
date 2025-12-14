---
tags:
  - token-leak
  - github
  - information-disclosure
  - discovery
type: procedure
tools:
  - '[[tools/GitHub]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/github-search-tokens]]'
  - '[[commands/git-clone-repo]]'
platforms:
  - Web
techniques:
  - '[[Credentials In Files]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b4109915-ee0e-4fb5-b894-046f95858df8
created_at: '2025-12-14T17:32:10.808Z'
updated_at: '2025-12-14T17:32:10.808Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Discover-Exposed-Tokens-in-Public-GitHub-Repositories

## Summary

This procedure outlines how to identify and extract accidentally committed API access tokens or credentials from public GitHub repositories, exploiting information disclosure vulnerabilities caused by poor secret management in version control systems.

## Description

Attackers often find sensitive information like API tokens in public repositories due to developers committing credentials without using .gitignore or secret scanning tools. In this scenario, the token grants access to a user account on Reverb.com, though limited to an experimental project. The procedure involves searching repositories for token patterns and reviewing code files. Prerequisites include public access to GitHub; no authentication is needed for public repos. Expected outcomes include acquiring the token for potential unauthorized use, such as API calls to the associated service.

## Requirements

1. Internet access to GitHub
2. GitHub CLI (gh) installed for advanced searching
3. Git installed for cloning repositories
4. Basic command-line knowledge

## Defense

Defensive measures and detection strategies:

- Implement secret scanning tools like GitHub's built-in secret scanning or TruffleHog
- Use .gitignore to exclude credential files and enforce pre-commit hooks
- Regularly audit public repositories for exposed secrets and rotate tokens immediately upon discovery
- Monitor for anomalous API access using logging and alerting

## Objectives

1. Locate exposed credentials in public code
2. Extract and validate the token for usability
3. Assess potential access granted by the token

## Instructions

### Step 1: Search for Token Patterns

**Context**: Use GitHub's search to query for common token strings across the target repository or organization.

**Command** ([[commands/github-search-tokens]]):
```bash
gh search code "access_token OR api_key" --repo organization/repo-name --limit 100
```

> This command searches the specified repository for strings matching token patterns. Expected output includes file paths and code snippets containing potential secrets. Review results manually for valid tokens.

### Step 2: Clone and Grep Repository

**Context**: If search yields hits, clone the repo locally to inspect files thoroughly.

**Command** ([[commands/git-clone-repo]]):
```bash
git clone https://github.com/organization/repo-name.git
cd repo-name
grep -r -i "token\|key\|secret" .
```

> Clones the repository and searches all files for keywords indicating secrets. Expected output: File paths and lines with exposed credentials, such as API tokens in config files.

### Step 3: Validate Token

**Context**: Test the discovered token against the API to confirm validity (optional, depending on service).

**Command** (Manual curl test):
```bash
curl -H "Authorization: Bearer YOUR_TOKEN_HERE" https://api.example.com/user
```

> Sends a request using the token. Expected output: Successful response if token is valid, or 401/403 if expired/invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/github-search-tokens]]
- [[commands/git-clone-repo]]

## Tools Used

- [[tools/GitHub]]

## Tags

- [[token-leak]]
- [[tools/GitHub]]
- [[information-disclosure]]
