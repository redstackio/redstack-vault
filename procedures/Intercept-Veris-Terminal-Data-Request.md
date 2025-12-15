---
tags:
  - web-proxy
  - traffic-interception
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 4c9bf7e8-7911-493c-a174-1366b88cc046
created_at: '2025-12-14T17:25:23.336Z'
updated_at: '2025-12-14T17:25:23.336Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-Veris-Terminal-Data-Request

## Summary

This procedure captures the HTTP request sent by the Veris web application when retrieving an authenticated user's terminal data, using a man-in-the-middle proxy to inspect the request structure and identify the vulnerable ID parameter.

## Description

The Veris application sends HTTP requests to an API endpoint to fetch terminal data, including a terminal or gatekeeper ID specific to the user. By intercepting this request during normal usage, an attacker can analyze the format, headers, and parameters. This step is foundational for identifying the IDOR vulnerability, as it reveals how the application handles object references without proper validation. The target environment is the Veris web platform, assuming the attacker has a valid login. Expected outcomes include a clear view of the request, enabling subsequent manipulation.

## Requirements

1. Burp Suite installed and configured as a proxy
2. Browser proxy settings pointed to the tool (e.g., 127.0.0.1:8080)
3. Active authenticated session in the Veris application

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning and HTTP Public Key Pinning (HPKP) to block proxy interception
- Monitor network traffic for signs of proxy usage, such as additional CA certificates installed
- Use Web Application Firewalls (WAF) to detect anomalous request patterns

## Objectives

1. Capture the exact HTTP request for terminal data retrieval
2. Identify the terminal/gatekeeper ID parameter location
3. Prepare for request modification without alerting the application

## Instructions

### Step 1: Launch and Configure Proxy Tool

**Context**: Set up the interception environment to monitor all traffic to Veris.

**Instructions**: Start Burp Suite, navigate to the Proxy tab, and ensure "Intercept is on". Install the Burp CA certificate in the browser if needed to handle HTTPS. Configure the browser's proxy settings to route through Burp.

> This positions the tool to capture outgoing requests. Expected output: Proxy listening confirmation in Burp.

### Step 2: Trigger Terminal Data Retrieval

**Context**: Simulate legitimate user action to generate the target request.

**Instructions**: Log in to the Veris application, navigate to the terminal or dashboard section, and perform the action that loads terminal data (e.g., click 'View Terminal'). The request will pause in Burp's Intercept tab.

> Inspect the request details, such as method (GET/POST), URL (e.g., /api/terminal), and parameters. Expected output: Full request visible, including the user's own ID (e.g., terminal_id=12345).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web-proxy]]
- [[traffic-interception]]
- [[recon]]
