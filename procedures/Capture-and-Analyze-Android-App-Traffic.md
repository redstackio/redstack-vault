---
id: proc-android-traffic-capture
tags:
  - network-interception
  - android
  - http
  - api-key
type: procedure
tools:
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/mitmproxy-capture]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:24:39.513Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture-and-Analyze-Android-App-Traffic

## Summary

This procedure captures and analyzes network traffic from the Secret Android app to intercept unencrypted HTTP POST requests to Bugsnag's /metrics endpoint, exposing sensitive JSON data including device ID, model, OS version, app details, user ID, and API key. It simulates a man-in-the-middle attack on shared networks.

## Description

The Secret app transmits sensitive information over HTTP to third-party analytics services, allowing interception via proxy tools. This targets Android devices and requires network proximity or proxy configuration. Outcomes include plaintext access to credentials, enabling further exploitation like API abuse or user tracking. Prerequisites include a test Android device with the app installed and proxy setup capabilities.

## Requirements

1. Android device with Secret app installed and network access to Bugsnag.
2. Proxy tool (e.g., mitmproxy) running on a connected machine.
3. Ability to install CA certificates on the Android device for HTTPS interception (though HTTP here is unencrypted).
4. Shared Wi-Fi network or rooted device for transparent proxying.

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS for all third-party communications in mobile apps.
- Monitor network traffic for anomalous proxy configurations or certificate installations.
- Use certificate pinning to prevent MITM attacks.
- Implement app-level encryption for sensitive payloads before transmission.

## Objectives

1. Intercept unencrypted HTTP traffic from the app.
2. Extract and parse sensitive data from JSON payloads.
3. Identify exploitable elements like API keys for follow-on attacks.

## Instructions

### Step 1: Set Up Proxy for Traffic Capture

**Context**: Configure mitmproxy to listen for Android traffic and route the device's requests through it.

**Command** ([[commands/mitmproxy-capture]]):
```bash
mitmproxy --mode transparent --listen-port 8080
```

> This starts mitmproxy in transparent mode on port 8080. Note your machine's IP address for proxy setup.

### Step 2: Configure Android Device and Capture Traffic

**Context**: Point the Android device's Wi-Fi to the proxy and trigger app activity to generate requests.

Install the mitmproxy CA certificate via Settings > Security > Install from storage. Set Wi-Fi proxy to your machine's IP:8080. Launch the Secret app, perform actions like login or usage to trigger POST requests. In mitmproxy, filter for host notify.bugsnag.com and path /metrics.

**Expected Output**: Flow view showing POST request with request body as JSON: {"device_id": "abc123", "api_key": "sk-xyz789"}.

### Step 3: Analyze and Extract Data

**Context**: Inspect the intercepted payload for sensitive information.

Export the flow to a file using mitmproxy's interface (press 'w' to save). Parse the JSON to identify keys like user_id and api_key.

**Expected Output**: Extracted data ready for exploitation, e.g., API key for testing against Bugsnag endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used

- [[commands/mitmproxy-capture]]

## Tools Used

- [[tools/mitmproxy]]

## Tags

- network-interception
- android
- http
- api-key
