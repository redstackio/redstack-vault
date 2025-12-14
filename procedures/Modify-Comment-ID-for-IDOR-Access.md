---
tags:
  - idor
  - parameter-tampering
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/vimeo-get-modified-comment-edit-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.416Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 85293b0c-d78f-4f6e-b5b0-1eca6a0157a0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Comment-ID-for-IDOR-Access

## Summary

This procedure exploits IDOR by altering the comment_id parameter in the edit form GET request to access and load another user's comment for editing without authorization.

## Description

After capturing the legitimate edit request, change the comment_id to one belonging to another user (e.g., decrement by 1). The server fails to validate ownership, allowing the edit form to load. This requires intercepting and modifying the request, typically with a proxy. The impact is unauthorized access to sensitive comment content.

## Requirements

1. Known comment_id of target user's comment (e.g., via enumeration or guessing sequential IDs)
2. Authenticated session
3. Ability to intercept and modify HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership verification for comment_ids
- Log and alert on mismatched user-ID and comment ownership

## Objectives

1. Bypass access controls via direct object reference
2. Load unauthorized edit form
3. Prepare for content modification

## Instructions

### Step 1: Identify Target ID

**Context**: Select a nearby comment_id, e.g., 13010972.

Inspect forum for sequential IDs or guess.

### Step 2: Send Modified Request

**Context**: Replay the GET with tampered ID.

**Command** ([[commands/vimeo-get-modified-comment-edit-form]]):

```bash
curl -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010972&is_sticky=0&action=comment_edit_form" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://vimeo.com/forums/wanted_and_offered/topic:130606" \
  -H "Cookie: [insert full auth cookies]"
```

> Expected output: Edit form for the target comment loads, showing their content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/vimeo-get-modified-comment-edit-form]]

## Tools Used


## Tags

- idor
- parameter-tampering
