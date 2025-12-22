---
id: ac-secret-http-intercept
tags:
  - insecure-communication
  - http
  - mobile
  - api-key-leak
  - network-interception
type: attack_chain
tools:
  - '[[tools/mitmproxy]]'
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Android
  - iOS
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Capture-and-Analyze-Android-App-Traffic]]'
  - '[[procedures/Capture-and-Analyze-iOS-App-Traffic]]'
step_count: 2
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:24:39.528Z'
description: >-
  Demonstrates interception of sensitive user and device data, including API
  keys, transmitted over unencrypted HTTP by the Secret mobile app to
  third-party services like Bugsnag and Flurry.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Intercepting Sensitive Data Transmission in Secret Mobile App via Unencrypted HTTP

Multi-stage attack chain demonstrating the interception of sensitive information transmitted over unencrypted HTTP connections by the Secret mobile app for iOS and Android. The app sends device details, user IDs, and API keys to third-party services like Bugsnag and Flurry without encryption, allowing attackers on the same network to capture this data via man-in-the-middle techniques. This can lead to privacy breaches or unauthorized access using exposed API keys.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Capture Android Traffic] --> B[Analyze Intercepted Data]
    B --> C[Capture iOS Traffic]
    C --> D[Analyze Intercepted Data]
    D --> E[Exploit Exposed Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/mitmproxy]]
- [[tools/Charles-Proxy]]

### Target Environment

- Mobile platforms: Android and iOS
- Required services: Bugsnag (notify.bugsnag.com) and Flurry (data.flurry.com)
- Network access: Same local network as the target device or rooted/jailbroken device for traffic interception

### Initial Access Requirements

- Physical or network proximity to the victim's device
- Ability to install proxy certificates on the mobile device (requires user trust or device compromise)
- No prior credentials needed, but app installation on a test device is assumed

## Detailed Attack Procedures

### Step 1: Capture Android App Traffic
procedure: [[procedures/Capture-and-Analyze-Android-App-Traffic]]

**Objective**: Intercept and analyze unencrypted HTTP POST requests from the Secret Android app to Bugsnag, revealing sensitive JSON payloads with device ID, model, OS version, app details, user ID, and API key.

**Instructions**: Set up a proxy tool like mitmproxy on your machine and configure the Android device to route traffic through it. Launch the Secret app to trigger network requests, then capture the traffic. Filter for POST requests to notify.bugsnag.com/metrics.

Use [[commands/mitmproxy-capture]] to start the proxy:

```bash
mitmproxy --mode transparent --listen-port 8080
```

Configure the Android device's Wi-Fi proxy to point to your machine's IP and port 8080. Install the mitmproxy CA certificate on the device. Run the app and monitor for requests.

**Expected Output**: Captured POST request with JSON payload: {"device_id": "abc123", "model": "Pixel 6", "os_version": "13", "user_id": "user456", "api_key": "sk-xyz789"}.

**Success Indicators**:
- HTTP POST to /metrics on notify.bugsnag.com intercepted
- Sensitive fields like API key visible in plaintext

### Step 2: Capture iOS App Traffic
procedure: [[procedures/Capture-and-Analyze-iOS-App-Traffic]]

**Objective**: Intercept and analyze unencrypted HTTP POST requests from the Secret iOS app to Flurry, extracting binary payloads containing device architecture, OS version, model, screen resolution, UUIDs, and other device info.

**Instructions**: Use a proxy like Charles Proxy configured for iOS traffic. Enable SSL proxying for data.flurry.com. Launch the app on the iOS device to generate traffic, then inspect the requests.

Start Charles Proxy and enable transparent mode. Set the iOS device's proxy settings to your machine's IP and port (default 8888). Install the Charles root certificate in the device's trusted certificates. Trigger app activity and filter for POST to /aas.do.

**Expected Output**: Intercepted POST request with binary/octet-stream payload decoding to fields like architecture: "arm64", os_version: "16.0", model: "iPhone 14", uuid: "def456", screen_resolution: "1170x2532".

**Success Indicators**:
- HTTP POST to /aas.do on data.flurry.com captured
- Device identifiers and info extracted from payload

## Attack Chain Summary

### Key Achievements

1. Successful interception of API keys and user IDs from Android app traffic, enabling potential unauthorized API access.
2. Extraction of detailed device information from iOS app, facilitating targeted privacy attacks or device fingerprinting.
3. Demonstration of insecure HTTP usage in third-party integrations, highlighting risks of man-in-the-middle attacks on shared networks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Sniffing]] Network Sniffing

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
