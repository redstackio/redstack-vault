---
tags:
  - token-leak
  - information-disclosure
  - github
  - travis-ci
type: attack_chain
tools:
  - '[[tools/Travis-CI]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-travis-logs]]'
  - '[[commands/github-api-token-verify]]'
platforms:
  - Web
  - CI/CD
complexity: low
procedures:
  - '[[procedures/Identify-Leaked-Tokens-in-CI-Build-Logs]]'
  - '[[procedures/Verify-Token-Validity-and-Access-Scope]]'
  - '[[procedures/Report-Vulnerability-to-Affected-Party]]'
step_count: 3
techniques:
  - '[[Search Open Technical Databases]]'
  - '[[Unsecured Credentials]]'
description: >-
  Discovery and verification of a leaked GitHub token in public Travis CI build
  logs, potentially allowing access to Grammarly repositories
skill_level: beginner
impact_level: medium
id: 69c7ab49-b228-455a-a7fd-bbd6f6020b79
created_at: '2025-12-11T06:10:15.522Z'
updated_at: '2025-12-11T06:10:15.522Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1596]]'
  - '[[T1552]]'
---
# GitHub Token Leak Discovery in Travis CI Build Logs

## Overview

This attack chain outlines the process of identifying a leaked GitHub token exposed in public Travis CI build logs associated with Grammarly repositories. The discovery was part of broader research into Travis CI's attack surface. The token provided potential access to a limited number of repositories, but was revoked promptly after reporting, with no unauthorized access confirmed.

## Attack Flow

```mermaid
graph LR
    A[Reconnaissance: Scan Build Logs] --> B[Verification: Test Token Access]
    B --> C[Reporting: Submit Findings]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools
- [[tools/Travis-CI]]

### Target Environment
- Web-based CI/CD platform
- Publicly accessible build logs
- Services: Travis CI, GitHub

### Initial Access Requirements
- Internet access to public Travis CI logs
- No credentials needed for initial reconnaissance

## Step 1: Reconnaissance - [[procedures/Identify-Leaked-Tokens-in-CI-Build-Logs]]

### Objective

Scan public Travis CI build logs for exposed sensitive information such as GitHub tokens.

### Instructions

Access public Travis CI build logs for target repositories (e.g., Grammarly-related) and search for leaked tokens. Use [[commands/curl-travis-logs]] to fetch logs:

```bash
curl -s https://api.travis-ci.org/repos/grammarly/repo/builds | jq
```

Analyze the logs for any exposed tokens, such as those accidentally printed in build output due to improper configuration.

### Validation

Confirm the presence of a token string in the logs that matches GitHub token format.

## Step 2: Verification - [[procedures/Verify-Token-Validity-and-Access-Scope]]

### Objective

Test the discovered token to determine its validity and the scope of access it provides.

### Instructions

Use the token to query the GitHub API and verify access to repositories. Execute [[commands/github-api-token-verify]]:

```bash
curl -H "Authorization: token DISCOVERED_TOKEN" https://api.github.com/user/repos
```

Check the response for accessible repositories, confirming limited access to Grammarly repos as per the report.

### Validation

Successful API response listing repositories indicates a valid token; error responses may indicate revocation or invalidity.

## Step 3: Reporting - [[procedures/Report-Vulnerability-to-Affected-Party]]

### Objective

Submit the findings to the affected organization for remediation.

### Instructions

Compile a detailed report including the leaked token, verification results, and potential impact. Submit via a bug bounty platform like HackerOne. No specific command is used here, but ensure secure communication channels.

### Validation

Receive confirmation from the organization (e.g., Grammarly) that the token has been revoked and no unauthorized access occurred.

## Attack Chain Summary

### Key Achievements
1. Identification of exposed sensitive token in public logs
2. Verification of token's access to repositories
3. Successful reporting leading to immediate revocation
