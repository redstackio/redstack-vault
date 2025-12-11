---
tags:
  - token-verification
  - credential-access
type: procedure
tools:
  - '[[tools/Travis-CI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-travis-logs]]'
  - '[[commands/github-api-token-verify]]'
platforms:
  - Web
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials in Files]]'
id: cfdd4937-0681-4bd1-a20a-22f360b33035
created_at: '2025-12-11T06:10:15.515Z'
updated_at: '2025-12-11T06:10:15.515Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1552]]'
---
# Verify Token Validity and Access Scope

## Summary

This procedure tests the validity of a discovered API token and determines the scope of resources it can access, such as GitHub repositories.

## Description

Using the leaked token from Travis CI logs, query the GitHub API to confirm its ability to access a limited number of Grammarly repositories. This step is inferred from the report and helps assess the potential impact of the leak.

## Requirements
1. The discovered token string
2. Access to GitHub API endpoints
3. Tools like curl for API requests

## Defense

- Implement token expiration and scope limitations
- Monitor API logs for unauthorized token usage
- Use secret scanning tools on repositories

## Objectives
1. Confirm token is active
2. Enumerate accessible resources
3. Document access level for reporting

## Instructions

### Step 1: Test Token with GitHub API

**Context**: Send an authenticated request to list repositories.

**Command** ([[commands/github-api-token-verify]]):
```bash
curl -H "Authorization: token DISCOVERED_TOKEN" https://api.github.com/user/repos
```

> Expect a JSON response listing repositories if valid; analyze for Grammarly-specific access.

### Step 2: Check for Errors

**Context**: Handle responses indicating invalid or revoked tokens.

Review HTTP status codes (e.g., 401 Unauthorized) to confirm validity.

## MITRE ATT&CK Mapping

### Tactics
- [[Discovery]]

### Techniques
- [[Unsecured Credentials]]

### Sub-Techniques
- [[Credentials in Files]]

## Commands Used
- [[commands/github-api-token-verify]]

## Tools Used

## Tags
- token-verification
- credential-access
