---
tags:
  - csrf
  - session-capture
  - nextcloud
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:49.445Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: d7d62170-728f-4b2b-8031-b491617180b4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Capture-Nextcloud-Admin-Session-Cookies

## Summary

This procedure sets up an HTTP proxy to intercept traffic, authenticates as a Nextcloud admin, and captures session cookies necessary for forging CSRF requests to the provisioning API.

## Description

In a CSRF attack, the attacker relies on the victim's authenticated session. This procedure simulates the setup by proxying the login process to extract cookies, which can then be used in curl commands to mimic requests from a malicious site. It targets Nextcloud web interfaces and requires admin credentials. Prerequisites include a running Nextcloud instance and proxy tool access. Expected outcome: Valid session cookies for exploitation.

## Requirements

1. HTTP proxy tool (e.g., Burp Suite or ZAP) installed and configured
2. Valid Nextcloud admin username and password
3. Network access to the Nextcloud server
4. Browser for proxied login

## Defense

Defensive measures and detection strategies:

- Implement strict proxy detection and block unauthorized interception
- Use multi-factor authentication (MFA) to limit session reuse risks
- Monitor for unusual login patterns or proxy traffic

## Objectives

1. Establish proxied connection to Nextcloud
2. Authenticate and capture session artifacts
3. Prepare cookies for CSRF forgery

## Instructions

### Step 1: Configure HTTP Proxy

**Context**: Set up the proxy to intercept all traffic between the browser and Nextcloud server.

**Command** (Proxy Configuration):
No specific command; configure via tool GUI (e.g., set browser proxy to 127.0.0.1:8080).

> Start the proxy listener and ensure it captures HTTPS traffic (handle self-signed certs with -k in curl later).

### Step 2: Authenticate as Admin

**Context**: Log in through the proxied browser to create an authenticated session.

**Command** (Browser Action):
Navigate to http://<nextcloud_server> and enter admin credentials.

> Successful login generates session cookies visible in proxy history.

### Step 3: Extract Cookies

**Context**: Copy the Cookie header from a post-login request.

**Command** (Manual Extraction):
From proxy logs, select a request after login and copy the 'Cookie' header value.

> Store the full cookie string for use in subsequent curl commands; it includes nc_session and other tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy]]

## Tags

- [[csrf]]
- [[session-capture]]
- [[nextcloud]]
