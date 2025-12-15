---
tags:
  - api-replay
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:12.864Z'
sub_techniques: []
id: 48564a1c-bc75-4733-a6b1-7235191281bc
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Replay-Intercepted-API-Request-for-User-Data

## Summary

This procedure replays the captured HTTP request to the unauthenticated API endpoint in Burp Suite, directly querying for a target user's sensitive data using their phone number.

## Description

Using Burp's Repeater, attackers send the GET request to the exposed endpoint /vtu-service/api/pwa/pub/get-bio-data/{phone_number}, bypassing the web interface. This exploits the lack of authorization in MTN's WildFly/Undertow-based app. Expected: Immediate data retrieval without creds.

## Requirements

1. Intercepted request from previous procedure
2. Burp Suite Repeater tab open
3. Target phone number (MTN format, e.g., 081xxxxxxxx)

## Defense

Defensive measures and detection strategies:

- Add authentication tokens or API keys to all endpoints
- Implement input validation and rate limiting on phone number queries
- Monitor API logs for direct access patterns without web interface referrals

## Objectives

1. Send direct API request without web form
2. Retrieve JSON response with user profile
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Load Request into Repeater

**Context**: Transfer the intercepted request to Burp Repeater for manipulation.

In Burp Proxy, right-click the captured request and select "Send to Repeater".

> Request appears in Repeater tab, ready for editing.

### Step 2: Modify and Send Request

**Context**: Update the phone number parameter and execute the request.

Edit the path to /vtu-service/api/pwa/pub/get-bio-data/07012345678, ensure headers (e.g., User-Agent, Accept: application/json), and click Send.

> Expected: HTTP 200 with JSON payload including user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[api-replay]]
- [[information-disclosure]]
