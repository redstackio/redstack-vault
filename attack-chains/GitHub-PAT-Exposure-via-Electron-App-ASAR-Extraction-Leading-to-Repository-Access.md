---
tags:
  - credential-exposure
  - github
  - electron
  - token-leak
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
  - '[[Discovery]]'
commands: []
platforms:
  - macOS
  - Electron
complexity: medium
procedures:
  - '[[procedures/Extract-Credentials-from-Electron-ASAR]]'
  - '[[procedures/Validate-GitHub-Token-Authentication]]'
  - '[[procedures/Access-and-Verify-Repository-Permissions]]'
step_count: 3
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
description: >-
  Multi-stage attack chain exploiting exposed GitHub Personal Access Token in a
  public Electron app's ASAR archive to gain unauthorized repository access.
skill_level: intermediate
impact_level: high
id: 7000a6a9-9898-44e6-967a-c1e335dea789
created_at: '2025-12-11T03:48:06.071Z'
updated_at: '2025-12-11T03:48:06.071Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0006]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1552]]'
  - '[[T1078]]'
  - '[[T1087]]'
---
# GitHub PAT Exposure via Electron App ASAR Extraction Leading to Repository Access

Multi-stage attack chain demonstrating the discovery and exploitation of an exposed GitHub Personal Access Token (PAT) in a public Electron app's app.asar file, leading to unauthorized read/write access to organizational repositories.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Extract ASAR and Credentials] --> B[Validate Token] --> C[Access Repositories]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- #asar
- #curl
- #git

### Target Environment

- macOS or compatible platform for Electron app extraction
- Access to GitHub API
- Node.js environment for asar tool

### Initial Access Requirements

- Publicly available Electron app DMG file
- No prior credentials needed

## Detailed Attack Procedures

## Step 1: Extract Credentials from Electron App - [[procedures/Extract-Credentials-from-Electron-ASAR]]

**Objective**: Download and extract the Electron app's ASAR archive to discover exposed credentials in a .env file.

**Instructions**:

First, download the macOS DMG file containing the Electron app. Extract the app.asar from the app's Resources directory.

Then, use [[commands/npx-asar-extract]] to unpack the ASAR archive:

```bash
npx asar extract path/to/app.asar extracted/path
```

Examine the extracted files to locate the .env file containing the GH_TOKEN.

**Expected Output**: Extracted directory with .env file revealing the GitHub token.

**Success Indicators**:
- .env file found with GH_TOKEN
- Confirmation that the file is a build leftover not loaded by the app

## Step 2: Validate GitHub Token Authentication - [[procedures/Validate-GitHub-Token-Authentication]]

**Objective**: Test the discovered token's validity and scopes by querying the GitHub API.

**Instructions**:

Use [[commands/curl-github-user]] to authenticate and retrieve user information:

```bash
curl -H "Authorization: token $GH_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user
```

Check the user's organizations by sending a GET request to https://api.github.com/user/orgs.

**Expected Output**: JSON response confirming user details and organization membership, such as Shopify.

**Success Indicators**:
- Successful authentication
- Organization list includes target (e.g., Shopify)

## Step 3: Access and Verify Repository Permissions - [[procedures/Access-and-Verify-Repository-Permissions]]

**Objective**: Confirm repository access by listing repos and cloning one for proof.

**Instructions**:

List the organization's repositories using a GET request to https://api.github.com/orgs/Shopify/repos to verify push/pull permissions.

Then, use [[commands/git-clone-repo]] to clone a repository:

```bash
git clone https://$GH_TOKEN@github.com/Shopify/repo.git /tmp/repo
```

Compute SHA512 of a file like README.md for proof of access.

**Expected Output**: Cloned repository and hash verification.

**Success Indicators**:
- List of private repos returned
- Successful clone without additional authentication

## Attack Chain Summary

### Key Achievements

1. Discovery of exposed PAT in public app
2. Validation of token scopes and access
3. Proof of unauthorized repository read/write capabilities

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]]
- [[Valid Accounts]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]
- [[Discovery]]

*Last updated: 2023-10-01*
