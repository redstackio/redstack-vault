---
id: proc-post-xss-comment
tags:
  - xss
  - persistence
  - concrete-cms
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
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
updated_at: '2025-12-14T03:15:53.585Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Post Malicious Comment

## Summary

This procedure submits the comment containing the injected script payload, storing it in the database and triggering immediate execution for the posting user, establishing persistence for Stored XSS.

## Description

Submitting the form saves the raw HTML to MySQL without sanitization. The payload executes on post-render, affecting the poster first. This step completes the storage phase of the attack in Concrete CMS Conversations.

## Requirements

1. Payload inserted in comment form
2. Valid blog post with comments enabled
3. User session (anonymous ok if allowed)

## Defense

Defensive measures and detection strategies:

- Validate and escape user input before DB storage
- Audit comment submissions for script patterns
- Block submissions with external URLs

## Objectives

1. Store payload in database
2. Trigger initial execution
3. Confirm persistence

## Instructions

### Step 1: Submit Form

**Context**: Post the comment to save and execute.

No command; UI action:

- Click "Post Comment" or submit button
- Wait for page reload

> Expected: Comment appears, script executes; check console for log.

### Step 2: Initial Verification

**Context**: Confirm execution for poster.

Open developer console (F12):

- Look for poc.js load and log message

> Expected: Console output: 'This file is loaded from bl4de.tech domain and executed in context of [domain]'

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- [[xss]]
- [[Persistence]]
