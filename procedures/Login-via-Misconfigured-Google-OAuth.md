---
tags:
  - oauth
  - auth-bypass
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Jenkins
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 69c035d6-3a86-4a77-8c02-ed51cb9d50d3
created_at: '2025-12-11T03:47:56.629Z'
updated_at: '2025-12-11T03:47:56.629Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Login via Misconfigured Google OAuth

## Summary

This procedure exploits misconfigured Google OAuth in Jenkins to gain unauthorized access using any valid Google account.

## Description

Due to improper restrictions, the OAuth integration allows authentication without domain checks, granting dashboard access. This targets Jenkins environments with external auth providers, leading to initial access for further exploitation.

## Requirements

1. Valid Google account credentials
2. Access to the Jenkins login page
3. Web browser for OAuth flow

## Defense

Defensive measures and detection strategies:

- Configure OAuth to restrict to specific domains
- Log and alert on unexpected logins

## Objectives

1. Achieve authenticated session in Jenkins
2. Access dashboard and features
3. Enable subsequent discovery steps

## Instructions

### Step 1: Navigate to Login Page

**Context**: Open the Jenkins login URL in a browser.

Visit https://jenkins.target.com/login and select Google sign-in.

### Step 2: Complete OAuth Flow

**Context**: Authenticate with Google credentials.

Enter any valid Google email and password, then authorize the app if prompted.

> Upon success, you will be redirected to the Jenkins dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser]]

## Tags

- #oauth
- #auth-bypass
