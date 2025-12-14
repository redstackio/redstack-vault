---
id: proc-trigger-reflected-xss-referer
tags:
  - xss
  - reflected-xss
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
updated_at: '2025-12-13T23:56:03.470Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger Reflected XSS via Referer Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in the referer parameter of the Twitter Flight School award page by injecting a javascript: scheme payload, which is reflected into an <a> tag without sanitization.

## Description

The referer parameter in https://www.twitterflightschool.com/student/award/[ID] is user-controlled and inserted directly into an HTML <a> tag's href attribute. By using a javascript: URI, attackers can inject executable code that runs in the victim's browser context upon interaction. This enables arbitrary JavaScript execution, serving as an entry point for further escalation like token theft. The target environment is a web application using JavaScript and HTML, with no input validation on the referer.

## Requirements

1. Access to craft and distribute a malicious URL to the victim
2. Victim must be authenticated or have session on the target site
3. Browser supporting javascript: schemes (most modern browsers)

## Defense

Defensive measures and detection strategies:

- Sanitize or strip javascript: schemes from URL parameters reflected in HTML
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous referer headers in logs

## Objectives

1. Inject payload to reflect XSS in the page
2. Set up for execution on user click
3. Gain JavaScript execution in victim context

## Instructions

### Step 1: Craft Malicious URL

**Context**: Create the URL with the payload in the referer parameter to test or deliver the exploit.

No specific command; manually construct: https://www.twitterflightschool.com/student/award/████████?referer=javascript:alert(document.domain)

> This URL, when visited, reflects the payload into an <a> tag. Expected output: Payload visible in page source as href="javascript:alert(document.domain)".

### Step 2: Deliver to Victim

**Context**: Trick the victim into visiting the URL, e.g., via phishing email or link.

> Victim loads the page, setting up the reflected payload. Success: Page renders with vulnerable <a> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- referer
- javascript
