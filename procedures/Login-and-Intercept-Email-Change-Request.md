---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Login-and-Intercept-Email-Change-Request
tags:
  - login
  - intercept
  - web
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.341Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Intercept-Email-Change-Request

## Summary

This procedure authenticates to the Atavist platform and uses a proxy to intercept the HTTP request generated when updating an email address, revealing the vulnerable 'id' parameter for IDOR exploitation.

## Description

In the Atavist CMS, the account settings page allows authenticated users to update their email via a POST request to /cms/reader/account. Without proper authorization, this request includes a user 'id' that can be inspected and modified. This step sets up the baseline for exploiting the IDOR by capturing the request structure, including form data like email and id. Prerequisites include valid login credentials and a proxy tool configured to intercept traffic.

## Requirements

1. Valid Atavist account credentials (username/email and password)
2. Proxy tool like Burp Suite installed and browser traffic routed through it
3. Access to https://magazine.atavist.com over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement proxy detection (e.g., JA3 fingerprinting) to block anomalous traffic
- Log all account modification requests and alert on unusual IP or user agent changes

## Objectives

1. Establish authenticated session
2. Capture and analyze the email update request
3. Identify the sequential 'id' parameter for targeting

## Instructions

### Step 1: Authenticate to the Platform

**Context**: Log in to create an authenticated session required for accessing account settings.

Navigate to https://magazine.atavist.com/login and enter credentials.

> Successful login redirects to the dashboard, with session cookies set.

### Step 2: Access Settings and Intercept Request

**Context**: Go to the account page to trigger the email change form and capture the submission.

Navigate to https://magazine.atavist.com/cms/reader/account. Configure proxy to intercept. Enter a new email and submit the form.

> Proxy captures POST to https://magazine.atavist.com/cms/reader/account with body including 'id': current_user_id and 'email': new_email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[login]]
- [[intercept]]
- [[web]]
- [[proxy]]
