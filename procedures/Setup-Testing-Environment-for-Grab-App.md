---
id: proc-grab-setup-env-001
tags:
  - mobile-testing
  - api-recon
type: procedure
tools:
  - '[[tools/Nox-App-Player]]'
  - '[[tools/Web-Debugging-Proxy]]'
  - '[[tools/Grab-Android-App]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:27.432Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Setup-Testing-Environment-for-Grab-App

## Summary

This procedure sets up an Android emulator environment with proxy interception to analyze the Grab App's phone login flow and identify vulnerable API endpoints for OTP handling.

## Description

In a controlled testing setup, install the Grab Android App in an emulator like Nox App Player and route its traffic through a web debugging proxy (e.g., Burp Suite or Charles Proxy) to intercept HTTP requests. Initiate a test registration or login using a phone number to trigger the SMS OTP flow, revealing endpoints like /activationsms for resends and /activate for validation. This reconnaissance step uncovers the lack of rate limiting, enabling subsequent brute-force exploitation. Prerequisites include a development machine with emulator support and proxy tools; expected outcome is full visibility into API interactions without alerting production defenses.

## Requirements

1. Android emulator software installed (e.g., Nox App Player)
2. Web debugging proxy configured (e.g., listening on localhost:8080)
3. Grab Android App downloaded from Google Play
4. Test phone number for initial flow verification

## Defense

Defensive measures and detection strategies:

- Monitor emulator traffic patterns in mobile app logs
- Implement proxy detection in app (e.g., certificate pinning)
- Rate limit unusual API probing from non-mobile IPs

## Objectives

1. Gain visibility into OTP login API endpoints
2. Confirm 30-second cooldown on resends and 3-attempt limit per OTP
3. Prepare for automated exploitation without manual intervention

## Instructions

### Step 1: Install and Launch Emulator

**Context**: Create a virtual Android device to run the target app isolated from real hardware.

Install Nox App Player and launch an Android instance (API level 28+ recommended for Grab compatibility).

> Download from official site and follow standard installation; allocate sufficient RAM (2GB+) for smooth app performance.

### Step 2: Configure Proxy Interception

**Context**: Route app traffic to capture and analyze API calls during login.

Set up the web debugging proxy to intercept HTTPS traffic by installing the proxy's CA certificate in the emulator and configuring system proxy settings to point to the proxy host/port (e.g., 127.0.0.1:8080).

> In Nox, go to Settings > Wi-Fi > Modify Network > Advanced > Proxy; for HTTPS, trust the proxy cert via Settings > Security > Install from storage.

### Step 3: Install and Test Grab App

**Context**: Run the app and initiate phone login to observe OTP flow.

Download and install the Grab App via Google Play within the emulator. Register a test account using a disposable phone number to trigger SMS OTP, monitoring proxy for requests to https://p.grabtaxi.com/api/passenger/v2/profiles/activationsms.

> Expected proxy logs: POST requests with phone number payload; response triggers SMS (simulated in emulator).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Nox-App-Player]]
- [[tools/Web-Debugging-Proxy]]
- [[tools/Grab-Android-App]]

## Tags

- mobile-testing
- api-recon
