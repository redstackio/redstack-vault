---
id: proc-uuid-2
tags:
  - request-interception
  - proxy-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.238Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Password-Reset-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and capture the HTTP POST request from the password reset form submission, allowing inspection and preparation for automated attacks.

## Description

Attackers targeting vulnerable web endpoints often use proxy tools to capture traffic. Here, after configuring Burp Suite as an intercepting proxy, the user submits the password reset form, halting the request for analysis. The captured request reveals the email parameter structure, content-length, and headers, enabling modifications like payload injection. This is crucial for bypassing client-side limits (e.g., 254-character email fields) via direct request crafting. The target environment is any web app with HTTP/HTTPS traffic; expected outcomes include a frozen request in Burp for editing.

## Requirements

1. Burp Suite installed and running
2. Browser proxy configured to route through Burp (e.g., 127.0.0.1:8080)
3. Access to the password reset page

## Defense

Defensive measures and detection strategies:

- Monitor for proxy-like traffic patterns or unusual user-agent strings
- Use HTTPS with HSTS to complicate interception
- Implement request signing or anomaly detection in WAF

## Objectives

1. Intercept the legitimate POST request
2. Analyze parameters for exploitation points
3. Prepare request for forwarding to Intruder

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept traffic from the browser.

Launch Burp Suite and ensure the Proxy tab is active with interception enabled.

> Configure browser proxy settings to 127.0.0.1:8080. Expected output: Traffic routed through Burp.

### Step 2: Submit and Capture

**Context**: Perform the form submission to capture the request.

Navigate to the reset page, enter email, and click 'Send Email' with interception on.

> Request appears in Burp Proxy > Intercept tab. Inspect the POST body for email=... and forward it. Success: Full request details captured.

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

- [[request-interception]]
- [[proxy-capture]]
