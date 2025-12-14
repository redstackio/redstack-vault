---
id: proc-uuid-002
name: Publish-Note-for-Persistent-Storage
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.357Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - persistence
  - publish
  - stored-xss
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Publish-Note-for-Persistent-Storage

## Summary

This procedure publishes the injected note in Simplenote to store the malicious SVG payload persistently, generating a public URL that any viewer can access to trigger the XSS.

## Description

Simplenote's publish feature allows notes to be shared via URL, rendering the Markdown server-side or client-side without re-sanitizing the SVG. This creates a stored XSS vector affecting authenticated users who view the note. The procedure assumes the payload is already injected; it focuses on the UI interaction to make it persistent. Expected outcome: A shareable URL hosting the exploit.

## Requirements

1. Note with injected payload already created
2. Access to the note's UI options
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Sanitize content on publish and render endpoints
- Rate-limit or review published notes for suspicious HTML/SVG
- Use Content Security Policy (CSP) to block inline JavaScript execution

## Objectives

1. Achieve persistence beyond the session
2. Expose the payload to multiple victims via URL
3. Enable cross-user impact through shared rendering

## Instructions

### Step 1: Access Publish Option

**Context**: Use the note interface to initiate publishing, storing the payload on the server.

No command; click the triple dots icon (...) in the top-right of the note and select 'Publish'.

> UI prompts for confirmation; a unique URL is generated upon success.

### Step 2: Verify Publication

**Context**: Confirm the note is live and payload intact by previewing.

Copy the provided URL and open in a new tab to check rendering.

> Note displays with SVG element visible; no immediate execution until interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[publish]]
- [[stored-xss]]
