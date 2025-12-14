---
tags:
  - osint
  - idor
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:32:58.230Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 10614184-afee-4443-bebb-b1bcf574bc96
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Steal Web Session Cookie]]'
---
# Staff-Account-Takeover-via-OSINT-and-IDOR

## Summary

This procedure uses the extracted API token to list staff, performs OSINT on social media for a staff ID, and exploits IDOR on the staff endpoint to retrieve credentials.

## Description

With the token, GET /api/staff lists members. Twitter OSINT (@BountyPayHQ retweet) reveals Sandra's ID STF:8FJ3KFISL3. POST /api/staff with this ID returns her credentials without auth checks.

## Requirements

1. API token from APK
2. Access to Twitter for OSINT
3. Tool like Burp for API requests

## Defense

- Require authentication for sensitive API endpoints
- Validate staff_id against user permissions (prevent IDOR)
- Limit public OSINT exposure of internal IDs

## Objectives

1. Enumerate staff via API
2. Identify target via OSINT
3. Retrieve credentials via IDOR

## Instructions

### Step 1: List Staff with Token

**Context**: Use token to GET staff list.

Use Burp or curl: GET https://api.bountypay.h1ctf.com/api/staff with Authorization: Bearer <token>.

> Returns list of staff.

### Step 2: OSINT for Staff ID

**Context**: Search social media for new staff.

No command; check Twitter @BountyPayHQ for retweets mentioning Sandra, ID STF:8FJ3KFISL3.

> Obtains specific staff_id.

### Step 3: Retrieve Credentials

**Context**: POST to /api/staff with ID.

POST https://api.bountypay.h1ctf.com/api/staff with JSON {"staff_id": "STF:8FJ3KFISL3"} and token.

> Returns sandra.allison / s4ndra!b00typay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Discovery]] Account Discovery
- [[Steal Web Session Cookie]] Data from Information Repositories

### Sub-Techniques

- None

## Commands Used

None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[osint]]
- [[idor]]
- [[auth-bypass]]
