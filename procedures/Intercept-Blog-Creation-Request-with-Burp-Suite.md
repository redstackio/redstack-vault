---
tags:
  - request-interception
  - burp-suite
  - web
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
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3c72235a-ccd4-4742-8e88-c680c705b1ff
created_at: '2025-12-14T17:30:07.260Z'
updated_at: '2025-12-14T17:30:07.260Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Blog-Creation-Request-with-Burp-Suite

## Summary

Capture a legitimate HTTP POST request for blog creation from an eligible Lichess account using Burp Suite, preserving form data and CAPTCHA for modification.

## Description

Using an old account that meets Lichess's eligibility criteria (e.g., sufficient activity), prepare and intercept the blog submission request. This allows replication of a valid request structure while dropping the original to avoid unintended creation. Burp Suite acts as a man-in-the-middle proxy to inspect and hold the traffic.

## Requirements

1. Eligible old Lichess account
2. Browser configured to proxy through Burp Suite
3. Burp Suite running with Proxy and Repeater tabs active
4. CAPTCHA solving capability (manual or automated)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic patterns or repeated failed requests
- Rate-limit blog creation attempts per IP/session
- Use CSRF tokens to prevent request replay

## Objectives

1. Obtain a valid blog creation request payload
2. Include solved CAPTCHA to bypass additional checks
3. Prepare for cookie substitution without alerting the server

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception for the eligible account's browser.

Launch Burp Suite, enable Intercept in the Proxy tab, and configure the browser (e.g., Firefox) to use Burp's proxy (default 127.0.0.1:8080). Install Burp's CA certificate if needed for HTTPS.

### Step 2: Prepare and Intercept Request

**Context**: Generate the request from the eligible account.

Log in to the old account, navigate to /blog/new, fill the form (title, content), solve CAPTCHA, and submit. In Burp Proxy, intercept the POST request, forward to Repeater, then drop the original.

**Expected Output**: Request in Repeater showing POST /blog/new with multipart/form-data or x-www-form-urlencoded, including cookies, CAPTCHA token, and post content.

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

- [[request-interception]]
- [[tools/Burp-Suite]]
- [[web]]
