---
tags:
  - aws
  - sso
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.708Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 907f0ffd-c2ee-47d2-a2ee-1de8cf9faa67
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-AWS-Console-via-SSO

## Summary

This procedure establishes an initial authenticated session in the AWS Management Console using AWS IAM Identity Center (SSO), setting the stage for exploiting session management inconsistencies.

## Description

In the context of AWS environments, logging in via SSO creates a session token that is subject to the console's timeout policy. This step is prerequisite for demonstrating the bypass where the Access Portal does not honor the expired console session. It requires valid SSO credentials and simulates legitimate user access that could be left unattended.

## Requirements

1. Valid AWS SSO credentials (username/password or MFA)
2. Access to the AWS Management Console URL (https://console.aws.amazon.com)
3. Web browser with cookies enabled

## Defense

Defensive measures and detection strategies:

- Enforce short session timeouts across all AWS services
- Monitor for anomalous login patterns via AWS CloudTrail
- Implement device trust or conditional access policies in IAM Identity Center

## Objectives

1. Gain initial access to AWS Management Console
2. Establish exploitable session state
3. Prepare for timeout-based bypass testing

## Instructions

### Step 1: Navigate to AWS Console

**Context**: Open the browser and direct to the AWS login endpoint to initiate SSO flow.

No command required; use browser:

Navigate to `https://console.aws.amazon.com/console/home` and select 'Sign in to the AWS Management Console using your organization's identity source'.

> This redirects to the SSO provider login page.

### Step 2: Authenticate via SSO

**Context**: Enter credentials to create the session.

Provide username, password, and complete MFA if enabled.

> Upon success, the console dashboard loads, confirming session establishment. Check browser dev tools (Application > Cookies) for session tokens like `aws-ui` or SSO-related cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[aws]]
- [[sso]]
- [[login]]
