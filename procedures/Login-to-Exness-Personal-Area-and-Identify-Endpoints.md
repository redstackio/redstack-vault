---
id: proc-login-exness-001
tags:
  - exness
  - login
  - api-discovery
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/query-exness-base-stats]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:39.172Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Login-to-Exness-Personal-Area-and-Identify-Endpoints

## Summary

This procedure authenticates a user to the Exness Personal Area and navigates to the performance summary page to inspect and identify the vulnerable stats API endpoints used for fetching trading data.

## Description

In the context of exploiting an IDOR vulnerability, initial access requires logging into the Exness web portal at https://my.exness.com. Navigating to the performance summary page triggers API calls to /v3/personal_area/stats/* endpoints, revealing the structure including the 'accounts=' parameter. This step sets up the authenticated session (via Bearer token) and documents the endpoints for subsequent manipulation. Prerequisites include valid Exness credentials; expected outcome is visibility into API behavior without alerting defenses.

## Requirements

1. Valid Exness account email and password for login.
2. Web browser with developer tools enabled (e.g., Chrome) for network inspection.
3. Stable internet access to https://my.exness.com (HTTPS/443).

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for Personal Area login to prevent credential compromise.
- Monitor for unusual network inspection patterns or API call volumes from authenticated sessions.
- Use web application firewalls (WAF) to log anomalous parameter values in API requests.

## Objectives

1. Establish an authenticated session to the Exness platform.
2. Trigger and document API endpoints for stats retrieval.
3. Obtain Bearer token for API replication.

## Instructions

### Step 1: Authenticate to Exness Personal Area

**Context**: Log in to gain access to protected pages and obtain session token.

**Command** ([[commands/query-exness-base-stats]]):
```bash
# Use browser or curl to login (manual step, token captured from response)
curl -X POST "https://api.exness.com/auth/login" -H "Content-Type: application/json" -d '{"email":"user@example.com","password":"pass"}'
```

> This command (or browser login) returns a Bearer token in the response headers or body. Capture it for subsequent API calls. Expected output: JSON with access_token.

### Step 2: Navigate to Performance Summary and Inspect Network

**Context**: Load the page to trigger API calls and identify endpoints.

**Command** ([[commands/query-exness-base-stats]]):
```bash
# No direct command; use browser to visit https://my.exness.com/pa/performance/summary and check Network tab
# Replicate initial call: curl -X GET "https://api.exness.com/v3/personal_area/stats/net_profit?time_range=365&accounts={ownAccount}" -H "Authorization: Bearer {token}"
```

> Inspect DevTools Network tab for requests to /v3/personal_area/stats/* with parameters time_range=365 and accounts={accountNumber}. Document endpoints like net_profit, equity. Expected output: Initial JSON stats for own account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/query-exness-base-stats]]

## Tools Used

- [[tools/curl]]

## Tags

- exness
- login
- api-discovery
