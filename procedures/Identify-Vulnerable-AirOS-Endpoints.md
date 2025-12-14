---
tags:
  - xss
  - recon
  - ubnt
  - airos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-xss-test]]'
verified: false
platforms:
  - Web
  - Embedded Device
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.659Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1041ea0e-3f37-4ebb-ac93-5263a60afa41
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-AirOS-Endpoints

## Summary

This procedure scans the AirOS web interface on Ubiquiti devices (v6.2.0 and prior) to identify endpoints and parameters vulnerable to reflected XSS due to lack of input sanitization.

## Description

In the attack scenario, an attacker with network access to the device probes the web interface (e.g., http://<device-ip>) for parameters like 'search', 'filter', or 'msg' in endpoints such as /status.html or /login.html. Unsanitized inputs reflect user-supplied data, allowing JavaScript injection. Prerequisites include device IP knowledge and tools like Burp Suite for interception. Expected outcome: Confirmation of injectable parameters for payload delivery.

## Requirements

1. Network access to the AirOS device IP
2. Web proxy tool like Burp Suite
3. Basic knowledge of HTTP requests and JavaScript

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity escaping) on all parameters
- Deploy Web Application Firewall (WAF) to block script tags
- Monitor access logs for anomalous queries with <script> patterns

## Objectives

1. Discover vulnerable endpoints in the AirOS interface
2. Verify reflection of input without sanitization
3. Prepare for payload injection

## Instructions

### Step 1: Access Web Interface

**Context**: Navigate to the device's web login or status page to enumerate endpoints.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -v "http://<device-ip>/status.html"
```

> This fetches the page and identifies form parameters or query strings. Look for GET/POST params in response headers or body.

### Step 2: Test for Reflection

**Context**: Inject a benign payload to check if input is echoed back unsanitized.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -G "http://<device-ip>/status.html" --data-urlencode "search=test<123>"
```

> If '<123>' appears as-is in the HTML response (not &lt;123;&gt;), it's vulnerable. Escalate to <script>alert(1)</script> for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- recon
- ubnt
