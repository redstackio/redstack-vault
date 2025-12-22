---
tags:
  - web-access
  - registration
  - email-connection
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
updated_at: '2025-12-14T03:15:53.209Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f0e74409-4736-4d71-aa26-64c7fe035890
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Access-RelateIQ-Registration-and-Initiate-Exchange-Connection

## Summary

This procedure outlines the initial steps to access the RelateIQ registration page and initiate the Microsoft Exchange connection feature, setting the stage for exploiting the XSS vulnerability in the email input handling.

## Description

In the context of testing or exploiting the RelateIQ web application, this procedure involves navigating to the public registration endpoint and selecting the MS Exchange/Office365 integration. It requires no authentication and targets the web-based interface at app.relateiq.com. Successful completion positions the attacker at the vulnerable form where input reflection occurs. Expected outcomes include loading the connection interface without errors, enabling subsequent payload injection.

## Requirements

1. Web browser with JavaScript enabled
2. Internet access to https://app.relateiq.com/
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on registration attempts to prevent automated probing
- Monitor for unusual browser behaviors or error page accesses in application logs
- Enforce HTTPS and Content Security Policy (CSP) to mitigate potential XSS impacts

## Objectives

1. Reach the registration form to begin the attack chain
2. Activate the MS Exchange connection option to expose the vulnerable fields
3. Prepare the environment for error triggering without alerting defenses

## Instructions

### Step 1: Navigate to Registration

**Context**: Start by accessing the main application page and locating the registration entry point.

Visit https://app.relateiq.com/ and click 'Register as a new user'.

> This loads the initial registration interface. Expected output: Form fields for user details and connection options appear.

### Step 2: Proceed to Email Connection

**Context**: Accept terms to advance to service integration selection.

Agree to the terms of service, click 'Continue', and choose 'Connect to MS Exchange or Office365'.

> This transitions to the email-specific form. Expected output: Email input field and connection button visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- registration
- email-connection
