---
id: proc-ios-traffic-capture
tags:
  - network-interception
  - ios
  - http
  - device-info
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:24:39.499Z'
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
# Capture-and-Analyze-iOS-App-Traffic

## Summary

This procedure intercepts and analyzes network traffic from the Secret iOS app, focusing on unencrypted HTTP POST requests to Flurry's /aas.do endpoint. It reveals binary/octet-stream payloads with device architecture, OS version, model, screen resolution, UUIDs, and other identifiers, enabling privacy violations through device fingerprinting.

## Description

The app uses HTTP for error reporting to Flurry, exposing detailed device info in transit. This procedure uses proxy interception on iOS, requiring certificate trust. It applies to shared networks or jailbroken devices, with outcomes including UUID collection for tracking or correlation attacks. Assumes iOS device with app installed.

## Requirements

1. iOS device with Secret app and access to Flurry services.
2. Proxy tool (e.g., Charles Proxy) on a Mac or connected machine.
3. Installation of proxy root certificate in iOS Settings > General > VPN & Device Management.
4. Wi-Fi proxy configuration or USB tethering for traffic routing.

## Defense

Defensive measures and detection strategies:

- Mandate HTTPS and TLS 1.3 for mobile app communications.
- Detect proxy usage via app integrity checks or anomaly monitoring.
- Obfuscate or encrypt device metadata before sending to analytics.
- Use network firewalls to block unencrypted outbound traffic.

## Objectives

1. Capture HTTP traffic from the iOS app.
2. Decode binary payloads to extract device details.
3. Compile identifiers for potential exploitation like targeted phishing.

## Instructions

### Step 1: Launch Proxy and Enable SSL Proxying

**Context**: Start Charles Proxy and configure it to handle iOS traffic, including enabling interception for Flurry domains.

Open Charles Proxy, go to Proxy > SSL Proxying Settings, and add location data.flurry.com with wildcard paths. Enable transparent HTTP proxying.

**Expected Output**: Proxy listening on port 8888, ready for connections.

### Step 2: Configure iOS Device Proxy

**Context**: Route iOS traffic through the proxy to capture app requests.

On the iOS device, go to Settings > Wi-Fi, tap the info icon for your network, and set HTTP Proxy to Manual with your machine's IP:8888. Install the Charles root certificate by visiting chls.pro/ssl on the device and trusting it in Settings.

Launch the Secret app and interact to generate traffic (e.g., open sessions or report errors).

**Expected Output**: Charles shows POST request to /aas.do with Content-Type: application/octet-stream.

### Step 3: Inspect and Decode Payload

**Context**: Analyze the binary payload for embedded device information.

In Charles, select the request, view the raw body, and use a hex editor or script to decode. Look for strings like OS version, model, and UUIDs in the stream.

**Expected Output**: Decoded data: architecture "arm64", model "iPhone 14", UUID "def456", screen "1170x2532".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- network-interception
- ios
- http
- device-info
