---
id: proc-embed-iframe-001
tags:
  - clickjacking
  - iframe
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.773Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Target-in-Iframe

## Summary

This procedure embeds a target web application, such as Respondly, into an iframe on a malicious page, exploiting the absence of X-Frame-Options to enable further UI manipulation in a clickjacking attack.

## Description

In a clickjacking scenario, the attacker creates an HTML page that loads the vulnerable application in an iframe. Without the X-Frame-Options header set to DENY or SAMEORIGIN, the embedding succeeds, allowing the attacker to overlay elements and trick users. This step sets up the foundation for invisible framing, targeting web apps like https://app.respond.ly where role management is accessible post-login.

## Requirements

1. Basic HTML knowledge and text editor
2. Browser for testing (e.g., Chrome with dev tools to inspect)
3. Internet access to load the target URL

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on all pages
- Use Content-Security-Policy (CSP) with frame-ancestors directive
- Monitor for unusual embedding attempts via web application firewall (WAF)

## Objectives

1. Successfully load the target application in an unrestricted iframe
2. Verify no framing protections are in place
3. Prepare for overlay and invisibility modifications

## Instructions

### Step 1: Create Base HTML Page

**Context**: Start with a simple HTML structure to host the iframe.

No command; write the following HTML:

```html
<!DOCTYPE html>
<html>
<head><title>Clickjacking PoC</title></head>
<body>
<iframe src="https://app.respond.ly" width="100%" height="100%" style="border:none; margin:0; padding:0;"></iframe>
</body>
</html>
```

> Save as .html and open in browser. Expected: Target loads fully in frame.

### Step 2: Test Iframe Loading

**Context**: Confirm the target embeds without errors.

Use browser dev tools (F12) to inspect the iframe src and ensure content renders.

> Expected: No console errors about framing; application UI visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[iframe]]
