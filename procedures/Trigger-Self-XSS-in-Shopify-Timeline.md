---
tags:
  - xss
  - self-xss
  - shopify
  - javascript
  - safari
type: procedure
tools:
  - '[[tools/Safari-Browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - macOS
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:13.148Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2a16a189-06e3-4084-9058-a2e178c42e9d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Self-XSS-in-Shopify-Timeline

## Summary

This procedure exploits a self-XSS vulnerability in Shopify's Timeline feature by pasting malicious javascript: URLs, which render as clickable links in Safari browsers, allowing JavaScript execution in the user's own context. It demonstrates the lack of protocol sanitization and can be chained with social engineering to affect other users like admins.

## Description

The Shopify Timeline allows users to post updates, but fails to sanitize pasted URLs starting with 'javascript:', particularly in Safari on macOS and iOS. When a user pastes such a link (e.g., javascript:alert(123)), it posts and renders as a hyperlink. Clicking it executes the JS payload in the browser's context, limited to self-XSS. However, if an admin copies and pastes this content from a storefront or report, it could lead to broader impact. This targets web environments with Shopify, requiring only user access and Safari for reproduction.

## Requirements

1. Access to a Shopify account with Timeline feature
2. Safari browser on macOS or iOS 13.4.1 or later
3. Standard internet access to Shopify's web interface

## Defense

Defensive measures and detection strategies:

- Implement client-side URL protocol validation to block 'javascript:' schemes in input fields
- Use Content Security Policy (CSP) to restrict inline script execution
- Educate users on risks of clicking untrusted links and monitor for anomalous JS alerts in browser logs

## Objectives

1. Execute arbitrary JavaScript in the attacker's browser session via self-XSS
2. Demonstrate vulnerability for reporting or chaining with social engineering
3. Highlight sanitization gaps in URL rendering

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Craft a javascript: URL that executes JS, optionally disguised with a benign trailing URL to appear safe.

No command required; manually type or copy `javascript:alert(123)` or `javascript:alert(123);//http://google.com`.

> This creates the payload for pasting. Expected output: Payload string ready in clipboard.

### Step 2: Paste into Timeline and Submit

**Context**: Insert the payload into the Timeline to test rendering without sanitization.

Navigate to Shopify Timeline, paste the payload into the input field, and post it. If needed, copy the posted content and repaste into a new entry.

> The link should render as clickable. Expected output: Post appears with hyperlink in Timeline view.

### Step 3: Click to Execute

**Context**: Interact with the rendered link to trigger JS execution.

Click the link in the Timeline post using Safari.

> Payload executes, e.g., alert box pops up. Expected output: JS runs in browser context, confirming self-XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari-Browser]]

## Tags

- xss
- self-xss
- shopify
- javascript
- safari
