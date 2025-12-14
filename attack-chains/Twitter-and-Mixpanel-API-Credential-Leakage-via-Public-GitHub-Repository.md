---
id: ac-liberapay-credential-leak-361089
tags:
  - credential-leak
  - github
  - api-keys
  - twitter
  - mixpanel
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Leaked-Twitter-API-Credentials-in-GitHub]]'
  - '[[procedures/Identify-Leaked-Mixpanel-Token-in-GitHub]]'
  - '[[procedures/Browse-SQL-Config-for-Additional-Leaked-Keys]]'
step_count: 3
techniques:
  - '[[Credentials In Files]]'
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:01.862Z'
description: >-
  Discovery of sensitive API credentials for Twitter and Mixpanel stored in
  cleartext within Liberapay's public GitHub repository, enabling potential
  impersonation and data access.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Hardware]]'
---
# Twitter and Mixpanel API Credential Leakage via Public GitHub Repository

Multi-stage attack chain demonstrating the discovery of leaked API credentials in a public GitHub repository, allowing attackers to impersonate the organization on external services like Twitter and access analytics data via Mixpanel.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Repository Reconnaissance] --> B[Credential Discovery]
    B --> C[Service Impersonation Potential]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Public GitHub repository
- No authentication required
- Services: Twitter API, Mixpanel

### Initial Access Requirements

- Internet access
- No prior credentials needed
- Public repository visibility

## Detailed Attack Procedures

### Step 1: Discover Leaked Twitter API Credentials
procedure: [[procedures/Discover-Leaked-Twitter-API-Credentials-in-GitHub]]

**Objective**: Identify exposed Twitter consumer keys, secrets, access tokens, and callback URLs in repository files to enable API impersonation.

**Instructions**: Navigate to the Liberapay GitHub repository and search for configuration files containing Twitter-related variables. Manually inspect files for unredacted credentials.

**Expected Output**: Exposure of TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET, and TWITTER_CALLBACK URL (e.g., pointing to localhost:8537).

**Success Indicators**:
- Credentials visible in plain text
- Callback URL reveals internal service details

### Step 2: Identify Leaked Mixpanel Token
procedure: [[procedures/Identify-Leaked-Mixpanel-Token-in-GitHub]]

**Objective**: Locate the Mixpanel analytics token to gain access to usage insights and sensitive data.

**Instructions**: Continue browsing the same repository context, searching for analytics or tracking configurations. Look for MIXPANEL_TOKEN in environment or config files.

**Expected Output**: MIXPANEL_TOKEN=cb9dec68ac0ee57071f0be39f164a417 directly exposed.

**Success Indicators**:
- Token found in cleartext
- Potential for querying Mixpanel API

### Step 3: Browse SQL Configuration for Additional Leaked Keys
procedure: [[procedures/Browse-SQL-Config-for-Additional-Leaked-Keys]]

**Objective**: Examine SQL files for further sensitive keys and secrets to expand the scope of compromise.

**Instructions**: Access specific file paths in the repository, such as the SQL configuration file, and review contents for any additional API keys or secrets.

**Expected Output**: Additional credentials in https://github.com/liberapay/liberapay.com/blob/4419a95916f4af3bfd61361341776fce66bf7a6a/sql/app-conf-defaults.sql.

**Success Indicators**:
- More keys/secrets identified
- Confirmation of broad exposure

## Attack Chain Summary

### Key Achievements

1. Uncovered Twitter API credentials enabling impersonation and unauthorized actions like posting tweets or accessing user data.
2. Exposed Mixpanel token allowing analytics data queries and potential data leakage.
3. Identified additional leaks in SQL configs, highlighting systemic storage issues.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]] Credentials In Files
- [[Hardware]] Gather Victim Identity Information: Credentials

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
