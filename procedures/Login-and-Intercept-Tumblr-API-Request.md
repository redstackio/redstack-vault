---
id: proc-tumblr-login-intercept-001
tags:
  - ssrf
  - intercept
  - api
  - tumblr
type: procedure
tools:
  - '[[tools/Burp-Suite-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:39:09.737Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Intercept-Tumblr-API-Request

## Summary

This procedure authenticates to the Tumblr platform and intercepts the GET /api/v2/url_info request generated when following a blog, preparing for SSRF exploitation by capturing the modifiable 'url' parameter.

## Description

In the context of exploiting blind SSRF, an authenticated session is required to trigger the vulnerable endpoint. By following a blog, Tumblr issues a request to /api/v2/url_info with the target blog's URL. Intercepting this via a proxy allows modification of the 'url' parameter to arbitrary values, bypassing any client-side checks. This step assumes the attacker has valid credentials and a proxy tool like Burp Suite configured to intercept traffic from the browser.

## Requirements

1. Valid Tumblr account credentials
2. Browser with proxy configuration (e.g., Burp Suite CA certificate installed)
3. Network access to https://www.tumblr.com/

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on API endpoints to detect anomalous request patterns
- Monitor for proxy-intercepted traffic anomalies in web application firewalls (WAF)
- Enforce strict session validation and log authentication events

## Objectives

1. Establish authenticated access to trigger the vulnerable endpoint
2. Capture the baseline request for modification
3. Prepare for parameter tampering without alerting the application

## Instructions

### Step 1: Authenticate to Tumblr

**Context**: Log in to create a valid session cookie, enabling API calls.

No specific command; use browser to navigate to https://www.tumblr.com/ and enter credentials.

> Successful login redirects to dashboard with session established.

### Step 2: Trigger and Intercept Request

**Context**: Follow a blog to generate the /api/v2/url_info request, capturing it in the proxy.

Configure [[tools/Burp-Suite-Proxy]] to intercept HTTPS traffic. Navigate to a blog page and click 'Follow'.

**Expected Output**: Intercepted GET request: GET /api/v2/url_info?url=https%3A%2F%2Fexample.tumblr.com%2F&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary HTTP/1.1 with Host: www.tumblr.com.

> Request paused in proxy for modification; forward after inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Proxy]]

## Tags

- ssrf
- intercept
- api
- tumblr
