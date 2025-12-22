---
tags:
  - csrf
  - interception
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b3205c3b-30d3-4a46-b8e7-84e178d82e20
created_at: '2025-12-14T17:33:24.594Z'
updated_at: '2025-12-14T17:33:24.594Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Capture-Callback-Request

## Summary

This procedure uses Burp Suite to intercept the Yahoo authentication callback request during the connection workflow, capturing the OpenID parameters including the auth token for later CSRF exploitation.

## Description

As part of the CSRF-based account takeover on Discourse, the attacker enables traffic interception to monitor the authentication flow. After initiating the Yahoo connection and logging in, the callback to /auth/yahoo/callback is captured as a GET request with sensitive OpenID parameters. The request is forwarded initially but dropped after copying to prevent legitimate connection, allowing token reuse against a victim.

## Requirements

1. Burp Suite installed and browser proxy configured to 127.0.0.1:8080
2. Active Yahoo connection workflow in progress
3. Knowledge of OpenID parameters (e.g., openid.claimed_id, openid.ax.value.email)

## Defense

Defensive measures and detection strategies:

- Enforce POST methods for sensitive actions
- Validate state parameters in OAuth/OpenID flows
- Log and alert on intercepted or dropped auth requests

## Objectives

1. Capture the vulnerable GET callback
2. Extract the Yahoo auth token
3. Prevent completion on attacker's account

## Instructions

### Step 1: Enable Interceptor

**Context**: Set up Burp Suite to capture all HTTP traffic from the browser.

No command executed; in Burp Suite, turn on the Proxy > Intercept tab.

> Browser traffic now routes through Burp for inspection.

### Step 2: Forward Initial Requests and Capture Callback

**Context**: Complete Yahoo login and forward requests until the callback is hit.

No command executed; forward each intercepted request in Burp until reaching the GET to /auth/yahoo/callback with OpenID params.

> The request contains the auth token; inspect and copy the full URL with query parameters.

### Step 3: Copy and Drop Request

**Context**: Save the request for crafting the CSRF payload and abort the flow.

No command executed; copy the HTTP request details, then drop it in Burp to halt processing.

> Token is now available for victim-targeted replay.

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

- [[csrf]]
- [[interception]]
