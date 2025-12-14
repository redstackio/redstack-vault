---
id: proc-id-mozilla-endpoint-identify
tags:
  - idor
  - web
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-inspect-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:47.443Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify Vulnerable Delete Endpoint in Mozilla Monitor

## Summary

This procedure involves inspecting the Mozilla Monitor application's delete secondary email feature to identify the endpoint and request structure, revealing the IDOR vulnerability where email IDs are directly referenceable without authorization scoping.

## Description

In the Mozilla Monitor web application, the delete secondary email feature uses a direct object reference for the email ID in the API request. By capturing legitimate delete requests from an authenticated session, attackers can analyze the endpoint (e.g., `/api/emails/{id}`) and confirm that it lacks user-specific checks, enabling exploitation against other accounts. This step is crucial for understanding the vulnerability before attempting unauthorized deletions, targeting web-based identity management systems.

## Requirements

1. Authenticated access to Mozilla Monitor account
2. Browser with developer tools or proxy tool like Burp Suite
3. Basic knowledge of HTTP requests and API structures

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks scoping operations to the authenticated user
- Log and monitor API requests for anomalous email ID usage
- Use rate limiting on delete operations to detect abuse

## Objectives

1. Locate the delete secondary email API endpoint
2. Extract the email ID parameter format
3. Confirm lack of user scoping in the request

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to Mozilla Monitor and access the secondary email management to prepare for request inspection.

**Command** ([[commands/curl-inspect-request]]):
```bash
# No direct command; use browser or proxy to navigate
```

> Manually log in via browser at https://monitor.mozilla.org, go to account settings > secondary emails, and attempt to delete one of your own emails to trigger the request.

### Step 2: Capture and Analyze Request

**Context**: Intercept the delete request to identify the vulnerable endpoint and ID reference.

**Command** ([[commands/curl-inspect-request]]):
```bash
curl -X GET 'https://monitor.mozilla.org/api/emails' -H 'Authorization: Bearer YOUR_TOKEN'  # First, list emails to see IDs
```

> Use Burp Suite or browser dev tools to capture the DELETE request. Look for patterns like `DELETE /api/emails/12345` where `12345` is the email ID. Expected output: Request details showing direct ID usage without user context.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[web]]
- [[recon]]
