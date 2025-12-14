---
tags:
  - xss
  - stored-xss
  - mapbox
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.175Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 10e05271-2241-4e5d-b670-28c4bb199408
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Map-Project-in-Classic-Editor

## Summary

This procedure involves creating a new map project in Mapbox's classic map editor and injecting a malicious JavaScript payload into the project title, exploiting the lack of sanitization to store XSS for later execution.

## Description

In the context of the stored XSS vulnerability in Mapbox, the classic map editor allows users to set a project title without proper escaping. By using payloads like `<img src=a onerror=confirm(2)>` or more evasive ones such as `'><script>alert(1);</script><iframe onload=alert(97)>`, the attacker stores executable JavaScript on Mapbox servers. This payload remains dormant until rendered in the share control modal. Prerequisites include a valid Mapbox account and access to the web-based editor. Expected outcomes include successful project creation with the payload persisted, setting up for sharing and victim exploitation.

## Requirements

1. Valid Mapbox account with editor access
2. Web browser with JavaScript enabled
3. Knowledge of XSS payloads to bypass any basic filters

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization for all user-supplied fields like titles
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous project titles containing script tags via logging

## Objectives

1. Store malicious JavaScript in the map title without detection
2. Ensure the payload survives saving and rendering
3. Prepare for propagation via share URL

## Instructions

### Step 1: Access Mapbox Classic Editor

**Context**: Log in to initiate project creation.

Navigate to the Mapbox classic map editor dashboard and start a new project.

### Step 2: Inject Malicious Payload

**Context**: Set the title to embed the XSS payload.

In the project settings, enter a title such as `<img src=a onerror=confirm(2)>` or the shorter variant `<img src=a >\"<iframe onload=alert('XSS')>`. Save the project.

> This step exploits the unsanitized input field, storing the HTML/JS directly.

### Step 3: Verify Storage

**Context**: Confirm the payload is persisted.

Reload the project editor and check that the title displays the injected content without alteration.

**Expected Output**: Title renders with the payload intact, no errors on save.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[mapbox]]
