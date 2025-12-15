---
id: proc-intercept-starbucks-traffic
tags:
  - network-sniffing
  - mobile-interception
  - ssl-pinning
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:32:20.544Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Intercept-App-Traffic-with-Burp-Suite

## Summary

This procedure sets up Burp Suite to intercept HTTPS traffic from the Starbucks Turkey Android app, revealing SSL pinning protections and identifying bypass opportunities on unpinned paths.

## Description

In the attack on the Starbucks app, initial attempts to proxy traffic failed due to SSL pinning, but manual navigation exposed interceptable requests. This involves configuring a proxy on a rooted Android device or emulator, installing Burp's CA certificate, and monitoring app interactions to capture requests.

## Requirements

1. Burp Suite Professional installed and running.
2. Android device/emulator with Starbucks Turkey app installed (rooted for full proxying).
3. Network access to route app traffic through Burp (e.g., Wi-Fi proxy at 127.0.0.1:8080).

## Defense

Defensive measures and detection strategies:

- Implement full SSL pinning across all API paths.
- Monitor for unusual proxy traffic or CA certificate installations on devices.
- Use certificate transparency logs to detect unauthorized CAs.

## Objectives

1. Establish interception of app-server communication.
2. Identify pinned vs. unpinned endpoints.
3. Capture initial requests for analysis.

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp to listen for mobile traffic and generate a CA certificate.

Turn on Intercept in Burp Suite's Proxy tab and configure the Android device's Wi-Fi proxy to point to your host's IP:8080.

> Export Burp's CA certificate and install it on the Android device via Settings > Security > Install from storage.

### Step 2: Launch App and Attempt Interception

**Context**: Run the app to trigger network requests while monitoring Burp.

Open the Starbucks app, log in if prompted (minimal auth), and navigate screens like home and rewards.

> Most requests will fail with pinning errors; note any successes in Burp's HTTP history.

### Step 3: Validate Setup

**Context**: Confirm proxy is working by checking for any intercepted plaintext or errors.

Review Burp's Proxy > HTTP history for app-originated requests.

> Expected: SSL errors on pinned paths; proceed to explore app for unpinned triggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques

- None

## Commands Used

- None (tool-based configuration)

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- network-sniffing
- mobile-interception
