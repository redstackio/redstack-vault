---
tags:
  - user-enumeration
  - wordpress
  - login
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 40115b1c-f9eb-4b04-8328-e9c5cc22760e
created_at: '2025-12-14T17:28:36.661Z'
updated_at: '2025-12-14T17:28:36.661Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Attempt-Login-with-Non-Existing-WordPress-Username

## Summary

This procedure involves submitting a login attempt with a fabricated invalid username to generate a generic error message, which can be compared against responses from valid usernames for enumeration purposes.

## Description

WordPress's login system reveals username validity through distinct error handling: invalid usernames prompt a straightforward rejection, while valid ones indicate a password issue. This step completes the enumeration by providing the baseline response for non-existent users, enabling attackers to systematically identify active accounts. As usernames are deemed public by WordPress policy, this has limited sensitivity but can aid in targeted attacks.

## Requirements

1. Access to a web browser
2. URL of the WordPress wp-admin login page
3. A fabricated username that likely doesn't exist (e.g., random string)

## Defense

Defensive measures and detection strategies:

- Use uniform error messaging to obscure username validity
- Deploy CAPTCHA or multi-factor authentication on login
- Log and alert on repeated failed logins from the same IP

## Objectives

1. Generate the invalid username error for comparison
2. Rule out non-existent usernames in enumeration efforts
3. Build a profile of valid vs. invalid responses

## Instructions

### Step 1: Access the Login Page

**Context**: Return to or refresh the wp-admin login form to initiate a new attempt.

Navigate to `https://target.com/wp-admin` in your browser.

> Ensures a clean form state for the invalid attempt.

### Step 2: Submit Invalid Username Login

**Context**: Input a non-existent username to elicit the generic error.

Enter a made-up username (e.g., 'fakeuser123') and any password (e.g., 'pass'). Submit the form.

> Response should be: "Invalid username."

### Step 3: Document the Response

**Context**: Record the error for differential analysis.

Screenshot or note the exact error text using browser tools.

> This generic message confirms the username does not exist when contrasted with valid username errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-enumeration]]
- [[wordpress]]
- [[authentication]]
