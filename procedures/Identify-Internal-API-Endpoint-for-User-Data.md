---
tags:
  - api-recon
  - information-disclosure
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-api-call]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:39.397Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 680c276b-f850-47c0-a19b-1c2ac27e39ae
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Internal-API-Endpoint-for-User-Data

## Summary

This procedure involves inspecting the frontend application of the LGTM platform to identify the internal getPersonBySlug API endpoint, revealing its lack of authorization checks and potential to expose sensitive user data like email addresses.

## Description

In the context of Semmle's LGTM platform, the frontend makes unauthenticated calls to internal APIs for user profile retrieval. By monitoring network traffic, attackers can discover the getPersonBySlug method, which fetches data including emails for accounts linked to Google, without verifying user permissions. This reconnaissance step is crucial for identifying information disclosure risks in web applications with integrated third-party services like Google Accounts.

## Requirements

1. Access to the LGTM web frontend
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTTP requests and JSON responses

## Defense

Defensive measures and detection strategies:

- Implement API gateway with rate limiting and auth enforcement
- Monitor for anomalous API calls from non-authenticated sources
- Use web application firewalls (WAF) to block unauthorized endpoint access

## Objectives

1. Discover the API endpoint structure and parameters
2. Confirm absence of authorization headers or checks
3. Identify exposed sensitive fields like email

## Instructions

### Step 1: Monitor Frontend Network Traffic

**Context**: Open the LGTM platform in a browser and navigate to a user profile page to trigger API calls.

**Command** ([[commands/curl-api-call]]):
Use DevTools Network tab to filter for XHR/Fetch requests and inspect calls to /person endpoints.

> This reveals the getPersonBySlug method and its response format, showing email exposure for Google-linked accounts.

### Step 2: Test Endpoint Accessibility

**Context**: Verify the endpoint responds without authentication by replicating the request.

**Command** ([[commands/curl-api-call]]):
```bash
curl -X GET "https://api.lgtm.com/person/test-slug" -H "Accept: application/json" -v
```

> Expected output includes verbose headers confirming no auth requirement, and JSON with user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-call]]

## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- [[api-recon]]
- [[web-vulnerability]]
