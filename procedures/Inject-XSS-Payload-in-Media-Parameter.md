---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - payload
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-09-18T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.844Z'
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
# Inject-XSS-Payload-in-Media-Parameter

## Summary

This procedure modifies the intercepted save request in Burp Suite to inject a malicious XSS payload into the media shortcode parameter, bypassing sanitization to store executable JavaScript on the server.

## Description

The vulnerability stems from insufficient validation of embedded media shortcodes, allowing HTML and event handler injection. Using Burp's request editor, the media parameter is altered to close the shortcode tag and append an onload SVG payload. This stores the payload server-side, which executes on subsequent page loads. Requires the intercepted request from the prior step. Outcome is a forwarded request that saves the tainted survey question.

## Requirements

1. Intercepted POST request in Burp Suite
2. Knowledge of XSS payload syntax
3. Valid Crowdsignal session

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all user-supplied shortcodes with allowlisting
- Scan saved content for script tags or event handlers before rendering

## Objectives

1. Craft and insert a functional XSS payload
2. Ensure payload survives server-side processing
3. Store the malicious content for later execution

## Instructions

### Step 1: Edit Media Parameter

**Context**: Locate and modify the vulnerable parameter in the request body.

In Burp's request editor, find the line media[11111111]=[dailymotion id=x8oma9] and change it to media[11111111]=[dailymotion id=x8oma9"><svg/onload=prompt(document.domain)>].

> The payload closes the attribute and injects an SVG with onload JavaScript.

### Step 2: Review and Forward

**Context**: Validate the modification and send the request.

Check the updated request for syntax errors, then click "Forward" to submit to the server.

> Server accepts and saves the question with the injected payload.

### Step 3: Confirm Save

**Context**: Ensure the operation completes without errors.

Observe the application response; the survey question should save successfully.

> No immediate execution; payload is stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[injection]]
