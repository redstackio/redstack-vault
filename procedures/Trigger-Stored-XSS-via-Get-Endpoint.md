---
id: proc-uuid-002
name: Trigger-Stored-XSS-via-Get-Endpoint
tags:
  - xss
  - stored-xss
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:34.130Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Get-Endpoint

## Summary

This procedure redirects the victim to the get.php endpoint after CSRF injection, causing the unsanitized 'age' value to be rendered as HTML, executing arbitrary JavaScript in the victim's browser for attacks like session hijacking.

## Description

The get.php endpoint retrieves and outputs the 'age' value (from cookie or session) without HTML escaping, allowing stored XSS. After setting the payload via CSRF, the attacker uses JavaScript to redirect upon iframe load, triggering the injection. The payload decodes to a script that can alert cookies or perform other client-side exploits. This targets browsers visiting the legitimate site post-injection, with outcomes including JS execution for data theft or phishing. Prerequisites include prior payload storage and no output sanitization on the endpoint.

## Requirements

1. Malicious 'age' payload already set via CSRF
2. Access to the get.php endpoint: GET /php/videoplayer_cache/get.php
3. Victim's browser with the tainted cookie/session

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs with HTML entity encoding (e.g., htmlspecialchars in PHP)
- Use Content Security Policy (CSP) to restrict inline scripts and data URIs
- Log and alert on XSS payload patterns in rendered content or user agents

## Objectives

1. Execute injected JavaScript in victim's context
2. Steal sensitive data like cookies for session hijacking
3. Facilitate further attacks such as keylogging or redirects

## Instructions

### Step 1: Add Redirect Script to POC

**Context**: Listen for CSRF completion and navigate to trigger XSS.

Extend the HTML POC:

```javascript
window.addEventListener('load', function() {
    var iframe = document.querySelector('iframe');
    iframe.onload = function() {
        window.location = 'http://www.rockstargames.com/php/videoplayer_cache/get.php';
    };
});
```

> This redirects after submission, loading get.php with the payload.

### Step 2: Observe Execution

**Context**: Verify XSS fires on get.php.

Visit the POC page; upon redirect, the page renders the anchor. Click to execute.

> Expected: Alert with document.cookie; inspect DOM for injected HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript-execution
