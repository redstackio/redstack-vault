---
tags:
  - wordpress
  - information-disclosure
  - ajax
  - unauthenticated
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-ajax-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:17.941Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5c8bad0d-e433-44e6-87e4-e99a2b96f3a8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
---
# Access Sensitive Information via Computed AJAX Endpoints

## Summary

This procedure exploits the predictable AJAX endpoints identified in the Redux Framework plugin to send unauthenticated requests and retrieve sensitive system information, such as configuration details or plugin data.

## Description

Using the MD5 hashes computed from the site URL and salts, construct and send POST requests to WordPress's admin-ajax.php endpoint with action parameters like 'redux_support' or 'redux_redux'. The lack of authentication checks allows retrieval of sensitive info. Targets vulnerable WordPress installations; outcomes include exposure of system details, rated medium severity (CVSS 4.6). Prerequisites: Computed hashes from prior procedure and network access to the site.

## Requirements

1. Computed MD5 hashes from site URL + salts
2. Target site accessible via HTTP/HTTPS
3. Curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Enforce nonce or authentication tokens on AJAX actions
- Rate-limit requests to admin-ajax.php
- Log and alert on requests with hashed action parameters from unknown IPs

## Objectives

1. Send unauthenticated AJAX requests to guessed endpoints
2. Extract sensitive system information from responses
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Construct Endpoint URL

**Context**: Build the full AJAX URL using the target site's wp-admin path and computed hash.

No command; example URL: https://example.com/wp-admin/admin-ajax.php.

### Step 2: Send Unauthenticated Request

**Context**: POST data to the endpoint with action tied to the hash, bypassing auth to fetch sensitive info.

**Command** ([[commands/curl-ajax-request]]):
```bash
curl -X POST 'https://example.com/wp-admin/admin-ajax.php' \
  -d 'action=redux_support&endpoint=computed_hash_here' \
  -H 'Content-Type: application/x-www-form-urlencoded'
```

> Replace 'computed_hash_here' with the MD5 hash (e.g., from '-support' salt). Successful response contains sensitive data like system info; errors indicate invalid hash or patched plugin.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-ajax-request]]

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[unauthenticated]]
- [[cve-2021-38314]]
