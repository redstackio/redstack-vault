---
tags:
  - auth-bypass
  - openid
  - intercept
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4509da32-74a4-49e0-8486-8ec71f058673
created_at: '2025-12-14T17:31:42.526Z'
updated_at: '2025-12-14T17:31:42.526Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-and-Modify-OpenID-Request

## Summary

This procedure intercepts the POST request to Airflow's /login/ endpoint and modifies the 'openid' parameter to an arbitrary Identity Provider URL, exploiting the lack of validation in Flask-AppBuilder.

## Description

The vulnerability stems from Flask-AppBuilder's failure to check the client-supplied OpenID provider URL against the configured allowlist. By intercepting the request (e.g., using a proxy), an attacker can change the 'openid' value to any URL, such as https://openstackid.org, allowing redirection to an untrusted IDP. This occurs in the legacy OpenID 2.0 flow and requires tools for traffic manipulation.

## Requirements

1. Proxy tool (e.g., Burp Suite) configured between browser and target
2. Access to the login page from previous step
3. Knowledge of an arbitrary OpenID 2.0 endpoint

## Defense

Defensive measures and detection strategies:

- Validate all client-provided IDP URLs server-side against a strict allowlist
- Log and alert on anomalous 'openid' parameters in requests
- Use WAF rules to block modifications to authentication parameters

## Objectives

1. Bypass IDP allowlist enforcement
2. Redirect authentication to attacker-controlled IDP
3. Maintain request integrity for further steps

## Instructions

### Step 1: Set Up Interception

**Context**: Configure tools to capture the login submission.

Launch a proxy tool and set the browser to route traffic through it (e.g., set proxy to 127.0.0.1:8080). Ensure HTTPS interception is enabled if the target uses SSL.

> Successful setup: Browser traffic is visible in the proxy.

### Step 2: Submit and Intercept Request

**Context**: Trigger and capture the POST to /login/.

From the login page, select an IDP and submit. In the proxy, intercept the request before it reaches the server.

> The request body will include 'openid' set to an allowed URL.

### Step 3: Modify and Forward

**Context**: Alter the parameter to exploit the bypass.

Edit the 'openid' value in the POST body to https://openstackid.org (or similar). Forward the request to the server.

> Expected: Server processes the request and redirects to the arbitrary IDP without error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[openid]]
- [[intercept]]
