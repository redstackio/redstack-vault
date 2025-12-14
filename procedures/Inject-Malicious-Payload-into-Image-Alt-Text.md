---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - injection
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.406Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Image-Alt-Text

## Summary

This procedure involves entering a crafted JavaScript payload into the Image Alt Text field of Concrete CMS during image upload or editing, exploiting lack of input sanitization to set up a stored XSS attack.

## Description

In Concrete CMS, the alt text for images is not properly escaped, allowing attackers with upload permissions to inject HTML and JavaScript. The payload breaks out of the alt attribute using quote closure and injects an event handler like onmouseover. This is particularly dangerous in a CMS environment where images are viewed by multiple users, leading to persistent XSS execution. Prerequisites include authenticated access to the CMS dashboard.

## Requirements

1. Authenticated session in Concrete CMS with image upload/edit privileges
2. Web browser for form interaction
3. Knowledge of XSS payloads tailored to HTML attributes

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping for alt text fields (e.g., using htmlspecialchars in PHP)
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous JavaScript alerts or network requests from image views

## Objectives

1. Deliver unsanitized JavaScript into the alt text attribute
2. Prepare for persistent storage and execution
3. Enable arbitrary code execution on hover interaction

## Instructions

### Step 1: Access Image Upload/Edit

**Context**: Log in to the Concrete CMS dashboard and navigate to the file manager or page editor to upload a new image or edit an existing one.

**Action** (Browser Interaction):

Open the alt text input field and prepare to enter the payload.

> Ensure the form accepts the input without immediate rejection.

### Step 2: Enter the Payload

**Context**: Craft and input the XSS payload to escape the attribute and inject executable code.

**Action** (Form Submission):

Enter the following payload in the alt text field: `"><b onmouseover=alert('Wufff!')>click me!</b><"`

> This payload closes the alt attribute quote, injects a bold tag with an onmouseover event, and reopens the quote to avoid syntax errors. Expected output: Payload accepted in the form.

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
- [[stored-xss]]
- [[concrete-cms]]
