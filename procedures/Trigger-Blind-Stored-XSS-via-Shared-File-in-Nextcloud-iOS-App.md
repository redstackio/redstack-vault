---
tags:
  - xss
  - execution
  - exfiltration
  - ios
  - webview
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.418Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 50b0df92-324f-4421-b08b-82199fa06e0b
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Blind-Stored-XSS-via-Shared-File-in-Nextcloud-iOS-App

## Summary

This procedure shares the uploaded malicious HTML file with a victim using Nextcloud's features, relying on the victim to open it in the iOS app, which triggers JavaScript execution in the unsanitized WebView for data exfiltration.

## Description

Following the upload, the attacker shares the HTML file via Nextcloud's sharing links or direct shares. When the victim accesses and opens the file in the Nextcloud iOS app, the app's WebView (based on WebKit) renders the HTML without sanitization or content type restrictions, enabling arbitrary JavaScript execution. The payload exfiltrates victim-specific data (e.g., IP, geolocation via APIs, OS details) to the attacker's server. The WebView's sandbox limits some actions, but data theft remains possible. This is a blind attack, as execution is not immediately visible to the attacker.

## Requirements

1. Uploaded malicious HTML file in Nextcloud
2. Victim with Nextcloud iOS app installed
3. Sharing permissions enabled in Nextcloud
4. Social engineering to encourage file opening

## Defense

Defensive measures and detection strategies:

- Implement WebView sanitization in the iOS app (e.g., disable JS for HTML files or use safe browsing modes)
- Educate users on risks of opening shared files
- Log and alert on WebView JavaScript executions or outbound requests from the app
- Restrict sharing to verified users

## Objectives

1. Deliver payload to victim via legitimate sharing
2. Execute JavaScript in victim's app context
3. Collect and exfiltrate sensitive data to attacker

## Instructions

### Step 1: Share the Malicious File

**Context**: Use Nextcloud's sharing interface to generate a shareable link or directly share with the victim's account, tricking them into opening it (e.g., via email or chat).

No command required; in the Nextcloud web UI, right-click the file and select 'Share' to create a public or user-specific link.

**Expected Output**: Share link generated and sent to victim.

### Step 2: Monitor for Trigger and Exfiltration

**Context**: Wait for the victim to open the file in the iOS app. Upon opening, the WebView executes the JS payload, sending data to your server.

Set up a listener on your server (e.g., using netcat or a web server) to capture incoming requests.

**Expected Output**: HTTP request to your server with exfiltrated data, e.g., query params containing user agent, IP, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- blind-xss
- data-exfiltration
