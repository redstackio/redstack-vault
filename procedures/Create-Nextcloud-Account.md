---
tags:
  - account-creation
  - initial-access
  - nextcloud
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:30.624Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: abd3350b-9836-4011-a4c2-b7d0f32b60eb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Nextcloud-Account

## Summary

This procedure outlines the creation of a new user account on a Nextcloud instance, serving as the initial access point for subsequent attacks like the DoS exploitation in security settings.

## Description

In the context of targeting Nextcloud for resource exhaustion vulnerabilities, creating an account is the first step to gain authenticated access. This is performed via the public signup page, requiring no prior credentials. The procedure assumes the target Nextcloud allows self-registration, which is common in many deployments. Expected outcomes include a valid user session upon login, enabling navigation to vulnerable features.

## Requirements

1. Web browser with internet access
2. Target Nextcloud instance with open signup endpoint (e.g., https://nextcloud.example.com/signup)
3. Valid email address for registration (optional in some configs)

## Defense

Defensive measures and detection strategies:

- Disable self-registration in Nextcloud admin settings to require admin approval
- Monitor signup logs for unusual patterns or bulk creations
- Implement CAPTCHA on registration forms to deter automated abuse

## Objectives

1. Establish a foothold via a legitimate user account
2. Prepare for authenticated actions in user settings
3. Validate target accessibility without alerting defenses

## Instructions

### Step 1: Access Signup Page

**Context**: Locate and load the registration form to begin account creation.

Navigate to the signup URL, such as https://nextcloud.example.com/signup/.

> The page should display fields for username, email, and password.

### Step 2: Fill and Submit Form

**Context**: Provide minimal required details to complete registration.

Enter a unique username, an email address, and a standard password (e.g., 'password123'). Click 'Sign Up' or equivalent.

> Upon success, expect a confirmation message or email verification prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
