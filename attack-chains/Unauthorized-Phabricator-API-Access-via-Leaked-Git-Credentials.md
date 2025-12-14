---
tags:
  - credential-leak
  - git
  - phabricator
  - api-access
  - unauthorized-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Discover-Leaked-Credentials-in-Public-Git-Repository]]'
  - '[[procedures/Authenticate-to-Phabricator-API-Using-Leaked-Credentials]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
description: >-
  Multi-stage attack exploiting leaked username and certificate in a public git
  repository to gain unauthorized API access to an internal Phabricator
  instance, potentially exposing source code.
skill_level: beginner
impact_level: high
id: fed9bd6a-d91c-4050-bc45-a40deec35b85
created_at: '2025-12-14T17:32:48.619Z'
updated_at: '2025-12-14T17:32:48.619Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Unauthorized Phabricator API Access via Leaked Git Credentials

Multi-stage attack chain demonstrating the exploitation of leaked credentials in a public git repository to achieve unauthorized access to an internal Phabricator instance at code.uberinternal.com. The vulnerability stems from unsanitized sensitive information committed to a public repository, allowing attackers to authenticate via API and potentially access proprietary source code. This incident resulted in a $40,000 bounty on HackerOne.

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
    A[Discover Leaked Credentials] --> B[API Authentication and Access]
    B --> C[Source Code Exposure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Git client for repository inspection
- API testing tool (e.g., curl for authentication tests)

### Target Environment

- Public git repository hosting leaked credentials
- Internal Phabricator instance (e.g., code.uberinternal.com)
- API endpoint requiring username and certificate authentication

### Initial Access Requirements

- Internet access to public git repositories
- No prior credentials needed; relies on public exposure
- Basic understanding of git and API authentication

## Detailed Attack Procedures

### Step 1: Discover Leaked Credentials
procedure: [[procedures/Discover-Leaked-Credentials-in-Public-Git-Repository]]

**Objective**: Identify and extract sensitive credentials (username and certificate) exposed in a public git repository to enable subsequent authentication.

**Instructions**: Search public git repositories for sensitive files containing authentication details. Clone the repository and inspect commit history or files for exposed credentials.

For example, use git to clone and grep for keywords like 'certificate' or 'username':

```bash
git clone https://github.com/public-repo.git
cd public-repo
grep -r "certificate" . || grep -r "username" .
```

Review the output to locate the leaked username and certificate file.

**Expected Output**: Exposed username string and certificate content (e.g., PEM format) readable from repository files.

**Success Indicators**:
- Credentials found in plain text or committed files
- Certificate validates as usable for API auth

### Step 2: Authenticate to Phabricator API
procedure: [[procedures/Authenticate-to-Phabricator-API-Using-Leaked-Credentials]]

**Objective**: Use the discovered credentials to authenticate and gain unauthorized API access to the internal Phabricator instance, enabling data retrieval such as source code.

**Instructions**: Construct API requests using the leaked username and certificate. Test authentication by querying a basic endpoint on code.uberinternal.com.

For instance, use curl to authenticate with the certificate:

```bash
curl -u username: --cert leaked-cert.pem https://code.uberinternal.com/api/phabricator.info
```

If successful, proceed to query sensitive data like repository contents.

**Expected Output**: Valid API response with Phabricator data, such as instance info or source code listings.

**Success Indicators**:
- HTTP 200 response from API endpoint
- Access to private repositories or source code

## Attack Chain Summary

### Key Achievements

1. Discovery of leaked credentials in public git repo
2. Successful API authentication to internal Phabricator
3. Potential exposure of proprietary source code and instance data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
