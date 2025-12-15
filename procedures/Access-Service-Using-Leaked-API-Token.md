---
id: proc-access-leaked-token
tags:
  - initial-access
  - collection
  - api-token
  - cloud-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-authenticate-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:32:29.323Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Access Service Using Leaked API Token

## Summary

This procedure demonstrates authenticating to a restricted web service using a leaked API token to gain unauthorized access to dashboards and sensitive data, as seen in the Mozilla telemetry service breach.

## Description

Once a token is obtained from a leak, it can be used directly in HTTP requests to authenticate as the token owner. Here, the token grants access to https://sql.telemetry.mozilla.org/, a dashboard with confidential telemetry data. The approach involves setting the token in an Authorization header (Bearer scheme common for APIs). Prerequisites: The leaked token and curl or a browser with dev tools. Outcomes include viewing restricted resources, potentially exposing internal metrics.

## Requirements

1. Leaked API token string
2. Internet access to the target URL
3. Curl installed (or equivalent HTTP client)

## Defense

Defensive measures and detection strategies:

- Rotate tokens immediately upon leak detection
- Implement token scoping and short expiration times
- Log and alert on unusual authentication patterns (e.g., from unknown IPs)
- Use API gateways with rate limiting and anomaly detection

## Objectives

1. Authenticate successfully with the leaked token
2. Access and view confidential dashboard data
3. Collect sensitive telemetry information

## Instructions

### Step 1: Test Authentication with Token

**Context**: Send an HTTP request to the service endpoint using the token to verify access.

**Command** ([[commands/curl-authenticate-api]]):
```bash
curl -H "Authorization: Bearer <leaked_token>" https://sql.telemetry.mozilla.org/
```

> This command authenticates and fetches the dashboard. Replace `<leaked_token>` with the actual token. Expected output: JSON or HTML response indicating successful login, not 401/403 errors.

### Step 2: Browse and Extract Data

**Context**: If the initial request succeeds, interact with the dashboard to view telemetry data.

Use a browser: Open dev tools, set the Authorization header, and navigate to the URL. Or chain additional curl requests to specific endpoints (e.g., `/api/data` if known).

> Expected: Access to tables/charts with Mozilla's internal telemetry datasets, confirming unauthorized viewing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[T1078.004]] Valid Accounts: Cloud Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-authenticate-api]]

## Tools Used

- None

## Tags

- [[initial-access]]
- [[Collection]]
- [[api-token]]
