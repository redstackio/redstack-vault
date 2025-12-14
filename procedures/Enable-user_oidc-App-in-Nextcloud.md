---
id: proc-enable-user_oidc
tags:
  - enable-app
  - nextcloud
  - oidc
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.883Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-user_oidc-App-in-Nextcloud

## Summary

This procedure activates the user_oidc app within a Nextcloud instance, enabling OpenID Connect authentication features that introduce the stored XSS vulnerability when misconfigured.

## Description

Access the Nextcloud admin interface, navigate to the apps section, and enable the user_oidc integration app. This app allows external OIDC providers for user authentication but contains a flaw in LoginController.php where Safari-specific responses fail to escape URLs from discovery endpoints. Enabling it exposes the configuration UI needed for the malicious setup.

## Requirements

1. Administrative login to Nextcloud
2. Running Nextcloud instance with app store access
3. No prior custom apps conflicting with user_oidc

## Defense

Defensive measures and detection strategies:

- Regularly audit enabled apps via Nextcloud logs or admin dashboard
- Disable unused authentication apps to reduce attack surface
- Implement app whitelisting in Nextcloud config.php to prevent unauthorized enables

## Objectives

1. Activate the vulnerable user_oidc app
2. Unlock OIDC provider configuration settings
3. Prepare for payload injection via discovery endpoint

## Instructions

### Step 1: Access Apps Section

**Context**: Log in and navigate to app management.

**Instructions**: Go to http://localhost:8081, log in as admin, click the apps icon in the top-right, and search for "user_oidc" under the integration category.

> Expected output: App listed as available for enablement.

### Step 2: Enable the App

**Context**: Toggle the app to active status.

**Instructions**: Click "Download and enable" or simply "Enable" if already downloaded. Wait for the process to complete.

> Expected output: App moves to the "Active apps" section, with a success notification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[enable-app]]
- [[nextcloud]]
- [[oidc]]
