---
id: bfdf4c54-5517-4645-8fb1-fdc3373de22d
name: Access Phabricator API Using Leaked Credentials
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.530Z'
updated_at: '2025-12-11T06:10:15.530Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - api-access
  - phabricator
commands:
  - '[[commands/git-clone-public-repo]]'
  - '[[commands/curl-api-authenticate]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1078]]'
---

# Access Phabricator API Using Leaked Credentials

## Summary

This procedure uses leaked usernames and certificates to authenticate and gain unauthorized access to a Phabricator API endpoint, potentially allowing exposure of internal source code and data.

## Description

Leveraging credentials discovered from insecure storage, attackers authenticate to the Phabricator API on a domain like code.uberinternal.com. The target is a web-based code collaboration platform, and success results in API access for further exploitation or data exfiltration.

## Requirements

1. Leaked username and certificate file
2. Network access to the target API endpoint
3. Tool like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication on APIs
- Monitor for anomalous API access logs

## Objectives

1. Authenticate to the API using leaked credentials
2. Verify access to internal resources
3. Explore available endpoints for data exposure

## Instructions

### Step 1: Authenticate to API

**Context**: Use the leaked certificate and username to make an authenticated API request.

**Command** ([[commands/curl-api-authenticate]]):
```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api endpoint
```

> This command sends an authenticated request; replace 'endpoint' with specific Phabricator API paths.

### Step 2: Query API Endpoints

**Context**: Once authenticated, query available API methods to confirm access and explore data.

**Command** ([[commands/curl-api-authenticate]]):
```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api/user.whoami
```

> Expect a response confirming the authenticated user and access level.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

## Commands Used

- [[commands/curl-api-authenticate]]

## Tools Used

## Tags

- [[api-access]]
- [[phabricator]]
