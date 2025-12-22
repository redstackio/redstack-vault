---
tags:
  - initial-access
  - vendor-setup
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:28.813Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e4c0611d-05e6-4a96-ad03-8daee3871339
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Setup-Vendor-Account-and-Register-Test-Company

## Summary

This procedure establishes a legitimate vendor account in the DoD web application and registers a test company to facilitate discovery of the deletion endpoint, serving as the initial access point for IDOR exploitation.

## Description

In the context of testing a U.S. Department of Defense vendor portal built on ASP.NET Core, this procedure involves self-registration to gain authenticated access. It allows attackers to interact with company management features, creating a controlled environment to observe request patterns for vulnerabilities like IDOR. Prerequisites include browser access and Burp Suite for proxying traffic. Expected outcomes are a functional account and test company, enabling subsequent interception without raising immediate alarms.

## Requirements

1. Internet access to https://███████/████/Reception/Vendor
2. Standard web browser (e.g., Chrome with Burp proxy configured)
3. Valid email for account verification (if required by the form)

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate-limiting on registration endpoints to prevent automated account creation
- Monitor for unusual registration patterns from new IPs
- Log all account creations and tie them to subsequent actions for anomaly detection

## Objectives

1. Obtain authenticated access to the vendor companies management page
2. Create a test company to generate a legitimate deletion request
3. Prepare the environment for request interception without triggering defenses

## Instructions

### Step 1: Create Vendor Account

**Context**: Navigate to the registration page and submit the form to gain initial access.

No specific command; use browser to access https://███████/████/Reception/Vendor and complete the account creation form with required details (e.g., name, email, password).

> Upon submission, expect a success message or email verification link. Log in to confirm access.

### Step 2: Access Companies Management

**Context**: Post-login, reach the companies page to begin registration.

Navigate to https://██████/████/Vendor/Companies after successful login.

> The page should load the company dashboard; verify by checking for registration options.

### Step 3: Register Test Company

**Context**: Submit a new company form to create a target for deletion testing.

Fill out the company registration form (e.g., company name, details) and submit.

> Expect confirmation of registration and a new entry in the companies list with an assigned ID.

### Step 4: View Company Details

**Context**: Return to the test company's page to access the delete function.

Click back or navigate to the newly registered company's details page.

> The page should display company info and a delete button, ready for interception.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[initial-access]]
- [[vendor-setup]]
- [[web]]
