---
tags:
  - session-hijacking
  - cookie-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Credentials In Files]]'
id: 6cf0ea8c-3124-4243-bbc4-9c90731677e2
created_at: '2025-12-14T17:32:01.650Z'
updated_at: '2025-12-14T17:32:01.650Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Intercept-Session-Cookies-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and capture session cookies and nonces during login to the Semmle platform, enabling authenticated API requests in subsequent steps.

## Description

After account creation, logging in generates session cookies and CSRF nonces in HTTP requests. Burp Suite acts as a proxy to capture these values from GET/POST requests, which are then reused in automated scripts. This allows bypassing authentication for internal API abuse without re-logging in repeatedly.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Valid Semmle account credentials

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and HSTS to prevent MITM interception
- Use short-lived session tokens and rotate nonces frequently
- Monitor proxy-like traffic patterns or unusual request modifications

## Objectives

1. Extract authentication artifacts for API calls
2. Enable persistent authenticated access
3. Prepare data for automation scripts

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept traffic from the browser.

Launch Burp Suite and ensure the proxy listener is active on port 8080. Configure your browser's proxy settings to route through 127.0.0.1:8080.

> Install Burp's CA certificate in the browser to handle HTTPS interception.

### Step 2: Perform Login and Intercept

**Context**: Log in to Semmle and capture the session details.

Navigate to the login page, enter credentials, and submit. In Burp's Proxy > Intercept tab, forward requests while noting the cookie (e.g., session ID) and nonce from the POST request body or headers.

> Expected output: HTTP requests showing Set-Cookie headers and nonce parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files]]

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[session-interception]]
- [[tools/Burp-Suite]]
