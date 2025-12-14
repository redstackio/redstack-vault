---
id: proc-uuid-intercept-burp-proxy
tags:
  - proxy
  - http-intercept
  - burp-suite
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
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:29:20.492Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Intercept HTTP Login Requests with Burp Proxy

## Summary

This procedure uses Burp Suite's Proxy to capture and inspect HTTP requests to the WordPress login endpoint, preparing for automated attacks by analyzing request structure.

## Description

Burp Proxy acts as a man-in-the-middle to log traffic. After configuring the browser proxy, submitting a login attempt captures the POST to /wp-login.php, revealing parameters like log, pwd, and wp-submit. This is essential for payload positioning in brute force tools.

## Requirements

1. Burp Suite installed and running
2. Browser proxy configured to 127.0.0.1:8080
3. Target login page accessible

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to complicate proxying
- Detect proxy anomalies via TLS fingerprinting
- Log unusual User-Agent or proxy headers

## Objectives

1. Capture exact login request format
2. Identify modifiable parameters
3. Validate traffic flow

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept browser traffic.

Launch Burp Suite and ensure Proxy listener is on port 8080.

Configure browser proxy settings to use 127.0.0.1:8080.

> Burp intercepts all HTTP/S traffic; install CA certificate for HTTPS.

### Step 2: Submit and Capture Request

**Context**: Perform a login to log the request.

Navigate to /wp-admin/ and submit invalid credentials.

In Burp Proxy > HTTP history, view the captured POST request.

> Expected: Request shows Content-Type: application/x-www-form-urlencoded with log=admin&pwd=wrong.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[proxy]]
- [[http-intercept]]
