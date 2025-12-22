---
tags:
  - open-redirect
  - phishing
  - url-manipulation
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:23.461Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6687bddf-5989-4236-bb77-e80a9a5ff511
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Append-Malicious-Next-Parameter

## Summary

This procedure crafts malicious URLs by appending an unvalidated 'next' parameter to Weblate's social login endpoints, setting up redirection to a controlled malicious site.

## Description

The 'next' parameter in Weblate's social auth endpoints lacks validation, allowing attackers to specify external URLs like ///evil.com (triple slash bypasses some checks). This enables luring users to authenticate and then redirecting them to phishing sites for credential theft or session hijacking. Targets include endpoints for Facebook, Google-oauth2, GitHub, Bitbucket, and GitLab.

## Requirements

1. Identified endpoints from prior reconnaissance.
2. Control over a malicious domain (e.g., evil.com).
3. Method to deliver the crafted URL to victims (e.g., email, social engineering).

## Defense

Defensive measures and detection strategies:

- Validate 'next' URLs against a whitelist of internal domains.
- Sanitize input to prevent protocol-relative or external redirects.
- Monitor access logs for suspicious 'next' parameter values.

## Objectives

1. Create exploitable URLs for each social provider.
2. Ensure the parameter triggers no immediate errors.
3. Distribute links to potential victims.

## Instructions

### Step 1: Craft URL for Specific Provider

**Context**: Select a provider endpoint and append the malicious parameter.

For Facebook: Modify to https://hosted.weblate.org/accounts/login/facebook/?next=///evil.com.

> Expected output: Valid URL that loads the login page.

### Step 2: Repeat for All Providers

**Context**: Apply the same modification to other endpoints.

Examples:
- Google: https://hosted.weblate.org/accounts/login/google-oauth2/?next=///evil.com
- GitHub: https://hosted.weblate.org/accounts/login/github/?next=///evil.com

> Expected output: Set of crafted URLs ready for use.

### Step 3: Test URL Loading

**Context**: Verify the page loads without blocking the parameter.

Load each URL in a browser and confirm the social login prompt appears.

> Expected output: No 4xx errors; parameter is accepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
