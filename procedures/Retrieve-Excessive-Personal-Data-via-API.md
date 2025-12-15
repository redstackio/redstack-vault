---
tags:
  - information-disclosure
  - pii
  - api
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.030Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 81ce1a73-ad7a-43e9-9256-53bbadc1d2b7
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Excessive-Personal-Data-via-API

## Summary

This procedure exploits an API endpoint that discloses more personal information than necessary, such as full user profiles, when accessed without adequate controls, especially in combination with CORS bypass.

## Description

Targeting the profile information endpoint on https://studyroom.line.me, the API returns excessive PII like names, emails, and other details accessible via simple GET requests if the user is authenticated. This is tested using own accounts to avoid harm, confirming the lack of data minimization.

## Requirements

1. Valid session or authentication to the API (e.g., via cookies)
2. Knowledge of the profile endpoint URL
3. Cross-origin access enabled (from prior CORS test)

## Defense

Defensive measures and detection strategies:

- Limit API responses to minimal necessary data
- Implement proper authorization checks on sensitive endpoints
- Log and alert on unusual data access patterns

## Objectives

1. Extract PII from profile API
2. Demonstrate excessive disclosure
3. Prepare data for exfiltration

## Instructions

### Step 1: Access Profile Endpoint with Authentication

**Context**: Use browser dev tools or curl with session cookies to fetch profile data.

Open browser console on a test page and execute:

```javascript
fetch('https://studyroom.line.me/api/profile', {credentials: 'include'}).then(r => r.json()).then(console.log);
```

> This retrieves the JSON profile. Expected output: Object with fields like user_id, name, email, etc., confirming excessive info.

### Step 2: Test Cross-Origin Access

**Context**: Verify from unauthorized origin.

From a local HTML file:

```html
<script>fetch('https://studyroom.line.me/api/profile', {credentials: 'include'}).then(r => r.json()).then(data => console.log(data));</script>
```

> If data loads, disclosure is possible cross-origin.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[pii]]
- [[api]]
