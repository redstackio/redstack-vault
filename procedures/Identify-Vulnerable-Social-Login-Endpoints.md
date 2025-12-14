---
tags:
  - recon
  - open-redirect
  - weblate
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
updated_at: '2025-12-14T17:24:23.464Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 26332990-339a-4247-8eeb-2c25eb26f64f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-Social-Login-Endpoints

## Summary

This procedure involves manually inspecting a Weblate instance to identify social authentication endpoints that are susceptible to open redirect attacks due to unvalidated 'next' parameters.

## Description

In Weblate, social login endpoints for providers like Facebook, Google, GitHub, Bitbucket, and GitLab allow a 'next' parameter in the URL query string. Without proper validation, this parameter can be manipulated to redirect users to arbitrary external sites after authentication, facilitating phishing. This step focuses on reconnaissance to locate these endpoints on the target instance, such as hosted.weblate.org.

## Requirements

1. Access to a web browser for URL inspection.
2. Knowledge of the target's base URL (e.g., https://hosted.weblate.org).
3. No authentication required for initial endpoint discovery.

## Defense

Defensive measures and detection strategies:

- Implement URL validation to restrict 'next' parameters to internal domains only.
- Log all redirect attempts and monitor for external domains in 'next' parameters.
- Use Content Security Policy (CSP) to limit redirect destinations.

## Objectives

1. Locate all social login endpoints.
2. Confirm acceptance of 'next' parameter.
3. Prepare for parameter manipulation in subsequent steps.

## Instructions

### Step 1: Inspect Base Login Paths

**Context**: Navigate to the Weblate login page and identify social provider links.

No command required; manually visit https://hosted.weblate.org/accounts/login/ and note social buttons or links leading to provider-specific endpoints like /accounts/login/facebook/.

> Expected output: Visible or inspectable URLs for each provider.

### Step 2: Verify Parameter Acceptance

**Context**: Test if the endpoint accepts a benign 'next' parameter to confirm vulnerability potential.

Append ?next=/safe-internal-page to a sample URL, e.g., https://hosted.weblate.org/accounts/login/facebook/?next=/dashboard, and load it in a browser.

> Expected output: Page loads without error, indicating parameter processing.

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
- [[open-redirect]]
