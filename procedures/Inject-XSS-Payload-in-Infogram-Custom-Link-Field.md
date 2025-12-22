---
tags:
  - xss
  - injection
  - persistent-xss
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
updated_at: '2025-12-14T03:16:14.230Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8f7921d8-41c4-4a13-b702-6fb0dc71c853
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Infogram-Custom-Link-Field

## Summary

This procedure injects a persistent XSS payload into the custom link field of an Infogram infographic's Share button, exploiting insufficient sanitization to store malicious JavaScript for later execution.

## Description

In the Infogram platform, the custom link field for the Share button allows users to specify a URL. Due to lack of proper input sanitization, attackers can inject HTML and JavaScript payloads that break out of the URL attribute context. The payload is persisted in the infographic's configuration and rendered unsafely when the Share button is displayed. This enables arbitrary code execution in the browser of any user who views the public infographic and interacts with the button. Prerequisites include an authenticated Infogram account with editing permissions.

## Requirements

1. Authenticated access to Infogram dashboard
2. Ability to create or edit an infographic
3. Web browser for manual interaction

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all user-controlled fields, especially URL attributes
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript payloads in stored content via WAF or backend logs

## Objectives

1. Store malicious JavaScript in the custom link field without triggering errors
2. Ensure payload persistence across infographic saves and loads
3. Set up for execution in victim browsers

## Instructions

### Step 1: Access Infographic Editor

**Context**: Log in to Infogram and create or open an existing infographic to access the Share button settings.

Navigate to the infographic editor and locate the Share button configuration panel.

### Step 2: Modify Custom Link Field

**Context**: Append the XSS payload to the custom link field to inject executable JavaScript.

Enter the following payload in the custom link field: `"><svg/onload=confirm(document.domain)>`

> This payload closes the URL attribute with "></, then injects an SVG element with an onload handler that executes confirm(document.domain), demonstrating domain access. Save the infographic to persist the payload.

**Expected Output**: Infographic saves successfully; payload is stored without visible errors.

### Step 3: Verify Payload Storage

**Context**: Preview the infographic to ensure the payload is embedded but not yet triggered.

Preview the infographic in edit mode and inspect the Share button's HTML source to confirm the payload is present in the link attribute.

> Look for the injected SVG tag in the rendered HTML of the Share button.

**Expected Output**: Payload visible in source code, no immediate execution during preview.

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
- [[persistent-xss]]
- [[infogram]]
