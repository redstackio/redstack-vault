---
tags:
  - android
  - network-inspection
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:44.774Z'
sub_techniques: []
id: faa58760-68be-4cc7-b2fc-34e2c9c7da84
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-Insecure-GET-Request-in-Grab-Android-App-Notifications

## Summary

This procedure involves inspecting network traffic in the Grab Android app's notifications section to identify an insecure GET request that exposes authentication tokens in URL query parameters, setting the stage for information disclosure.

## Description

In the Grab Android app, navigating to the 'Notifications' section triggers a GET request to a web endpoint where the auth_token is appended directly to the URL. This misconfiguration allows the token to be logged, intercepted, or directly accessed, leading to unauthorized exposure of private user data. The procedure requires the app to be installed and uses basic network inspection to capture the request.

## Requirements

1. Grab Android app installed and logged in with a user account
2. Device with developer options enabled or a proxy tool for traffic inspection
3. Basic knowledge of app navigation and network requests

## Defense

Defensive measures and detection strategies:

- Implement proper API design using POST requests for sensitive operations to avoid token exposure in URLs
- Use HTTPS and token validation on the server-side to reject unauthorized access
- Monitor network logs for unusual GET requests to sensitive endpoints

## Objectives

1. Capture the insecure endpoint URL with exposed auth_token
2. Understand the misconfiguration for further exploitation
3. Identify potential for broader information disclosure

## Instructions

### Step 1: Launch App and Navigate to Notifications

**Context**: Open the Grab app and access the notifications to trigger the vulnerable request.

No command required; perform manually in the app.

> Navigate to the 'Notifications' section. The app will make the GET request automatically.

### Step 2: Inspect Network Traffic

**Context**: Use device tools or a proxy to view the request details.

No specific command; enable USB debugging and use tools like Android Studio's Network Profiler or tcpdump.

> Observe the request to `https://grab-attention.grabtaxi.com/passenger/passenger.html?auth_token=[token]&view=268435456`. Note the full URL for the next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[network-inspection]]
- [[information-disclosure]]
