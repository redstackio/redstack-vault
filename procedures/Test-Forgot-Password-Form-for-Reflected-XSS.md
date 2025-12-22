---
id: test-acronis-form-xss-001
tags:
  - xss
  - web
  - recon
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
updated_at: '2025-12-13T23:55:37.670Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Test-Forgot-Password-Form-for-Reflected-XSS

## Summary

This procedure identifies and tests the Acronis forgot password form for reflected XSS by submitting various parameters to check for unsanitized input reflection in the server response.

## Description

The Acronis forgot registration email form at https://www.acronis.com/en-us/my/remind/index.html accepts POST requests with parameters like token, SN, OrderId, Submit, and allows custom parameters. Testing reveals that inputs are reflected back in the HTML response without proper escaping, enabling potential XSS. This step focuses on reconnaissance to confirm the vulnerability exists before crafting exploits. Prerequisites include a web browser and access to the public site; no authentication is needed.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools) for inspecting responses.
2. Public internet access to the target URL.
3. Basic knowledge of HTTP POST requests and HTML inspection.

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity encoding) on all user inputs.
- Use Content Security Policy (CSP) to restrict inline script execution.
- Monitor server logs for unusual parameter values or repeated test submissions.

## Objectives

1. Confirm reflection of form parameters in the response.
2. Identify vulnerable parameters like the custom 'c' field.
3. Establish a baseline for payload crafting.

## Instructions

### Step 1: Access the Target Form

**Context**: Navigate to the forgot password endpoint and prepare to submit a test POST request.

Open your browser and go to https://www.acronis.com/en-us/my/remind/index.html. Use the browser's developer console or a tool like Postman to simulate a POST request.

### Step 2: Submit Test Payloads

**Context**: Inject simple test strings into form parameters to check for direct reflection.

Craft a POST request to https://www.acronis.com/en-us/my/remind/index.html with parameters: token=example, SN=123, OrderId=456, Submit=Send, c=test<Script>alert(1)</Script>. Submit and inspect the response HTML.

> The response will show the 'c' parameter value reflected, e.g., in a div or error message, without escaping the <Script> tags.

### Step 3: Verify Reflection

**Context**: Analyze the response source to confirm lack of sanitization.

In the browser's Network tab or View Source, search for the injected value. If it appears as raw HTML (e.g., test<Script>alert(1)</Script>), reflection is confirmed.

> Expected output: Unescaped input in the page body, indicating potential for XSS.

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
- [[web]]
- [[recon]]

