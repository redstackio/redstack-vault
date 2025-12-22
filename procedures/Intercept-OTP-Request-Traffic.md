---
tags:
  - traffic-interception
  - proxy
  - sniffing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:32:48.211Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 31afc9a7-e258-4ca7-a6e3-005a870ab0e2
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Intercept-OTP-Request-Traffic

## Summary

This procedure sets up a proxy to capture HTTP traffic during the OTP submission in the MTN Group insurance quote process, allowing visibility into the API requests and responses that leak sensitive authentication data.

## Description

Using a tool like Burp Suite, the attacker configures their browser or application to route traffic through a local proxy. During the phone number submission for OTP verification, all requests to the backend API (likely an endpoint like /auth/otp or similar in the corporate.admyntec.co.za domain) are intercepted. This enables real-time inspection of both requests and responses. The target is the web-based insurance portal, and prerequisites include proxy configuration on the client side. Successful execution reveals the full API interaction, including the vulnerable response containing the OTP.

## Requirements

1. Installed proxy tool (e.g., Burp Suite)
2. Browser configured to use the proxy (e.g., 127.0.0.1:8080)
3. HTTPS interception enabled with CA certificate installed

## Defense

Defensive measures and detection strategies:

- Enforce HSTS and certificate pinning to block proxy interception
- Log and alert on proxy-like user agents or unusual traffic patterns
- Use encrypted channels with end-to-end verification

## Objectives

1. Capture the OTP request API call
2. Monitor for the response containing leaked data
3. Ensure no traffic drops during interception

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite as a proxy to intercept traffic from the browser.

Launch Burp Suite and configure the proxy listener on 127.0.0.1:8080. Install the Burp CA certificate in the browser to handle HTTPS.

> Browser traffic now routes through Burp, allowing interception of all requests to the MTN domain.

### Step 2: Submit Request Through Proxy

**Context**: Perform the phone number submission while traffic is intercepted.

With proxy active, revisit the insurance page, enter the target MTN phone number, and submit to trigger the OTP request.

> Burp captures the POST request to the authentication endpoint, showing headers, body (phone number), and prepares for response inspection.

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

- [[traffic-interception]]
- [[proxy]]
- [[sniffing]]
