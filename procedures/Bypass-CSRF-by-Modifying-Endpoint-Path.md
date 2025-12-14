---
id: proc-bypass-csrf-path-95555
tags:
  - csrf
  - bypass
  - twitter
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/bypassed-vote-submission-without-json-extension]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.008Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass CSRF by Modifying Endpoint Path

## Summary

This procedure exploits a flaw in Twitter's CSRF protection by altering the API endpoint path from /i/cards/api/v1.json to /i/cards/api/v1, evading the token check and allowing unauthorized vote submission.

## Description

The server enforces _authenticity_token only on the exact .json path, but accepts requests to the base path without it, processing the vote normally. This enables attackers to send POST requests with poll parameters, recording votes using the victim's session cookies without explicit consent.

## Requirements

1. Captured parameters from a normal request (tweet_id, card_uri, etc.)
2. Authenticated Twitter session (for testing; in attack, victim's browser)
3. Tool to send HTTP requests (e.g., curl or proxy)

## Defense

Defensive measures and detection strategies:

- Standardize CSRF checks across path variations and extensions
- Log and alert on API requests missing tokens, even on alternate paths
- Implement SameSite cookies and token binding to session

## Objectives

1. Submit vote request without CSRF token via modified path
2. Confirm successful vote recording (HTTP 200)
3. Validate bypass for CSRF attack chaining

## Instructions

### Step 1: Modify and Send Request

**Context**: Change the endpoint by removing .json and omit the token, reusing analyzed parameters.

**Command** ([[commands/bypassed-vote-submission-without-json-extension]]):
```bash
curl -X POST "https://twitter.com/i/cards/api/v1?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1" \
  -H "Content-Type: application/json" \
  -d '{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}'
```

> Expects HTTP 200; include session cookies for real authentication.

### Step 2: Verify Vote Recording

**Context**: Check the poll on Twitter to confirm the vote was applied.

No command; manually inspect the tweet or API response for success indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/bypassed-vote-submission-without-json-extension]]

## Tools Used


## Tags

- csrf
- bypass
- path-modification
- twitter
