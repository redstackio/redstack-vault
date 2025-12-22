---
tags:
  - xss
  - web
  - url-path
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
updated_at: '2025-12-13T23:56:04.029Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c21f23a8-4d19-4294-9f42-4540943e0ffe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-XSS-Vulnerable-Endpoint-in-URL-Path

## Summary

This procedure involves observing and testing a web application's handling of URL path parameters to identify lack of input validation, specifically in the Rockstar Games GTA Online screens page where content after the last slash is blindly decoded and loaded, enabling XSS.

## Description

In this attack scenario, the target is a public-facing web page that processes URL paths without sanitization. By appending arbitrary strings to the endpoint /GTAOnline/jp/screens/, an attacker can confirm if the application decodes and attempts to load the content, setting the stage for XSS exploitation. This is particularly effective on sites with dynamic content loading. Prerequisites include browser access and developer tools for inspection. Expected outcomes include confirmation of vulnerability, paving the way for payload injection.

## Requirements

1. Public access to the target website (https://www.rockstargames.com/GTAOnline/jp/screens/)
2. Modern web browser with developer console
3. Basic understanding of URL encoding and web request inspection

## Defense

Defensive measures and detection strategies:

- Implement URL path validation and sanitization to reject unexpected characters or lengths
- Use Content Security Policy (CSP) to restrict script loading from external sources
- Monitor server logs for unusual URL patterns or high-frequency path manipulations

## Objectives

1. Confirm unvalidated decoding of URL path content
2. Identify potential for script injection
3. Gather evidence for further exploitation

## Instructions

### Step 1: Navigate to Base Endpoint

**Context**: Access the vulnerable page to establish baseline behavior.

Open a browser and navigate to https://www.rockstargames.com/GTAOnline/jp/screens/.

> Observe the page load normally without any appended path.

### Step 2: Append Arbitrary Content

**Context**: Test the application's response to unsanitized input in the URL path.

Modify the URL by adding /arbitrary after the last slash, e.g., https://www.rockstargames.com/GTAOnline/jp/screens/arbitrary. Reload the page and open developer tools (F12) to inspect the network tab and console for any decoding or loading attempts.

> Look for signs that the 'arbitrary' content is processed, such as error messages or unexpected rendering, indicating blind loading.

### Step 3: Validate Vulnerability

**Context**: Confirm the lack of validation by testing multiple inputs.

Try variations like /<script>alert(1)</script> and monitor if the page attempts to interpret it as HTML/JS without blocking.

> Successful validation shows no rejection; the input is decoded and potentially executable.

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
- [[url-path]]
