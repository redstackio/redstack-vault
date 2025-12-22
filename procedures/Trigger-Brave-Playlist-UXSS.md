---
tags:
  - xss
  - uxss
  - javascript-injection
  - swift
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
  - WebView
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.349Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7ff41845-cee0-4280-92a0-de8e7e1f4288
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger-Brave-Playlist-UXSS

## Summary

This procedure exploits unsafe string concatenation in Brave iOS PlaylistHelper.swift to inject and execute arbitrary JavaScript on the main WebView frame, achieving universal XSS across origins.

## Description

The Brave Playlist feature in iOS uses Swift code (PlaylistHelper.swift, line 228) to build and evaluate JavaScript strings for the mainframe WebView. User-supplied input like nodeTag (from JS tagId) is directly concatenated without sanitization, allowing attackers to inject payloads like '');alert(document.location);//'. Combined with retrieved tokens from prior exposure, this leads to execution on arbitrary domains. The attack requires user interaction (adding to playlist and opening it) but results in cross-origin JS execution, bypassing same-origin policy.

## Requirements

1. Retrieved security tokens from exposed JS (via prior procedure)
2. Victim interaction with Brave Playlist UI on iOS
3. Vulnerable Brave version where concatenation lacks escaping

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in Swift JS builders using proper escaping (e.g., JSON serialization)
- Use WKWebView's scriptMessageHandler with strict validation on received messages
- Log and alert on unexpected JS evaluations in WebView; implement runtime JS sandboxing

## Objectives

1. Inject malicious payload via playlist addition
2. Execute arbitrary JS on mainframe upon playlist open
3. Demonstrate impact with cross-domain alert

## Instructions

### Step 1: Add Malicious Item to Playlist

**Context**: Trigger concatenation by simulating playlist addition with crafted nodeTag.

**Technical Details**: After token retrieval, the postMessage sends the payload. User presses 'Add to Brave Playlist' button, invoking Swift code: let js = "...nodeTag='" + nodeTag + "'..."; webView.evaluateJavaScript(js, ...); where nodeTag breaks out to alert(document.location);

### Step 2: Open Playlist to Execute Payload

**Context**: Finalize and run the injected JS on main WebView.

**Technical Details**: In Brave settings, select and 'Open' the playlist item. This evaluates the concatenated string, executing the payload universally.

### Step 3: Verify Execution

**Context**: Confirm UXSS on target domain.

**Technical Details**: Observe alert popping on the original page's domain (e.g., sites.google.com), proving arbitrary JS ran cross-origin.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- uxss
- javascript-injection
- swift

---
