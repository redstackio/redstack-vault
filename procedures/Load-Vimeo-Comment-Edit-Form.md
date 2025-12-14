---
tags:
  - edit-form
  - get-request
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/vimeo-get-comment-edit-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.418Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a7a2e0d2-ceac-4f32-a1c5-5447dcd2a3eb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Load-Vimeo-Comment-Edit-Form

## Summary

This procedure loads the edit form for a legitimately owned comment in Vimeo's forum, capturing the GET request structure including the comment_id parameter for later manipulation.

## Description

By clicking the edit button on your own comment, this step retrieves the HTML form via an AJAX GET request. It requires authentication and is used to understand the normal flow before exploiting IDOR. The request includes headers like X-Requested-With and Referer, with cookies for session validation. Success grants access to the editable comment content.

## Requirements

1. Valid comment_id from a previously posted comment
2. Authenticated session cookies
3. Proxy tool or browser dev tools for request inspection

## Defense

Defensive measures and detection strategies:

- Server-side checks on edit requests to ensure ownership
- Monitoring for unusual edit form loads

## Objectives

1. Retrieve the edit interface for baseline analysis
2. Capture request parameters for IDOR preparation
3. Verify authentication works for editing

## Instructions

### Step 1: Trigger Edit in UI

**Context**: Initiate the request by interacting with the comment.

Click 'Edit' on your comment in the forum.

### Step 2: Replicate with Command

**Context**: Use the captured request to load the form programmatically.

**Command** ([[commands/vimeo-get-comment-edit-form]]):

```bash
curl -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010973&is_sticky=0&action=comment_edit_form" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://vimeo.com/forums/wanted_and_offered/topic:130606" \
  -H "Cookie: [insert full auth cookies]"
```

> This command fetches the edit form HTML. Expected output is the form containing your comment text.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/vimeo-get-comment-edit-form]]

## Tools Used


## Tags

- edit-form
- get-request
