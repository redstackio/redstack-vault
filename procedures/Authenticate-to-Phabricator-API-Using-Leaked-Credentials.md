---
tags:
  - api-access
  - phabricator
  - unauthorized-access
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
id: 51f8b714-2d4a-4bbe-98f2-22e969fa24cc
created_at: '2025-12-14T17:32:48.605Z'
updated_at: '2025-12-14T17:32:48.605Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate to Phabricator API Using Leaked Credentials

## Summary

This procedure uses discovered leaked credentials (username and certificate) to authenticate to a Phabricator API endpoint, granting unauthorized access to internal instance data and source code repositories.

## Description

The attack targets Phabricator instances like code.uberinternal.com, where API access is protected by username-certificate authentication. By supplying the leaked details, attackers bypass normal access controls. The scenario assumes credentials are valid and unrevoked. Outcomes include API queries for sensitive data. Prerequisites: Valid leaked credentials and network access to the API endpoint.

## Requirements

1. Leaked username and certificate file
2. Network connectivity to the Phabricator domain (e.g., code.uberinternal.com)
3. API client like curl for testing authentication

## Defense

Defensive measures and detection strategies:

- Rotate and revoke certificates immediately upon leak detection
- Implement API rate limiting and IP whitelisting
- Log and monitor authentication attempts with anomaly detection

## Objectives

1. Establish authenticated session to Phabricator API
2. Retrieve internal data such as source code or instance metadata
3. Escalate access to private repositories

## Instructions

### Step 1: Prepare Authentication Request

**Context**: Set up the credentials for API use.

Load the certificate and username into your API client.

```bash
export USERNAME="leaked-username"
export CERT_PATH="/path/to/leaked-cert.pem"
```

> This prepares environment variables for reuse in requests.

### Step 2: Test API Authentication

**Context**: Send a basic request to verify access.

Use curl to authenticate to a info endpoint:

```bash
curl -u $USERNAME: --cert $CERT_PATH https://code.uberinternal.com/api/phabricator.info
```

> Expected output is JSON with Phabricator version and instance details, indicating successful auth.

### Step 3: Query Sensitive Data

**Context**: Expand access to retrieve source code or repositories.

Query for repository data:

```bash
curl -u $USERNAME: --cert $CERT_PATH https://code.uberinternal.com/api/diffusion.repository.search
```

> Successful output lists accessible repositories, allowing further enumeration of source code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-access]]
- [[phabricator]]
- [[unauthorized-access]]
