---
id: proc-3
tags:
  - user-interaction
  - qdesktopservices
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Desktop
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:54.896Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Malicious-URI-in-WebView

## Summary

This procedure relies on user interaction to click a malicious link in the Nextcloud client's WebView, invoking QDesktopServices::openUrl() which passes unvalidated URIs to the OS.

## Description

The WebView, based on QT, does not filter URI schemes from server content. Clicking the link triggers the call in webview.cpp (L226-L232), handing off to the system's default handler for schemes like sftp://, enabling exploitation without client-side blocks.

## Requirements

1. Loaded malicious page in WebView
2. User access to the client interface
3. No additional tools; relies on social engineering

## Defense

Defensive measures and detection strategies:

- Add URI scheme whitelisting in client code (e.g., only http/https)
- Log and alert on openUrl() calls with non-web schemes
- Sandbox WebView to prevent external handler invocation

## Objectives

1. Invoke OS handler via unvalidated URI
2. Transfer control from client to OS
3. Set up for RCE payload

## Instructions

### Step 1: Induce Click

**Context**: Prompt the user to interact with the page (e.g., via fake login button).

No command; observe user clicking the <a> tag.

> The click executes QDesktopServices::openUrl(maliciousUri).

### Step 2: Monitor Handler Activation

**Context**: Verify the OS responds to the URI.

Check system logs or processes for handler launch (e.g., WinSCP.exe starts).

**Expected Output**: Default SFTP client or file manager opens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- webview-click
- uri-trigger
