---
id: proc-1
tags:
  - input-validation
  - web
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:24.824Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Forgot-Password-with-Arbitrary-Inputs

## Summary

This procedure tests the forgot password endpoint for improper input validation by submitting arbitrary strings in the email field, confirming that they are processed and queried against the database without rejection.

## Description

In the context of the NordVPN affiliates site, the /users/forgot_password endpoint accepts inputs like %0a or %0d, which are URL-encoded newline characters, and executes database queries on them. This reveals a lack of server-side email validation, allowing invalid data to reach the backend. The expected outcome is a response indicating no user found, but the query execution confirms the vulnerability. Prerequisites include direct access to the web application over HTTPS.

## Requirements

1. Web browser access to https://affiliates.nordvpn.com
2. Basic understanding of URL encoding
3. No special tools required for initial manual testing

## Defense

Defensive measures and detection strategies:

- Implement server-side email format validation using regex (e.g., matching RFC 5322)
- Log and monitor anomalous inputs to the forgot password endpoint
- Use WAF rules to block non-email payloads

## Objectives

1. Verify that arbitrary inputs bypass client-side validation
2. Confirm database interaction with invalid data
3. Identify potential for further exploitation like injection

## Instructions

### Step 1: Navigate to the Forgot Password Page

**Context**: Access the target endpoint to prepare for input testing.

Navigate to https://affiliates.nordvpn.com/users/forgot_password in your browser.

### Step 2: Submit Arbitrary Email Payloads

**Context**: Enter encoded strings to test validation; observe if the system processes them as potential emails.

Fill the email field with payloads such as %0a or %0a%0d and submit the form.

**Expected Output**: The server responds with 'No user account was found for the address given', indicating the input was queried in the database.

### Step 3: Verify Response and Logs

**Context**: Check for signs of backend processing to confirm vulnerability.

Inspect the HTTP response for any differences; successful processing shows the query executed despite invalid input.

**Expected Output**: Standard error message without rejection, confirming lack of validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- input-validation
- web-testing
