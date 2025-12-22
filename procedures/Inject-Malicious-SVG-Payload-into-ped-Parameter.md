---
tags:
  - xss
  - payload-injection
  - svg
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.744Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b9c772b1-d125-44b4-9583-2e1019782b69
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-SVG-Payload-into-ped-Parameter

## Summary

This procedure injects a malicious SVG payload into the 'ped' GET parameter of the /mission.php endpoint in a DoD web application, exploiting insufficient input sanitization to reflect and execute JavaScript in the browser after a prior auth bypass.

## Description

The attack targets a reflected XSS vulnerability where user input from the 'ped' parameter is not properly encoded, allowing an SVG element with an onload handler to execute arbitrary JavaScript. This is performed post-authorization bypass to access the internal endpoint structure. The payload is URL-encoded to evade basic filters and triggers upon page load, enabling potential session theft or further exploitation.

## Requirements

1. Burp Suite installed and browser proxy configured to route through it
2. Prior access via auth bypass to the /mission.php endpoint
3. Target URL: https://██████████/mission.php?content=crew&flight=DOC&line=Right&missionDate=19-Mar-19

## Defense

Defensive measures and detection strategies:

- Implement output encoding for all user inputs in PHP responses (e.g., htmlspecialchars)
- Use Content Security Policy (CSP) to block inline scripts and SVG execution
- Monitor for anomalous GET parameters and JavaScript alerts in web logs

## Objectives

1. Deliver and reflect the XSS payload without detection
2. Prepare for response modification to ensure execution
3. Enable follow-on attacks like cookie exfiltration

## Instructions

### Step 1: Enable Interception and Navigate to Target

**Context**: Activate Burp Suite's proxy to capture the request containing the payload.

Turn on Proxy-Intercept in Burp Suite, then manually construct and visit the URL with the payload:

```url
https://██████████/mission.php?content=crew&flight=DOC&line=Right&missionDate=19-Mar-19&ped=%3Csvg+onload=alert(%27jarvis7%27)%3E
```

> This URL includes the encoded SVG payload `<svg onload=alert('jarvis7')>` in the 'ped' parameter. The request will be intercepted, pausing before sending to the server.

### Step 2: Confirm Payload in Request

**Context**: Verify the payload is correctly formed in the intercepted request.

Inspect the GET request in Burp's Proxy tab to ensure the 'ped' parameter contains the encoded SVG.

> Expected: The raw request shows the full URL with payload; no modifications needed at this stage.

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
- [[svg-payload]]
