---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - oauth
  - initiate-flow
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.641Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-OAuth-Flow-for-Admin-Account-Addition

## Summary

This procedure triggers the OAuth authentication flow in the admin.8x8.vc application by starting the admin account addition process, exposing the successRedirectUrl parameter for subsequent manipulation.

## Description

In the context of exploiting OAuth misconfigurations, this initial step accesses the target web application and initiates the account addition feature, which relies on Gmail for authentication. The flow generates an OAuth URL without validating the redirect URI, setting the stage for interception. Expected outcome is redirection to Gmail login with inspectable parameters. Prerequisites include network access to the admin portal.

## Requirements

1. Web browser access to admin.8x8.vc
2. Basic understanding of OAuth flows
3. No special credentials required for initiation

## Defense

Defensive measures and detection strategies:

- Monitor admin account addition logs for unusual patterns
- Implement rate limiting on OAuth initiations
- Use web application firewall to inspect OAuth parameters

## Objectives

1. Trigger Gmail OAuth redirection
2. Expose successRedirectUrl for modification
3. Prepare for redirect URI tampering

## Instructions

### Step 1: Access the Admin Application

**Context**: Navigate to the target application to begin the account setup process.

Open a web browser and go to https://admin.8x8.vc. Locate the 'Add Admin Account' or similar feature in the dashboard.

> This loads the interface without authentication if public, or use any available access.

### Step 2: Start Account Addition

**Context**: Initiate the OAuth flow to generate the authentication URL.

Click the button to add a new admin account, selecting Gmail as the provider. The application will redirect to the OAuth endpoint.

> Observe the URL in the browser address bar, noting the successRedirectUrl parameter pointing to the default domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[web-exploit]]
