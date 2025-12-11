---
id: 4feaf05f-8bdf-4c5e-9993-d045dd56923e
name: >-
  Leaked Credentials in Git Repository Enabling Unauthorized Phabricator API
  Access
type: attack_chain
description: >-
  Attack chain exploiting leaked username and certificate in a public Git
  repository to gain unauthorized API access to Uber's internal Phabricator
  instance.
verified: false
submitted: true
step_count: 2
created_at: '2025-12-11T06:10:15.535Z'
updated_at: '2025-12-11T06:10:15.535Z'
procedures:
  - '[[procedures/Discover-Leaked-Credentials-in-Git-Repository]]'
  - '[[procedures/Access-Phabricator-API-Using-Leaked-Credentials]]'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
tags:
  - credential-leak
  - git
  - phabricator
  - api-access
platforms:
  - Web
tools: []
commands:
  - '[[commands/git-clone-public-repo]]'
  - '[[commands/curl-api-authenticate]]'
complexity: low
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1552]]'
  - '[[T1078]]'
---

# Leaked Credentials in Git Repository Enabling Unauthorized Phabricator API Access

Multi-stage attack chain demonstrating how leaked credentials in a public Git repository can be exploited to gain unauthorized access to an internal Phabricator API, potentially exposing source code and private data.

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
    A[Discover Leaked Credentials] --> B[Access Phabricator API]
    B --> C[Potential Data Exposure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specifically required, but basic tools like git and curl are assumed.

### Target Environment

- Web-based platform
- Phabricator API on code.uberinternal.com
- Access to public Git repositories

### Initial Access Requirements

- Internet access to public Git repos
- No prior credentials needed for discovery

## Detailed Attack Procedures

### Step 1: Discover Leaked Credentials - [[procedures/Discover-Leaked-Credentials-in-Git-Repository]]

**Procedure**: [[procedures/Discover-Leaked-Credentials-in-Git-Repository]]

**Objective**: Identify and extract sensitive credentials such as usernames and certificates from publicly accessible Git repositories.

**Expected Output**: Obtained username and certificate files.

**Success Indicators**:
- Successful clone of the repository
- Identification of leaked credentials in repository files

First, clone the public Git repository using [[commands/git-clone-public-repo]]:

```bash
git clone https://github.com/example/public-repo.git
```

Then, inspect the repository files for sensitive information like certificates and usernames.

### Step 2: Access Phabricator API - [[procedures/Access-Phabricator-API-Using-Leaked-Credentials]]

**Procedure**: [[procedures/Access-Phabricator-API-Using-Leaked-Credentials]]

**Objective**: Use the leaked credentials to authenticate and gain API access to the internal Phabricator instance.

**Expected Output**: Successful API authentication and access to endpoints.

**Success Indicators**:
- Valid API response from code.uberinternal.com
- Ability to query Phabricator data

Authenticate to the Phabricator API using [[commands/curl-api-authenticate]] with the leaked certificate and username:

```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api endpoint
```

Verify access by querying available API methods.

## Attack Chain Summary

### Key Achievements

1. Discovery of leaked sensitive credentials in public repositories
2. Unauthorized access to internal API endpoints
3. Potential exposure of source code and private instance details

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---

*Last updated: [TIMESTAMP]*
