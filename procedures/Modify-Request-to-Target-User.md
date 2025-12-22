---
id: proc-gitlab-modify-request
tags:
  - parameter-injection
  - modification
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.873Z'
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
# Modify Request to Target User

## Summary

This procedure alters the intercepted 2FA request by adding the target user's login parameter, exploiting the find_user method's precedence to switch verification context from attacker to target.

## Description

The GitLab SessionsController's find_user prioritizes params[:login] over session[:otp_user_id]. By injecting user[login] with the target's username (e.g., 'john'), the OTP verification targets the wrong account. This is done in Burp's Repeater or Inspector on the multipart request.

## Requirements

1. Intercepted 2FA POST request
2. Knowledge of target username
3. Burp Suite active

## Defense

Defensive measures and detection strategies:

- Validate all parameters against session user ID
- Reject unexpected login params in 2FA stage
- Audit logs for parameter mismatches in auth flows

## Objectives

1. Add user[login] field to request
2. Preserve existing OTP field
3. Prepare for OTP replacement

## Instructions

### Step 1: Edit Form Data

**Context**: Locate the request body in Burp and insert the new parameter.

In Burp Inspector, add: Content-Disposition: form-data; name="user[login]"

Value: target's username (e.g., john)

> Ensures form-data format: boundary-separated fields.

### Step 2: Verify Request Integrity

**Context**: Check that the modification doesn't corrupt the multipart structure.

Preview the raw request; ensure Content-Type remains multipart/form-data.

> Expected: Request includes both user[login] and user[otp_attempt].

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[parameter-injection]]
- [[modification]]
- [[auth-bypass]]
