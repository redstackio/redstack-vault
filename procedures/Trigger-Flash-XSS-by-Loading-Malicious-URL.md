---
id: proc-khan-trigger-flash-xss
tags:
  - xss
  - execution
  - flash
  - trigger
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
updated_at: '2025-12-14T03:16:25.437Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Flash XSS by Loading Malicious URL

## Summary

This procedure triggers the XSS vulnerability by accessing the SWF URL with the crafted payload, executing arbitrary JavaScript in the browser context for potential data exfiltration.

## Description

Once the payload is injected into the 'iceID' parameter, loading the SWF in a Flash-enabled browser processes it client-side, breaking out to run JS. This affects users on the smarthistory.khanacademy.org subdomain, leading to impacts like cookie theft. The approach relies on Flash's legacy JS integration, with outcomes including alert() proof-of-concept or advanced payloads for session hijacking.

## Requirements

1. Browser with Adobe Flash Player enabled (e.g., legacy Chrome <80 or Firefox with Flash addon)
2. Direct internet access to the target URL
3. Crafted payload from prior step

## Defense

Defensive measures and detection strategies:

- Deprecate and remove all Flash content; redirect to HTML5 alternatives
- Enable Flash blocking via browser policies or extensions like NoScript
- Detect via WAF rules on encoded payloads in SWF parameter requests

## Objectives

1. Execute the injected JavaScript
2. Confirm control over victim browser
3. Demonstrate potential for further attacks like data collection

## Instructions

### Step 1: Prepare Malicious URL

**Context**: Combine the SWF base URL with the encoded payload.

Construct: http://smarthistory.khanacademy.org/assets/flash/cozimo.swf?iceID=%5C%22%29%29%7Dcatch%28e%29%7Balert%28%27XSS%27%29;%7D//

> Ensure encoding is correct to avoid URL parsing issues.

### Step 2: Load URL in Target Browser

**Context**: Open the URL to invoke Flash and trigger payload execution.

Paste and access the URL in a Flash-enabled browser.

> Expected output: Upon SWF loading, an alert('XSS') dialog appears, confirming JS execution in the page context.

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
- [[Execution]]
- [[trigger]]
