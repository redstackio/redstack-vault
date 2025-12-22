---
tags:
  - account-creation
  - setup
  - idor-prep
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.955Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5334f489-80de-4309-ba43-0d5b49b81e49
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-Test-Accounts-and-Fill-Details

## Summary

This procedure sets up two authenticated test accounts in the DoD JOINOnline web application, populating them with demographic details to generate unique user IDs necessary for subsequent IDOR exploitation.

## Description

In the context of testing for IDOR vulnerabilities, this initial step involves registering and configuring test users to simulate real data. The DoD application assigns sequential numeric IDs upon profile completion, which are exposed in URLs. This procedure requires valid access to the application's registration flow and ensures data is entered to trigger ID generation. Expected outcomes include obtaining IDs like 1327 and 1328 for manipulation, setting the stage for unauthorized access without alerting defenses.

## Requirements

1. Network access to https://www.██████████/JOINOnline/.
2. Valid credentials or registration eligibility for DoD users.
3. Web browser for form interactions.

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation to prevent bulk testing.
- Log all registration and profile update events for anomaly detection.
- Require CAPTCHA or additional verification for new accounts.

## Objectives

1. Establish baseline authenticated sessions with unique user IDs.
2. Populate profiles with sample PII to mimic real leak scenarios.
3. Prepare environment for parameter tampering without data loss.

## Instructions

### Step 1: Register Test Accounts

**Context**: Access the application's entry point to create two distinct user profiles.

Navigate to the DoD JOINOnline landing page and follow the registration process for User-A and User-B.

**Expected Output**: Confirmation emails or success messages for both accounts.

### Step 2: Log In and Complete Profiles

**Context**: Authenticate each account and input required biographical details to assign IDs.

Log in to User-A, then User-B separately. Access the form at https://www.██████████/JOINOnline/Board/BoardIntro/1021/1327/False and enter details such as name, contact info, and demographics.

**Expected Output**: Profiles saved, with URLs now including unique numeric IDs (e.g., /1327/ for User-B).

### Step 3: Verify Profile Accessibility

**Context**: Ensure details are visible in the Contact-Info section for each account.

From each logged-in session, navigate to the Contact-Info endpoint and confirm data loads correctly.

**Expected Output**: Personal details displayed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[setup]]
- [[idor-prep]]
