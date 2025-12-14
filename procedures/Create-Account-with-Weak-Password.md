---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Create-Account-with-Weak-Password
tags:
  - weak-password
  - signup
  - initial-access
type: procedure
tools: []
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
updated_at: '2025-12-14T17:33:12.193Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Account-with-Weak-Password

## Summary

This procedure demonstrates how to exploit a weak password policy by registering a new account with an easily guessable password during the signup process, bypassing any intended security controls and setting the stage for credential leaks or brute-force attacks.

## Description

In scenarios where a web platform like Stripo Inc's fails to enforce strong password requirements (e.g., minimum length, complexity, or uniqueness checks), attackers can create accounts using simple passwords such as "password" or "123456". This violates secure design principles and exposes the platform to risks like password reuse across services or leaks via insecure storage. The procedure targets the signup endpoint, typically a POST request to /signup or similar, and confirms acceptance of weak credentials. Expected outcomes include successful registration, highlighting the vulnerability for reporting or exploitation.

## Requirements

1. Access to the public signup page of the target web application.
2. A standard web browser for manual interaction.
3. No authentication required, as this is initial access.

## Defense

Defensive measures and detection strategies:

- Implement strict password policies with enforcement (e.g., min 12 characters, mix of types, no common words) using client-side and server-side validation.
- Monitor signup logs for patterns of weak password usage and alert on suspicious registrations.
- Use rate-limiting on signup attempts and integrate CAPTCHA to prevent automated abuse.

## Objectives

1. Successfully register an account with a weak password to prove policy weakness.
2. Verify that the password is stored without hashing or salting issues (inferred from acceptance).
3. Establish a vector for broader credential access attacks.

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Locate and access the registration form to test password validation.

Open a web browser and go to the target's signup URL (e.g., https://target.com/signup). Fill in required fields like email and username, then enter a weak password such as "password123" in the password field.

> No specific command needed; this is manual browser interaction. Submit the form and observe if it accepts the password without rejection.

### Step 2: Submit and Verify Registration

**Context**: Confirm that the weak password is accepted and the account is created.

Click the submit button on the signup form. Check for a success message or email verification link. Attempt to log in immediately using the same weak password to validate access.

> Expected output: Welcome email or dashboard access upon login, indicating the weak password was stored and usable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- weak-password
- signup
- initial-access
