---
tags:
  - error-trigger
  - input-reflection
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-duplicate-registration-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:47:12.917Z'
sub_techniques: []
id: 806aa451-8c07-46c7-a826-b9e860a647b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Trigger-Duplicate-Email-Error

## Summary

This procedure resubmits the registration form with an already-registered email to elicit an error response that reflects user input, exposing the vulnerability point for XSS injection.

## Description

Targeting the same /ioss/site/customer.cfm endpoint, this step replays the initial registration data but reuses the email, causing the application to return an error like 'this email address already exists in the system'. The prefixRank input is echoed back in the HTML without escaping, creating an opportunity for payload injection. This is key to confirming reflection before exploitation. Expected outcome is an error page with visible unsanitized input.

## Requirements

1. Successfully completed initial registration with known email
2. Ability to replay HTTP POST requests identically
3. Access to inspect response HTML for reflection

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs in error messages with HTML entity encoding
- Log and alert on repeated registration failures for the same email
- Use WAF rules to block suspicious error-triggering patterns

## Objectives

1. Provoke input reflection in the error response
2. Verify lack of output encoding on prefixRank parameter
3. Set stage for payload testing

## Instructions

### Step 1: Replay Registration Request

**Context**: Use the exact same form data from initial registration, ensuring the email matches the registered one.

No command needed; reuse data.

### Step 2: Submit Duplicate Request

**Context**: Send the POST to trigger the error and observe reflection.

**Command** ([[commands/submit-duplicate-registration-curl]]):
```bash
curl -X POST https://www.████.gov/ioss/site/customer.cfm \
  -d "email=user@example.com" \
  -d "prefixRank=Mr" \
  -d "firstName=Test" \
  -d "lastName=User" \
  --data-urlencode "other fields as required"
```

> This mirrors the initial request but with a duplicate email. Expected output includes an error message with reflected prefixRank in the HTML body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used

- [[commands/submit-duplicate-registration-curl]]

## Tools Used


## Tags

- [[error-trigger]]
- [[input-reflection]]
- [[web]]
