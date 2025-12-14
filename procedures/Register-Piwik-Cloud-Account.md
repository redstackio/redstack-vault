---
id: uuid-register-piwik
tags:
  - account-creation
  - piwik-cloud
  - compromise
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Email Accounts]]'
updated_at: '2025-12-14T05:32:31.154Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Register Piwik Cloud Account

## Summary

This procedure creates a new account on Piwik Cloud, enabling the registration and claiming of available subdomains as part of a takeover attack.

## Description

Piwik Cloud allows free registration for analytics services, which includes the ability to claim subdomains. In the context of a dangling subdomain like gratipay.piwik.pro, this step establishes an account that can be used to hijack the subdomain by associating the parent domain. The process is straightforward via the web interface and requires only basic user details, with outcomes including account access for further configuration.

## Requirements

1. Web browser
2. Valid email for potential verification
3. No prior Piwik Cloud account

## Defense

Defensive measures and detection strategies:

- Limit subdomain claiming to verified domain owners via DNS proofs
- Monitor for new account creations targeting known domains
- Require additional verification for high-value subdomains

## Objectives

1. Gain legitimate access to Piwik Cloud features
2. Enable subdomain claiming
3. Set up for hijacking without raising alarms

## Instructions

### Step 1: Navigate to Signup

**Context**: Access the Piwik Cloud registration page to begin account creation.

No command; browser navigation.

> Open http://piwik.pro/cloud and click on signup or register options.

### Step 2: Complete Registration

**Context**: Enter required details to create the account.

No command; form submission.

> Provide a username and password, then submit the form. Check email if verification is needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Email Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[piwik-cloud]]
