---
id: proc-streamlabs-setup
tags:
  - setup
  - streamlabs
  - account
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
updated_at: '2025-12-14T17:27:57.327Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Set-Up-Streamlabs-Account-for-Testing

## Summary

This procedure establishes a functional Streamlabs account with donation settings configured, enabling testing of the CSRF-vulnerable API endpoint without encountering redirect loops.

## Description

In the context of exploiting the CSRF vulnerability in Streamlabs' donation settings API, initial setup is crucial to replicate the environment where the endpoint is active. This involves creating or logging into a Streamlabs account, connecting a PayPal email for donations, and publishing settings to make the POST endpoint available. The outcome is a testable account where donation configurations can be observed and manipulated.

## Requirements

1. Valid email for Streamlabs registration
2. PayPal account for email connection
3. Web browser access to streamlabs.com

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) on Streamlabs accounts to limit unauthorized access.
- Monitor for unusual account setup patterns, such as rapid PayPal connections from new IPs.

## Objectives

1. Activate the donation settings API endpoint.
2. Avoid common setup errors like redirect loops.
3. Prepare for request interception and testing.

## Instructions

### Step 1: Log In and Navigate to Dashboard

**Context**: Access the Streamlabs dashboard to begin configuration.

Log in at streamlabs.com and go to the dashboard settings section.

### Step 2: Connect PayPal Email

**Context**: Link a payment method to enable donation features.

Add your PayPal email (e.g., example@email.com) in the donation settings and submit the form.

### Step 3: Publish Settings

**Context**: Finalize setup to activate the API endpoint.

Navigate to the editor, configure any basic settings, and click 'Save & Publish' to enable the vulnerable endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- streamlabs
- account
