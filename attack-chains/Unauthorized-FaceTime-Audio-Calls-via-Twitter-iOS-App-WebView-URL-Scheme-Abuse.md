---
id: ac-facetime-twitter-ios-001
tags:
  - url-scheme
  - facetime
  - ios
  - twitter
  - webview
  - iframe
  - auto-launch
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - iOS
  - Web (WebView)
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Embed-FaceTime-URL-Scheme-in-Iframe]]'
  - '[[procedures/Trigger-URL-Scheme-via-Twitter-iOS-WebView]]'
step_count: 2
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:44.715Z'
description: >-
  This attack chain exploits the Twitter iOS app's web view to silently initiate
  FaceTime Audio calls without user permission by embedding malicious URL
  schemes in iframes, leaking the victim's caller ID information.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Drive-by Compromise]]'
---
# Unauthorized FaceTime Audio Calls via Twitter iOS App WebView URL Scheme Abuse

Multi-stage attack chain demonstrating how to exploit the Twitter iOS app's web view to automatically launch FaceTime Audio calls without user interaction, resulting in the leakage of the victim's email or phone number as caller ID.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious HTML with Iframe] --> B[Load HTML in Twitter iOS WebView]
    B --> C[Auto-Launch FaceTime Call and Leak Caller ID]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses basic HTML file hosting)

### Target Environment

- iOS device with Twitter app (tested on iOS 8 and later)
- FaceTime service enabled on the victim's device
- Hosted HTML page accessible via HTTP

### Initial Access Requirements

- Victim must open a link in the Twitter iOS app
- No credentials required
- Network access to host the malicious HTML

## Detailed Attack Procedures

### Step 1: Create Malicious HTML with Embedded FaceTime URL Scheme
procedure: [[procedures/Embed-FaceTime-URL-Scheme-in-Iframe]]

**Objective**: Generate an HTML page containing an iframe that embeds a FaceTime URL scheme to trigger an automatic audio call upon loading.

**Instructions**: Create a simple HTML file with an iframe sourcing the FaceTime URL scheme. Host it on a web server (e.g., http://binaryfactory.ca/urlschemes/facetime.html). The iframe will parse the custom URL and invoke the FaceTime app without user confirmation.

**Expected Output**: An HTML page that, when loaded in a web view, silently initiates a FaceTime Audio call to the specified target (e.g., guillaume@binaryfactory.ca).

**Success Indicators**:
- HTML file created and hosted successfully
- Iframe src attribute correctly set to facetime-audio://target@example.com

### Step 2: Deliver and Trigger via Twitter iOS App WebView
procedure: [[procedures/Trigger-URL-Scheme-via-Twitter-iOS-WebView]]

**Objective**: Lure the victim to load the malicious HTML within the Twitter app's web view, causing the automatic launch of the FaceTime call and exposure of their caller ID.

**Instructions**: Share the hosted HTML link via a tweet or direct message in Twitter. When the victim taps the link on an iOS device, the app's web view loads the page, parses the iframe, and triggers the FaceTime URL scheme without prompting.

**Expected Output**: Victim's device initiates a FaceTime Audio call to the attacker's account, displaying the victim's email or phone number as the caller ID.

**Success Indicators**:
- Victim opens the link in Twitter iOS app
- Incoming FaceTime call received on attacker's device with victim's details leaked

## Attack Chain Summary

### Key Achievements

1. Silent initiation of native app (FaceTime) from web content without user interaction
2. Leakage of sensitive user information (caller ID) via unauthorized call
3. Exploitation of iOS web view's lack of URL scheme validation in third-party apps like Twitter

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
