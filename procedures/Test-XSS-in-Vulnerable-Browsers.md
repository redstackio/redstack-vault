---
id: proc-uuid-15125-step3
tags:
  - xss
  - testing
  - browser-exploit
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.048Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test XSS in Vulnerable Browsers

## Summary

This procedure tests the crafted XSS payload in browsers without full CSP support, confirming arbitrary JavaScript execution in the Twitter Amplify web player context.

## Description

Access the malicious URL in targeted environments like older Android browsers, where CSP does not block data URI JS injection. The payload executes onload, demonstrating impact such as alerts, which could extend to session hijacking or phishing. Expected outcomes include visible JS execution, validating the vulnerability for reporting or exploitation.

## Requirements

1. Vulnerable browser (e.g., older Android WebView)
2. Crafted URL from previous procedure
3. Network access to the endpoint

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers blocking unsafe-inline and data: URIs
- User-agent detection for legacy browsers with warnings
- Log and alert on JS errors or unexpected onload events

## Objectives

1. Verify payload execution
2. Assess impact in real browsers
3. Identify mitigation gaps like CSP absence

## Instructions

### Step 1: Select Vulnerable Environment

**Context**: Choose a browser lacking CSP enforcement.

Use an older Android device or emulator with WebView pre-2016.

> Avoid modern browsers like Chrome which block via CSP.

### Step 2: Load the Malicious URL

**Context**: Trigger the player and observe injection.

Navigate to: https://amp.twimg.com/amplify-web-player/prod/source.html?url=...&image_src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAAAAACH5BAAAAAAALAAAAAABAAEAAAICTAEAOw%27onload%3D%27alert(1000)

> The img tag loads, firing onload.

### Step 3: Validate Execution

**Context**: Confirm JS runs as expected.

Look for alert(1000) popup.

> Success: Popup appears; failure: Blocked by CSP or sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[testing]]
