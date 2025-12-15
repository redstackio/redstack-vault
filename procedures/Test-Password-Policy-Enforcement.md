---
tags:
  - weak-password
  - password-policy
  - brute-force
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9ad77cae-c786-4d63-8a17-67ce001607c5
created_at: '2025-12-14T17:28:20.219Z'
updated_at: '2025-12-14T17:28:20.219Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Test-Password-Policy-Enforcement

## Summary

This procedure tests the enforcement of password complexity rules on web applications, specifically identifying cases where documented requirements for special characters and numbers are not validated, allowing weaker alphabetic-only passwords that facilitate brute force attacks.

## Description

In the context of Khan Academy, the password policy documentation specifies that passwords must include mixtures of uppercase/lowercase letters, numbers, and symbols. However, the backend does not enforce this during registration or password reset, accepting purely alphabetic inputs. This leads to reduced password strength, increasing vulnerability to automated guessing attacks. The procedure involves manual interaction with the site's forms to submit invalid passwords and confirm acceptance, highlighting a configuration weakness between frontend guidance and server-side validation.

## Requirements

1. Access to a web browser with developer tools for inspection (optional)
2. Public access to the target website's registration or password reset endpoint
3. Basic understanding of password entropy and brute force risks

## Defense

Defensive measures and detection strategies:

- Implement strict server-side validation matching documented policies
- Use password strength meters and enforce minimum entropy requirements
- Monitor for anomalous registration patterns indicating weak password usage
- Conduct regular policy audits and penetration testing for enforcement gaps

## Objectives

1. Confirm non-enforcement of password complexity rules
2. Create a weak password to demonstrate vulnerability
3. Assess impact on account security against brute force

## Instructions

### Step 1: Access Registration or Password Reset Form

**Context**: Locate the entry point for creating or changing passwords on the target site to begin testing.

Navigate to https://www.khanacademy.org and select the sign-up or login option, then choose to reset or create a password.

> Fill in required fields like email or username, but focus on the password field.

### Step 2: Submit Alphabetic-Only Password

**Context**: Attempt to use a password that violates the policy by excluding numbers and symbols, verifying if the system accepts it.

Enter a password such as "abcdeFghij" (only letters, mixed case) and submit the form.

> If accepted, the procedure succeeds, indicating weak enforcement. Inspect network requests in browser dev tools to confirm no backend rejection.

### Step 3: Validate Account Creation

**Context**: Confirm the weak password is active and functional.

Log in with the new alphabetic-only password to ensure it works as expected.

> Successful login confirms the vulnerability; report as a policy enforcement issue.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- weak-password
- password-policy
- brute-force
