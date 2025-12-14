---
id: proc-burp-config-001
tags:
  - interception
  - proxy
  - http-logging
type: procedure
tools:
  - '[[tools/Burp-Suite-CE]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:12.760Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Configure Burp Suite for HTTP Interception

## Summary

This procedure sets up Burp Suite Community Edition to passively log and intercept HTTP requests from a browser, enabling analysis of web application traffic during security testing, such as capturing API calls in verification flows.

## Description

Burp Suite is configured in logging mode (Proxy interception disabled) to avoid disrupting user interactions while capturing requests to endpoints like those in EXNESS's KYC process. This is essential for identifying unauthenticated or flawed API updates post-verification. Prerequisites include Java runtime and a browser like Chrome or Firefox. Expected outcome: All site traffic logged in Burp's HTTP history for later replay and modification.

## Requirements

1. Burp Suite CE installed (download from PortSwigger)
2. Browser with proxy configuration capability
3. Target site access (e.g., my.exness.com)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or tool signatures in network logs
- Implement client-side certificate pinning to block proxy interception
- Use HSTS and secure headers to limit request tampering

## Objectives

1. Establish passive monitoring of web traffic
2. Prepare for request replay and modification
3. Ensure seamless browsing during testing

## Instructions

### Step 1: Launch and Configure Burp Proxy

**Context**: Start Burp Suite and set it to log mode to capture requests without halting the browser.

No specific command; use GUI:
- Launch Burp Suite CE.
- In the Proxy tab, go to Options and ensure Intercept is OFF (for logging only).
- Set proxy listener to 127.0.0.1:8080.

> Burp will now log all proxied traffic in the HTTP history tab.

### Step 2: Configure Browser Proxy

**Context**: Route browser traffic through Burp to begin logging requests to the target site.

No specific command; use browser settings:
- In browser network settings, set HTTP proxy to 127.0.0.1 port 8080.
- For HTTPS, install Burp's CA certificate (from http://burp/cert) into browser trust store.
- Navigate to target site (e.g., my.exness.com) to test logging.

> Successful setup shows requests appearing in Burp's HTTP history without browser errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-CE]]

## Tags

- interception
- proxy-setup
