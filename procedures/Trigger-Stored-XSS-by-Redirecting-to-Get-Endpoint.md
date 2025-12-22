---
id: proc-uuid-003
name: Trigger-Stored-XSS-by-Redirecting-to-Get-Endpoint
tags:
  - xss
  - stored-xss
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:57.065Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Redirecting-to-Get-Endpoint

## Summary

This procedure redirects the victim to get.php after CSRF submission, triggering the stored XSS from the unsanitized age cookie reflection.

## Description

After the cookie is set, an event listener on the iframe load event redirects to http://www.rockstargames.com/php/videoplayer_cache/get.php. The endpoint reflects the age cookie value without escaping, executing the decoded JavaScript payload in the victim's browser. This can lead to cookie theft or further attacks. Prerequisites: Successful prior steps and browser navigation.

## Requirements

1. Cookie set from previous procedures
2. JavaScript event handling enabled
3. Access to get.php endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize and HTML-escape all reflected cookie values
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for XSS payloads in logs or WAF rules

## Objectives

1. Redirect post-submission to trigger reflection
2. Execute arbitrary JS like alert(document.cookie)
3. Demonstrate impact such as session theft

## Instructions

### Step 1: Add Load Event Listener

**Context**: Listen for iframe load to confirm POST success, then redirect.

**Code**:
```javascript
<script>
var xssframe = document.getElementsByName('xssframe')[0];
xssframe.addEventListener('load', function() {
  window.location = 'http://www.rockstargames.com/php/videoplayer_cache/get.php';
});
</script>
```

> Integrate into the HTML. Upon iframe load (POST complete), redirects to get.php.

### Step 2: Verify XSS Execution

**Context**: Visit get.php manually post-cookie set to test.

**Code**:
```javascript
// Expected behavior on get.php load
// Payload executes: alert(document.cookie);
```

> Success: Alert pops with cookies. Inspect source to confirm reflection of age value.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[JavaScript]]
