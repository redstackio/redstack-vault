---
tags:
  - api-disclosure
  - idor
  - twitter-media-studio
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/twitter-ingest-list-get]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 00670dae-6116-4dfc-9c06-928cb3c201af
created_at: '2025-12-14T17:25:13.084Z'
updated_at: '2025-12-14T17:25:13.084Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Retrieve-Sensitive-Source-Information-via-API

## Summary

This procedure exploits an IDOR and information disclosure vulnerability in Twitter Media Studio's API, allowing an Analyst to retrieve victim producer source details (names, URLs, keys) despite UI restrictions, enabling unauthorized broadcast creation.

## Description

The API endpoint https://studio.twitter.com/1/live/ingest/list.json lacks proper role validation when owner_id and user_id parameters are supplied, permitting analysts to access data owned by others. This step follows account switching, using network inspection to gather account_id. The target is the Live Ingest service in Twitter Media Studio web platform. Prerequisites: Analyst access and UI verification; outcomes include JSON disclosure of sensitive sources for exfiltration or misuse.

## Requirements

1. Analyst session switched to victim account
2. account_id from network traffic inspection
3. owner_id (victim's user ID) and user_id (analyst's user ID)
4. Authorization token from browser session

## Defense

Defensive measures and detection strategies:

- Validate user ownership and role on all API parameters
- Implement rate limiting and logging for ingest endpoints
- Audit API calls for mismatched owner_id and user_id

## Objectives

1. Query API to bypass UI and disclose sources
2. Extract names, URLs, and keys
3. Enable unauthorized use of victim's sources

## Instructions

### Step 1: Obtain Account ID via Network Inspection

**Context**: Use developer tools to capture account_id from producer page requests.

Open Browser Developer Tools > Network tab, refresh https://studio.twitter.com/producer, and inspect requests for account_id.

> Expected output: account_id value extracted from traffic.

### Step 2: Execute API Request

**Context**: Send GET request with parameters to retrieve ingest list.

**Command** ([[commands/twitter-ingest-list-get]]):
```bash
curl -X GET "https://studio.twitter.com/1/live/ingest/list.json?account_id=ACCOUNT_ID&owner_id=OWNER_ID&user_id=USER_ID" -H "Authorization: Bearer SESSION_TOKEN"
```

> This command fetches the JSON list; replace placeholders with actual IDs and token from browser. Expected output: JSON array with source objects containing name, url, and key fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/twitter-ingest-list-get]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[api-disclosure]]
- [[idor]]
- [[twitter-media-studio]]
