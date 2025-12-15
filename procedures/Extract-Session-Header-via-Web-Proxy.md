---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - traffic-interception
  - proxy
  - android
type: procedure
tools:
  - '[[tools/Charles-Web-Proxy]]'
  - '[[tools/Nox-App-Player]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:31:42.917Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Extract-Session-Header-via-Web-Proxy

## Summary

This procedure intercepts app network traffic using a web proxy to capture the x-mts-ssid session header required for authenticated API requests.

## Description

Configure the Android emulator to route traffic through Charles Proxy. Perform actions like profile edit to generate requests, then extract the session ID from headers. This token is essential for the brute-force step without re-authenticating.

## Requirements

1. Charles Proxy installed and running
2. Emulator proxy settings configured to 8888 port
3. SSL certificate installed on emulator for HTTPS

## Defense

Defensive measures and detection strategies:

- Detect proxy usage via TLS fingerprinting
- Log anomalous traffic routing from emulators

## Objectives

1. Capture x-mts-ssid header
2. Enable authenticated API calls
3. Prepare for brute-force

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception.

In Nox, set WiFi proxy to Charles IP:8888; install Charles root cert.

### Step 2: Monitor and Extract

**Context**: Trigger traffic during profile edit.

Perform OTP trigger; inspect requests in Charles for x-mts-ssid.

**Expected Output**: Header value like a long session string.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Web-Proxy]]
- [[tools/Nox-App-Player]]

## Tags

- traffic-interception
- proxy
- android
