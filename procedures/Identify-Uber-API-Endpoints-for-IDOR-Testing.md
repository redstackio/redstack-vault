---
id: p1q2r3s4-t5u6-7890-bcde-fg1234567890
tags:
  - api
  - recon
  - idor
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-api-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:17.777Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Uber API Endpoints for IDOR Testing

## Summary

This procedure involves inspecting network traffic in Uber's web or app interface to identify API endpoints in the U4B and Vouchers services that use direct object references, setting the stage for IDOR exploitation by revealing manipulable identifiers like organization and voucher IDs.

## Description

In the context of Uber's U4B platform, users with business accounts interact with APIs for managing vouchers and policies. By monitoring these interactions, attackers can map endpoints vulnerable to IDOR, where authorization is not properly enforced on object IDs. This reconnaissance step is crucial for chaining exploits to access PII and modify policies, assuming an authenticated session. Expected outcomes include a catalog of endpoints ready for parameter tampering, typically completed in under 5 minutes with developer tools.

## Requirements

1. Valid Uber account with U4B access for authentication.
2. Browser with developer tools (e.g., Chrome DevTools) or proxy tool like Burp Suite.
3. Network access to Uber's API domains over HTTPS.

## Defense

Defensive measures and detection strategies:

- Implement API gateway logging to monitor unusual endpoint access patterns.
- Enforce strict authorization checks on all object IDs using indirect references or session-bound scoping.
- Use web application firewalls (WAF) to detect ID parameter anomalies in requests.

## Objectives

1. Catalog API endpoints handling organization and voucher data.
2. Identify ID parameters susceptible to manipulation.
3. Establish baseline for authenticated requests to replay in exploits.

## Instructions

### Step 1: Authenticate and Navigate to U4B Interface

**Context**: Gain an authenticated session and trigger API calls by interacting with voucher management features to capture traffic.

**Command** ([[commands/curl-api-request]]):
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -X GET "https://api.uber.com/v1/business/vouchers" -o endpoints.json
```

> This command fetches initial voucher data; inspect the response and request headers in a tool like Burp to note endpoint patterns. Expected output: JSON with voucher listings, revealing ID structures.

### Step 2: Monitor and Extract Endpoint Details

**Context**: Use proxy or dev tools to log requests while creating or viewing vouchers, focusing on paths containing {org_id} or {voucher_id}.

No specific command; manually inspect traffic for endpoints like `/v1/organizations/{org_id}/employees` or `/v1/vouchers/{voucher_id}/policy`.

> Document IDs from responses (e.g., extract foreign org_ids from error messages during enumeration). Expected output: List of 5-10 endpoints with parameter details.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-request]]

## Tools Used


## Tags

- [[api]]
- [[recon]]
- [[idor]]
