---
tags:
  - xss
  - infogram
  - api-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T03:16:30.586Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e84c8e3c-c4ee-4ec7-a8c3-6790a49457d9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Infogram-and-Intercept-Request

## Summary

This procedure sets up an Infogram project and configures request interception to prepare for payload injection in a stored XSS attack, focusing on the initial access and reconnaissance of the API endpoint.

## Description

In the context of exploiting Infogram's infographics feature, this procedure involves creating a new project, adding a media element with a benign link to trigger an API update, and intercepting the request using a web debugger. It targets the web-based platform where user inputs are processed without protocol validation, laying the groundwork for XSS injection. Expected outcomes include a captured API request ready for modification, requiring only basic account access.

## Requirements

1. Active Infogram account (free tier sufficient)
2. Browser with proxy support (e.g., Chrome or Firefox)
3. Web debugger tool like Burp Suite installed and configured
4. Internet access to infogram.com

## Defense

Defensive measures and detection strategies:

- Implement client-side proxy detection (e.g., check for unusual headers or delays)
- Log and monitor API update requests for anomalous payloads
- Enforce strict Content Security Policy (CSP) to block inline JavaScript execution

## Objectives

1. Establish initial access to the infographic editor
2. Trigger and intercept the media update API call
3. Prepare the request body for payload modification

## Instructions

### Step 1: Create New Infographic

**Context**: Start a project to access the editor interface.

Log in to Infogram and click 'Create new infographic'.

> This opens the editor; no commands needed, purely UI interaction.

### Step 2: Add Media Element

**Context**: Insert a benign link to initiate the API request.

In the editor, select 'Add media' and enter `http://google.com/` as the link.

> The UI prepares to send a POST request upon confirmation.

### Step 3: Enable Interception

**Context**: Configure the debugger to capture the request.

Launch Burp Suite, set your browser proxy to 127.0.0.1:8080, and turn on intercept in the Proxy tab.

> Confirm the link in the UI to trigger interception of the POST to `/api/infographics/update/[project_id]`.

### Step 4: Verify Interception

**Context**: Ensure the request is captured before proceeding.

Inspect the intercepted request body for the link parameter.

> Success: Request shows benign link; do not forward yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss-prep
- api-recon
