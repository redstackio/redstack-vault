---
tags:
  - proxy
  - interception
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:16.119Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: be98b61e-f242-4452-9589-b5853591c88e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Setup-Burp-Suite-for-Interception

## Summary

This procedure configures Burp Suite as a proxy to intercept and modify HTTP requests from the browser, essential for testing and exploiting web vulnerabilities like reflected XSS by capturing POST submissions.

## Description

Burp Suite acts as a man-in-the-middle proxy to inspect, modify, and replay web traffic. In this scenario, it is used to capture the multipart/form-data POST request during MoPub report creation, allowing payload injection into parameters. Prerequisites include a running Burp instance and browser proxy settings. Outcomes include successful request tampering without alerting the target application.

## Requirements

1. Burp Suite installed and launched
2. Browser configured for manual proxy (e.g., 127.0.0.1:8080)
3. No HTTPS interception certificate issues (install Burp CA if needed)

## Defense

Defensive measures and detection strategies:

- Enforce certificate pinning to block proxy interception
- Detect proxy usage via TLS fingerprinting or JA3 hashes
- Log anomalous request patterns indicating tampering

## Objectives

1. Route browser traffic through Burp proxy
2. Enable interception for specific requests like POST to /reports/custom/add_network_report/
3. Verify interception without disrupting normal flow

## Instructions

### Step 1: Launch and Configure Burp Proxy

**Context**: Start the proxy listener to capture traffic.

No specific command; in Burp Suite, navigate to Proxy > Options, ensure 'Intercept Client Requests' is set to 'On' for the default listener on 127.0.0.1:8080.

> Proxy tab shows 'Intercept is on'; test by browsing a site and seeing captured requests.

### Step 2: Set Browser Proxy Settings

**Context**: Direct the browser to use Burp as its proxy for all traffic.

No specific command; in browser settings (e.g., Chrome: Settings > System > Open proxy settings), set HTTP/HTTPS proxy to 127.0.0.1 port 8080.

> Reload MoPub page; requests should appear in Burp. Install Burp CA certificate for HTTPS if interception fails.

### Step 3: Intercept Specific Request

**Context**: Trigger and pause the vulnerable request.

No specific command; perform the action in the app (e.g., submit form); forward non-relevant requests in Burp until the target POST is captured.

> The intercepted request displays raw HTTP, including body parameters like 'nrnew-interval'.

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

- [[proxy]]
- [[interception]]
- [[web]]
