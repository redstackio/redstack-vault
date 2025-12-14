---
tags:
  - account-creation
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[External Remote Services]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b4ac5827-c0bb-42a4-87e0-8496bd3e74be
created_at: '2025-12-14T17:32:01.652Z'
updated_at: '2025-12-14T17:32:01.652Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Account-on-Semmle-Platform

## Summary

This procedure involves registering a new user account on the Semmle (LGTM) platform to obtain initial authenticated access, which is a prerequisite for exploiting internal API endpoints.

## Description

The Semmle platform at lgtm-com.pentesting.semmle.net allows open registration. By creating an account, an attacker gains a valid session that can be used to authenticate API calls. This step sets up the foundation for subsequent DoS attacks by providing legitimate credentials without raising immediate suspicion.

## Requirements

1. Internet access to lgtm-com.pentesting.semmle.net
2. Valid email address for verification
3. Web browser for registration

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on registration to prevent automated account creation
- Monitor for unusual registration patterns from single IPs
- Require email verification and limit registrations per IP

## Objectives

1. Obtain authenticated access to the platform
2. Prepare for session hijacking or API abuse
3. Establish a foothold for further exploitation

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the platform's signup page to begin account creation.

No specific command; use a web browser to visit https://lgtm-com.pentesting.semmle.net and click on the registration link.

> Fill in the required fields: username, email, and password. Submit the form.

### Step 2: Verify Account

**Context**: Complete any email verification if prompted.

Check your email for a verification link from Semmle and click it to activate the account.

> Expected output: Account activated, redirect to login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[web-registration]]
