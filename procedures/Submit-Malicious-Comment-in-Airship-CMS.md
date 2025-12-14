---
id: proc-uuid-2
tags:
  - xss-injection
  - persistent-xss
  - airship-cms
  - comment-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.046Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malicious-Comment-in-Airship-CMS

## Summary

This procedure injects a persistent XSS payload into the anonymous comment name field of a blog post in Airship CMS v2.0.0, leveraging the lack of encoding to store malicious JavaScript for later execution.

## Description

The comment system in Airship CMS allows anonymous submissions by default, reading the name field from form input and storing it without HTML/JS encoding. An attacker submits a payload that breaks out of the attribute context, such as `'><img src=no onerror=alert(1)>`, which persists in the database and displays in the DOM. This sets up execution when victims interact with the comment. The target is any blog post with open comments, leading to arbitrary JS in victim browsers.

## Requirements

1. Access to a blog post URL with comments enabled
2. No authentication required (anonymous by default)
3. Web browser to submit the form

## Defense

Defensive measures and detection strategies:

- Implement server-side HTML/JS encoding for all user inputs in comment fields
- Sanitize name fields to strip script tags and event handlers
- Enable moderation for comments to review before publishing

## Objectives

1. Store XSS payload persistently in comment metadata
2. Ensure payload survives storage and retrieval without alteration
3. Position for execution via user interaction

## Instructions

### Step 1: Navigate to Blog Post

**Context**: Locate a target blog post to submit the comment.

Open the blog post page in your browser, e.g., `https://target.com/blog/post-title`.

> Scroll to the comments section and click to add a new comment.

### Step 2: Inject Payload

**Context**: Enter the malicious payload in the name field to exploit the lack of encoding.

In the 'Name' field, input: `'><img src=no onerror=alert(1)>`

Fill optional fields if needed (e.g., blank comment body) and submit the form.

> Expected: Comment posts successfully; inspect DOM to see payload in the author's name element, e.g., `<div class="author">'><img src=no onerror=alert(1)></div>`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[persistent-xss]]
