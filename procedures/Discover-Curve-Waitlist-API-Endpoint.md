---
tags:
  - reconnaissance
  - api-discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:45.241Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9dc5faf1-c9b1-464f-bb1d-09131041e406
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Curve-Waitlist-API-Endpoint

## Summary

This procedure involves navigating to the Curve website's waitlist page and interacting with the 'Track my position' form to trigger and observe the underlying API call, revealing the endpoint used for user position queries without authentication.

## Description

In the context of assessing the Curve waitlist system, this step uncovers the public-facing API endpoint by simulating user interaction. The endpoint accepts email-based lookups and returns user data, exposing a vulnerability. Prerequisites include a web browser and proxy tool like Burp Suite. Expected outcomes include identification of the POST /api/waitlist/us endpoint and confirmation of its unauthenticated nature.

## Requirements

1. Web browser with proxy configuration (e.g., Burp Suite at 127.0.0.1:8080)
2. Access to https://curve.com/usa
3. Basic knowledge of HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on API endpoints to prevent brute-forcing
- Require authentication or CAPTCHA for lookup requests
- Monitor for anomalous request volumes from single IPs

## Objectives

1. Trigger the waitlist API call through legitimate user flow
2. Capture initial request details for further analysis
3. Verify endpoint accessibility without credentials

## Instructions

### Step 1: Access the Waitlist Page

**Context**: Load the target page to begin the interaction and prepare for request capture.

No command required; manually navigate to https://curve.com/usa in your browser.

> Ensure proxy is enabled to intercept traffic.

### Step 2: Initiate Track Position Functionality

**Context**: Submit a test email to generate the API request.

Click 'Track my position', enter a test email (e.g., test@example.com), and submit.

> This triggers a POST request; observe in proxy tool for capture in next procedures.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[Reconnaissance]]
- [[api-discovery]]
