---
id: proc-uuid-1
tags:
  - csrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
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
updated_at: '2025-12-14T17:27:42.838Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Capture Legitimate Account Closure Request

## Summary

This procedure involves intercepting a legitimate HTTP POST request to the account closure endpoint using a proxy tool to analyze its structure, identifying the absence of CSRF protection for subsequent exploitation.

## Description

In a CSRF attack scenario targeting web applications, the first step is to understand the vulnerable endpoint's request format. By proxying traffic through Burp Suite while performing a benign account closure, the attacker captures details like headers, cookies, and form parameters. This reveals the lack of CSRF token validation in /services/user/closeAccount, enabling forgery from external sites. Prerequisites include a test account and browser proxy setup; expected outcome is a detailed request log for PoC crafting.

## Requirements

1. Burp Suite Professional installed and running
2. Browser configured to proxy through Burp (e.g., 127.0.0.1:8080)
3. Access to a test user account in the target application
4. Knowledge of the account settings page

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST endpoints
- Monitor for anomalous proxy traffic or unusual request patterns in logs
- Use Web Application Firewalls (WAF) to detect missing tokens

## Objectives

1. Obtain exact request structure for the vulnerable endpoint
2. Confirm absence of anti-CSRF mechanisms
3. Prepare data for forging requests

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept application traffic.

Launch Burp Suite, start the proxy listener on port 8080, and configure your browser's proxy settings to 127.0.0.1:8080. Install Burp's CA certificate in the browser to handle HTTPS.

### Step 2: Perform Legitimate Action

**Context**: Trigger the account closure request to capture it.

Navigate to the target's login page (e.g., https://target.com/#/login), authenticate with test credentials, then go to account settings and submit the close account form. In Burp, the request will appear in the Proxy history.

### Step 3: Analyze Request

**Context**: Inspect and document the captured request.

Send the request to Burp Repeater, note the POST to /services/user/closeAccount, headers (e.g., Cookie, Referer), and body parameters. Verify no CSRF token is required.

**Expected Output**: Raw HTTP request, e.g.,

```http
POST /services/user/closeAccount HTTP/1.1
Host: target.com
Cookie: session=abc123
Content-Type: application/x-www-form-urlencoded

confirm=close
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[recon]]
- [[web]]
