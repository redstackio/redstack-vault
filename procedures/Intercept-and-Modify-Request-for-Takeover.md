---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - request-modification
  - burp-suite
  - idor
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.610Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Request-for-Takeover

## Summary

This procedure intercepts the profile edit submission using a proxy, modifies the user ID to the victim's, and forwards the request to overwrite the victim's account credentials.

## Description

Exploiting the lack of user ID validation, the intercepted POST request to EditUserProfile is altered to target the victim's user ID while using the attacker's password authentication. If the user ID is unknown, brute-force enumeration may be needed. A 302 response confirms the update, effectively linking the victim's email to the attacker's password.

## Requirements

1. Burp Suite or similar proxy configured to intercept traffic
2. Captured form submission request with victim's email
3. Victim's user ID (obtained via brute-force if necessary)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and session binding to user ID
- Validate all parameters against authenticated user
- Monitor for anomalous request modifications via WAF logs

## Objectives

1. Alter request parameters to target victim account
2. Execute overwrite without ownership verification
3. Confirm update via response codes

## Instructions

### Step 1: Intercept Form Submission

**Context**: Capture the POST request before it reaches the server.

With proxy active, submit the prepared form and forward to Repeater in Burp Suite.

**Expected Output**: Raw HTTP request displayed in Repeater, including email=victim@gmail.com and user_id=attacker_id.

### Step 2: Modify User ID

**Context**: Change the target from attacker to victim account.

In the request body or parameters, replace user_id from attacker's value to victim's (e.g., brute-force 1-1000 if needed).

**Expected Output**: Updated request with user_id=victim_id.

### Step 3: Test Initial Forward

**Context**: Send to observe behavior, noting any login errors post-overwrite.

Forward the request and attempt victim login (expect failure initially due to partial overwrite).

**Expected Output**: 302 redirect on success; login error for verification.

### Step 4: Finalize Modification

**Context**: Revert and resubmit if needed to complete credential linkage.

Adjust email/user_id back if testing, then send the targeting request again.

**Expected Output**: Successful 302 without errors.

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

- request-modification
- burp-suite
- idor
