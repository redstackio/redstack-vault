---
id: proc-trigger-intercept-001
tags:
  - xss
  - web
  - http-request
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
updated_at: '2025-12-14T03:46:37.267Z'
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
# Trigger HTTP Request Interception

## Summary

This procedure generates an HTTP GET request to the target page, causing it to be intercepted by Burp Suite for further modification in XSS testing.

## Description

By navigating to or refreshing the target URL, a standard HTTP request is sent through the Burp proxy. The lack of sanitization in the Nextcloud about page allows URL parameters to be reflected, setting the stage for payload injection. This step confirms the interception setup works in a web environment.

## Requirements

1. Burp Suite proxy active and intercept enabled
2. Browser proxy configured
3. Internet access to https://nextcloud.com/about/

## Defense

Defensive measures and detection strategies:

- Log all HTTP requests for anomalies in user-agent or timing
- Use HTTPS with HSTS to prevent proxy interception

## Objectives

1. Capture the initial request to the vulnerable page
2. Verify proxy routing
3. Pause execution for modification

## Instructions

### Step 1: Navigate to Target

**Context**: Open the about page to initiate the request.

No specific command; in the browser, enter https://nextcloud.com/about/.

> Expected output: Request intercepted in Burp, page load paused.

### Step 2: Refresh for New Request

**Context**: Force a fresh GET request if needed.

No specific command; press F5 or Ctrl+R in the browser.

> Expected output: New intercepted request in Burp's Intercept tab.

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
- [[http-request]]
