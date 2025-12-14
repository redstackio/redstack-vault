---
tags:
  - xss-execution
  - open-redirect
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.643Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1f90f976-a632-42f7-9886-e230a863d4b9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Banner-Interaction-in-Revive-Adserver

## Summary

This procedure triggers the stored XSS payload by interacting with the generated banner in the affiliate preview, executing JavaScript for redirects or further exploitation in Revive Adserver.

## Description

Once the preview renders the unsanitized URL, the injected `<img>` tag with `onclick` attribute becomes interactive. Clicking the banner executes the JavaScript, demonstrating the stored XSS and open redirect, which can lead to phishing or credential theft in a real scenario.

## Requirements

1. Admin session with preview loaded
2. Visible banner element from injected payload
3. Target malicious site prepared for redirect

## Defense

Defensive measures and detection strategies:

- Strip event handlers (e.g., onclick) from rendered URLs
- Use sandboxed iframes for previews
- Monitor client-side script execution via browser security tools
- Alert on unexpected redirects from admin sessions

## Objectives

1. Execute arbitrary JavaScript in admin context
2. Redirect to external malicious resources
3. Achieve impact like data theft or session hijacking

## Instructions

### Step 1: Locate Banner Element

**Context**: Identify the injectable content in the preview.

Inspect the generated page for the Header Script Banner image.

> The `<img>` tag from the payload should be present.

### Step 2: Interact to Trigger

**Context**: Fire the event handler.

Click on the banner image.

> JavaScript executes, redirecting the browser.

### Step 3: Verify Impact

**Context**: Confirm exploitation success.

Observe the redirect to `http://google.com` (or replace with malicious URL).

> In production, this could exfiltrate cookies or load phishing pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[open-redirect]]
- [[JavaScript]]
