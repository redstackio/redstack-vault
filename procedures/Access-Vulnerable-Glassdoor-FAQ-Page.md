---
tags:
  - xss
  - recon
  - glassdoor
type: procedure
tools:
  - '[[tools/Safari]]'
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.223Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 09c8839d-685e-42f4-9c8c-0b65b9889e14
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Vulnerable Glassdoor FAQ Page

## Summary

This procedure involves navigating to the base URL of Glassdoor's FAQ page to establish the vulnerable endpoint for path-based reflected XSS exploitation. It serves as the initial reconnaissance step to confirm the page's accessibility and structure.

## Description

The Glassdoor FAQ page at `https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true` reflects user-supplied input from the URL path directly into the HTML content without sanitization. This procedure ensures the attacker can access the page in a controlled environment, such as a browser, to prepare for payload injection. Expected outcomes include loading the page without errors, allowing subsequent manipulation of the path parameter.

## Requirements

1. Internet access to reach Glassdoor's public website.
2. A web browser (Safari, Chrome, or Firefox).
3. No authentication or special permissions needed.

## Defense

Defensive measures and detection strategies:

- Implement URL path validation and sanitization on the server side.
- Use Content Security Policy (CSP) headers to restrict inline script execution.
- Monitor for anomalous URL patterns in web server logs.

## Objectives

1. Confirm accessibility of the vulnerable FAQ page.
2. Identify the exact path structure for payload insertion.
3. Establish a baseline for testing the reflection.

## Instructions

### Step 1: Launch Browser and Navigate

**Context**: Open a supported web browser and directly access the vulnerable URL to verify the page loads correctly.

No specific command required; use the browser's address bar:

```url
https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true
```

> This loads the Microsoft FAQ page. Inspect the source to confirm the path 'Microsoft-Question-FAQ200086-E1651.htm' is rendered in the HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari]]
- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[xss]]
- [[recon]]
- [[glassdoor]]
