---
id: proc-37signals-exchange-token-001
tags:
  - oauth2
  - token-exchange
  - api-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-authorization-token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:30:07.303Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Exchange-Code-for-Access-Token

## Summary

This procedure exchanges the captured authorization code for a long-lived access token, granting full API access to the victim's 37signals account.

## Description

Using the code from the redirect, POST to /authorization/token with client credentials. This completes the OAuth flow, providing an access token usable for Basecamp 3 API calls without further interaction.

## Requirements

1. Authorization code from previous step
2. Client_id, client_secret, redirect_uri
3. Access to token endpoint

## Defense

Defensive measures and detection strategies:

- Bind codes to specific client and redirect_uri
- Shorten code lifetimes
- Audit token issuances for anomalies

## Objectives

1. Obtain access token
2. Validate API access
3. Achieve persistent unauthorized access

## Instructions

### Step 1: Prepare Token Request

**Context**: Gather parameters for the POST.

Ensure code, client_id, etc., are ready.

**Expected Output**: Formatted request body.

### Step 2: Execute Exchange

**Context**: Submit to token endpoint.

Execute [[commands/post-authorization-token]]:

```bash
curl -X POST https://launchpad.37signals.com/authorization/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "type=web_server&client_id={your-client-id}&redirect_uri={your-redirect-uri}&client_secret={your-client-secret}&code={authorization-code}"
```

> Returns JSON with access_token; use for API requests like GET /api/v1/projects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used

- [[commands/post-authorization-token]]

## Tools Used


## Tags

- oauth2
- token-exchange
