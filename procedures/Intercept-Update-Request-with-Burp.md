---
id: proc-intercept-request-001
tags:
  - interception
  - burp
  - http-proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:23.723Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Update-Request-with-Burp

## Summary

This procedure uses Burp Suite to capture the POST request when updating low stock variant column settings, exposing the endpoint for IDOR manipulation.

## Description

Burp Suite acts as a man-in-the-middle proxy to intercept HTTPS traffic. By modifying settings (e.g., disabling columns via show_*=0 parameters) and submitting, the request to POST /settings_for_low_stock_variants/{ID} is captured, including Rails authenticity_token for CSRF protection.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. CA certificate installed for HTTPS interception

## Defense

Defensive measures and detection strategies:

- Monitor for proxy anomalies in traffic
- Enforce HSTS to prevent interception

## Objectives

1. Capture legitimate update request
2. Analyze endpoint and parameters
3. Prepare for modification

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept browser traffic.

Launch Burp, enable Intercept in Proxy tab, configure browser proxy settings.

> Expected output: Traffic routed through Burp.

### Step 2: Trigger and Intercept Update

**Context**: Perform action to generate request.

In Stocky, change column settings (e.g., uncheck Title), click Update. Intercept in Burp.

> Expected output: POST request with body like authenticity_token=...&show_title=0&show_price=1.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[interception]]
