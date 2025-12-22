---
id: proc-analyze-normal-vote-95555
tags:
  - csrf
  - analysis
  - twitter
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/normal-vote-submission-to-twitter-cards-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:29.018Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze Normal Vote Request to Twitter Cards API

## Summary

This procedure involves intercepting and analyzing a legitimate poll vote request to Twitter's cards API to understand the request structure and confirm the CSRF token enforcement, setting the stage for bypass exploitation.

## Description

In the attack scenario, an authenticated user submits a vote on a Twitter poll card via a POST request to /i/cards/api/v1.json. The server requires an _authenticity_token for CSRF protection on this exact path. Without it, the request fails with HTTP 403. This analysis reveals parameters like tweet_id, card_name, and JSON payload with card_uri and selected_choice, which are reused in the bypass.

## Requirements

1. Access to Twitter with an authenticated session
2. Web proxy tool (e.g., Burp Suite) for request interception
3. Knowledge of a target poll tweet ID (e.g., 657629231309041664)

## Defense

Defensive measures and detection strategies:

- Implement comprehensive CSRF token validation regardless of path variations
- Monitor for anomalous API requests from authenticated sessions
- Use Web Application Firewall (WAF) rules to detect missing tokens on sensitive endpoints

## Objectives

1. Capture and document the protected request format
2. Verify CSRF enforcement on the standard endpoint
3. Identify reusable parameters for bypass testing

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Perform a normal vote on a Twitter poll to capture the request in a proxy tool.

**Command** ([[commands/normal-vote-submission-to-twitter-cards-api]]):
```bash
curl -X POST "https://twitter.com/i/cards/api/v1.json?tweet_id=657629231309041664&card_name=poll2choice_text_only&forward=false&capi_uri=capi%3A%2F%2Fpassthrough%2F1" \
  -H "Content-Type: application/json" \
  -d '{"twitter:string:card_uri":"card://657629230759415808","twitter:long:original_tweet_id":"657629231309041664","twitter:string:selected_choice":"2"}'
```

> This simulates the request without the token, expecting HTTP 403. In a real session, include cookies and the token for success.

### Step 2: Analyze Response and Parameters

**Context**: Review the 403 response to confirm CSRF block and note all query and body parameters for reuse.

No command needed; inspect proxy logs for details like forward=false (disables forwarding) and capi_uri (passthrough encoding).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning: Scanning Application Protocol Implementation

### Sub-Techniques


## Commands Used

- [[commands/normal-vote-submission-to-twitter-cards-api]]

## Tools Used


## Tags

- csrf
- twitter
- api
- analysis
