---
tags:
  - token-validation
  - github
type: procedure
tools:
  - '[[tools/npx]]'
  - '[[tools/asar]]'
  - '[[tools/curl]]'
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npx-asar-extract]]'
  - '[[commands/asar-extract]]'
  - '[[commands/curl-github-user-auth]]'
platforms:
  - macOS
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1e43add3-f0c0-469f-b49a-6b460ae1b3fb
created_at: '2025-12-11T06:10:40.493Z'
updated_at: '2025-12-11T06:10:40.493Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Verify GitHub Token Validity

## Summary

This procedure tests the authentication of a discovered GitHub token against the GitHub API to confirm its validity and associated user details.

## Description

After extracting a GH_TOKEN from an Electron app's .env file, use curl to make an authenticated API call to GitHub's /user endpoint. This verifies if the token is active and belongs to a valid user, such as a Shopify employee. The procedure requires the token value and internet access. Successful execution returns user details in JSON, indicating the token can be used for further access.

## Requirements

1. Valid GH_TOKEN from prior extraction
2. Curl installed
3. Access to GitHub API

## Defense

Defensive measures and detection strategies:

- Regularly rotate and monitor GitHub tokens
- Implement API rate limiting and anomaly detection for unauthorized queries

## Objectives

1. Confirm token is active
2. Retrieve user information
3. Proceed to organization and repo access checks

## Instructions

### Step 1: Authenticate to GitHub API

**Context**: Query user details to validate the token.

**Command** ([[commands/curl-github-user-auth]]):
```bash
curl -H "Authorization: token $GH_TOKEN" -H "Accept: application/vnd.github.v3+json" https://api.github.com/user
```

> Returns JSON with user details if token is valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

## Commands Used

- [[commands/curl-github-user-auth]]

## Tools Used

- [[tools/curl]]

## Tags

- [[token-validation]]
- [[commands/curl-github-user-auth]]
