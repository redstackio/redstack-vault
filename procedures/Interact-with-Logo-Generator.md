---
tags:
  - ssrf
  - shopify
  - websocket
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: dd22c993-7503-4e1d-ae44-c7d51fb0a2f7
created_at: '2025-12-14T03:46:09.114Z'
updated_at: '2025-12-14T03:46:09.114Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Interact-with-Logo-Generator

## Summary

This procedure initiates interaction with the hatchful.shopify.com logo creation interface to establish a WebSocket connection and receive initial SVG data, setting the stage for SSRF exploitation.

## Description

The logo generator uses a WYSIWYG editor where users select templates and provide details like email addresses. The server pushes large SVG payloads over WebSockets, which are then echoed back for PNG conversion. This step focuses on normal usage to map the data flow without raising suspicion, targeting the public-facing web application.

## Requirements

1. Browser access to hatchful.shopify.com
2. Proxy tool like Burp Suite configured for WebSocket interception
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Monitor WebSocket traffic for unusual payload sizes
- Implement client-side validation of SVG inputs before transmission

## Objectives

1. Establish legitimate session and WebSocket channel
2. Capture baseline SVG data for modification
3. Avoid detection by mimicking normal user behavior

## Instructions

### Step 1: Access the Interface

**Context**: Navigate to the logo creator and start a new design session.

Open https://hatchful.shopify.com in your browser and click through to the logo editor. Select a basic template.

### Step 2: Input Details and Trigger Data Exchange

**Context**: Provide minimal input to initiate WebSocket communication.

Enter a test email address (e.g., test@example.com) and proceed to preview the logo. Use browser DevTools (Network tab, filter WS) to observe incoming SVG messages from the server.

**Expected Output**: Escaped SVG code in WebSocket frames, ready for client-side echo.

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

- [[ssrf]]
- [[shopify]]
