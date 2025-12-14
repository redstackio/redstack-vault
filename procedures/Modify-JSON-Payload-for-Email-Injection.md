---
id: proc-003
tags:
  - payload-modification
  - email-injection
  - json
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.523Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Modify-JSON-Payload-for-Email-Injection

## Summary

This procedure modifies the intercepted JSON payload in the GitLab password reset request by converting the email field to an array containing both the victim's and attacker's emails, exploiting improper input validation to receive an unauthorized reset link.

## Description

After conversion to JSON, the payload is edited directly in Burp Suite. The vulnerability stems from the backend accepting and processing email arrays without checking for singular values, sending reset tokens to all listed emails. This enables account takeover. Requires prior interception; outcome: Dual email reset triggers.

## Requirements

1. Intercepted and JSON-converted request in Burp Suite
2. Knowledge of attacker's own email address
3. Basic JSON editing skills

## Defense

Defensive measures and detection strategies:

- Validate email parameters as single strings only; reject arrays or unexpected formats
- Implement server-side checks for email domain whitelisting or length limits
- Audit logs for multiple emails in single reset requests

## Objectives

1. Inject attacker's email into the reset process
2. Exploit lack of array validation
3. Ensure reset links are generated for unauthorized access

## Instructions

### Step 1: Edit the JSON Body

**Context**: Open the request in Burp's editor and alter the email structure.

Switch to the JSON view or Raw tab.

> Change {"user":{"email":"victim@gmail.com"}} to {"user":{"email":["victim@gmail.com","attacker@gmail.com"]}}. Validate JSON syntax.

### Step 2: Update Headers if Needed

**Context**: Ensure the request remains properly formatted.

Confirm Content-Type is application/json.

> No further changes; the modification exploits the server's processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

None

## Commands Used

None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[payload-modification]]
- [[email-injection]]
- [[json]]
- [[account-takeover]]
