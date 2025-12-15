---
tags:
  - video-manipulation
  - unauthorized-modify
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-move-video-version]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 861d0315-80ed-48e4-bd47-74a433b5d024
created_at: '2025-12-14T17:32:39.452Z'
updated_at: '2025-12-14T17:32:39.452Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Move-Victims-Video-Version-to-Attackers-Video

## Summary

This procedure crafts an API request to associate a victim's private video version with the attacker's video, enabling content hijacking without proper authorization.

## Description

By exploiting the same improper authentication, the attacker sends a POST request to the versions endpoint of their own video, specifying the victim's version ID in the payload. This moves the version linkage, causing the victim's private content to be served under the attacker's video. The target environment is Vimeo's API, requiring the attacker's video ID and victim's version ID (obtained from prior access). Outcomes include successful version reassignment, leading to potential leakage.

## Requirements

1. Attacker's video ID and API token
2. Victim's private video version ID (from Step 1)
3. Ability to craft JSON payloads in HTTP requests

## Defense

Defensive measures and detection strategies:

- Enforce ownership and account type validation on version modification requests
- Log and alert on cross-video version associations
- Implement input validation to prevent unauthorized version IDs

## Objectives

1. Reassign victim's private version to attacker's resource
2. Prepare for content exfiltration
3. Achieve data tampering without detection

## Instructions

### Step 1: Craft and Send Move Request

**Context**: Use a POST request to the attacker's video versions endpoint, including the victim's version ID to perform the move.

**Command** ([[commands/curl-move-video-version]]):
```bash
curl -X POST -H "Authorization: bearer YOUR_ATTACKER_TOKEN" -d '{"version_id": VICTIM_VERSION_ID}' https://api.vimeo.com/videos/ATTACKER_VIDEO_ID/versions
```

> This submits the version ID in JSON format. Expected output is a 200 OK response with confirmation. The victim's version is now linked to the attacker's video.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-move-video-version]]

## Tools Used


## Tags

- [[video-manipulation]]
- [[unauthorized-modify]]
