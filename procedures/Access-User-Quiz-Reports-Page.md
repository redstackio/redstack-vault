---
id: proc-access-reports-001
tags:
  - web
  - recon
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.208Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-User-Quiz-Reports-Page

## Summary

This procedure navigates to the quizzes-taken-by-user reports section on training.smartpay.gsa.gov, setting the stage for IDOR exploitation by accessing the vulnerable endpoint.

## Description

In the context of testing for IDOR vulnerabilities in web applications like the GSA SmartPay training portal (built on Drupal 8), this step involves logging in as an authenticated user and directly accessing the reports page. The page exposes user-specific quiz data, which becomes exploitable in subsequent steps. Prerequisites include valid credentials and a proxied browser session for traffic interception. Expected outcome: Visibility into the attacker's own quiz reports, confirming endpoint accessibility.

## Requirements

1. Authenticated session to https://training.smartpay.gsa.gov
2. Browser configured to proxy through Burp Suite
3. Knowledge of the target URL: https://training.smartpay.gsa.gov/reports/quizzes-taken-by-user

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to restrict reports page to authorized users only.
- Monitor access logs for unusual navigation patterns to reports endpoints.

## Objectives

1. Gain initial access to the vulnerable reports interface.
2. Verify authenticated session functionality.
3. Prepare for request interception.

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate to the portal and reach the reports section to trigger the vulnerable workflow.

No specific command; perform via browser:

- Log in at https://training.smartpay.gsa.gov/login.
- Navigate directly to https://training.smartpay.gsa.gov/reports/quizzes-taken-by-user.

> This loads the page showing the user's quiz history. Ensure no redirects or errors occur, indicating successful access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web]]
- [[recon]]
