---
id: proc-create-user-dod-access
tags:
  - initial-access
  - account-creation
  - dod
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
updated_at: '2025-12-14T03:46:26.022Z'
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
# Create-User-Account-for-Initial-Access

## Summary

This procedure involves registering a new user account on the target DoD web application to establish an authenticated session, enabling access to protected endpoints like RequestAccess.asp for subsequent vulnerability testing.

## Description

In the context of testing a U.S. Department of Defense ASP application, creating a legitimate user account provides the necessary session authentication to interact with the backend SQL Server without triggering immediate access controls. This step is crucial for mimicking legitimate user behavior before escalating to injection attacks. Expected outcomes include a valid session cookie for request interception.

## Requirements

1. Direct network access to https://████████.asp registration page
2. Browser with proxy support for Burp Suite
3. No special credentials; open registration assumed

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification on registration to prevent automated account creation
- Monitor for unusual registration patterns from testing IPs

## Objectives

1. Establish authenticated access to the application
2. Obtain session cookies for request manipulation
3. Prepare for vulnerability probing without unauthenticated errors

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the user creation endpoint to fill out the form.

No command required; use browser to visit https://████.asp and complete the registration fields, then log in.

> Upon success, you will be redirected to https://████.asp with a session established.

### Step 2: Verify Access

**Context**: Confirm the account allows access to the target endpoint.

Navigate to https://████████mil/AFServices/RequestAccess.asp?selMajcom=MAT\*&selbase=MXRD&Submitted=1&Appid=29&FuncID=23&App=Activity+Database+FMP while logged in.

> Expected output: Page loads without authentication errors, displaying form or results.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[initial-access]]
- [[account-creation]]
