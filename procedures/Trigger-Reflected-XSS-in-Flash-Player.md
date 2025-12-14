---
tags:
  - xss
  - flash
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.365Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7ad801b7-a5d0-42a3-82d7-116294441a81
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-in-Flash-Player

## Summary

This procedure exploits a reflected XSS vulnerability in the JWPlayer SWF file by injecting unsanitized JavaScript via the 'playerready' parameter, executing in the browser context of the hosting domain.

## Description

The player.swf file on ssl-ccstatic.highwebmedia.com uses Flash's ExternalInterface to call the 'playerready' parameter as JavaScript without validation, allowing arbitrary code execution. This is triggered by appending a payload to the URL, leading to immediate JS execution upon SWF load. Impact is domain-specific but can chain with other vulns like cross-domain policies.

## Requirements

1. Browser with Flash Player enabled (e.g., legacy versions)
2. Direct access to the target URL
3. No authentication needed for trigger

## Defense

Defensive measures and detection strategies:

- Disable Flash globally or per-site
- Sanitize all ExternalInterface callbacks in SWF files
- Monitor for anomalous JS execution in Flash contexts via browser dev tools
- Use Content Security Policy (CSP) to restrict script sources, though limited against Flash

## Objectives

1. Execute arbitrary JavaScript in the ssl-ccstatic.highwebmedia.com context
2. Confirm vulnerability with a proof-of-concept alert
3. Prepare for chaining with cross-domain exploitation

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL with a JavaScript payload in the playerready parameter to test execution.

No command required; manually enter or bookmark the URL:

```url
https://ssl-ccstatic.highwebmedia.com/jwplayer/player.swf?playerready=alert(document.domain)
```

> This loads the SWF and passes the alert as a JS call via ExternalInterface, popping an alert with the domain.

### Step 2: Load and Verify Execution

**Context**: Open the URL in a Flash-enabled browser to trigger the payload.

Navigate to the URL in the browser address bar.

> Expected: Alert box appears immediately after SWF loads, confirming XSS. Check browser console for any Flash errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- flash
- externalinterface
