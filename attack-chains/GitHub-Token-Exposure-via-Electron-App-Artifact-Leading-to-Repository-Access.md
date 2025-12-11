---
tags:
  - credential-exposure
  - github
  - electron
  - token-leak
type: attack_chain
tools:
  - '[[tools/npx]]'
  - '[[tools/asar]]'
  - '[[tools/curl]]'
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/npx-asar-extract]]'
  - '[[commands/asar-extract]]'
  - '[[commands/curl-github-user-auth]]'
platforms:
  - macOS
  - Electron
complexity: medium
procedures:
  - '[[procedures/Extract-Credentials-from-Electron-App]]'
  - '[[procedures/Verify-GitHub-Token-Validity]]'
  - '[[procedures/Query-User-and-Organization-Details]]'
  - '[[procedures/Confirm-Repository-Access-and-Read-Permissions]]'
step_count: 4
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
description: >-
  Exploitation of exposed GitHub Personal Access Token in a public Electron app
  leading to unauthorized repository access
skill_level: intermediate
impact_level: high
id: 5ce8244b-141c-4f20-881d-7916e8424873
created_at: '2025-12-11T06:10:40.516Z'
updated_at: '2025-12-11T06:10:40.516Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1552]]'
  - '[[T1078]]'
---
# GitHub Token Exposure via Electron App Artifact Leading to Repository Access

Multi-stage attack chain demonstrating the discovery and exploitation of an exposed GitHub Personal Access Token (PAT) in a public Electron app's .env file, leading to potential unauthorized access to private repositories.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Download App] --> B[Extract Artifact]
    B --> C[Verify Token]
    C --> D[Access Repos]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npx]]
- [[tools/asar]]
- [[tools/curl]]
- [[tools/git]]

### Target Environment

- macOS platform with Electron app
- Access to GitHub API
- Network access to download public app and query APIs

### Initial Access Requirements

- Public download link to the Electron app
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Download and Extract App Artifact - [[procedures/Extract-Credentials-from-Electron-App]]

**Procedure**: [[procedures/Extract-Credentials-from-Electron-App]]

**Objective**: Obtain and extract the public Electron app to uncover embedded credentials.

**Expected Output**: Extracted .env file containing GH_TOKEN.

**Success Indicators**:
- Successful download of macOS Electron app
- Extraction of app.asar revealing .env file

First, download the public macOS Electron app from the provided link.

Then, extract the app.asar file using [[commands/npx-asar-extract]]:

```bash
npx asar extract path/to/app.asar extracted/path
```

Alternatively, use [[commands/asar-extract]]:

```bash
asar extract app.asar asar-out-dir
```

Examine the extracted files to identify the .env file with GH_TOKEN.

### Step 2: Test Token Authentication - [[procedures/Verify-GitHub-Token-Validity]]

**Procedure**: [[procedures/Verify-GitHub-Token-Validity]]

**Objective**: Confirm the validity of the discovered GitHub token via API authentication.

**Expected Output**: JSON response confirming token validity and user details.

**Success Indicators**:
- Successful API response with user information
- No authentication errors

Use [[commands/curl-github-user-auth]] to test the token:

```bash
curl -H "Authorization: token $GH_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user
```

Review the response to verify the token is active.

### Step 3: Query Affiliations - [[procedures/Query-User-and-Organization-Details]]

**Procedure**: [[procedures/Query-User-and-Organization-Details]]

**Objective**: Identify the token's affiliation with organizations like Shopify.

**Expected Output**: List of organizations confirming Shopify membership.

**Success Indicators**:
- API response listing Shopify as an organization
- Confirmation of access scopes

Use curl to query user organizations via the /user/orgs endpoint.

### Step 4: Verify Repository Access - [[procedures/Confirm-Repository-Access-and-Read-Permissions]]

**Procedure**: [[procedures/Confirm-Repository-Access-and-Read-Permissions]]

**Objective**: Clone repositories to prove read access without full disclosure.

**Expected Output**: Successful clone and hash computation of repository files.

**Success Indicators**:
- Ability to clone private repos
- Computed SHA512 hash matches expected

Use git to clone a Shopify repository to /tmp and compute SHA512 hash of README.md at a specific commit.

## Attack Chain Summary

### Key Achievements

1. Discovery of exposed GitHub PAT in public app artifact
2. Verification of token validity and scopes
3. Confirmation of read/write access to private repositories

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

*Last updated: 2023-10-01*
