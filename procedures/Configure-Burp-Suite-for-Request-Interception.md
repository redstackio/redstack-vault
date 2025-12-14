---
id: proc-burp-config-intercept-001
tags:
  - xss
  - web
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.272Z'
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
# Configure Burp Suite for Request Interception

## Summary

This procedure sets up Burp Suite to act as a proxy and intercept HTTP requests from the browser, enabling inspection and modification for vulnerability testing such as XSS exploitation.

## Description

Burp Suite is configured in the browser's proxy settings to capture outgoing traffic. The Proxy tab's Intercept feature is enabled to pause requests for manual review. This is a foundational step for man-in-the-middle style testing on web applications like the Nextcloud about page, where URL parameters are reflected unsanitized.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp proxy (e.g., localhost:8080)
3. Target URL accessible (https://nextcloud.com/about/)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or certificate pinning to detect interception tools
- Implement Content Security Policy (CSP) to mitigate XSS risks

## Objectives

1. Establish interception capability for HTTP requests
2. Prepare for payload injection in subsequent steps
3. Ensure all traffic routes through Burp without errors

## Instructions

### Step 1: Launch and Configure Proxy

**Context**: Start Burp Suite and enable the proxy listener to capture browser traffic.

No specific command; use the Burp Suite GUI: Navigate to Proxy > Options, ensure listener on 127.0.0.1:8080 is running.

> Configure browser proxy settings to point to 127.0.0.1:8080. Expected output: Traffic icon in Burp shows incoming requests.

### Step 2: Enable Active Intercept

**Context**: Turn on interception to pause requests for editing.

No specific command; in Proxy > Intercept tab, click 'Intercept is on'.

> Expected output: Button changes to 'Intercept is on', ready to capture the next request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[web]]
- [[interception]]
