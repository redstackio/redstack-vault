---
tags:
  - xss
  - trigger
  - admin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9586afcf-d52e-43ec-895e-9f8316cedab1
created_at: '2025-12-14T17:23:20.691Z'
updated_at: '2025-12-14T17:23:20.691Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Admin-Visit

## Summary

This procedure triggers the stored XSS payload when an administrator views the malicious post, loading the invisible iframe to the plugin editor page.

## Description

Upon admin access to the post, the JavaScript executes in the admin's browser context, creating an iframe that loads the same-origin admin page `/wp-admin/plugin-editor.php?file=hello.php`. The iframe is hidden via CSS, evading visual detection. This step relies on the admin's session cookies for authentication to the editor page.

## Requirements

1. Admin with active session views the post URL
2. Same-origin policy allows iframe loading
3. No X-Frame-Options blocking same-origin frames

## Defense

Defensive measures and detection strategies:

- Role-based content filtering: Prevent admins from viewing untrusted editor posts
- Browser protections: Enable strict CSP to block iframes
- Session monitoring: Log unusual admin page loads from content views

## Objectives

1. Execute JavaScript in admin context
2. Load plugin editor in background iframe
3. Maintain stealth for subsequent manipulation

## Instructions

### Step 1: Direct Admin to Post

**Context**: Ensure the admin loads the malicious content.

Share the post link via email or dashboard.

> Admin browser fetches the post, executing embedded script.

### Step 2: Iframe Loading

**Context**: Script creates and sources the iframe.

The payload includes:

```javascript
document.body.appendChild(iframe);
iframe.src = "/wp-admin/plugin-editor.php?file=hello.php";
```

> Iframe loads admin page using admin's cookies, no redirect.

### Step 3: Delay for Load

**Context**: Wait for iframe content to render.

Use `setTimeout(..., 2000)` before accessing DOM.

> Page ready for cross-frame scripting.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[trigger]]
- [[iframe]]
