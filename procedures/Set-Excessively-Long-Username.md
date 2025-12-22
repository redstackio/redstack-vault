---
id: proc-uuid-2
tags:
  - dos
  - input-validation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-submit-long-username]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.454Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Set-Excessively-Long-Username

## Summary

This procedure demonstrates submitting an arbitrarily long username via the hey.com edit form, bypassing client-side checks and injecting data that causes rendering issues in client applications.

## Description

The hey.com platform does not enforce server-side limits on username length, allowing strings exceeding 10,000 characters to be set. This leads to denial of service when the name is rendered in lists like contacts or messages, as UI components fail to handle the size. Prerequisites include an active session; outcomes include successful update and subsequent client disruptions.

## Requirements

1. Active hey.com session cookie
2. File with long string (e.g., name.txt >10k chars)
3. User ID for the target endpoint

## Defense

Defensive measures and detection strategies:

- Enforce server-side length limits (e.g., 255 chars) on name fields
- Monitor for oversized POST payloads and rate-limit edit requests

## Objectives

1. Inject oversized data into user profile
2. Trigger client-side rendering failures
3. Validate update without immediate rejection

## Instructions

### Step 1: Prepare Long String

**Context**: Generate or load an excessively long input to exceed processing limits.

Create name.txt with repeated characters (e.g., echo 'A' > /dev/null | head -c 10000 > name.txt).

> File ready with oversized content.

### Step 2: Submit via Form or curl

**Context**: POST the long name to the edit endpoint.

**Command** ([[commands/curl-submit-long-username]]):
```bash
curl -X POST -d "name=$(cat name.txt)" https://app.hey.com/contacts/%user_id_number%/user/edit -H "Cookie: your_session_cookie" -H "Content-Type: application/x-www-form-urlencoded"
```

> Response indicates successful update (200 OK); long name now stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used

- [[commands/curl-submit-long-username]]

## Tools Used


## Tags

- dos
- input-validation
