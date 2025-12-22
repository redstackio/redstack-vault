---
tags:
  - credential-leak
  - api-key
  - github
  - jumpcloud
type: attack_chain
tools:
  - '[[tools/GitHub]]'
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-jumpcloud-systems]]'
  - '[[commands/curl-jumpcloud-systemusers]]'
  - '[[commands/curl-jumpcloud-applications]]'
platforms:
  - Web
  - Cloud (AWS)
complexity: low
procedures:
  - '[[procedures/Search-Public-GitHub-for-Leaked-Credentials]]'
  - '[[procedures/Extract-Hard-Coded-API-Key-from-Source-Code]]'
  - '[[procedures/Exploit-Leaked-JumpCloud-API-Key-to-Access-Internal-Resources]]'
step_count: 3
techniques:
  - '[[Active Scanning]]'
  - '[[Credentials in Files]]'
  - '[[Valid Accounts]]'
description: >-
  Exploitation of a hard-coded JumpCloud API key exposed in a public GitHub
  repository, leading to unauthorized access to systems, users, and SSO
  applications.
skill_level: beginner
impact_level: high
id: 682f1103-d5dd-401b-ba56-11e5856aaccd
created_at: '2025-12-11T06:10:28.781Z'
updated_at: '2025-12-11T06:10:28.781Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
  - '[[TA0001]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1595]]'
  - '[[T1552.001]]'
  - '[[T1078]]'
---
# Leaked JumpCloud API Key in Public GitHub Repository Enabling Unauthorized Access

Multi-stage attack chain demonstrating the discovery and exploitation of a leaked JumpCloud API key in a public GitHub repository, allowing unauthorized access to internal systems, users, and SSO applications, with potential for further compromise like command execution and AWS account takeover.

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
    A[Reconnaissance] --> B[Credential Extraction]
    B --> C[API Exploitation]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GitHub]]
- [[tools/curl]]

### Target Environment

- Web-based services (GitHub, JumpCloud)
- Cloud (AWS) integration
- No specific ports required; internet access to APIs

### Initial Access Requirements

- Public access to GitHub repositories
- No prior credentials needed
- Internet connectivity for API requests

## Detailed Attack Procedures

### Step 1: GitHub Repository Search - [[procedures/Search-Public-GitHub-for-Leaked-Credentials]]

**Procedure**: [[procedures/Search-Public-GitHub-for-Leaked-Credentials]]

**Objective**: Identify public repositories containing sensitive information related to the target organization.

**Expected Output**: Discovery of a repository with hard-coded credentials.

**Success Indicators**:
- Repository URL identified
- Source file containing potential credentials found

First, use GitHub search functionality to find Starbucks-related repositories. Navigate to https://github.com and search for terms like "Starbucks JumpCloud".

This leads to the repository at https://github.com/██████████/Project and the file getSystemUsers.go.

### Step 2: API Key Extraction - [[procedures/Extract-Hard-Coded-API-Key-from-Source-Code]]

**Procedure**: [[procedures/Extract-Hard-Coded-API-Key-from-Source-Code]]

**Objective**: Extract the hard-coded JumpCloud API key from the identified source code file.

**Expected Output**: Obtain the API key value.

**Success Indicators**:
- API key string extracted
- Confirmation that the key is not obfuscated

Examine the source code in getSystemUsers.go. Look for lines adding headers, such as req.Header.Add("x-api-key", "████████").

Copy the key value for use in subsequent steps.

### Step 3: API Key Exploitation - [[procedures/Exploit-Leaked-JumpCloud-API-Key-to-Access-Internal-Resources]]

**Procedure**: [[procedures/Exploit-Leaked-JumpCloud-API-Key-to-Access-Internal-Resources]]

**Objective**: Use the extracted API key to query JumpCloud endpoints and access unauthorized information.

**Expected Output**: Lists of systems, users, and SSO applications.

**Success Indicators**:
- Successful API responses with internal data
- No authentication errors

Test the key by executing [[commands/curl-jumpcloud-systems]]:

```bash
curl -H "x-api-key: ████████" "https://console.jumpcloud.com/api/systems"
```

Then, execute [[commands/curl-jumpcloud-systemusers]]:

```bash
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"
```

Finally, execute [[commands/curl-jumpcloud-applications]]:

```bash
curl -H "x-api-key: ██████" "https://console.jumpcloud.com/api/applications"
```

Validate by checking the responses for lists of systems, users, and applications.

## Attack Chain Summary

### Key Achievements

1. Discovered leaked API key in public repo
2. Extracted and validated the key
3. Gained unauthorized access to internal JumpCloud resources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]]
- [[Credentials in Files]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Initial Access]]
- [[Discovery]]

*Last updated: [TIMESTAMP]*
