---
id: p2q3r4s5-t6u7-8901-cdef-234567890123
name: Tamper-Registration-Parameters-for-Escalation
tags:
  - parameter-tampering
  - privilege-escalation
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - ColdFusion
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:58.589Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[JavaScript]]'
---
# Tamper-Registration-Parameters-for-Escalation

## Summary

This procedure intercepts a web registration POST request and modifies key parameters to bypass access controls and inject code delimiters, escalating a new user to administrator privileges in a vulnerable ColdFusion-based DoD application.

## Description

The attack exploits lack of server-side validation on the user_type parameter (default 5 for user, 4 for admin) and poor sanitization of fname/lname fields, allowing injection of ColdFusion delimiters like '<%'. This occurs during anonymous registration on https://████/████████/newuser.cfm, leading to unauthorized admin access and PII exposure. Prerequisites include proxy setup and form filling with unique data.

## Requirements

1. Active proxy intercept (e.g., Burp Suite)
2. Filled registration form with unique SSN
3. Knowledge of parameter names (user_type, fname, lname)
4. Target endpoint accessible

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation and authorization on all parameters
- Sanitize inputs to block special characters like '<%'
- Log and alert on anomalous user_type values during registration
- Use parameterized queries and escape user inputs in ColdFusion

## Objectives

1. Change user_type to 4 for admin escalation
2. Inject '<%' into names to potentially execute code or bypass logic
3. Complete registration with elevated privileges

## Instructions

### Step 1: Intercept the POST Request

**Context**: Capture the submission before it reaches the server.

**Instructions**: Submit the form with proxy intercept on. In Burp Repeater or Proxy, view the POST to newuser.cfm.

> Request body shows parameters like user_type=5&fname=Test&lname=User. Expected: Full form data paused.

### Step 2: Modify Parameters

**Context**: Alter values to exploit vulnerabilities.

**Instructions**: Edit user_type=4, fname=Hackerone<% , lname=test<%xss . Ensure other fields remain valid (e.g., valid SSN).

> The '<%' acts as ColdFusion expression start, potentially contributing to escalation. Expected: Modified request ready to forward.

### Step 3: Forward and Observe Response

**Context**: Send tampered request to server.

**Instructions**: Click Forward in Burp. Monitor response for success (e.g., 200 OK with login redirect).

> Server processes without validation errors. Expected: Registration succeeds, user logged in.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[JavaScript]] JavaScript (adapted for ColdFusion injection)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- parameter-tampering
- privilege-escalation
- injection
