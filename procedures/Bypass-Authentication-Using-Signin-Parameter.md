---
id: proc-uuid-002
tags:
  - auth-bypass
  - web
  - sso
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:52.393Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Authentication-Using-Signin-Parameter

## Summary

This procedure exploits a lack of validation on the 'signin' parameter in a login endpoint to authenticate as any user without credentials or registration, granting access to protected resources.

## Description

The vulnerability stems from improper authentication checks in a web application's SSO endpoint, allowing arbitrary user identifiers via the 'signin' parameter in GET requests. Attackers can craft URLs to impersonate users and access areas like /portal/index.php. This targets web platforms with OAuth/SSO integration, leading to unauthorized access and potential data exposure.

## Requirements

1. Access to the login endpoint URL
2. Knowledge of target user identifiers (e.g., usernames or IDs)
3. Web browser or curl for GET requests

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all input parameters, rejecting arbitrary 'signin' values
- Require proper credential checks and session tokens for authentication
- Log and alert on unusual authentication patterns, such as logins without passwords

## Objectives

1. Authenticate as an arbitrary user without registration
2. Gain access to protected application resources
3. Demonstrate bypass of standard login flows

## Instructions

### Step 1: Craft Malicious URL

**Context**: Append the vulnerable parameter to the login endpoint to initiate bypass.

Construct the URL by adding ?signin=<arbitrary_user_identifier> to the base login URL, e.g., ██████████?signin=targetuser.

> This crafts a GET request that skips credential validation.

### Step 2: Execute Bypass Request

**Context**: Send the crafted URL to authenticate and access protected areas.

Visit the modified URL in a browser or use a tool like curl: curl "██████████?signin=targetuser".

> Expected output: Redirect to /portal/index.php or dashboard as the targeted user, confirming bypass success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web]]
- [[sso]]
