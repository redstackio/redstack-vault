---
tags:
  - account-discovery
  - information-disclosure
  - api-enumeration
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-api-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:01.787Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: aee6c8b0-046d-41e2-880c-6fa5aaf97ef6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Users-Endpoint-for-Discovery

## Summary

This procedure queries Shopify's API users endpoint with a limited token to retrieve the full list of store staff, bypassing interface restrictions and enabling account discovery.

## Description

Due to mismatched controls between API and web interfaces, even no-access or limited tokens can access /admin/api/2023-10/staff_members.json. This discloses emails and roles without sensitive data but aids targeting. Prerequisites: token and store URL.

## Requirements

1. Captured access token
2. Store subdomain
3. HTTP client for GET requests

## Defense

Defensive measures and detection strategies:

- Align API and UI permission checks uniformly
- Require explicit scopes for read operations
- Monitor for bulk user queries from low-privilege tokens

## Objectives

1. Retrieve complete staff member list
2. Identify admin accounts for targeting
3. Expose user inventory for social engineering

## Instructions

### Step 1: Query Users Endpoint

**Context**: Perform GET to list all users.

Execute [[commands/curl-api-request]] with the token.

```bash
curl -H "X-Shopify-Access-Token: <token>" https://<store>.myshopify.com/admin/api/2023-10/staff_members.json
```

> Expected output: JSON array like {"staff_members": [{"id":1,"email":"admin@store.com",...}]}.

### Step 2: Parse and Validate

**Context**: Analyze response for completeness.

Save output to file and grep for emails/roles to confirm full disclosure beyond limited view.

**Expected Output**: List of all users, including hidden ones.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Discovery]]
- [[shopify]]
- [[api]]
