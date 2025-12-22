---
id: p1q2r3s4-t5u6-7890-bcde-f12345678901
name: Setup-Web-Proxy-Intercept
tags:
  - proxy-intercept
  - web-testing
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.592Z'
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
# Setup-Web-Proxy-Intercept

## Summary

This procedure configures a web proxy tool like Burp Suite to intercept and inspect HTTP/HTTPS traffic, enabling modification of requests in web applications such as the DoD registration process.

## Description

In the context of testing web vulnerabilities, setting up an intercepting proxy is essential for capturing form submissions and tampering with parameters. This targets public-facing web apps on platforms like ColdFusion, where no authentication is needed initially. Expected outcome: Full control over outgoing requests to identify and exploit flaws like improper access controls.

## Requirements

1. Burp Suite installed and running
2. Browser configured for proxy (e.g., Firefox with FoxyProxy extension)
3. Target web app accessible (e.g., https://████/████████)
4. CA certificate installed for HTTPS interception

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning to block proxy interception
- Monitor for unusual traffic patterns or proxy IP addresses in logs
- Use Web Application Firewalls (WAFs) to detect tampered requests

## Objectives

1. Capture all HTTP requests from the browser
2. Enable request modification without disrupting flow
3. Prepare for parameter tampering in registration

## Instructions

### Step 1: Launch and Configure Burp Suite

**Context**: Start the proxy listener to route browser traffic.

**Instructions**: Open Burp Suite, go to Proxy tab, ensure listener on 127.0.0.1:8080 is running. No command needed; GUI-based.

> Burp will log all intercepted traffic. Expected: Proxy tab shows 'Intercept is on'.

### Step 2: Configure Browser Proxy

**Context**: Point browser to Burp proxy.

**Instructions**: In browser settings, set HTTP proxy to 127.0.0.1:8080. For HTTPS, install Burp's CA cert from http://burp/cert.

> Test by browsing a site; request should appear in Burp. Expected: No SSL warnings, traffic intercepted.

### Step 3: Test Interception on Target

**Context**: Verify on the DoD app.

**Instructions**: Navigate to https://████/████████/screen_questions.cfm with intercept on. Turn on interception in Burp.

> Request to target is paused in Burp. Expected: Full request details visible for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- proxy-intercept
- web-testing
