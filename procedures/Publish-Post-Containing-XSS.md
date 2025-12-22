---
tags:
  - xss
  - persistence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.077Z'
sub_techniques: []
id: dc893cb3-a15c-4f3f-b439-5cb7a570d57f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Publish Post Containing XSS

## Summary

This procedure saves and publishes the post, storing the XSS payload in the WordPress database for frontend rendering.

## Description

Publishing commits the post title with the embedded script to the MySQL database via PHP backend. In WordPress 5.3, no additional sanitization occurs for capable users, ensuring the payload survives storage. This step transitions the attack from injection to persistence, enabling execution upon view.

## Requirements

1. Post editor open with payload in title
2. Publish permissions (admin/editor role)
3. No content filters enabled

## Defense

Defensive measures and detection strategies:

- Implement database-level escaping for all user inputs
- Log publish events and scan for script tags in new posts
- Restrict publish rights to trusted users only

## Objectives

1. Persist the malicious title in the database
2. Generate a public permalink
3. Make the post accessible for triggering

## Instructions

### Step 1: Review Post

**Context**: Verify payload integrity before saving.

Check the title for the script tag and preview if available.

> Preview should display the raw HTML without execution in editor.

### Step 2: Publish

**Context**: Submit the post to storage.

Click the blue 'Publish' button and confirm.

> Status updates to 'Published'; copy the permalink from the editor.

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
- [[Persistence]]
