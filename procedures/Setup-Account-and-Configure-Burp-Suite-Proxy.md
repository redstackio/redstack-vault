---
id: proc-weblate-setup-burp-001
tags:
  - setup
  - proxy
  - account-creation
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.956Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Account-and-Configure-Burp-Suite-Proxy

## Summary

This procedure creates a new account on Weblate's hosted platform and configures Burp Suite as a proxy to intercept browser traffic, enabling capture of subsequent requests during the trial signup process.

## Description

In the context of exploiting a race condition in the trial signup, this initial step establishes the attacker's presence on the platform and prepares for traffic manipulation. The target environment is the web-based hosted.weblate.org, running on Django. Prerequisites include a browser (e.g., Firefox or Chrome) and Burp Suite installed. Expected outcome: A functional account and proxy setup ready for interception.

## Requirements

1. Internet access to https://hosted.weblate.org/
2. Burp Suite installed and running
3. Browser configured to use system proxy (e.g., 127.0.0.1:8080)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic patterns from user IPs
- Implement client-side certificate pinning to detect proxy interception
- Rate limit account registrations

## Objectives

1. Gain initial access via new account
2. Enable request interception for exploitation
3. Position for trial request capture

## Instructions

### Step 1: Register New Account

**Context**: Create a legitimate user account to access the trial feature.

Navigate to https://hosted.weblate.org/ and complete the registration form with valid details (email, username, password). No specific command; use the web interface.

> Upon submission, expect a confirmation email and login success.

### Step 2: Configure Burp Suite Proxy

**Context**: Set up Burp to intercept all browser traffic to the target.

Launch Burp Suite, ensure the proxy listener is running on 127.0.0.1:8080. In the browser, set the proxy to this address and install Burp's CA certificate if prompted for HTTPS interception.

> Test by browsing to a non-sensitive page on hosted.weblate.org; requests should appear in Burp's Proxy > HTTP history tab.

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

- setup
- proxy
- account-creation
