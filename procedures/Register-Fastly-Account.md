---
id: p-register-fastly-account
tags:
  - domain-takeover
  - account-creation
type: procedure
tools:
  - '[[tools/Fastly-Management-Dashboard]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Accounts]]'
updated_at: '2025-12-14T04:51:10.680Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Compromise Accounts]]'
---
# Register-Fastly-Account

## Summary

This procedure outlines creating a free Fastly account, which is the initial step in claiming subdomains via their free TLS service for domain takeover attacks.

## Description

Fastly provides a free tier for TLS-enabled domains, allowing any user to register and provision subdomains under freetls.fastly.net. In the context of this attack, registering an account enables access to the dashboard for service creation, targeting whitelisted domains like those in GitLab's CSP. The process requires only an email and basic info, with no verification barriers that prevent malicious use. Expected outcome: Account access for subsequent domain configuration steps.

## Requirements

1. Web browser with internet access
2. Valid email address for registration
3. No prior Fastly credentials needed

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous Fastly account creations linked to sensitive subdomains
- Implement domain monitoring tools to alert on takeovers of whitelisted assets
- Regularly audit CSP headers for hardcoded, takeover-prone domains

## Objectives

1. Gain authenticated access to Fastly's management platform
2. Enable subdomain provisioning for takeover
3. Set foundation for CSP bypass in target applications like GitLab

## Instructions

### Step 1: Access Signup Page

**Context**: Begin the registration to create a new account.

Navigate to the Fastly signup page (https://www.fastly.com/signup) and fill in the required fields: email, password, and organization details.

### Step 2: Complete Registration

**Context**: Submit and verify the account creation.

Submit the form and check your email for a confirmation link. Click it to activate the account.

**Expected Output**: Redirect to the login page upon successful verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Compromise Accounts]] Compromise Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Fastly-Management-Dashboard]]

## Tags

- [[domain-takeover]]
- [[account-creation]]
