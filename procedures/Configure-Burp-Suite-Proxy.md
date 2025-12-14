---
tags:
  - proxy
  - traffic-interception
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:32:10.202Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 72ee4fd9-5001-4826-a72d-c1b541173efe
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Configure-Burp-Suite-Proxy

## Summary

This procedure configures Burp Suite as a system-wide proxy on macOS to intercept all HTTP/HTTPS traffic, including localhost communications, enabling the capture of sensitive data leaks from applications like Blockstack Browser.

## Description

Burp Suite acts as a man-in-the-middle proxy to monitor and analyze network requests. In this scenario, it's used to observe internal API calls from the Blockstack app that inadvertently expose the Core API Password. Configuration must include removing localhost exceptions to capture traffic to 127.0.0.1:8888. Prerequisites include having Burp Suite installed and basic knowledge of proxy settings.

## Requirements

1. Burp Suite Professional or Community edition installed
2. Administrative access to change system proxy settings
3. Target application (Blockstack) ready for launch

## Defense

Defensive measures and detection strategies:

- Detect proxy configurations via system logs or network monitoring
- Enforce certificate pinning to prevent MITM interception
- Use tools like Wireshark for anomaly detection in traffic patterns

## Objectives

1. Establish full traffic visibility including local endpoints
2. Prepare for real-time request inspection
3. Ensure no traffic bypasses the proxy

## Instructions

### Step 1: Launch and Configure Burp Suite

**Context**: Start Burp and set it to listen on the default proxy port.

No command required; use the Burp interface.

> Open Burp Suite, navigate to Proxy > Options, and ensure it's listening on 127.0.0.1:8080.

### Step 2: Set System Proxy and Remove Exceptions

**Context**: Configure macOS to route all traffic through Burp, including localhost.

No command required; adjust system settings.

> Go to System Preferences > Network > Advanced > Proxies, enable HTTP/HTTPS proxy to 127.0.0.1:8080, and remove any 127.0.0.1 or localhost bypass rules.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- proxy-setup
- interception
- macos
