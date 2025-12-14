---
id: proc-uuid-step1
tags:
  - web-recon
  - traffic-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:32.108Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept Profile Update Request with Burp Suite

## Summary

This procedure uses Burp Suite to capture and analyze the HTTP POST request for updating user profile information, revealing key parameters like frm_email that are later exploited for XSS.

## Description

In a web application environment, profile updates are often handled via POST requests lacking proper security. By proxying traffic through Burp Suite, attackers can inspect the request structure, including authentication cookies and form fields, to identify potential injection points. This step is crucial for understanding the endpoint `/██████` and its parameters such as action=F█████, token=████████, frm_email, frm_zip5, and cmd_submit=Submit, originating from https://███████.

## Requirements

1. Burp Suite Professional installed and running
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Authenticated access to the target web application

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to monitor proxy-like traffic patterns
- Use certificate pinning to prevent proxy interception in production
- Log all profile update requests for anomaly detection

## Objectives

1. Capture the exact request format for reproduction
2. Identify sensitive parameters for vulnerability testing
3. Establish baseline for crafting malicious requests

## Instructions

### Step 1: Configure Proxy and Authenticate

**Context**: Set up Burp Suite to intercept traffic from the target application.

Launch Burp Suite and ensure the Proxy listener is active on port 8080. Configure your browser's proxy settings to route through Burp. Install Burp's CA certificate in the browser to handle HTTPS.

Navigate to the target site, authenticate, and go to the profile update page.

### Step 2: Submit Form and Intercept

**Context**: Trigger the profile update to capture the request.

Fill out and submit the profile form normally. In Burp's Proxy > HTTP history, locate the POST to `/██████`. Right-click and send to Repeater for analysis.

Inspect parameters: action=F█████, token=████████, frm_email (e.g., user@example.com), frm_zip5 (e.g., 12345), cmd_submit=Submit. Note cookies for session authentication.

**Expected Output**: Full request details displayed, including headers like Origin: https://███████ and Cookie: session=abc123.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- web-recon
- traffic-intercept
