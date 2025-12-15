---
id: proc-weblate-csrf-identify-001
name: Identify Vulnerable CSRF Endpoint in Weblate Authentication
tags:
  - csrf
  - reconnaissance
  - weblate
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:29.492Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable CSRF Endpoint in Weblate Authentication

## Summary

This procedure involves manually inspecting Weblate's profile and authentication pages to identify endpoints for third-party account connections (e.g., Facebook, GitHub) that lack CSRF token validation, setting the stage for exploitation.

## Description

In Weblate, the third-party authentication feature uses the Python Social Auth library without proper CSRF protections on certain POST endpoints. By navigating to the profile page and examining links, attackers can pinpoint vulnerable URLs like /accounts/login/facebook/. This reconnaissance confirms the root cause in the social-app-django backend, enabling subsequent PoC development. The target environment is a web-based Django application, and success relies on public access to the hosted instance.

## Requirements

1. Web browser for manual inspection
2. Access to the target Weblate instance (e.g., https://hosted.weblate.org)
3. Basic knowledge of web authentication flows

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous authentication attempts in logs
- Use Web Application Firewalls (WAF) to detect missing token requests

## Objectives

1. Locate unprotected third-party auth endpoints
2. Document the lack of CSRF validation
3. Prepare for PoC generation

## Instructions

### Step 1: Access Profile Page

**Context**: Navigate to the authentication section to reveal backend links.

Browse to https://hosted.weblate.org/accounts/profile/#auth and inspect the HTML or network requests for links to providers like Facebook.

**Expected Output**: Visible links to /accounts/login/facebook/ without CSRF form fields.

### Step 2: Verify Endpoint Vulnerability

**Context**: Test for CSRF absence by attempting a manual POST without tokens using browser dev tools or a proxy.

Intercept a sample request with Burp Suite to confirm no token is required or validated.

**Expected Output**: Request succeeds without token, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[Reconnaissance]]
- [[weblate]]
