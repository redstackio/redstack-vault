---
id: proc-uuid-3
tags:
  - login-trigger
  - redirect
  - token-exposure
type: procedure
tools:
  - '[[tools/Google-Analytics]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:57.296Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Trigger-Victim-Login-and-Redirect-with-Token

## Summary

This procedure relies on the victim's authentication during the redirect to Shopify's app page, where the CSRF authenticity_token is appended to the URL query parameter, captured by the embedded GA code.

## Description

Once the victim is redirected to the app support page, Shopify checks authentication. If not logged in, it prompts login at https://apps.shopify.com/#login. Post-login, the redirect to https://apps.shopify.com/[app_id]?authenticity_token=[token] exposes the token in the URL, which GA tracks and sends externally.

## Requirements

1. Victim must have or create a Shopify account
2. Attacker's app support page active
3. No direct attacker control; depends on victim action

## Defense

Defensive measures and detection strategies:

- Use token binding to sessions or avoid URL exposure
- Sanitize analytics tracking to exclude query params
- Rate-limit login redirects from suspicious sources

## Objectives

1. Prompt victim authentication
2. Generate token-appended redirect URL
3. Ensure GA captures the full URL passively

## Instructions

### Step 1: Initiate Redirect to Support Page

**Context**: The malicious page's script opens the support endpoint, which handles unauthenticated users by redirecting to login.

No specific command; the JavaScript from the previous procedure triggers this automatically upon page load.

> Expected output: If unauthenticated, browser navigates to login page.

### Step 2: Complete Login and Observe Redirect

**Context**: Victim enters credentials; Shopify redirects back with token in URL, activating GA tracking.

No specific command; victim interacts with Shopify's login form; attacker monitors via GA for capture confirmation.

> Expected output: URL in browser shows ?authenticity_token=...; GA logs the hit.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Analytics]]

## Tags

- login-trigger
- redirect
- token-exposure
