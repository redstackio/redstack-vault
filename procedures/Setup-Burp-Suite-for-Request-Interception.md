---
id: proc-uuid-1
name: Setup-Burp-Suite-for-Request-Interception
tags:
  - burp-suite
  - proxy-setup
  - traffic-interception
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
  - '[[Standard Application Layer Protocol]]'
updated_at: '2025-12-14T17:25:13.208Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Standard Application Layer Protocol]]'
---
# Setup-Burp-Suite-for-Request-Interception

## Summary

This procedure configures Burp Suite to act as a proxy for intercepting and monitoring HTTP(S) traffic, essential for capturing and modifying API requests in web application testing.

## Description

Burp Suite is used to sniff all outgoing traffic from a browser, allowing capture of legitimate requests to a template Salesforce instance. This sets up the foundation for request replay and modification without direct interaction with the target. Prerequisites include Burp Suite installed and a browser configured to use the proxy (e.g., localhost:8080). Expected outcome is full visibility into HTTP requests for subsequent exploitation steps.

## Requirements

1. Burp Suite Professional or Community edition installed
2. Browser (e.g., Firefox) with proxy settings enabled for HTTP/HTTPS on 127.0.0.1:8080
3. No CA certificate issues (install Burp's CA for HTTPS interception)

## Defense

Defensive measures and detection strategies:

- Monitor proxy traffic anomalies via network logs (e.g., unusual localhost connections)
- Implement WAF rules to detect repeated request modifications
- Use client certificate pinning to prevent proxy interception

## Objectives

1. Establish traffic interception for request templating
2. Ensure all HTTP(S) flows through Burp without disruption
3. Prepare for request forwarding to Repeater module

## Instructions

### Step 1: Launch and Configure Proxy

**Context**: Start Burp Suite and enable the proxy listener to capture traffic.

No specific command; use GUI:
- Open Burp Suite > Proxy tab > Options > Ensure 'Intercept is on' for initial setup, then turn off for background sniffing.
- Add listener on 127.0.0.1:8080 if not default.

> This configures Burp to passively log all proxied traffic. Expected output: Proxy status 'Running' in the interface.

### Step 2: Route Browser Traffic

**Context**: Direct browser requests through Burp proxy.

No command; manual browser settings:
- In Firefox: Preferences > Network Settings > Manual proxy: HTTP Proxy 127.0.0.1 port 8080, check 'Use this proxy for all protocols'.
- Install Burp CA certificate via http://burp/ to handle HTTPS.

> Browser now routes all traffic via Burp. Expected output: Requests appear in Proxy > HTTP history.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[proxy]]
- [[interception]]
