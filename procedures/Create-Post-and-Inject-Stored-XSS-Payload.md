---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Create-Post-and-Inject-Stored-XSS-Payload
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.039Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss-injection
  - post-creation
  - stored-xss
commands: []
platforms:
  - Web
tools:
  - '[[tools/Hexo-Admin]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Create-Post-and-Inject-Stored-XSS-Payload

## Summary

This procedure creates a new blog post in the hexo-admin panel and injects a stored XSS payload into the content field, triggering immediate script execution due to lack of sanitization.

## Description

In the admin panel's posts section, a new post is created with a benign title, but the content field accepts raw HTML/JS without escaping. Payloads like "><img src=x onerror=alert('XSS')>" close the editor's HTML tag and inject an onload error handler, executing JavaScript in the viewer's context. This stored variant persists in the post data.

## Requirements

1. Active Hexo server with admin panel accessible
2. Valid admin credentials
3. Browser developer tools for payload testing

## Defense

Defensive measures and detection strategies:

- Sanitize post content with libraries like DOMPurify before storage
- Validate input in hexo-admin to escape script tags and event handlers
- Scan posts for common XSS patterns using automated tools

## Objectives

1. Demonstrate vulnerability in post editor rendering
2. Achieve client-side code execution in admin session
3. Store payload for later persistence

## Instructions

### Step 1: Navigate to Posts Section

**Context**: Enter the post management area in the admin UI.

No command; UI action:

Click 'Posts' in the sidebar.

> Displays list of existing posts and 'New Post' button.

### Step 2: Create New Post

**Context**: Initiate a new post entry with a test title.

No command; UI action:

Click 'New Post', enter title 'Test XSS here', leave other fields default.

> Opens the editor with title and content fields.

### Step 3: Inject XSS Payload

**Context**: Insert malicious payload into content to exploit unsanitized input.

No command; UI action:

In the content field, append: "><img src=x onerror=alert('XSS')>"

> Triggers alert immediately in the editor preview or on focus.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Hexo-Admin]]

## Tags

- xss-injection
- post-creation
- stored-xss
