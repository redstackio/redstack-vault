---
tags:
  - auth-bypass
  - openid
  - recon
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
impact_level: low
detection_risk: low
sub_techniques: []
id: 93591035-00df-4fd2-8a68-16ffe81125da
created_at: '2025-12-14T17:31:42.537Z'
updated_at: '2025-12-14T17:31:42.537Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Apache-Airflow-Login-Page

## Summary

This procedure accesses the login page of an Apache Airflow instance configured with legacy OpenID 2.0 authentication, preparing for subsequent exploitation steps.

## Description

In Apache Airflow using AUTH_TYPE = AUTH_OID via Flask-AppBuilder, the login page serves as the entry point for OpenID authentication. This step verifies accessibility and observes the initial form, which includes a dropdown of allowed Identity Providers (IDPs). No exploitation occurs here, but it sets up the flow for request interception. The target environment must have OpenID enabled, and the attacker needs unauthenticated network access.

## Requirements

1. Web browser with network access to the Airflow instance
2. Airflow configured with AUTH_OID
3. No prior credentials needed

## Defense

Defensive measures and detection strategies:

- Monitor access logs for repeated login page hits from suspicious IPs
- Disable legacy OpenID 2.0 in favor of modern OAuth 2.0 or SAML
- Implement rate limiting on /login/ endpoint

## Objectives

1. Confirm OpenID authentication is active
2. Identify the login form structure
3. Prepare for request modification

## Instructions

### Step 1: Navigate to Login Page

**Context**: Directly access the authentication interface to load the OpenID form.

Open a web browser and enter the URL of the Airflow instance followed by /login/, e.g., http://target.com/login/. Wait for the page to fully load.

> The page should display a form with fields for OpenID selection. If it redirects or shows an error, the configuration may differ.

### Step 2: Interact with the Form

**Context**: Trigger the initial authentication flow to observe the request.

Select an option from the IDP dropdown and submit the form. Do not complete the flow; instead, prepare to intercept.

> Expected: A POST request to /login/ is prepared with the 'openid' parameter.

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
- [[recon]]
