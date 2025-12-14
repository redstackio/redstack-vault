---
id: proc-access-remedy-sso-admin-page
tags:
  - recon
  - web
  - sso
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:51.557Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Access-Remedy-SSO-Admin-Page

## Summary

This procedure involves navigating to the administrative login page of a Remedy Single Sign-On (SSO) server exposed on the internet, enabling subsequent authentication attempts in vulnerability assessments targeting misconfigured SSO systems.

## Description

In scenarios where Remedy SSO servers are deployed with default configurations and exposed publicly, attackers can directly access the admin interface by appending "/rsso/admin/#/" to the base URL. This step identifies the entry point for administrative access without requiring prior reconnaissance tools, relying on known paths for BMC Remedy products. Successful execution confirms the presence of the login interface, setting the stage for credential testing. Prerequisites include public internet access to the target domain, such as "remedysso.mtncameroon.net". Expected outcomes include visibility of the login form, indicating potential for further exploitation if weak authentication is in place.

## Requirements

1. Web browser with JavaScript enabled for single-page application rendering
2. Direct internet access to the target SSO server's domain (e.g., HTTPS on port 443)
3. Knowledge of the Remedy SSO URL structure

## Defense

Defensive measures and detection strategies:

- Restrict admin endpoints to internal networks using firewalls or IP whitelisting
- Implement web application firewalls (WAF) to block unauthorized access to admin paths
- Monitor access logs for anomalous direct hits to admin URLs from external IPs

## Objectives

1. Confirm exposure of the Remedy SSO admin interface
2. Prepare for authentication testing
3. Identify misconfigurations in public-facing SSO deployments

## Instructions

### Step 1: Navigate to Admin Endpoint

**Context**: Use a standard web browser to directly access the admin login page, bypassing any front-end protections.

No specific command required; perform manual navigation.

```plaintext
URL: https://remedysso.mtncameroon.net/rsso/admin/#/
```

> Enter the URL into the browser address bar and press Enter. The page should load the Angular-based admin login interface if the server is Remedy SSO.

**Expected Output**: Login form with fields for Username and Password, possibly branded with BMC Remedy.

### Step 2: Verify Page Accessibility

**Context**: Inspect the page to ensure it's the correct admin interface and not redirected or protected.

No specific command; use browser developer tools.

> Right-click and select "Inspect" to check for Remedy SSO-specific elements like RSSO branding or admin scripts.

**Expected Output**: DOM elements confirming admin context, no error messages like 404 or 403.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[sso]]
