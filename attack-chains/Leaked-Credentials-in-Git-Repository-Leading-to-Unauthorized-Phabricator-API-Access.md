---
tags:
  - credential-leak
  - git
  - phabricator
  - api-access
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Discover-Leaked-Credentials-in-Git-Repository]]'
  - '[[procedures/Authenticate-to-Phabricator-API-Using-Leaked-Credentials]]'
step_count: 2
techniques:
  - '[[Gather Victim Network Information]]'
  - '[[Valid Accounts]]'
description: >-
  Exploitation of leaked certificate and username in a public git repository to
  gain unauthorized API access to Uber's internal Phabricator instance.
skill_level: beginner
impact_level: high
id: 09ffa96e-7e60-4236-a051-c32e443409c2
created_at: '2025-12-11T03:48:06.085Z'
updated_at: '2025-12-11T03:48:06.085Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1590]]'
  - '[[T1078]]'
---
# Leaked Credentials in Git Repository Leading to Unauthorized Phabricator API Access

Multi-stage attack chain demonstrating the discovery and exploitation of leaked credentials in a public git repository to access an internal Phabricator API, potentially leading to source code disclosure.

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
    A[Reconnaissance: Discover Leaked Credentials] --> B[Initial Access: Authenticate to API]
    B --> C[Objective: Access Internal Resources]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #git
- #curl

### Target Environment

- Target OS/Platform: Web
- Required services/ports: Phabricator API on code.uberinternal.com
- Network access requirements: Internet access to public git repo and target domain

### Initial Access Requirements

- Credential requirements: None initially; leaked creds discovered during recon
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Discover Leaked Credentials - [[procedures/Discover-Leaked-Credentials-in-Git-Repository]]

**Procedure**: [[procedures/Discover-Leaked-Credentials-in-Git-Repository]]

**Objective**: Identify sensitive credentials such as certificates and usernames exposed in a public git repository.

**Expected Output**: Extraction of leaked username and certificate file from the repository.

**Success Indicators**:
- Successful cloning of the git repository
- Identification of sensitive files containing credentials

First, clone the public git repository using [[commands/git-clone-public-repo]]:

```bash
git clone https://github.com/example-repo.git
```

Then, search the repository for sensitive files or strings, such as certificates or usernames, by inspecting commit history or files.

Validate by checking for files like certificates or config files containing usernames.

### Step 2: Authenticate to API - [[procedures/Authenticate-to-Phabricator-API-Using-Leaked-Credentials]]

**Procedure**: [[procedures/Authenticate-to-Phabricator-API-Using-Leaked-Credentials]]

**Objective**: Use the discovered credentials to authenticate and access the Phabricator API on the target domain.

**Expected Output**: Successful API response indicating access to internal Phabricator resources.

**Success Indicators**:
- HTTP 200 OK response from the API
- Ability to query internal project details or source code

Use the leaked username and certificate to authenticate via [[commands/curl-authenticate-api]]:

```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api/
```

Verify access by attempting to retrieve protected resources, such as project lists or source code repositories.

## Attack Chain Summary

### Key Achievements

1. Discovery of leaked credentials in a public git repository
2. Unauthorized access to internal Phabricator API
3. Potential for source code and project detail disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Network Information]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Initial Access]]

*Last updated: 2023-10-01*
