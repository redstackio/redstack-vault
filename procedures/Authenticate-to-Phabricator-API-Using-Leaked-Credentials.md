---
tags:
  - authentication
  - api-access
  - phabricator
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: dc0bb3d0-053f-4046-9166-eb5c9dfbab50
created_at: '2025-12-11T03:48:06.080Z'
updated_at: '2025-12-11T03:48:06.080Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Authenticate to Phabricator API Using Leaked Credentials

## Summary

This procedure uses discovered leaked credentials (username and certificate) to authenticate to a Phabricator API endpoint, gaining unauthorized access to internal resources like source code and project details.

## Description

The procedure targets web-based Phabricator instances where credentials have been leaked. By authenticating with the stolen username and certificate, an attacker can access API functions on domains like code.uberinternal.com. Expected outcomes include disclosure of sensitive internal information.

## Requirements

1. Leaked username and certificate file
2. Network access to the target API endpoint
3. Curl or similar HTTP client installed

## Defense

Defensive measures and detection strategies:

- Rotate credentials regularly and monitor for leaks
- Implement multi-factor authentication and API rate limiting

## Objectives

1. Authenticate to the API using leaked credentials
2. Verify access to protected resources
3. Potentially exfiltrate data like source code

## Instructions

### Step 1: Prepare Credentials

**Context**: Ensure the leaked certificate and username are ready for use in authentication.

> No specific command; manually verify the certificate file (e.g., leaked_certificate.pem) and username.

### Step 2: Authenticate to API

**Context**: Send an authenticated request to the Phabricator API.

**Command** ([[commands/curl-authenticate-api]]):
```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api/
```

> This command uses basic auth with the username and attaches the certificate for TLS client authentication; expect a successful response if credentials are valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/curl-authenticate-api]]

## Tools Used

- #curl

## Tags

- [[Authentication]]
- #phabricator
