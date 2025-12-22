---
id: proc-uber-signup-001
tags:
  - signup
  - initial-access
  - uber-eats
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
updated_at: '2025-12-13T23:52:49.546Z'
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
# Sign-Up-for-Uber-Eats-Restaurant-Account

## Summary

This procedure outlines the process of creating a new restaurant account on Uber Eats to gain access to the onboarding features, serving as the initial entry point for exploiting vulnerabilities in the signup flow.

## Description

The Uber Eats restaurant signup page at https://www.ubereats.com/restaurant/en-CA/signup allows public registration without prior authentication. By completing the form, an attacker establishes a foothold to access restricted onboarding functionalities, including file uploads. This step is prerequisite for subsequent exploitation and assumes no CAPTCHA or rate limiting blocks basic signups.

## Requirements

1. Web browser with JavaScript enabled
2. Valid email address for verification
3. Basic personal or fictional details for restaurant information

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification on signup to prevent automated abuse
- Rate limit signup attempts from IP addresses
- Monitor for anomalous signup patterns leading to immediate onboarding activity

## Objectives

1. Establish authenticated access to Uber Eats restaurant dashboard
2. Unlock onboarding workflow for vulnerability probing
3. Prepare for file upload exploitation

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Access the public registration endpoint to begin account creation.

Open a web browser and visit https://www.ubereats.com/restaurant/en-CA/signup. The page loads a form for restaurant details.

### Step 2: Complete Registration Form

**Context**: Provide required information to submit the signup request.

Fill in fields such as restaurant name, email, phone number, and location. Agree to terms and submit the form. Await email confirmation if prompted.

> Upon success, you will be redirected to the onboarding dashboard, confirming account creation.

### Step 3: Verify Access

**Context**: Ensure the account grants entry to protected features.

Log in if necessary and confirm access to the post-signup onboarding steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[signup]]
- [[initial-access]]
- [[uber-eats]]
