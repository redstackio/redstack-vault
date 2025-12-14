---
id: proc-intercept-burp-001
tags:
  - recon
  - web-proxy
  - request-interception
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:20.160Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-Login-Request-with-Burp-Suite

## Summary

This procedure captures HTTP login requests using Burp Suite to analyze form parameters for potential vulnerabilities like SQL injection.

## Description

In web penetration testing, intercepting requests from a login form allows inspection of how user input is handled by the backend. For the Sony endpoint, this revealed unsanitized inputs in the login query, setting the stage for SQL injection testing. The target is a public-facing web application, and success depends on proxy configuration.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Access to the target login endpoint

## Defense

Defensive measures and detection strategies:

- Monitor proxy traffic anomalies in web application firewalls (WAF)
- Use HTTPS with HSTS to complicate interception
- Log all login attempts for unusual patterns

## Objectives

1. Capture the exact HTTP POST request to the login form
2. Identify injectable parameters like username or password
3. Prepare the request for further vulnerability testing

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept traffic from your browser.

Launch Burp Suite and ensure the Proxy tab is active with Intercept on. Configure your browser's proxy settings to route through Burp (default: 127.0.0.1:8080). Install Burp's CA certificate if using HTTPS.

### Step 2: Submit Login Form

**Context**: Trigger the login request to capture it.

Navigate to the target login page (e.g., Sony's web endpoint) and submit a test login with dummy credentials. In Burp's Proxy > Intercept tab, the request will pause for inspection.

**Expected Output**: HTTP POST request details, including headers, body with parameters like username=admin&password=test.

### Step 3: Forward and Save Request

**Context**: Analyze and save the request for SQLMap.

Review the request in Burp, then forward it to the server. Right-click the request in the Proxy history and select "Save item" to export as request.txt for later use.

**Expected Output**: Saved request file ready for injection testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[web-proxy]]
