---
tags:
  - nextcloud
  - web-access
  - recon
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.130Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 731221f1-9fcf-4cfc-905f-3465b8e66d2d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Nextcloud-Login-Page

## Summary

This procedure accesses the public login page of a Nextcloud instance to prepare for password reset exploitation, confirming the endpoint's availability without authentication.

## Description

In the context of testing rate limiting on password reset, start by navigating to the login page of the target Nextcloud instance (e.g., https://ppp.woelkli.com/login). This step ensures the service is responsive and sets up for intercepting subsequent requests. No credentials are needed as the login and reset are public-facing. Expected outcome: Page loads, revealing the forgot password link.

## Requirements

1. Web browser with Burp Suite proxy configured (e.g., FoxyProxy extension)
2. Network access to the target Nextcloud URL
3. Burp Suite running to proxy traffic

## Defense

Defensive measures and detection strategies:

- Monitor access logs for repeated login page hits from suspicious IPs
- Implement WAF rules to rate-limit unauthenticated page views

## Objectives

1. Confirm target accessibility
2. Position for request interception
3. Identify reset functionality presence

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept browser traffic.

Start Burp Suite and configure your browser to use its proxy (default: 127.0.0.1:8080). Enable interception in the Proxy tab.

### Step 2: Navigate to Login

**Context**: Access the login endpoint to load the interface.

In the browser, enter the target URL (e.g., https://ppp.woelkli.com/login) and press Enter. Allow the GET request to pass through Burp if intercepted.

> Expected output: HTML page with login form and 'Forgot password?' link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[nextcloud]]
- [[web-access]]
