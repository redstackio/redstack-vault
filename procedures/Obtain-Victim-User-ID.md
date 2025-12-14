---
id: proc-snapchat-userid-001
name: Obtain-Victim-User-ID
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.359Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - user-discovery
  - api-enumeration
platforms:
  - Web
  - Mobile (Android)
commands: []
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Obtain-Victim-User-ID

## Summary

This procedure extracts the victim's user_id from Snapchat's API responses, such as friend request endpoints, which expose it without proper access controls, enabling targeting for the OTP exploit.

## Description

Snapchat's API leaks user_ids in responses to authenticated requests like /friends/get, even for non-friended users if discoverable. Using the attacker's session, intercept and parse these responses in Burp Suite. This is a discovery step prerequisite for the authentication bypass. Target environment: Authenticated mobile API calls. Expected outcome: Numeric user_id for the victim.

## Requirements

1. Active attacker session from previous procedure
2. Victim's username (to search friends or public endpoints)
3. Burp Suite for request interception and response inspection
4. Knowledge of API endpoints like /friends/get or /phoenix/connections/

## Defense

Defensive measures and detection strategies:

- Remove user_id from non-essential API responses
- Implement role-based access to friend data
- Log and alert on excessive friend enumeration requests

## Objectives

1. Discover victim's unique user_id
2. Validate exposure in API
3. Prepare for OTP token exploitation

## Instructions

### Step 1: Send Friend Request or List Query

**Context**: Use an authenticated GET to friend endpoints to retrieve user details including IDs.

**Command** ([[curl-friend-enumerate]]):
```bash
curl -X GET 'https://gcp.api.snapchat.com/phoenix/connections/friends/get' -H 'X-Snapchat-Client-Auth: [token]' -H 'User-Agent: Snapchat/10.78.1.0 [device]'
```

> Expected output: JSON array with {"user_id": "[victim_user_id]", "username": "[victim_username]", ...}. Search for the target victim.

### Step 2: Extract and Verify ID

**Context**: Parse the response in Burp or manually to isolate the user_id.

No command; manual extraction.

> Success if user_id is a valid numeric string associated with the victim's username.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- user-discovery
- api-enumeration
