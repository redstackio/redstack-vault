---
id: proc-uuid-3
tags:
  - xss
  - blind-xss
  - exfiltration
  - webview
  - ios
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile App
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:42.892Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Blind-Stored-XSS-in-Nextcloud-iOS-App-WebView

## Summary

This procedure relies on the victim opening the shared HTML file in the Nextcloud iOS App, where the unsanitized WKWebView executes the JavaScript payload, enabling blind data exfiltration to the attacker's server.

## Description

The vulnerability stems from the iOS app's WebView (WKWebView) enabling JavaScript for office document interactions without validating or whitelisting content. When the victim opens the file, the payload runs in the app's sandboxed context, capturing and sending device info like IP, geolocation, and user agent (indicating iOS). The attacker monitors the callback server for blind confirmation of execution. Impact is limited by the sandbox but allows reconnaissance data theft.

## Requirements

1. Victim using vulnerable Nextcloud iOS App
2. Active callback server to log incoming requests
3. Shared file link accessed via iOS app (not web)

## Defense

Defensive measures and detection strategies:

- Update Nextcloud iOS App to patched version with WebView sanitization
- Disable JavaScript in WebView for HTML previews
- Monitor network traffic for unexpected beacons from mobile apps

## Objectives

1. Execute JavaScript in victim's app context
2. Exfiltrate reconnaissance data (IP, location, OS)
3. Confirm blind XSS success via callback

## Instructions

### Step 1: Monitor Callback Server

**Context**: Set up a server to receive and log POST/GET requests from the payload.

Use a simple HTTP server (e.g., Python's http.server) on your endpoint.

> Expected output: Server running and listening on port 80/443.

### Step 2: Await Victim Opening and Verify Exfiltration

**Context**: Once victim opens the file in iOS app, the payload triggers.

Check server logs for incoming request with victim data.

> Expected output: Log entry like "GET /beacon?ip=192.168.1.1&ua=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)".

**Success Indicators**:
- Request from new IP
- User agent confirms iOS execution

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[blind-xss]]
- [[Exfiltration]]
