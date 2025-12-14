---
id: proc-burp-intercept-001
tags:
  - intercept
  - api
  - burp
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:38.709Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Capture-API-Request-with-Burp-Suite

## Summary

This procedure sets up Burp Suite to intercept and capture HTTP requests to the target API endpoint, enabling isolation for modification in subsequent steps of an API exploitation attack.

## Description

In the context of testing public-facing REST APIs like the PlayStation DSS API, this procedure uses Burp Suite's proxy and repeater features to monitor and capture unauthenticated GET requests to sensitive endpoints such as /api/application/state. It requires no special privileges and assumes direct network access to the target. The outcome is a captured request ready for tampering to exploit missing authorization.

## Requirements

1. Burp Suite installed and running with proxy listener enabled (default port 8080)
2. System proxy configured to route traffic through Burp (e.g., browser set to 127.0.0.1:8080)
3. Access to https://dss.api.playstation.com

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to detect anomalous proxy traffic patterns
- Monitor for unusual request forwarding to tools like Burp Repeater via network logs
- Enforce client certificate pinning to prevent proxy interception

## Objectives

1. Capture the initial legitimate GET request to the state endpoint
2. Prepare the request for modification without alerting the target
3. Enable seamless transition to payload injection

## Instructions

### Step 1: Launch Embedded Browser and Enable Interception

**Context**: Start Burp's built-in browser to ensure all traffic is proxied and intercepted.

In Burp Suite Proxy tab -> Intercept tab, click Open Browser to launch Chromium. Set the proxy if needed and enter https://dss.api.playstation.com/api/application/state in the address bar.

> This routes the request through Burp, capturing it in the Intercept tab. Forward the request to proceed.

### Step 2: Locate and Send to Repeater

**Context**: From the history, isolate the request for editing.

In Burp Suite Proxy tab -> HTTP history, highlight the GET request to /api/application/state and press CTRL+R to send to Repeater.

> The request now appears in Repeater, preserving original headers and method for modification.

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

- intercept
- api
- burp
