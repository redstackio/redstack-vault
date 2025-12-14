---
id: proc-access-semmle-settings
tags:
  - web
  - authentication
  - access
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:30.697Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Semmle-Account-Settings

## Summary

This procedure outlines logging into the Semmle application and navigating to the account settings page to access the profile update form, setting the stage for vulnerability testing in authenticated sessions.

## Description

In the context of testing for input sanitization issues in web applications like Semmle, initial access requires authentication to reach protected endpoints such as the profile update form at /settings. This step ensures a valid session is established, allowing subsequent interception and modification of requests. The target environment is a web-based platform, and outcomes include access to form submission capabilities. Prerequisites include valid credentials; without them, the procedure fails at authentication.

## Requirements

1. Valid username and password for a Semmle account
2. Web browser configured to proxy traffic through Burp Suite (127.0.0.1:8080)
3. Network access to the Semmle platform (https://lgtm-com.pentesting.semmle.net)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized access
- Monitor login attempts for anomalies, such as unusual IP addresses or failed logins
- Use web application firewalls (WAF) to detect proxy interception patterns

## Objectives

1. Establish an authenticated session to access user-specific features
2. Reach the profile update form for testing input handling
3. Confirm session validity for request interception

## Instructions

### Step 1: Authenticate to the Platform

**Context**: Log in to create a session cookie necessary for accessing settings.

No specific command; use the web form:

- Navigate to the Semmle login page.
- Enter credentials and submit.

> Successful login redirects to the dashboard, setting session cookies. Failure indicates invalid credentials.

### Step 2: Navigate to Settings

**Context**: Access the profile update interface to prepare form submission.

No specific command; browser navigation:

- From the dashboard, click on account or settings link (likely /settings).

> The page loads with the update form, including fields like 'location'. Verify by inspecting the form action pointing to /internal_api/v0.2/savePublicInformation.

### Step 3: Prepare Form Submission

**Context**: Fill minimal data to trigger the POST request.

No specific command; interact with form:

- Enter test data in fields and click 'Save'.

> The request is sent (or intercepted if proxy is active), confirming access to the endpoint.

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

- web
- authentication
