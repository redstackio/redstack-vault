---
tags:
  - token-leak
  - github
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/GitHub]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/github-search-tokens]]'
  - '[[commands/git-clone-repo]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Discover-Exposed-Tokens-in-Public-GitHub-Repositories]]'
step_count: 1
techniques:
  - '[[Credentials In Files]]'
description: >-
  A simple information disclosure attack where an API access token is discovered
  in a public GitHub repository, potentially allowing unauthorized access to the
  associated user account.
skill_level: beginner
impact_level: medium
id: c4b7fa32-7d9b-4daf-8a55-3547f5f17e97
created_at: '2025-12-14T17:32:10.812Z'
updated_at: '2025-12-14T17:32:10.812Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Exposed API Token Discovery in Public GitHub Repository

## Overview

This attack chain demonstrates an information disclosure vulnerability where an access token for a user account is accidentally committed to a public GitHub repository. The attacker discovers the token by browsing or searching the repository, which could lead to unauthorized access to the associated account. In this case, the token was tied to an experimental project with limited sensitive data access, reducing the overall impact. The chain highlights the risks of not sanitizing credentials in version control systems.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery] --> B[Token Acquisition]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GitHub]]

### Target Environment

- Public GitHub repository
- Web browser or GitHub CLI access
- No special ports or services beyond internet access

### Initial Access Requirements

- Public internet access
- No credentials needed for public repos
- Basic knowledge of GitHub navigation

## Detailed Attack Procedures

### Step 1: Repository Reconnaissance and Token Discovery
procedure: [[procedures/Discover-Exposed-Tokens-in-Public-GitHub-Repositories]]

**Objective**: Identify and extract exposed API tokens from public code files in the target repository.

**Instructions**: Start by searching for the target organization's repositories on GitHub. Use the GitHub search functionality to look for potential token patterns, such as API keys or access tokens. For example, execute [[commands/github-search-tokens]] to query for suspicious strings:

```bash
gh search code "api_token" --repo reverb/reverb-experimental
```

If a specific file is suspected, clone the repository using [[commands/git-clone-repo]]:

```bash
git clone https://github.com/reverb/reverb-experimental.git
cd reverb-experimental
grep -r "token" .
```

Review the output for any committed credentials, such as access tokens in configuration files or source code.

**Expected Output**: Search results or grep output showing lines with potential tokens, e.g., a string like "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...".

**Success Indicators**:
- Exposed token identified in repository files
- Token format matches expected API access token structure
- Ability to validate token by testing against the API endpoint (if applicable)

## Attack Chain Summary

### Key Achievements

1. Successful discovery of an exposed access token in a public repository
2. Limited impact assessment confirming no sensitive data access
3. Demonstration of information disclosure risks in version control

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
