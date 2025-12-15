---
id: proc-intercept-login-001
name: Intercept Legitimate Login Request with Burp Suite
tags:
  - intercept
  - burp-suite
  - request-capture
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.689Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept Legitimate Login Request with Burp Suite

## Summary

This procedure uses Burp Suite to capture a standard login request from the target web application, providing the baseline structure needed for subsequent parameter manipulation to exploit the authentication bypass.

## Description

To exploit the vulnerability, attackers first need to understand the login request format by intercepting a successful authentication attempt with their own credentials. Burp Suite acts as a man-in-the-middle proxy, allowing capture of the POST request to /app/login. The request includes JSON with 'updates' array containing 'userEmail' and 'gateway' parameters. This step occurs in a browser proxied through Burp, targeting applications like the MTN service running behind nginx.

## Requirements

1. Burp Suite installed and running with proxy listener on localhost:8080
2. Browser configured to use Burp as proxy (e.g., manual proxy settings)
3. Attacker account credentials

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to prevent proxy interception in production
- Log and monitor for proxy-like user agents or unusual request patterns
- Use client-side certificate pinning to block MITM tools

## Objectives

1. Capture the exact structure of a legitimate POST /app/login request
2. Identify key parameters like userEmail and gateway
3. Prepare for modification without alerting the server

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept HTTP traffic from the browser.

No command; launch Burp Suite, go to Proxy tab, ensure Intercept is on, and configure browser proxy to 127.0.0.1:8080.

> Install Burp's CA certificate in the browser to handle HTTPS.

### Step 2: Perform Legitimate Login

**Context**: Submit attacker credentials to trigger the request capture.

Navigate to the login page (https://████████/login) and enter attacker email and password.

> In Burp Proxy > Intercept, forward the captured POST request after viewing it. Note the JSON body with userEmail set to attacker's email and gateway: false.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[request-capture]]
