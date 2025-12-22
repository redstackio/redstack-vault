---
tags:
  - intercept
  - proxy
  - http
type: procedure
tools:
  - '[[tools/Burp-Suite-Pro]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.984Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 622319f1-cf83-48ac-b341-87a262ab5275
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Redemption-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept the HTTP POST request during gift card redemption, capturing key parameters like the token and CSRF authenticity_token for later exploitation.

## Description

Targeting the /<lang>/redeem endpoint (e.g., /fi/redeem), this step involves proxying traffic through Burp Suite while initiating a redemption. The request includes form data such as utf8=✓, authenticity_token=<CSRF>, token=<GIFT_TOKEN>, commit=Redeem Now, and headers like User-Agent and Cookies. This allows analysis and forwarding to Turbo Intruder. Prerequisites: Running Burp Suite proxy and authenticated session.

## Requirements

1. Burp Suite Pro installed and proxy configured (e.g., browser set to 127.0.0.1:8080)
2. Authenticated Reverb session
3. Gift card token obtained

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF token validation and monitor for intercepted traffic patterns
- Use WAF to detect proxy-like User-Agent anomalies

## Objectives

1. Capture the exact redemption request structure
2. Preserve session integrity for replay
3. Identify vulnerability parameters

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception in Burp Suite.

Launch Burp Suite and enable Intercept in the Proxy tab.

**Expected Output**: Proxy listening on default port 8080.

### Step 2: Initiate Redemption and Intercept

**Context**: Trigger the request to capture it.

Navigate to https://sandbox.reverb.com/<lang>/redeem, enter the token, and submit. Intercept the POST request.

**Expected Output**: Request details in Burp: POST /fi/redeem with token parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Pro]]

## Tags

- intercept
- burp
