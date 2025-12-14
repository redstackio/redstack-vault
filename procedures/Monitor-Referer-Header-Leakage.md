---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - referrer-leak
  - traffic-monitoring
  - info-disclosure
type: procedure
tools:
  - '[[tools/Local-Proxy-for-Traffic-Monitoring]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.014Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Monitor-Referer-Header-Leakage

## Summary

This procedure uses a local proxy to intercept and analyze HTTP traffic from the password reset page, capturing instances where the sensitive reset URL is leaked via the Referer header to third-party domains like Google Analytics.

## Description

Browsers automatically include the Referer header in requests to resources on the page. Without a Referrer-Policy header or meta tag, the full URL (including query parameters with token and email) is sent to external analytics scripts. This allows passive collection by third parties. The procedure involves setting up a proxy to observe this behavior in real-time.

## Requirements

1. Local proxy tool installed and running (e.g., Burp Suite or mitmproxy)
2. Browser configured to route traffic through the proxy
3. Access to the loaded password reset page from the previous procedure

## Defense

Defensive measures and detection strategies:

- Set Referrer-Policy: no-referrer or same-origin to prevent cross-domain leaks
- Audit third-party scripts for unnecessary data exposure
- Log and alert on unexpected Referer headers in analytics data

## Objectives

1. Intercept requests to third-party resources
2. Extract sensitive data from Referer headers
3. Validate the leakage for exploitation potential

## Instructions

### Step 1: Configure Local Proxy

**Context**: Set up the proxy to intercept all browser traffic.

No specific command; configure via tool UI:

- Launch the local proxy (e.g., Burp Suite)
- Set browser proxy to 127.0.0.1:8080
- Install any required CA certificate for HTTPS interception

> Proxy is now ready to capture traffic.

### Step 2: Load Page and Monitor Requests

**Context**: Reload or access the password reset page while proxying traffic to observe leaks.

No specific command; interact via browser:

- Navigate to or refresh https://instagram-brand.com/register/reset/<security_token>?email=<email_address>
- In proxy interface, filter for requests to www.google-analytics.com and pixel.wp.com
- Inspect Referer headers for the full reset URL

> Logs show GET requests with Referer: https://instagram-brand.com/register/reset/<token>?email=<email>

### Step 3: Analyze and Extract Data

**Context**: Parse the captured headers to obtain the token and email for takeover.

No specific command; manual inspection:

- Copy the Referer value from logs
- Note the embedded email and token

> Sensitive data is now available for use in completing the reset on a controlled domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Local-Proxy-for-Traffic-Monitoring]]

## Tags

- [[traffic-interception]]
- [[header-analysis]]
