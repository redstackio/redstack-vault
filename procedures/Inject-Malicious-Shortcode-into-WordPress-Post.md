---
tags:
  - xss
  - injection
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.638Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 11c27cc4-c218-46a1-ad95-1628d8230289
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Shortcode-into-WordPress-Post

## Summary

This procedure involves injecting a malicious shortcode payload into a WordPress post using the Gutenberg editor to set up a stored XSS attack that executes when previewed in the admin interface.

## Description

In WordPress 5.0, the Post Shortcode function lacks proper sanitization during preview rendering, allowing attackers with Contributor permissions to inject HTML and JavaScript. The payload breaks out of the shortcode tag and injects an <img> element with an onerror handler to execute JS, such as prompting an alert or stealing session data. This targets admins previewing drafts, leading to arbitrary code execution in their browser context.

## Requirements

1. WordPress account with Contributor or higher role
2. Access to Gutenberg post editor
3. Vulnerable WordPress 5.0 installation

## Defense

Defensive measures and detection strategies:

- Enable strict content sanitization plugins like Wordfence or Sucuri
- Restrict draft preview access to trusted roles
- Monitor admin logs for unusual post edits

## Objectives

1. Embed executable JavaScript payload in post content
2. Ensure payload survives saving without triggering errors
3. Prepare for execution on admin preview

## Instructions

### Step 1: Access Post Editor

**Context**: Log in and navigate to create or edit a post to insert the payload.

No specific command; use the WordPress dashboard to go to Posts > Add New or Edit.

> Manually switch to the code editor view if needed to paste raw HTML.

### Step 2: Insert Payload

**Context**: Add the malicious shortcode to exploit the preview rendering flaw.

Insert the following payload into the post content:

```html
"><img src=1 onerror=prompt(1)>
```

> This payload closes any open shortcode tag and injects an image that executes JS on error. Adapt for real attacks, e.g., replace prompt(1) with document.cookie theft.

### Step 3: Verify Insertion

**Context**: Check that the payload is present without immediate execution.

Preview the post briefly in the editor (non-admin full preview) to ensure it doesn't trigger yet.

> Expected: Payload visible in source but no JS execution until admin draft preview.

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
- [[wordpress]]
- [[injection]]
