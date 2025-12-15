---
id: proc-semrush-auth-navigate
tags:
  - authentication
  - web
  - semrush
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:34.089Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Navigate-to-Semrush-Academy

## Summary

This procedure establishes an authenticated session on the Semrush Academy platform and navigates to the courses library, setting the stage for intercepting enrollment requests in an IDOR exploitation attack.

## Description

In the context of exploiting an IDOR vulnerability in Semrush Academy's course enrollment, authentication provides the necessary session context, while navigation to the courses library triggers the legitimate request flow that can be intercepted and modified. This step assumes the attacker has valid credentials and uses a proxied browser to route traffic through Burp Suite. Expected outcomes include a valid session and visibility into course enrollment actions, enabling subsequent IDOR manipulation without alerting the server to unauthorized access.

## Requirements

1. Valid Semrush Academy login credentials (username and password)
2. Web browser (e.g., Firefox or Chrome) configured to use Burp Suite as a proxy (typically localhost:8080)
3. Internet access to https://www.semrush.com/academy

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential-based initial access
- Monitor for unusual login patterns or proxy-related anomalies in web traffic logs
- Use web application firewalls (WAF) to detect proxy interception attempts via abnormal headers like X-Forwarded-For

## Objectives

1. Establish an authenticated session to mimic legitimate user behavior
2. Position the attacker at the enrollment interface for request interception
3. Ensure all subsequent traffic is proxied for manipulation

## Instructions

### Step 1: Configure Browser Proxy

**Context**: Route browser traffic through Burp Suite to enable request interception from the start.

In your browser's network settings, set the proxy to manual configuration using HTTP proxy at 127.0.0.1:8080. Install Burp's CA certificate if prompted to handle HTTPS interception.

### Step 2: Authenticate to Semrush Academy

**Context**: Log in to create a session that the server trusts for subsequent requests.

Navigate to https://www.semrush.com/academy/login and enter your valid credentials. Submit the login form.

**Expected Output**: Redirect to the dashboard with session cookies set.

### Step 3: Navigate to Courses Library

**Context**: Access the page containing enrollment triggers to prepare for the exploit.

From the dashboard, go to https://www.semrush.com/academy/library/courses?spec=ALL&lang=en-US to load the course listings.

**Expected Output**: Page displays available courses with enrollment options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication]]
- [[web]]
- [[semrush]]
