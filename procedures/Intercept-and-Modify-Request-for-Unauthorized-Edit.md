---
id: proc-intercept-modify-request
tags:
  - idor
  - request-tampering
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
updated_at: '2025-12-14T17:25:48.116Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Request-for-Unauthorized-Edit

## Summary

This procedure uses Burp Suite to intercept a profile save request from the attacker, substitutes the victim's hidBlogID, and forwards it to achieve unauthorized editing of the victim's blog/website information via IDOR.

## Description

The core exploitation step involves tampering with the POST request to /edit-user-profile, where the lack of authorization on hidBlogID allows cross-account modifications. After forwarding, verify impact by checking the victim's profile. Expected outcome: Victim's data altered without their consent.

## Requirements

1. Burp Suite proxy active and intercepting
2. Victim's hidBlogID value
3. Attacker's form ready for submission

## Defense

Defensive measures and detection strategies:

- Validate object ownership server-side (e.g., check user ID matches blog owner)
- Log all parameter changes and audit for ID mismatches
- Use signed tokens or CSRF protection to prevent tampering

## Objectives

1. Capture and alter the vulnerable parameter
2. Execute unauthorized data modification
3. Confirm impact on target account

## Instructions

### Step 1: Intercept the Request

**Context**: Capture the save action in Burp.

**Instructions**: Click 'Save Settings' in the attacker's profile form; Burp will intercept the POST request to /edit-user-profile.

> Inspect the request body for the hidBlogID parameter.

### Step 2: Modify hidBlogID

**Context**: Substitute to target victim's object.

**Instructions**: In Burp's Repeater or Intercept tab, edit the 'hidBlogID' value to the victim's extracted ID (e.g., change from attacker's ID to '12345'), then click 'Forward' or 'Send'.

> The server processes the request as if from the attacker but targeting victim data.

### Step 3: Verify Unauthorized Edit

**Context**: Check for successful tampering.

**Instructions**: Log out, log in as victim, return to https://www.intensedebate.com/edit-user-profile, and observe the blog/website section for attacker's changes.

> Changes persist due to missing checks.

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

- [[idor]]
- [[request-tampering]]
