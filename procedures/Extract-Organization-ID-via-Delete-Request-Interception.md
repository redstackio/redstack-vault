---
tags:
  - request-interception
  - organization-id
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.390Z'
sub_techniques: []
id: 55e62e02-f3f0-4fe2-91d2-0f07c33b268a
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Organization-ID-via-Delete-Request-Interception

## Summary

This procedure uses a web proxy to intercept a failed organization delete attempt from a read-only account, extracting the target organization ID for use in subsequent unauthorized requests.

## Description

Logged in as the read-only user (B), attempt to delete the admin's organization, which should fail due to permissions. Intercept the HTTP DELETE request with a proxy tool like Burp Suite. The request typically includes the organization ID in the URL path (e.g., /api/organizations/{org_id}) or JSON body. This ID reveals the direct reference to the admin's object, enabling IDOR attacks. Prerequisites include active read-only access and proxy setup. Expected outcome: ID captured without alerting the server.

## Requirements

1. Read-only access to target organization
2. Proxy tool configured (e.g., Burp Suite with browser proxy settings)
3. Browser developer tools or proxy for request inspection

## Defense

Defensive measures and detection strategies:

- Enforce authorization checks on all object IDs in requests, rejecting mismatched user-org pairs
- Rate-limit failed delete attempts and log proxy-like traffic anomalies
- Use indirect references (e.g., slugs) instead of raw IDs to mitigate IDOR

## Objectives

1. Trigger a delete action from read-only session
2. Intercept and parse the request for organization ID
3. Store ID for tampering in update requests

## Instructions

### Step 1: Configure Proxy for Interception

**Context**: Set up Burp Suite to capture traffic from the read-only session.

Launch Burp Suite, start the proxy listener on localhost:8080, and configure the browser (e.g., Firefox) to use it as HTTP proxy. Install Burp's CA certificate to handle HTTPS.

> Expected: All traffic from browser routed through Burp; no interception errors.

### Step 2: Attempt Organization Delete as B

**Context**: Initiate the failed delete to generate the request.

Log in as B, navigate to the organization's page in Helium console, and attempt to delete it (e.g., click delete button or use API endpoint if available).

> The action fails with a permission error, but the request is sent.

### Step 3: Intercept and Extract Organization ID

**Context**: Capture the DELETE request in the proxy.

In Burp's Proxy > HTTP history or Interceptor, find the DELETE request (e.g., DELETE /api/v1/organizations/org_123abc). Copy the org_id from the path, headers, or body (e.g., {"organization_id": "org_123abc"}).

> Expected Output: Raw ID string, such as "org_123abc", saved for later use.

### Step 4: Forward and Verify Failure

**Context**: Ensure the request completes without suspicion.

Forward the intercepted request in Burp; observe the 403/401 response confirming read-only denial.

> Success: ID extracted, no permanent changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-interception
- organization-id
- proxy
