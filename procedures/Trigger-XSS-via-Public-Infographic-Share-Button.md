---
tags:
  - xss
  - trigger
  - execution
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
updated_at: '2025-12-14T03:16:14.226Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 57b44c55-06b0-4263-90f0-fd114fa701cb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Public-Infographic-Share-Button

## Summary

This procedure triggers the persistent XSS payload by navigating to the public Infogram URL and clicking the Share button, executing arbitrary JavaScript in the visitor's browser.

## Description

Visiting the public infographic renders the Share button with the unsanitized custom link, which includes the injected payload. Clicking the button parses the link as HTML, executing the JavaScript (e.g., confirm dialog). This occurs in the victim's browser context, potentially leading to session hijacking or data exfiltration. No authentication is needed for the victim, making it highly impactful for public content.

## Requirements

1. Public URL of the infographic with XSS payload
2. Victim's web browser (any modern browser)
3. No special permissions; simulates normal user interaction

## Defense

Defensive measures and detection strategies:

- Encode all outputs in HTML contexts to prevent attribute breakout
- Add event handlers to buttons that validate links before rendering
- Monitor browser consoles and error logs for unexpected script execution

## Objectives

1. Render the vulnerable Share button in a victim browser
2. Execute the injected JavaScript payload
3. Demonstrate impact like domain confirmation or cookie access

## Instructions

### Step 1: Access Public URL

**Context**: Simulate a victim visiting the infographic by loading the public URL.

Open the generated public URL in a web browser.

### Step 2: Interact with Share Button

**Context**: Click the Share button to trigger payload rendering and execution.

Locate and click the Share button on the infographic.

> This action causes the browser to process the custom link, executing the onload JavaScript in the SVG element.

**Expected Output**: A confirm dialog appears displaying the document domain (e.g., infogram.com).

### Step 3: Validate Execution

**Context**: Confirm arbitrary code execution and assess potential impact.

After the dialog, inspect browser developer tools for executed scripts or modify the payload for further tests (e.g., alert(document.cookie)).

> Successful execution indicates full JavaScript control in the page context.

**Expected Output**: Dialog confirms domain; console shows script activity.

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
- [[javascript-execution]]
- [[client-side]]
