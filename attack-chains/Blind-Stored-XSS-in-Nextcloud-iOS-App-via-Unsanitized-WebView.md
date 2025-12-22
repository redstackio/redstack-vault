---
tags:
  - xss
  - stored-xss
  - blind-xss
  - nextcloud
  - ios
  - webview
  - data-exfiltration
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-HTML-Payload-to-Nextcloud]]'
  - '[[procedures/Trigger-Blind-Stored-XSS-via-Shared-File-in-Nextcloud-iOS-App]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.429Z'
description: >-
  A multi-stage attack exploiting a Blind Stored XSS vulnerability in the
  Nextcloud iOS app by uploading and sharing a malicious HTML file that executes
  JavaScript in an unsanitized WebView to exfiltrate victim data.
skill_level: intermediate
impact_level: high
id: 4fc38e8e-0b9f-4701-ab2f-9a4b759e74ed
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Blind Stored XSS in Nextcloud iOS App via Unsanitized WebView

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Blind Stored XSS vulnerability in the Nextcloud iOS app. The attack involves uploading a malicious HTML file containing JavaScript for data exfiltration and sharing it with a victim, who triggers the payload upon opening the file in the app's unsanitized WebView.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious Payload] --> B[Share and Trigger Execution]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual upload via Nextcloud interface)

### Target Environment

- Nextcloud server with iOS app
- iOS device for victim interaction
- Attacker-controlled server for receiving exfiltrated data

### Initial Access Requirements

- Valid Nextcloud account for uploading files
- Sharing capabilities enabled
- No prior victim access needed; relies on social engineering for file opening

## Detailed Attack Procedures

### Step 1: Upload Malicious HTML Payload
procedure: [[procedures/Upload-Malicious-HTML-Payload-to-Nextcloud]]

**Objective**: Create and upload an HTML file with embedded JavaScript to the Nextcloud server for storage and potential sharing.

**Instructions**: Prepare a malicious HTML file with a JavaScript payload that exfiltrates data (e.g., via an image src attribute pointing to the attacker's server). Upload the file using the Nextcloud web interface or API.

**Expected Output**: File successfully uploaded and visible in the user's Nextcloud storage.

**Success Indicators**:
- File upload confirmation in Nextcloud
- File accessible in the file list

### Step 2: Share File and Trigger XSS
procedure: [[procedures/Trigger-Blind-Stored-XSS-via-Shared-File-in-Nextcloud-iOS-App]]

**Objective**: Share the malicious file with the victim and wait for them to open it in the Nextcloud iOS app, executing the JavaScript in the unsanitized WebView.

**Instructions**: Use Nextcloud's sharing features to send the HTML file link to the victim. When the victim opens the file on their iOS device via the app, the WebView renders the HTML without sanitization, triggering the payload to send data like IP, location, and OS to the attacker's server.

**Expected Output**: Incoming request to attacker's server with victim details.

**Success Indicators**:
- Victim opens the file (observed via exfiltration logs)
- Data received on attacker's server

## Attack Chain Summary

### Key Achievements

1. Successful upload of unsanitized HTML payload to Nextcloud
2. Triggering of Blind Stored XSS in iOS WebView upon file opening
3. Exfiltration of sensitive victim data including IP, location, and OS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
