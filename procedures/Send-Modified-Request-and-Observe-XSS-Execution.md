---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - execution
  - cookie-theft
type: procedure
tools:
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.384Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Modified-Request-and-Observe-XSS-Execution

## Summary

This procedure forwards the payload-injected request via Burp Repeater and verifies XSS by observing JavaScript execution in the browser response, confirming arbitrary code execution and potential data exfiltration.

## Description

Upon sending the modified POST to /store/checkout/, the server reflects the unsanitized billing[address] in the HTML response, executing the injected <script>alert(document.cookie)</script>. This demonstrates client-side impact like session theft (e.g., PHPSESSID cookie). The attack relies on the site's low profile for reduced severity, but in high-traffic scenarios, it could enable phishing or keylogging.

## Requirements

1. Modified request with encoded payload in Burp Repeater
2. Browser integrated with Burp or capable of rendering responses
3. Target site responsive to the endpoint
4. No anti-automation measures like CAPTCHA on checkout

## Defense

Defensive measures and detection strategies:

- Validate and sanitize reflected inputs server-side with output encoding
- Use HTTP-only and Secure flags on session cookies to mitigate theft
- Deploy client-side XSS auditors or browser extensions for detection
- Scan responses for script tags in user-controlled fields

## Objectives

1. Trigger payload execution in the victim's context
2. Capture and analyze reflected output for confirmation
3. Assess impact, such as cookie visibility

## Instructions

### Step 1: Forward Request from Repeater

**Context**: Send the tampered request to the server to elicit the vulnerable response.

In Burp Repeater, click the "Send" button for the modified request.

> Expected output: HTTP response received, typically 200 OK with HTML body containing echoed form data.

### Step 2: Inspect Response for Reflection

**Context**: Check if the payload is unsanitized in the response body.

In the Response tab, search for the payload string (e.g., alert(document.cookie)). Look for HTML like <input value="1 Main Streetzbn0b"><script>...">

> Expected output: Raw script tags visible in the HTML source, indicating no escaping.

### Step 3: Render in Browser for Execution

**Context**: Load the response in a browser to simulate victim execution and observe JS.

Copy the response HTML to a local file or use Burp's "Render in Browser" if available. Open in a browser pointed at the target domain.

> Expected output: JavaScript alert dialog displaying session cookies like PHPSESSID=abc123.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Repeater]]

## Tags

- xss
- execution
- cookie-theft
