---
id: proc-verify-xss-visitors
tags:
  - xss
  - verification
  - concrete-cms
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
  - '[[tools/Firefox-Browser]]'
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
updated_at: '2025-12-14T03:15:53.582Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Payload Execution for Site Visitors

## Summary

This procedure tests the Stored XSS by viewing the comment in a separate browser session as an anonymous or authenticated user, confirming arbitrary JS execution for all site visitors.

## Description

The payload persists in the database and renders for any viewer, executing the external script. This demonstrates the broad impact on frontend users in Concrete CMS, potentially leading to session hijacking or data theft.

## Requirements

1. Malicious comment posted and visible
2. Separate browser or incognito session
3. Developer tools enabled

## Defense

Defensive measures and detection strategies:

- Render comments through sanitized templates
- Implement JS execution monitoring in browsers
- Alert on anomalous console activity

## Objectives

1. Confirm execution for non-posters
2. Validate persistence across sessions
3. Assess impact on anonymous users

## Instructions

### Step 1: Open in New Session

**Context**: Simulate another user viewing the page.

No command; browser action:

- Open the blog post in incognito or different browser
- Scroll to the malicious comment

> Expected: Page loads normally, but script triggers.

### Step 2: Check Execution

**Context**: Use console to verify JS run.

Open F12 console in Chrome or Firefox:

- Look for poc.js network request and log

> Expected: Log message appears, confirming execution in visitor context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]
- [[tools/Firefox-Browser]]

## Tags

- [[xss]]
- [[verification]]
