---
id: proc-nextcloud-xss-trigger-231524
tags:
  - stored-xss
  - ie11-exploit
  - csp-bypass
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:13.868Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Logo-Endpoint-in-IE11

## Summary

This procedure triggers the rendering of the injected HTML logo in a victim's browser, executing JavaScript payloads in IE11 to achieve limited stored XSS, potentially allowing session-based attacks like CSRF bypass.

## Description

After upload, the logo is served as HTML at http://[server]/nextcloud/index.php/apps/theming/logo without proper headers or sanitization. In IE11, the embedded payloads execute due to weak CSP enforcement, but fail in modern browsers (Firefox, Chrome, Edge, etc.). This enables admins to trick other users (e.g., via links) into visiting the endpoint, leading to JS under the victim's session for unauthorized actions.

## Requirements

1. Uploaded malicious logo already set on the server.
2. Victim using IE11 on Windows 7, 10, or Windows Phone 8.1.
3. Direct URL access to the logo endpoint.
4. Social engineering to lure victim (e.g., email with logo link).

## Defense

Defensive measures and detection strategies:

- Enforce Content-Security-Policy headers to block inline JS on served assets.
- Disable or restrict logo rendering in emails/templates.
- Monitor access logs for repeated logo endpoint hits from non-admin IPs.

## Objectives

1. Render the HTML and execute JS in targeted browsers.
2. Confirm browser-specific exploitation.
3. Demonstrate potential for session theft or CSRF.

## Instructions

### Step 1: Access Logo Endpoint

**Context**: Direct browser to the served file to initiate rendering.

Open http://[server]/nextcloud/index.php/apps/theming/logo in the target browser (IE11).

> Expected: Page loads as HTML with heading and text; no image fallback.

### Step 2: Observe Payload Execution

**Context**: Verify JS triggers alerts or other effects.

Upon load, the SVG onload and img onerror should fire, displaying alerts like 'SVG' or 'image XSS'.

> In IE11: Alerts pop; in other browsers: No execution, just static HTML.

### Step 3: Simulate Victim Interaction

**Context**: Test impact by tricking a session into actions.

Under a victim session, visit the URL; use executed JS for CSRF (e.g., form submission) or data exfil.

> Expected: JS runs in victim context, enabling limited attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[ie11-exploit]]
