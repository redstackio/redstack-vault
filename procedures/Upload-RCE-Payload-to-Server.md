---
id: proc-upload-rce-payload
tags:
  - rce
  - payload-hosting
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:15.175Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-RCE-Payload-to-Server

## Summary

This procedure involves hosting a JavaScript payload on an attacker-controlled HTTPS server to enable Electron manipulation for RCE in the Slack desktop app.

## Description

The payload is a JavaScript file (e.g., t.html) that overwrites Slack's desktop functions, leaks the BrowserWindow object, and creates a new instance with nodeIntegration enabled to execute shell commands. This sets up the redirect target for the HTML injection attack. Tested on standard web servers like Apache or Nginx over HTTPS.

## Requirements

1. Access to an HTTPS server (self-hosted or cloud like AWS S3).
2. Basic web server configuration for static file serving.
3. Knowledge of Electron internals for payload crafting.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual HTTPS traffic to unknown domains from Slack app.
- Enforce strict Content Security Policy (CSP) in Electron apps.
- Use endpoint detection to block unauthorized child_process executions.

## Objectives

1. Host accessible RCE JavaScript for redirect delivery.
2. Ensure HTTPS to avoid mixed content blocks.
3. Prepare for integration with Slack HTML injection.

## Instructions

### Step 1: Create Payload File

**Context**: Write the JavaScript code that manipulates Electron objects.

No specific command; create t.html with content like the RCE payload from [[commands/electron-browserwindow-rce-mac]].

> Save as t.html and verify by loading in a browser.

### Step 2: Upload to Server

**Context**: Deploy the file to make it publicly accessible via HTTPS.

Use server tools (e.g., scp or git) to upload t.html to /var/www/html/ on your HTTPS server.

> Expected: URL https://attacker.com/t.html loads the JS without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- payload-hosting
