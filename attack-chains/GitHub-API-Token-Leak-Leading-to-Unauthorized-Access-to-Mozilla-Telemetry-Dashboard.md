---
id: ac-mozilla-token-leak-2735646
tags:
  - token-leak
  - github
  - api-token
  - information-disclosure
  - cloud-access
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Leaked-API-Token-in-GitHub-Repository]]'
  - '[[procedures/Access-Service-Using-Leaked-API-Token]]'
step_count: 2
techniques:
  - '[[Search Open Websites-Domains]]'
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:32:29.327Z'
description: >-
  An attack chain exploiting an accidentally committed API token in a public
  Mozilla GitHub repository to gain unauthorized access to the
  sql.telemetry.mozilla.org dashboard and view confidential telemetry data.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
  - '[[T1078.004]]'
---
# GitHub API Token Leak Leading to Unauthorized Access to Mozilla Telemetry Dashboard

Multi-stage attack chain demonstrating discovery of a leaked API token in a public GitHub repository and its use to access sensitive Mozilla telemetry data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Search Public Repos] --> B[Initial Access: Authenticate with Token]
    B --> C[Collection: View Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in browser or curl)

### Target Environment

- Web platform
- Public GitHub repositories
- Access to sql.telemetry.mozilla.org (internet connectivity)

### Initial Access Requirements

- No prior credentials needed
- Public internet access
- Ability to search GitHub

## Detailed Attack Procedures

### Step 1: Discover Leaked API Token
procedure: [[procedures/Discover-Leaked-API-Token-in-GitHub-Repository]]

**Objective**: Identify sensitive API tokens exposed in public GitHub commits by searching repositories.

**Instructions**: Use GitHub's advanced search to query for potential leaked tokens in Mozilla-related repositories. For example, search for phrases like "api token" or specific patterns in commits.

Navigate to GitHub search and enter: `api token mozilla` or use the API search endpoint if automated.

**Expected Output**: A list of public repositories and commits containing potential tokens.

**Success Indicators**:
- Token found in commit history
- Token format matches expected API key pattern (e.g., long alphanumeric string)

### Step 2: Access Service Using Leaked Token
procedure: [[procedures/Access-Service-Using-Leaked-API-Token]]

**Objective**: Authenticate to the target service using the discovered token to access restricted dashboard and view confidential data.

**Instructions**: Extract the token from the GitHub commit. Then, use [[commands/curl-authenticate-api]] to test authentication and access the dashboard:

```bash
curl -H "Authorization: Bearer <leaked_token>" https://sql.telemetry.mozilla.org/
```

If successful, browse the dashboard URL in a browser with the token in headers or query parameters as required.

**Expected Output**: Successful authentication response or dashboard HTML/JSON containing telemetry data.

**Success Indicators**:
- HTTP 200 response with dashboard content
- Access to confidential telemetry datasets

## Attack Chain Summary

### Key Achievements

1. Discovered leaked API token via public GitHub search
2. Gained unauthorized access to Mozilla's telemetry service
3. Viewed sensitive internal data without detection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Domains
- [[T1078.004]] Valid Accounts: Cloud Accounts

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
