---
id: 4b345547-4db5-47b1-9306-2d7722c3f4e8
name: Trigger-Attachment-Edit-Error-Redirect
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.107Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - error-trigger
  - redirect
  - xss-setup
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Trigger-Attachment-Edit-Error-Redirect

## Summary

This procedure simulates an attachment edit attempt on the TopCoder wiki to force an error and redirect to the vulnerable doeditattachment.action endpoint, reflecting the fileName parameter.

## Description

By accessing the edit URL for the previously added attachment, an error occurs due to the edit failure, redirecting to a endpoint that unsafely reflects user input. This step is crucial for identifying the reflection point in the error message. The attack targets the web application, assuming basic user access.

## Requirements

1. Existing attachment on the wiki page
2. Web browser
3. Access to the edit endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected parameters in error pages
- Log edit attempts and redirects
- Use Content Security Policy (CSP) to mitigate XSS

## Objectives

1. Force the vulnerable redirect
2. Confirm parameter reflection
3. Prepare for payload injection

## Instructions

### Step 1: Access Edit URL

**Context**: Navigate to the edit attachment URL to trigger the error condition.

No specific command; browser navigation to https://apps.topcoder.com/wiki/pages/editattachment.action?pageId=165871793&fileName=sss.svg.

> Error triggers, redirecting to doeditattachment.action with reflected fileName. Expected output: Error page showing fileName.

### Step 2: Observe Redirect

**Context**: Verify the redirect and reflection in the browser.

Inspect the final URL and page source.

> Confirms the unsanitized reflection in the error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[error-trigger]]
- [[redirect]]
- [[xss-setup]]
