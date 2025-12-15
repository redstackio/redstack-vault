---
id: proc-auth-nav-dod-portal
tags:
  - authentication
  - web-access
  - dod
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:34.980Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Navigate-DoD-Portal

## Summary

This procedure establishes authenticated access to the DoD self-service portal using Burp Suite as a proxy, allowing for traffic interception and navigation to sensitive data sections without raising immediate alerts.

## Description

In the context of IDOR exploitation, authentication is required to access the portal's dynamic data endpoints. The procedure involves proxying traffic through Burp Suite to monitor requests while logging in and navigating to tabs like 'My █████████ Data'. This sets the stage for capturing vulnerable requests. Expected outcomes include successful session establishment and visibility into user-specific pages, with no data alteration.

## Requirements

1. Valid DoD credentials (username/password for soldier account)
2. Burp Suite installed and running as a proxy (default port 8080)
3. Browser configured to use Burp proxy (e.g., via FoxyProxy extension)
4. Network access to https://█████████/SelfService/

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential misuse
- Monitor proxy traffic anomalies, such as unusual request patterns from authenticated sessions
- Use web application firewalls (WAF) to detect proxy-like modifications in headers

## Objectives

1. Gain valid session tokens for portal access
2. Navigate to PII-containing sections without interception
3. Prepare for request capture in subsequent steps

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Set up Burp to intercept all traffic from the browser for monitoring authentication.

No specific command, but configure browser proxy settings to 127.0.0.1:8080.

> Ensure CA certificate is installed in the browser to handle HTTPS interception.

### Step 2: Authenticate to the Portal

**Context**: Log in using provided credentials to obtain session cookies.

Navigate to https://█████████/SelfService/home/selfservice and enter credentials.

> Successful login results in a 302 redirect to the dashboard with Set-Cookie headers for session management.

### Step 3: Disable Interception and Navigate

**Context**: Turn off interception to allow fluid navigation to data sections.

In Burp Proxy tab, click 'Intercept is on' to toggle off.

> Scroll and click 'My █████████ Data' to load the GET request in HTTP History.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication]]
- [[web-proxy]]
