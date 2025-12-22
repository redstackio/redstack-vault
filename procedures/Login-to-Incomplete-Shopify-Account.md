---
tags:
  - authentication
  - shopify
  - incomplete-account
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 702ab09d-62c6-4868-b88e-a16cb80a8e01
created_at: '2025-12-13T23:55:38.253Z'
updated_at: '2025-12-13T23:55:38.253Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Incomplete-Shopify-Account

## Summary

This procedure authenticates to the Shopify Help Center using an account in an incomplete state (e.g., missing name and last name), which is necessary to trigger the subsequent XSS execution.

## Description

Shopify accounts require complete details for full functionality, but incomplete accounts can still log in and reach prompts. This state allows the 'returnTo' parameter to be processed insecurely upon clicking 'Continue'. The procedure simulates or uses a real incomplete account to advance the attack flow, enabling the reflected payload to execute post-login.

## Requirements

1. Valid Shopify credentials for an incomplete account
2. Web browser session from the malicious URL
3. Internet access to the Shopify domain

## Defense

Defensive measures and detection strategies:

- Enforce account completion before allowing navigation or redirects
- Log and alert on logins from incomplete accounts accessing sensitive endpoints
- Use multi-factor authentication to limit impact of stolen sessions

## Objectives

1. Gain authenticated access to the Help Center
2. Maintain incomplete state to bypass validations
3. Set up for payload triggering

## Instructions

### Step 1: Enter Credentials

**Context**: On the login form presented after loading the malicious URL, input the username and password for the incomplete account.

Fill out the login fields manually in the browser.

### Step 2: Submit Login Form

**Context**: Authenticate to proceed to the account details prompt.

Click the submit button on the login page.

**Expected Output**: Successful authentication, redirecting to a page indicating missing details (e.g., name and last name prompts).

### Step 3: Verify Incomplete State

**Context**: Confirm the account status to ensure vulnerability conditions are met.

Check the page for prompts requiring additional information.

**Expected Output**: Page shows incomplete account indicators without full access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[incomplete-account]]
