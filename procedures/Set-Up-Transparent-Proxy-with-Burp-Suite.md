---
id: proc-burp-transparent-proxy-001
tags:
  - mitm
  - proxy
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:44.854Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Set-Up-Transparent-Proxy-with-Burp-Suite

## Summary

This procedure configures Burp Suite in transparent mode to act as a man-in-the-middle proxy for HTTPS traffic, generating CA-signed per-host certificates without requiring trust on the client device, enabling interception of app communications like those from the Twitter iOS app.

## Description

In the context of attacking the Twitter iOS app, this setup allows transparent interception of traffic to api.twitter.com. Burp Suite handles SSL/TLS stripping by forging certificates for target domains. The app's failure to validate certificates means connections proceed without warnings. Prerequisites include a Linux host with Burp installed and network interfaces configured for proxying. Expected outcomes: full visibility into requests/responses, including sensitive headers.

## Requirements

1. Burp Suite Professional installed on Linux
2. Network interface (e.g., wlan0) for traffic routing
3. No client-side modifications needed due to app vulnerability

## Defense

Defensive measures and detection strategies:

- Enforce certificate pinning in apps to prevent proxy interception
- Monitor for anomalous WiFi networks and use VPNs on public networks
- Device-level logging for unexpected proxy connections

## Objectives

1. Establish MITM position for HTTPS traffic
2. Generate fake certificates for api.twitter.com
3. Enable capture of OAuth and auth data

## Instructions

### Step 1: Launch and Configure Burp Suite

**Context**: Start Burp in transparent mode to listen for redirected traffic and auto-generate certificates.

No command needed; use GUI:
- Open Burp Suite
- Go to Proxy > Options > Add listener on 127.0.0.1:8080
- Enable "Transparent proxying" and "Generate CA-signed per-host certificates"

> Burp will create a root CA if not present; export not required as client doesn't trust it anyway. Expected output: Proxy tab shows listening status.

### Step 2: Verify Proxy Readiness

**Context**: Test the proxy setup with a simple connection to ensure certificate generation works.

Use curl or browser to hit a test HTTPS site; observe in Burp.

> Successful if traffic appears in Proxy > HTTP history without client errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- mitm
- proxy
