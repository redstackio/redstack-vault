---
id: proc-uuid-2
tags:
  - xss
  - posts
  - comments
  - slack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.440Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Posts and Comments

## Summary

This procedure embeds the SVG XSS payload into Slack posts and comments expanding the attack surface for stored execution across workspace content.

## Description

Slack's post and comment features fail to sanitize HTML/SVG inputs allowing onload handlers to persist. By creating a post with the payload in title and body as code then sharing to slackbot and commenting this establishes multiple reflection points. Requires post creation permissions. Outcome: Payload visible and stored for later triggering.

## Requirements

1. Slack workspace access with post creation and commenting rights
2. Browser for UI interaction
3. Payload ready from prior steps

## Defense

Defensive measures and detection strategies:

- Enforce HTML entity encoding on all post/comment inputs
- Use DOM-based sanitization libraries like DOMPurify
- Log and review unusual content patterns in posts for SVG tags

## Objectives

1. Inject payload into post title body and comments
2. Share post to slackbot for cross-context storage
3. Confirm persistence without triggering filters

## Instructions

### Step 1: Create New Post with Payload

**Context**: Navigate to posts section and input payload in title and as code in a paragraph.

Manually enter in post form:

```html
Title: <img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>
Body: ``` <img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)> ```
```

> This disguises the payload as code in the body while title tests direct rendering.

### Step 2: Share and Comment with Payload

**Context**: Share the post to slackbot and add a comment.

Manually share via UI and enter comment:

```html
<img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>
```

> Expected output: Post shared comment attached payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[posts]]
