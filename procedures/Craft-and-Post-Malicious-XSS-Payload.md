---
tags:
  - xss
  - wordpress
  - payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 60db4c40-df45-4a0b-aefc-ec3544d2e59e
created_at: '2025-12-14T17:23:20.703Z'
updated_at: '2025-12-14T17:23:20.703Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Post-Malicious-XSS-Payload

## Summary

This procedure involves creating a stored XSS payload using an invisible iframe to load the WordPress plugin editor and posting it as editor content, setting up execution when viewed by admins.

## Description

The payload exploits unfiltered HTML by embedding JavaScript that creates an iframe sourcing the admin plugin-editor.php with a target file like hello.php. Delays ensure loading before manipulation. This targets same-origin policy allowances in WordPress 4.8.1, leading to DOM access for code injection. Expected outcome is the post being published and ready for admin interaction.

## Requirements

1. Editor login session active
2. Access to WordPress post editor
3. Knowledge of target plugin file (e.g., hello.php in wp-content/plugins)

## Defense

Defensive measures and detection strategies:

- Sanitize editor inputs: Use plugins to strip scripts from non-admin posts
- Content security policy (CSP): Block inline scripts and iframes
- Audit posts: Regularly scan for suspicious HTML in editor content

## Objectives

1. Deliver persistent XSS via stored post
2. Load admin-only page in iframe without detection
3. Prepare for cross-frame scripting

## Instructions

### Step 1: Create New Post

**Context**: Start a new post in WordPress editor to insert the payload.

Switch to Text/HTML mode.

> Post editor opens with raw HTML input.

### Step 2: Insert Payload

**Context**: Embed the iframe and JavaScript for delayed execution.

Insert code like:

```html
<iframe src="/wp-admin/plugin-editor.php?file=hello.php" style="display:none;"></iframe>
<script>
setTimeout(function() {
  // Manipulation code here (detailed in next procedure)
}, 2000);
</script>
```

> Payload saved without filtering, post publishes successfully.

### Step 3: Publish and Share

**Context**: Make the post live for admin viewing.

Click Publish and note the post URL.

> Post is accessible, payload dormant until viewed by admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload]]
