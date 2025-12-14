---
tags:
  - xss
  - injection
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:20.308Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: b0e7e58b-f006-405a-b5a1-07f3eb670775
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Payload-into-Rocket-Chat-Setup-Wizard

## Summary

This procedure exploits the lack of input sanitization in Rocket.Chat's setup wizard by injecting malicious JavaScript payloads into fields like the instance title, allowing the code to be stored for later execution.

## Description

In the context of a Rocket.Chat instance during initial setup, the wizard accepts user input without proper filtering, enabling attackers to insert HTML and JavaScript. This stored XSS vulnerability persists the payload in the application's data, which is then rendered unsafely when viewed. Prerequisites include access to the setup interface, typically available to administrators or during fresh installations. Expected outcomes include successful payload storage, confirmed by UI persistence, setting the stage for victim execution.

## Requirements

1. Web browser access to the Rocket.Chat setup wizard URL
2. No special credentials beyond setup permissions
3. Target running a vulnerable version of Rocket.Chat (pre-patch for this issue)

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization using libraries like DOMPurify
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript in logs or database fields

## Objectives

1. Store executable code in the application's persistent data
2. Bypass any basic validation in input fields
3. Prepare for cross-user script execution upon rendering

## Instructions

### Step 1: Access Setup Wizard

**Context**: Navigate to the vulnerable input interface to begin payload injection.

Open a web browser and go to the Rocket.Chat instance's setup wizard page. Identify fields like the "instance title" that accept free-text input.

### Step 2: Craft and Inject Payload

**Context**: Create a simple executable payload and submit it to test storage without sanitization.

Enter the following payload into the instance title field: `<img src="invalid" onerror="alert('Stored XSS Triggered')">`. This uses an HTML tag with a JavaScript onerror handler that executes if the image fails to load.

Submit the form to save the changes. The payload should be stored as-is.

> The input is rendered directly without escaping HTML entities, allowing tag parsing.

### Step 3: Verify Storage

**Context**: Confirm the payload persists in the application.

Reload the wizard page or check the saved configuration. The field should display the injected HTML, potentially triggering partial execution in your own browser.

**Expected Output**: Payload visible in the UI without alteration, no error on save.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- web-exploit
