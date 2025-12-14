---
id: proc-uuid-001
name: Inject-and-Trigger-onmouseover-XSS-in-URL-Path
tags:
  - xss
  - reflected-xss
  - onmouseover
  - javascript-injection
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:37.454Z'
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
  - '[[Exploit Public-Facing Application]]'
---
# Inject-and-Trigger-onmouseover-XSS-in-URL-Path

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the URL path of a web application's restaurant listing page, such as Zomato's, by injecting an onmouseover HTML attribute with JavaScript code. The payload is reflected into a link element without sanitization, allowing arbitrary script execution when the victim hovers over the link, potentially leading to session hijacking or data theft.

## Description

The attack targets endpoints like /cs/new-york-city/turtle-bay-restaurants/fast-casual/{restaurant_id}, where the restaurant_id parameter is not properly sanitized. By appending a payload like '/onmouseover=\'alert(1)\'/style=\'height:200;width:200\'/b=' to the ID, the application reflects it into an <a> tag, e.g., <a href="/.../1zqjrw'/onmouseover='alert(1)'/...">. Hovering triggers the script in the browser's context. This is effective in social engineering scenarios where victims are tricked into visiting and interacting with the link. Prerequisites include public access to the endpoint and a modern browser like Firefox.

## Requirements

1. Public access to the target web application (e.g., Zomato restaurant listings)
2. Knowledge of a valid restaurant ID (e.g., '1zqjrw')
3. Web browser supporting JavaScript (e.g., Firefox)
4. No authentication required for the listing page

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for URL path parameters, escaping HTML attributes
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Encode output in HTML contexts to prevent attribute injection
- Monitor for anomalous URL patterns or JavaScript alerts in client-side logs
- Employ Web Application Firewall (WAF) rules to block common XSS payloads

## Objectives

1. Inject and reflect malicious JavaScript into page elements
2. Execute arbitrary code in the victim's browser on user interaction (hover)
3. Demonstrate potential for client-side attacks like cookie theft

## Instructions

### Step 1: Identify Valid Endpoint and Parameter

**Context**: Locate the vulnerable restaurant listing endpoint and a valid restaurant ID to base the payload on.

Use the known endpoint: https://www.zomato.com/cs/new-york-city/turtle-bay-restaurants/fast-casual/1zqjrw

> Verify by visiting the clean URL; it should load without errors.

### Step 2: Craft and Encode Payload

**Context**: Append the onmouseover payload to the restaurant ID, URL-encoding special characters to ensure delivery.

Construct: https://www.zomato.com/cs/new-york-city/turtle-bay-restaurants/fast-casual/1zqjrw'/onmouseover='alert%281%29'/style='height:200;width:200'/b=

> The payload injects onmouseover='alert(1)' into the link href, reflected unsanitized.

### Step 3: Visit URL and Trigger Execution

**Context**: Load the URL in the browser and interact with the reflected element to execute the script.

Open in Firefox and hover over the affected link.

> Expect an alert(1) popup; this confirms XSS execution.

### Step 4: Validate and Document

**Context**: Capture evidence of successful exploitation.

Take a screenshot of the alert and page context.

> Success: Visual proof of script execution on hover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[onmouseover]]
- [[javascript-injection]]
