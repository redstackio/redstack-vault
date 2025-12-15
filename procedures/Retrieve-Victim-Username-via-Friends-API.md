---
tags:
  - information-disclosure
  - api-abuse
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-friends-api-disclose]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.473Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f9d3b682-70c0-4089-b575-a5e726e9bc64
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve-Victim-Username-via-Friends-API

## Summary

This procedure exploits an information disclosure in the friends API to retrieve a victim's username from their user ID, enabling targeted IDOR attacks.

## Description

The POST endpoint /api.ashx/v2/users/{userId}/friends.json accepts any valid session and arbitrary RequesteeId without access controls, returning profile details including username in ProfileUrl. This aids in account discovery for takeover.

## Requirements

1. Valid authenticated session
2. Known victim user ID
3. Tool for sending POST requests (e.g., curl or browser)

## Defense

Defensive measures and detection strategies:

- Enforce access controls on API endpoints to verify requester permissions
- Rate-limit requests to user-related APIs
- Sanitize and log exposed profile data

## Objectives

1. Disclose victim's username
2. Gather intel for IDOR exploitation
3. Identify targets without direct access

## Instructions

### Step 1: Prepare Request

**Context**: Construct the POST request with victim's ID.

Set RequesteeId to the target user ID.

### Step 2: Send Disclosure Request

**Context**: Query the API to extract username from response.

Execute [[commands/curl-friends-api-disclose]]:

```bash
curl -X POST https://target-site.com/api.ashx/v2/users/12345/friends.json \
  -H "Cookie: session=valid_session" \
  -d "RequesteeId=12345" \
  -s
```

> Parse JSON response for ProfileUrl (e.g., /profile/victim_username) to derive username.

**Expected Output**: JSON with friends list including ProfileUrl containing username.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-friends-api-disclose]]

## Tools Used


## Tags

- information-disclosure
- api-abuse
