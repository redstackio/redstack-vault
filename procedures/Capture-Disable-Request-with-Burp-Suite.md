---
id: proc-capture-insightly-request
tags:
  - traffic-interception
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:27:57.465Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Capture Disable Request with Burp Suite

## Summary

This procedure uses Burp Suite to intercept and analyze the HTTP request sent when disabling a Google-linked account in Insightly, providing the endpoint details and parameters needed for CSRF PoC development.

## Description

To exploit the CSRF vulnerability, the attacker must first understand the legitimate disable request. By proxying traffic through Burp Suite from an authenticated session, the POST request to the vulnerable endpoint is captured. This reveals the URL structure (https://crm.na1.insightly.com/Users/GoogleDisable/{id}), method, and parameters like _pjax=#main, confirming the lack of CSRF protections. This step is performed in a controlled test account to avoid impacting real users.

## Requirements

1. Burp Suite installed and configured as a browser proxy
2. Authenticated session in Insightly (Account A)
3. Knowledge of the linked account ID to disable
4. Web browser with proxy settings enabled

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and monitor for proxy interception attempts
- Log all disable requests and alert on unusual user agents (e.g., Burp)
- Implement client-side certificate pinning to block proxy tools

## Objectives

1. Intercept the disable action request
2. Extract endpoint URL and payload details
3. Validate vulnerability absence of CSRF tokens

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept traffic from the browser.

Launch Burp Suite, start the proxy listener on port 8080, and configure the browser to use localhost:8080 as the HTTP proxy. Install Burp's CA certificate in the browser to handle HTTPS.

### Step 2: Perform Disable Action and Capture

**Context**: Trigger the disable request while intercepting to capture the full details.

Log in to Account A, navigate to https://crm.na1.insightly.com/users/usersettings (or /usersettingstry), select the Google referral, and initiate the disable action. In Burp's Proxy > Intercept tab, capture the POST request to https://crm.na1.insightly.com/Users/GoogleDisable/{id}.

**Expected Output**: Raw HTTP request showing POST method, target URL with ID, and body parameter _pjax=#main.

**Success Indicators**:
- Request details match expected format
- No CSRF token observed in headers or body

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[traffic-interception]]
- [[tools/Burp-Suite]]
