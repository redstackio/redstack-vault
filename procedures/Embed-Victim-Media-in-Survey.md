---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - media-embedding
  - unauthorized-access
  - idor-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:29.578Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Embed-Victim-Media-in-Survey

## Summary

This procedure covers forwarding the modified request and verifying the embedding of unauthorized media in Crowdsignal surveys, including extensions to headers, footers, and team polls.

## Description

After modification, the server processes the request without validating media ownership, allowing the attacker's survey to display and embed the victim's private media. This can be repeated for survey headers/footers or team poll edits via /polls/:pollId/edit, potentially exposing sensitive content like images or videos.

## Requirements

1. Successfully modified request from prior procedure
2. Preview/publish access in survey editor
3. Target media IDs for testing (sequential guessing)

## Defense

Defensive measures and detection strategies:

- Enforce strict access controls on media endpoints
- Audit logs for cross-user media references
- Use signed URLs for media access

## Objectives

1. Confirm media display in survey
2. Extend exploitation to other elements (headers, polls)
3. Achieve persistent unauthorized embedding

## Instructions

### Step 1: Submit Modified Request

**Context**: Send the tampered request to embed the media.

Forward the request in the proxy tool after media_code modification.

> Response should be successful; check for errors in media loading.

### Step 2: Preview Survey

**Context**: Verify unauthorized media appearance.

Save and preview the survey in the Crowdsignal editor.

> Victim's media (e.g., private image) renders in the question or element.

### Step 3: Extend to Headers/Footers/Polls

**Context**: Repeat for other areas.

For headers/footers, trigger save on those sections and modify similarly. For team polls, use POST /polls/:pollId/edit with altered media_code.

> Allows access to team or external user media via ID substitution.

### Step 4: Validate Access

**Context**: Ensure full exploitation.

Publish or share the survey to confirm media persistence.

> Private content is now publicly or attacker-controllably accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[media-embedding]]
- [[unauthorized-access]]
