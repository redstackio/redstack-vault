---
id: uuid-setup-swiftype
tags:
  - setup
  - account-creation
  - api-engine
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
updated_at: '2025-12-14T03:16:20.014Z'
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
# Setup-Swiftype-Trial-Account-and-API-Engine

## Summary

This procedure establishes a Swiftype trial account and creates an API-based engine with a document type, providing the foundation for injecting documents via the API in a stored XSS attack.

## Description

Swiftype allows free trial signups to access its search engine features, including API-based engines for custom document indexing. By creating an account and engine, an attacker gains the credentials and endpoints needed to POST malicious documents. This step requires no special privileges and simulates legitimate onboarding, making it low-risk for detection. Expected outcomes include access to the app dashboard and API endpoints for further exploitation.

## Requirements

1. Valid email address for signup (e.g., qwerty.chan8@gmail.com)
2. Web browser for navigating the Swiftype app
3. Internet access to https://app.swiftype.com

## Defense

Defensive measures and detection strategies:

- Monitor for unusual trial account creations from disposable emails
- Rate-limit API engine creations to prevent abuse
- Implement CAPTCHA on signup to deter automated attacks

## Objectives

1. Gain initial access to Swiftype platform via trial
2. Prepare API-based engine for document injection
3. Establish external_id and field types for payload compatibility

## Instructions

### Step 1: Create Trial Account

**Context**: Sign up for a free trial to access the Swiftype dashboard.

Visit https://app.swiftype.com/ and enter your email (e.g., qwerty.chan8@gmail.com) to complete signup. Verify the email if prompted.

> Expected output: Redirect to dashboard with account confirmation.

### Step 2: Create API-Based Engine

**Context**: Set up an engine configured for API document management.

Navigate to https://app.swiftype.com/engines/api, enter an engine name (e.g., 123) and document type name (e.g., test), then click Create Engine.

> Expected output: Engine created and listed in the dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- trial-account
- api-engine
