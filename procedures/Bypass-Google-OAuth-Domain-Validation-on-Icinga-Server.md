---
id: proc-uuid-001
tags:
  - oauth
  - auth-bypass
  - google
  - icinga
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.853Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass Google OAuth Domain Validation on Icinga Server

## Summary

This procedure exploits a misconfiguration in Google OAuth integration where the 'hd' (hosted domain) parameter is not validated, allowing authentication with any Google account instead of restricting to a specific domain like shopify.com. It results in unauthorized access to the Icinga monitoring server, potentially exposing internal infrastructure data.

## Description

In the attack scenario, the target is a web-based Icinga monitoring server using Google OAuth for authentication. Normally, the 'hd' parameter in the OAuth request should enforce domain restrictions (e.g., hd=shopify.com), but due to misconfiguration, it's ignored. An attacker with any Google account can complete the OAuth flow and gain access to the dashboard. This was discovered on Shopify's setup, leading to potential data exposure. Prerequisites include a web browser and a Google account; no advanced tools are needed. Expected outcomes include full access to monitoring features without legitimate credentials.

## Requirements

1. Access to a web browser capable of handling OAuth redirects
2. A valid Google account (any domain, e.g., personal Gmail)
3. Network connectivity to the target's login endpoint (publicly accessible)

## Defense

Defensive measures and detection strategies:

- Enforce 'hd' parameter validation in OAuth configuration to restrict to approved domains
- Implement logging of OAuth authentication attempts, monitoring for non-corporate domains
- Use multi-factor authentication (MFA) beyond OAuth for sensitive internal tools
- Regularly audit OAuth integrations for misconfigurations using tools like OAuth scanners

## Objectives

1. Authenticate to the Icinga server using unauthorized Google credentials
2. Access internal monitoring data and features
3. Demonstrate the risk of sensitive infrastructure exposure

## Instructions

### Step 1: Initiate OAuth Login Flow

**Context**: Start the authentication process on the Icinga server's login page to trigger the Google OAuth redirect.

Navigate to the Icinga login URL (e.g., https://icinga.example.com/login) and select 'Sign in with Google'. This redirects to Google's authorization endpoint without specifying or validating the 'hd' parameter.

> The OAuth request URI will lack hd=shopify.com, allowing any Google account to proceed.

### Step 2: Complete Authentication with Arbitrary Google Account

**Context**: Use a non-restricted Google account to bypass domain checks and gain access.

On the Google login page, enter credentials for a personal Google account (e.g., attacker@gmail.com). Approve the requested scopes (typically email and profile). The flow completes, redirecting back to the Icinga dashboard.

> Successful authentication grants a session token, providing access to the monitoring interface without domain verification.

### Step 3: Verify Access to Monitoring Features

**Context**: Confirm unauthorized access by interacting with the Icinga dashboard.

Once logged in, navigate to sections like 'Hosts', 'Services', or 'Monitoring' to view internal data. No further actions are needed; the bypass is complete.

> Expected visibility includes sensitive metrics like server health, alerts, and configurations that should be employee-only.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- auth-bypass
- google
- icinga
- misconfiguration
