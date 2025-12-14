---
tags:
  - xss
  - execution
  - dashboard
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.981Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0c7ab6a3-32eb-4b0c-90ac-8feb2b74fa94
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Payload-in-Sentry-Admin-Dashboard

## Summary

This procedure describes the triggering mechanism where an admin logs into the Sentry dashboard and navigates to the vulnerable page, causing the stored User-Agent XSS payload to reflect and execute JavaScript in the high-privilege admin context.

## Description

After injection, the payload is reflected in the Marketplace Admin Production dashboard at http://sentry-test.mopub.com/exchange-marketplace/marketplace-admin-production/ inside an <option> tag. When an admin with credentials accesses this page, the payload executes, loading the external script. This step is passive for the attacker but critical for exploitation. Expected outcomes include script download and JS execution, enabling data theft from the admin's browser.

## Requirements

1. Admin credentials for Sentry login (simulated or real for testing)
2. Access to the internal Sentry instance (http://sentry-test.mopub.com/)
3. Previously injected payload via the login endpoint

## Defense

Defensive measures and detection strategies:

- Restrict dashboard access to verified admins with multi-factor authentication
- Log and alert on unusual JavaScript loads or external domain requests from admin sessions
- Use web application firewalls (WAF) to detect XSS patterns in reflected content

## Objectives

1. Cause reflection of the stored payload in the admin view
2. Execute the injected script in the browser context
3. Gain arbitrary code execution privileges in the admin session

## Instructions

### Step 1: Admin Login

**Context**: Log in to the Sentry dashboard using admin credentials to establish a privileged session.

No command; use browser to visit http://sentry-test.mopub.com/ and enter credentials.

> Expected: Successful login and dashboard access.

### Step 2: Navigate to Vulnerable Page

**Context**: Access the specific page where the User-Agent is reflected, triggering the payload.

No command; navigate to http://sentry-test.mopub.com/exchange-marketplace/marketplace-admin-production/ in the browser.

> Expected: Page loads, payload reflects in <option> tag, script loads from attacker domain, and executes to extract data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[dashboard]]
