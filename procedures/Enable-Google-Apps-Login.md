---
id: proc-enable-google-apps
name: Enable-Google-Apps-Login
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.077Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Modify Authentication Process]]'
sub_techniques: []
tags:
  - google-apps
  - login-service
  - shopify
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---

# Enable-Google-Apps-Login

## Summary

This procedure activates the Google Apps login service in Shopify's admin settings, enabling single sign-on via Google without disabling traditional email/password authentication.

## Description

Targeting Shopify's login services configuration, this step links a Google account (e.g., from Google Workspace) to the store admin. It occurs in the account settings and assumes prior 2FA setup. The misconfiguration arises because this does not notify or prompt disabling legacy methods, setting up the bypass. Expected outcome: Google login option available alongside standard login.

## Requirements

1. Admin access to Shopify store settings.
2. Linked Google account with Apps authentication enabled.
3. No existing Google login conflicts.

## Defense

Defensive measures and detection strategies:

- Audit login service changes in Shopify logs.
- Require explicit consent for auth method switches.

## Objectives

1. Integrate Google Apps for alternative login.
2. Maintain backward compatibility with email/password.
3. Observe any unintended side effects on existing security.

## Instructions

### Step 1: Navigate to Login Services

**Context**: Access the specific settings section for external logins.

Visit `https://[store-name].myshopify.com/admin/settings/account` and scroll to "Login services".

> Expected: Section displays available providers like Google Apps.

### Step 2: Activate Google Apps

**Context**: Enable and link the Google service.

Select "Google Apps", follow OAuth prompts to authorize the Google account, and save.

> Expected: Success message; Google button appears on login page.

### Step 3: Confirm No Disruptions

**Context**: Verify traditional login still functions.

Test email/password login to ensure it remains active pre-Google use trigger.

> Expected: Normal login without issues.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[google-apps]]
- [[login-service]]
- [[shopify]]
