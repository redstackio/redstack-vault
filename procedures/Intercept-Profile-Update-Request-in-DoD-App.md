---
id: proc-dod-intercept-update-request
tags:
  - intercept
  - proxy
  - http
  - dod
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:33.759Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-Profile-Update-Request-in-DoD-App

## Summary

This procedure details intercepting the HTTP POST request during a legitimate profile update in the DoD JOINOnline application using a proxy tool, capturing the structure for IDOR exploitation.

## Description

To exploit IDOR, first perform a normal profile update from the attacker's account (User-A, ID 1328) in the Biographical-Info section. Configure a proxy like Burp Suite to intercept the submission to /JOINOnline/Board/SubmitDoc. The request is multipart form-data with parameters: UserId=10268, Id=1328, BoardId=1021, que2800=Test (name), que2804=12/12/2001 (DOB), que2807=Male (gender), and __RequestVerificationToken. This step reveals the vulnerable parameter layout. Prerequisites: Authenticated session and proxy setup. Expected outcome: Captured request ready for editing.

## Requirements

1. Authenticated session as User-A
2. Proxy tool (Burp Suite) configured as browser proxy (e.g., 127.0.0.1:8080)
3. Access to Biographical-Info update form

## Defense

Defensive measures and detection strategies:

- Log all profile update requests and flag unusual UserId/Id mismatches
- Implement request signing or session-bound tokens to prevent interception tampering
- Use WAF rules to detect proxy-like traffic patterns

## Objectives

1. Capture baseline POST request structure
2. Identify key parameters for manipulation (e.g., Id)
3. Preserve cookies and tokens for valid resubmission

## Instructions

### Step 1: Configure Proxy and Perform Update

**Context**: Set up interception and trigger the profile update to capture the request.

No command; in Burp Suite, enable intercept, then in browser (proxied), log in as User-A, go to Biographical-Info, enter test data (name: Test, DOB: 12/12/2001, gender: Male, height: 167, weight: 80), and submit.

> Request intercepted in Burp's Proxy > Intercept tab. Expected output: Full HTTP POST with form-data visible.

### Step 2: Inspect and Forward Legitimately

**Context**: Verify the request works before modification by forwarding it.

In Burp, inspect parameters and forward the request.

> Server responds with success (e.g., redirect or 200). Expected output: User-A's profile updated, confirming request validity.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[http]]
- [[dod]]
