---
tags:
  - xss
  - referer
  - javascript
type: procedure
tools:
  - '[[tools/sec101-referer-xss-poc]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.023Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 58ea72fe-a47b-4556-94f2-ced889bbdeb7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Referer-Header-for-XSS

## Summary

This procedure involves creating a malicious HTTP Referer header that injects JavaScript into an onclick attribute on the target page, exploiting insufficient input sanitization in web applications like ownCloud apps.

## Description

In the context of the ownCloud apps vulnerability, the Referer header is directly inserted into an HTML onclick attribute without escaping. By crafting a payload that closes the string and injects script, attackers can execute arbitrary JavaScript when the victim interacts with the button. This is particularly effective in older browsers like IE that send raw Referer values. Prerequisites include understanding HTML attribute injection and access to an HTTP client for header manipulation.

## Requirements

1. HTTP client capable of custom headers (e.g., curl, Burp Suite)
2. Knowledge of the target endpoint's reflection point
3. Vulnerable browser for testing (e.g., IE for unencoded Referer)

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs, including headers, before insertion into HTML attributes
- Use Content Security Policy (CSP) to restrict inline scripts
- Monitor for anomalous Referer headers in server logs

## Objectives

1. Generate a payload that breaks out of the onclick string context
2. Ensure compatibility with Referer transmission behaviors
3. Validate payload syntax to avoid breaking the page

## Instructions

### Step 1: Design the Payload

**Context**: Construct a URL that, when reflected, closes the attribute string and injects JavaScript.

Use a simple payload like http://www.myevilsite.com/qwe';alert(1)+' to close the href quote and add an alert.

For advanced testing, leverage [[tools/sec101-referer-xss-poc]] to generate: http://sec101.sourceforge.net/referer-xss/?s=""><img src=1 onerror=alert(document.domain+String.fromCharCode(58,10,10,82,101,102,101,114,101,114,45,98,97,115,101,100,32,88,83,83,32,80,114,111,111,102,45,111,102,45,67,111,110,99,101,112,116,33))>&u=https://apps.owncloud.com/messages/?action=newmessage&username=anderslund

> This creates a full Referer that injects an onerror handler for immediate execution.

### Step 2: Validate Payload

**Context**: Test the payload string in a local HTML file to ensure it executes without errors.

Create a sample onclick="location.href='PASTE_REFERER_HERE'" and load in a browser.

> Expected: Script executes on click, confirming breakout success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/sec101-referer-xss-poc]]

## Tags

- xss
- referer
