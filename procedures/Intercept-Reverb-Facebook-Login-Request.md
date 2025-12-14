---
id: proc-intercept-reverb-fb-request-001
tags:
  - intercept
  - facebook-login
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.462Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-Reverb-Facebook-Login-Request

## Summary

This procedure captures the Facebook login request from the Reverb iOS app using network interception tools, allowing analysis of the authentication payload for subsequent modification in an account takeover attack.

## Description

In the context of exploiting the Reverb app's vulnerable Facebook login API, this step involves setting up a proxy to intercept the POST request to /api/auth/facebook. The request contains a JSON payload with the fb_token obtained during the app's login flow. This interception is crucial to identify the structure before token replacement. The target environment is the Reverb iOS app communicating with reverb.com servers via HTTPS, requiring mobile proxy configuration.

## Requirements

1. Burp Suite installed and running with proxy listener enabled (default port 8080)
2. iOS device with Reverb app installed, configured to route traffic through the proxy (e.g., via Wi-Fi settings or tools like Burp's CA certificate installation)
3. Ability to initiate Facebook login in the Reverb app

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or certificate installations on mobile devices
- Implement client-side request signing or pinning to prevent interception
- Log and alert on anomalous login attempts from non-standard user agents

## Objectives

1. Capture the exact format of the login request payload
2. Extract the original fb_token for reference
3. Prepare the request for modification without alerting the server

## Instructions

### Step 1: Configure Proxy on iOS Device

**Context**: Set up the device to route app traffic through Burp Suite for interception.

Install Burp Suite's CA certificate on the iOS device via Settings > General > VPN & Device Management. Configure Wi-Fi proxy to point to your machine's IP and Burp's listener port (e.g., 8080). Enable interception in Burp's Proxy tab.

### Step 2: Initiate Login and Intercept

**Context**: Trigger the vulnerable request to capture it in Burp.

Open the Reverb app, navigate to login, and select Facebook authentication. When the POST request to /api/auth/facebook appears in Burp, intercept it to pause and inspect the JSON payload: {"fb_token": "original_token"}.

**Expected Output**: Halted request in Burp with full headers and body visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[facebook-login]]
